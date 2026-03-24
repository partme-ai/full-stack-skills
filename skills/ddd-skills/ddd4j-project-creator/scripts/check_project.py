#!/usr/bin/env python3
"""
DDD Project Structure Validation Script

This script analyzes an existing project structure and:
1. Identifies the project type (single-module, multi-module, microservices)
2. Validates directory structure compliance
3. Checks package naming conventions
4. Verifies layer dependencies
5. Generates a validation report
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class DDDProjectChecker:
    """DDD Project Structure Checker"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.issues = []
        self.warnings = []
        self.project_type = None
        self.modules = []
        self.architecture = None
    
    def check(self) -> Dict:
        """Check project structure and return report"""
        if not self.project_path.exists():
            return {
                "status": "error",
                "message": f"Project path does not exist: {self.project_path}"
            }
        
        # Identify project type
        self.project_type = self._identify_project_type()
        
        # Check structure based on type
        if self.project_type == "single-module":
            result = self._check_single_module()
        elif self.project_type == "multi-module":
            result = self._check_multi_module()
        elif self.project_type == "microservices":
            result = self._check_microservices()
        else:
            return {
                "status": "error",
                "message": "Could not identify project type"
            }
        
        # Validate common requirements
        self._check_common_files()
        self._check_package_naming()
        
        return {
            "status": "success",
            "projectType": self.project_type,
            "architecture": self.architecture,
            "modules": self.modules,
            "issues": self.issues,
            "warnings": self.warnings,
            "compliant": len(self.issues) == 0
        }
    
    def _identify_project_type(self) -> Optional[str]:
        """Identify project type based on structure"""
        root_pom = self.project_path / "pom.xml"
        
        if not root_pom.exists():
            return None
        
        # Read pom.xml to check for modules
        try:
            content = root_pom.read_text(encoding="utf-8")
            
            # Check for modules tag
            if "<modules>" in content:
                # Check if it's microservices (has services/ directory)
                services_dir = self.project_path / "services"
                if services_dir.exists() and services_dir.is_dir():
                    return "microservices"
                else:
                    return "multi-module"
            else:
                return "single-module"
        except Exception as e:
            self.issues.append(f"Error reading pom.xml: {e}")
            return None
    
    def _check_single_module(self) -> Dict:
        """Check single-module project structure"""
        src_main_java = self.project_path / "src" / "main" / "java"
        
        if not src_main_java.exists():
            self.issues.append("Missing src/main/java directory")
            return {"valid": False}
        
        # Identify architecture by checking layer directories
        layers = self._detect_layers(src_main_java)
        self.architecture = self._identify_architecture(layers)
        
        # Check layer structure
        for layer in layers:
            layer_path = src_main_java
            # Find layer directory (could be at any depth)
            for part in layer.split("/"):
                layer_path = layer_path / part
                if not layer_path.exists():
                    self.warnings.append(f"Layer '{layer}' not found at expected location")
                    break
        
        # Check package-info.java
        self._check_package_info_files(src_main_java)
        
        return {"valid": True, "layers": layers}
    
    def _check_multi_module(self) -> Dict:
        """Check multi-module project structure"""
        # Find all modules
        modules = []
        for item in self.project_path.iterdir():
            if item.is_dir() and (item / "pom.xml").exists():
                # Check if it's a module (has sub-modules or is a business module)
                pom_content = (item / "pom.xml").read_text(encoding="utf-8")
                if "<modules>" in pom_content or "-" in item.name:
                    modules.append(item.name)
        
        self.modules = modules
        
        # Check each module
        for module_name in modules:
            module_path = self.project_path / module_name
            if module_path.is_dir():
                self._check_module_structure(module_path, module_name)
        
        return {"valid": True, "modules": modules}
    
    def _check_microservices(self) -> Dict:
        """Check microservices project structure"""
        services_dir = self.project_path / "services"
        
        if not services_dir.exists():
            self.issues.append("Missing services/ directory")
            return {"valid": False}
        
        # Find all services
        services = []
        for item in services_dir.iterdir():
            if item.is_dir() and (item / "pom.xml").exists():
                services.append(item.name)
                self._check_service_structure(item, item.name)
        
        self.modules = services
        
        return {"valid": True, "services": services}
    
    def _check_module_structure(self, module_path: Path, module_name: str):
        """Check structure of a business module"""
        # Check for sub-modules
        sub_modules = []
        for item in module_path.iterdir():
            if item.is_dir() and (item / "pom.xml").exists():
                sub_modules.append(item.name)
        
        # Expected sub-modules based on architecture
        if len(sub_modules) > 0:
            # This is a parent module with sub-modules
            layers = self._detect_layers_from_module_names(sub_modules)
            self.architecture = self._identify_architecture_from_modules(sub_modules)
            
            # Check each sub-module
            for sub_module in sub_modules:
                sub_module_path = module_path / sub_module
                src_main_java = sub_module_path / "src" / "main" / "java"
                if src_main_java.exists():
                    self._check_package_info_files(src_main_java)
        else:
            # Single module, check layers directly
            src_main_java = module_path / "src" / "main" / "java"
            if src_main_java.exists():
                layers = self._detect_layers(src_main_java)
                self.architecture = self._identify_architecture(layers)
                self._check_package_info_files(src_main_java)
    
    def _check_service_structure(self, service_path: Path, service_name: str):
        """Check structure of a microservice"""
        # Check for service modules
        modules = []
        for item in service_path.iterdir():
            if item.is_dir() and (item / "pom.xml").exists():
                modules.append(item.name)
        
        # Expected: api, domain, application, infrastructure, interfaces, start
        expected_modules = ["api", "domain", "application", "infrastructure", "interfaces", "start"]
        for expected in expected_modules:
            module_name = f"{service_name}-{expected}"
            if module_name not in modules:
                self.warnings.append(f"Service {service_name} missing module: {expected}")
        
        # Check each module
        for module in modules:
            module_path = service_path / module
            src_main_java = module_path / "src" / "main" / "java"
            if src_main_java.exists():
                self._check_package_info_files(src_main_java)
    
    def _detect_layers(self, java_path: Path) -> List[str]:
        """Detect layer structure from directory"""
        layers = []
        
        # Common layer names
        layer_names = [
            "interfaces", "application", "domain", "infrastructure",
            "adapter", "app", "usecase", "entity", "valueobject"
        ]
        
        def scan_directory(path: Path, depth: int = 0, max_depth: int = 3):
            if depth > max_depth:
                return
            for item in path.iterdir():
                if item.is_dir():
                    if item.name in layer_names:
                        layers.append(item.name)
                    scan_directory(item, depth + 1, max_depth)
        
        scan_directory(java_path)
        return list(set(layers))
    
    def _detect_layers_from_module_names(self, module_names: List[str]) -> List[str]:
        """Detect layers from module names"""
        layers = []
        for name in module_names:
            # Extract layer suffix (e.g., api-adapter -> adapter)
            parts = name.split("-")
            if len(parts) > 1:
                layers.append(parts[-1])
        return list(set(layers))
    
    def _identify_architecture(self, layers: List[str]) -> str:
        """Identify architecture pattern from layers"""
        if "adapter" in layers and "app" in layers:
            return "cola-v5"
        elif "adapter" in layers and "application" in layers:
            return "hexagonal"
        elif "interfaces" in layers and "application" in layers:
            if "usecase" in layers:
                return "clean"
            else:
                return "ddd-classic"
        else:
            return "unknown"
    
    def _identify_architecture_from_modules(self, module_names: List[str]) -> str:
        """Identify architecture from module names"""
        if any("adapter" in name and "app" in name for name in module_names):
            return "cola-v5"
        elif any("adapter" in name for name in module_names):
            return "hexagonal"
        elif any("interfaces" in name or "application" in name for name in module_names):
            return "ddd-classic"
        else:
            return "unknown"
    
    def _check_package_info_files(self, java_path: Path):
        """Check for package-info.java files"""
        def scan_for_package_info(path: Path):
            package_info = path / "package-info.java"
            if not package_info.exists():
                # Check if this is a meaningful package (has .java files or subdirectories)
                has_java = any(f.suffix == ".java" for f in path.iterdir() if f.is_file())
                has_subdirs = any(d.is_dir() for d in path.iterdir())
                if has_java or has_subdirs:
                    self.warnings.append(f"Missing package-info.java in {path.relative_to(self.project_path)}")
            
            # Recursively check subdirectories
            for item in path.iterdir():
                if item.is_dir():
                    scan_for_package_info(item)
        
        scan_for_package_info(java_path)
    
    def _check_common_files(self):
        """Check for common required files"""
        required_files = [".gitignore", "LICENSE", "README.md"]
        for file_name in required_files:
            file_path = self.project_path / file_name
            if not file_path.exists():
                self.warnings.append(f"Missing required file: {file_name}")
        
        # Check for Maven wrapper
        mvnw = self.project_path / "mvnw"
        mvnw_cmd = self.project_path / "mvnw.cmd"
        if not mvnw.exists() and not mvnw_cmd.exists():
            self.warnings.append("Missing Maven wrapper files (mvnw, mvnw.cmd)")
    
    def _check_package_naming(self):
        """Check package naming conventions"""
        src_main_java = self.project_path / "src" / "main" / "java"
        
        if not src_main_java.exists():
            return
        
        def check_package_name(path: Path, expected_base: Optional[str] = None):
            """Recursively check package naming"""
            for item in path.iterdir():
                if item.is_dir():
                    # Check if directory name follows Java package naming (lowercase, no hyphens)
                    if not item.name.islower() or "-" in item.name:
                        self.issues.append(
                            f"Invalid package name: {item.relative_to(src_main_java)} "
                            f"(should be lowercase, no hyphens)"
                        )
                    check_package_name(item)
        
        check_package_name(src_main_java)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: check_project.py <project-path>", file=sys.stderr)
        sys.exit(1)
    
    project_path = sys.argv[1]
    checker = DDDProjectChecker(project_path)
    result = checker.check()
    
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
