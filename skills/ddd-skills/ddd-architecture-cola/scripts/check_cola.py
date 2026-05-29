#!/usr/bin/env python3
"""
COLA V5 Architecture Compliance Checker

Validates a COLA project's architecture compliance:
1. Dependency direction (domain → infrastructure forbidden)
2. Domain layer framework purity (no Spring/JPA/MyBatis imports)
3. Module naming conventions
4. Circular dependency detection
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


class COLAComplianceChecker:
    """COLA v5 Architecture Compliance Checker"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.violations: List[Dict] = []
        self.module_imports: Dict[str, Set[str]] = defaultdict(set)

    def check(self) -> Dict:
        """Run all compliance checks and return report"""
        if not self.project_path.exists():
            return {"status": "error", "message": f"Project path not found: {self.project_path}"}

        modules = self._find_modules()

        for module in modules:
            self._check_domain_purity(module)
            self._check_layer_dependencies(module, modules)
            self._check_package_naming(module)

        self._check_circular_dependencies(modules)
        score = self._calculate_score()

        return {
            "status": "completed",
            "project": str(self.project_path),
            "modules": modules,
            "violations": self.violations,
            "score": score,
            "grade": self._grade(score),
        }

    def _find_modules(self) -> List[str]:
        """Find all COLA modules in the project"""
        modules = []
        for entry in self.project_path.iterdir():
            if entry.is_dir() and (entry / "pom.xml").exists():
                modules.append(entry.name)
        if not modules and (self.project_path / "pom.xml").exists():
            modules = ["root"]
        return modules

    def _find_java_files(self, module: str) -> List[Path]:
        """Find all Java source files in a module"""
        module_path = self.project_path / module if module != "root" else self.project_path
        src_path = module_path / "src" / "main" / "java"
        if not src_path.exists():
            return []
        return list(src_path.rglob("*.java"))

    def _get_imports(self, file_path: Path) -> List[str]:
        """Extract import statements from a Java file"""
        imports = []
        try:
            content = file_path.read_text(encoding="utf-8")
            for line in content.splitlines():
                match = re.match(r'^import\s+([\w.]+)', line.strip())
                if match:
                    imports.append(match.group(1))
        except Exception:
            pass
        return imports

    def _check_domain_purity(self, module: str):
        """Check domain layer has zero framework dependencies"""
        if "domain" not in module:
            return

        forbidden_patterns = [
            ("org.springframework", "Spring Framework"),
            ("javax.persistence", "JPA"),
            ("jakarta.persistence", "JPA"),
            ("org.apache.ibatis", "MyBatis"),
            ("org.mybatis", "MyBatis"),
            ("org.hibernate", "Hibernate"),
            ("java.sql", "JDBC"),
        ]

        java_files = self._find_java_files(module)
        for file_path in java_files:
            imports = self._get_imports(file_path)
            for imp in imports:
                for prefix, framework in forbidden_patterns:
                    if imp.startswith(prefix):
                        self._add_violation(
                            "P0",
                            "domain-purity",
                            f"Domain layer imports {framework}: {imp}",
                            str(file_path),
                        )

    def _check_layer_dependencies(self, module: str, all_modules: List[str]):
        """Check layer dependency direction rules"""
        is_domain = "domain" in module
        is_app = "app" in module or "application" in module
        is_adapter = "adapter" in module
        is_infra = "infra" in module

        java_files = self._find_java_files(module)
        for file_path in java_files:
            imports = self._get_imports(file_path)

            for imp in imports:
                imp_module = self._extract_module(imp, all_modules)

                if is_domain and imp_module and imp_module != module:
                    if "infra" in imp_module or "adapter" in imp_module or "app" in imp_module:
                        self._add_violation(
                            "P0",
                            "dependency-direction",
                            f"Domain depends on {imp_module}: {imp}",
                            str(file_path),
                        )

                if is_app and imp_module and "adapter" in imp_module:
                    self._add_violation(
                        "P1",
                        "dependency-direction",
                        f"Application depends on Adapter: {imp}",
                        str(file_path),
                    )

    def _extract_module(self, import_path: str, modules: List[str]) -> str:
        """Extract which module an import belongs to"""
        for module in modules:
            module_pkg = module.replace("-", ".")
            if module_pkg in import_path or module in import_path:
                return module
        return ""

    def _check_package_naming(self, module: str):
        """Check package naming follows COLA conventions"""
        java_files = self._find_java_files(module)
        for file_path in java_files:
            content = file_path.read_text(encoding="utf-8")
            match = re.search(r'package\s+([\w.]+)', content)
            if not match:
                continue
            package = match.group(1)

            is_domain = "domain" in module
            is_app = "app" in module or "application" in module
            is_adapter = "adapter" in module
            is_infra = "infra" in module

            if is_domain and ("service" in package):
                pass
            elif is_app and ("controller" in package):
                self._add_violation(
                    "P1", "naming",
                    f"Application layer contains 'controller' package: {package}",
                    str(file_path),
                )
            elif is_adapter and ("repository" in package):
                self._add_violation(
                    "P1", "naming",
                    f"Adapter layer contains 'repository' package: {package}",
                    str(file_path),
                )

    def _check_circular_dependencies(self, modules: List[str]):
        """Detect circular dependencies between modules"""
        deps = defaultdict(set)
        for module in modules:
            java_files = self._find_java_files(module)
            for file_path in java_files:
                imports = self._get_imports(file_path)
                for imp in imports:
                    imp_module = self._extract_module(imp, modules)
                    if imp_module and imp_module != module:
                        deps[module].add(imp_module)

        for module in modules:
            visited = set()
            if self._has_cycle(module, module, deps, visited):
                self._add_violation(
                    "P0", "circular-dependency",
                    f"Circular dependency detected involving module: {module}",
                    str(self.project_path),
                )

    def _has_cycle(self, start: str, current: str,
                   deps: Dict[str, Set[str]], visited: Set[str]) -> bool:
        """Detect cycle in dependency graph using DFS"""
        if current in visited:
            return current == start
        visited.add(current)
        for neighbor in deps.get(current, set()):
            if self._has_cycle(start, neighbor, deps, visited.copy()):
                return True
        return False

    def _add_violation(self, severity: str, rule: str, message: str, location: str):
        """Add a violation record"""
        self.violations.append({
            "severity": severity,
            "rule": rule,
            "message": message,
            "location": location,
        })

    def _calculate_score(self) -> float:
        """Calculate compliance score"""
        if not self.violations:
            return 100.0

        weights = {"P0": 10, "P1": 5, "P2": 2}
        penalty = sum(weights.get(v["severity"], 1) for v in self.violations)
        return max(0.0, 100.0 - penalty)

    def _grade(self, score: float) -> str:
        """Convert score to grade"""
        if score >= 90:
            return "A (Excellent)"
        elif score >= 70:
            return "B (Good)"
        elif score >= 50:
            return "C (Fair)"
        else:
            return "D (Needs Refactoring)"


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_cola.py <project_path>")
        sys.exit(1)

    checker = COLAComplianceChecker(sys.argv[1])
    report = checker.check()

    print("=" * 60)
    print("COLA Architecture Compliance Report")
    print("=" * 60)
    print(f"Project: {report.get('project', 'N/A')}")
    print(f"Modules: {', '.join(report.get('modules', []))}")
    print(f"Score: {report['score']:.1f}/100")
    print(f"Grade: {report['grade']}")
    print("-" * 60)

    violations = report.get("violations", [])
    if violations:
        print(f"\nViolations Found: {len(violations)}")
        for severity in ["P0", "P1", "P2"]:
            sev_violations = [v for v in violations if v["severity"] == severity]
            if sev_violations:
                print(f"\n  [{severity}] {len(sev_violations)} issues:")
                for v in sev_violations:
                    print(f"    - {v['message']}")
                    print(f"      Location: {v['location']}")
    else:
        print("\nNo violations found! 🎉")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
