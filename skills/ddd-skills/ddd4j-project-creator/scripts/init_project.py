#!/usr/bin/env python3
"""
DDD Project Initialization Script

This script creates a new DDD project structure based on the selected type:
- single-module: Single Maven module monolith
- multi-module: Multi-module monolith
- microservices: Microservices architecture
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional


class DDDProjectInitializer:
    """DDD Project Initializer"""
    
    def __init__(self, project_dir: str = "."):
        self.project_dir = Path(project_dir).resolve()
        self.project_dir.mkdir(parents=True, exist_ok=True)
    
    def init_single_module(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        parent_version: str,
        package_base: str,
        architecture: str = "ddd-classic"
    ):
        """Initialize single-module monolith project"""
        project_path = self.project_dir / artifact_id
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Create directory structure
        src_main_java = project_path / "src" / "main" / "java" / package_base.replace(".", "/")
        src_main_resources = project_path / "src" / "main" / "resources"
        src_test_java = project_path / "src" / "test" / "java" / package_base.replace(".", "/")
        src_test_resources = project_path / "src" / "test" / "resources"
        
        for path in [src_main_java, src_main_resources, src_test_java, src_test_resources]:
            path.mkdir(parents=True, exist_ok=True)
        
        # Create layer directories
        layers = self._get_layers(architecture)
        for layer in layers:
            layer_path = src_main_java / layer
            layer_path.mkdir(parents=True, exist_ok=True)
            # Create package-info.java
            self._create_package_info(layer_path, f"{package_base}.{layer}")
        
        # Create pom.xml
        self._create_single_module_pom(
            project_path, group_id, artifact_id, version, parent_version
        )
        
        # Create application class
        app_class_name = self._to_class_name(artifact_id)
        self._create_application_class(
            src_main_java, package_base, app_class_name
        )
        
        # Create common files
        self._create_common_files(project_path, artifact_id)
        
        return str(project_path)
    
    def init_multi_module(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        parent_version: str,
        package_base: str,
        modules: List[str],
        architecture: str = "ddd-classic"
    ):
        """Initialize multi-module monolith project"""
        project_path = self.project_dir / artifact_id
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Create parent pom.xml
        self._create_parent_pom(
            project_path, group_id, artifact_id, version, parent_version, modules
        )
        
        # Create BOM and dependencies modules
        self._create_bom_module(project_path, group_id, artifact_id, version, package_base)
        self._create_dependencies_module(project_path, group_id, artifact_id, version, package_base)
        
        # Create common module
        self._create_common_module(project_path, group_id, artifact_id, version, package_base)
        
        # Create business modules
        for module_name in modules:
            self._create_business_module(
                project_path, group_id, artifact_id, version, package_base,
                module_name, architecture
            )
        
        # Create start module
        self._create_start_module(
            project_path, group_id, artifact_id, version, package_base, modules
        )
        
        # Create common files
        self._create_common_files(project_path, artifact_id)
        
        return str(project_path)
    
    def init_microservices(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        parent_version: str,
        package_base: str,
        services: List[str],
        architecture: str = "ddd-classic"
    ):
        """Initialize microservices project"""
        project_path = self.project_dir / artifact_id
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Create parent pom.xml
        self._create_microservices_parent_pom(
            project_path, group_id, artifact_id, version, parent_version, services
        )
        
        # Create platform-common
        self._create_platform_common(project_path, group_id, artifact_id, version, package_base)
        
        # Create services
        services_dir = project_path / "services"
        services_dir.mkdir(parents=True, exist_ok=True)
        
        for service_name in services:
            self._create_service(
                services_dir, group_id, artifact_id, version, package_base,
                service_name, architecture
            )
        
        # Create gateway
        self._create_gateway(project_path, group_id, artifact_id, version, package_base)
        
        # Create common files
        self._create_common_files(project_path, artifact_id)
        
        return str(project_path)
    
    def _get_layers(self, architecture: str) -> List[str]:
        """Get layer names based on architecture"""
        layer_map = {
            "ddd-classic": ["interfaces", "application", "domain", "infrastructure"],
            "hexagonal": ["adapter", "application", "domain", "infrastructure"],
            "clean": ["interfaces", "application", "domain", "infrastructure"],
            "cola-v5": ["adapter", "app", "domain", "infrastructure"]
        }
        return layer_map.get(architecture, layer_map["ddd-classic"])
    
    def _create_package_info(self, path: Path, package_name: str):
        """Create package-info.java file"""
        package_info = path / "package-info.java"
        content = f"""/**
 * {package_name}
 * 
 * This package contains the {path.name} layer components.
 */
package {package_name};
"""
        package_info.write_text(content, encoding="utf-8")
    
    def _create_single_module_pom(
        self, project_path: Path, group_id: str, artifact_id: str,
        version: str, parent_version: str
    ):
        """Create single-module pom.xml"""
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>ddd4j-cloud-parent</artifactId>
        <version>{parent_version}</version>
        <relativePath/>
    </parent>

    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
    <packaging>jar</packaging>

    <name>{artifact_id}</name>
    <description>DDD Single-Module Monolith Project</description>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
"""
        (project_path / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_application_class(self, src_main_java: Path, package_base: str, class_name: str):
        """Create Spring Boot application class"""
        app_package = src_main_java
        app_package.mkdir(parents=True, exist_ok=True)
        
        app_class = app_package / f"{class_name}Application.java"
        content = f"""package {package_base};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * {class_name} Application
 * 
 * Main application entry point.
 */
@SpringBootApplication
public class {class_name}Application {{

    public static void main(String[] args) {{
        SpringApplication.run({class_name}Application.class, args);
    }}
}}
"""
        app_class.write_text(content, encoding="utf-8")
    
    def _create_common_files(self, project_path: Path, artifact_id: str):
        """Create common files (.gitignore, LICENSE, README.md)"""
        # .gitignore
        gitignore_content = """# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# IDE
.idea/
*.iml
*.iws
*.ipr
.vscode/
.classpath
.project
.settings/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
"""
        (project_path / ".gitignore").write_text(gitignore_content, encoding="utf-8")
        
        # LICENSE
        license_content = """MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        (project_path / "LICENSE").write_text(license_content, encoding="utf-8")
        
        # README.md
        readme_content = f"""# {artifact_id}

DDD (Domain-Driven Design) Project

## Project Structure

This project follows DDD principles with clear layer separation.

## Getting Started

### Prerequisites

- Java 17+
- Maven 3.6+

### Building

```bash
mvn clean install
```

### Running

```bash
mvn spring-boot:run
```

## Architecture

This project uses DDD Classic Layered Architecture:
- **interfaces**: Interface layer (Controllers, DTOs)
- **application**: Application layer (Application Services, Commands, Queries)
- **domain**: Domain layer (Aggregates, Entities, Value Objects)
- **infrastructure**: Infrastructure layer (Repository Implementations, External Services)
"""
        (project_path / "README.md").write_text(readme_content, encoding="utf-8")
    
    def _to_class_name(self, artifact_id: str) -> str:
        """Convert artifact_id to class name (e.g., ddd4j-order -> Ddd4jOrder)"""
        parts = artifact_id.split("-")
        return "".join(word.capitalize() for word in parts)
    
    def _create_parent_pom(
        self, project_path: Path, group_id: str, artifact_id: str,
        version: str, parent_version: str, modules: List[str]
    ):
        """Create parent pom.xml for multi-module project"""
        module_list = "\n".join(f"        <module>{artifact_id}-{module}</module>" for module in modules)
        module_list += f"\n        <module>{artifact_id}-common</module>"
        module_list += f"\n        <module>{artifact_id}-start</module>"
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>ddd4j-cloud-parent</artifactId>
        <version>{parent_version}</version>
        <relativePath/>
    </parent>

    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
    <packaging>pom</packaging>

    <name>{artifact_id}</name>
    <description>DDD Multi-Module Monolith Project</description>

    <modules>
        <module>{artifact_id}-bom</module>
        <module>{artifact_id}-dependencies</module>
{module_list}
    </modules>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
</project>
"""
        (project_path / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_bom_module(self, project_path: Path, group_id: str, artifact_id: str, version: str, package_base: str):
        """Create BOM module"""
        bom_dir = project_path / f"{artifact_id}-bom"
        bom_dir.mkdir(parents=True, exist_ok=True)
        
        src_main_java = bom_dir / "src" / "main" / "java" / package_base.replace(".", "/") / "bom"
        src_main_java.mkdir(parents=True, exist_ok=True)
        self._create_package_info(src_main_java, f"{package_base}.bom")
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-bom</artifactId>
    <packaging>pom</packaging>

    <name>{artifact_id}-bom</name>
    <description>BOM Dependency Management</description>
</project>
"""
        (bom_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_dependencies_module(self, project_path: Path, group_id: str, artifact_id: str, version: str, package_base: str):
        """Create dependencies module"""
        deps_dir = project_path / f"{artifact_id}-dependencies"
        deps_dir.mkdir(parents=True, exist_ok=True)
        
        src_main_java = deps_dir / "src" / "main" / "java" / package_base.replace(".", "/") / "dependencies"
        src_main_java.mkdir(parents=True, exist_ok=True)
        self._create_package_info(src_main_java, f"{package_base}.dependencies")
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-dependencies</artifactId>
    <packaging>pom</packaging>

    <name>{artifact_id}-dependencies</name>
    <description>Common Dependencies</description>
</project>
"""
        (deps_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_common_module(self, project_path: Path, group_id: str, artifact_id: str, version: str, package_base: str):
        """Create common module"""
        common_dir = project_path / f"{artifact_id}-common"
        common_dir.mkdir(parents=True, exist_ok=True)
        
        # Create sub-modules
        for sub_module in ["domain", "infrastructure"]:
            sub_dir = common_dir / f"{artifact_id}-common-{sub_module}"
            sub_dir.mkdir(parents=True, exist_ok=True)
            
            src_main_java = sub_dir / "src" / "main" / "java" / package_base.replace(".", "/") / "common" / sub_module
            src_main_java.mkdir(parents=True, exist_ok=True)
            self._create_package_info(src_main_java, f"{package_base}.common.{sub_module}")
            
            pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}-common</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-common-{sub_module}</artifactId>
    <packaging>jar</packaging>

    <name>{artifact_id}-common-{sub_module}</name>
    <description>Common {sub_module.capitalize()} Module</description>
</project>
"""
            (sub_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
        
        # Common parent pom
        common_pom = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-common</artifactId>
    <packaging>pom</packaging>

    <name>{artifact_id}-common</name>
    <description>Common Modules</description>

    <modules>
        <module>{artifact_id}-common-domain</module>
        <module>{artifact_id}-common-infrastructure</module>
    </modules>
</project>
"""
        (common_dir / "pom.xml").write_text(common_pom, encoding="utf-8")
    
    def _create_business_module(
        self, project_path: Path, group_id: str, artifact_id: str,
        version: str, package_base: str, module_name: str, architecture: str
    ):
        """Create business module with all layers"""
        module_dir = project_path / f"{artifact_id}-{module_name}"
        module_dir.mkdir(parents=True, exist_ok=True)
        
        layers = self._get_layers(architecture)
        layer_suffixes = {
            "interfaces": "adapter",
            "application": "app",
            "domain": "domain",
            "infrastructure": "infrastructure",
            "adapter": "adapter",
            "app": "app"
        }
        
        # Create sub-modules for each layer
        for layer in layers:
            layer_suffix = layer_suffixes.get(layer, layer)
            sub_module_dir = module_dir / f"{artifact_id}-{module_name}-{layer_suffix}"
            sub_module_dir.mkdir(parents=True, exist_ok=True)
            
            src_main_java = sub_module_dir / "src" / "main" / "java" / package_base.replace(".", "/") / module_name / layer
            src_main_java.mkdir(parents=True, exist_ok=True)
            self._create_package_info(src_main_java, f"{package_base}.{module_name}.{layer}")
            
            pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}-{module_name}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-{module_name}-{layer_suffix}</artifactId>
    <packaging>jar</packaging>

    <name>{artifact_id}-{module_name}-{layer_suffix}</name>
    <description>{module_name.capitalize()} {layer.capitalize()} Layer</description>
"""
            if layer == "domain":
                pom_content += f"""
    <dependencies>
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-common-domain</artifactId>
            <version>${{project.version}}</version>
        </dependency>
    </dependencies>
"""
            elif layer == "infrastructure":
                pom_content += f"""
    <dependencies>
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-{module_name}-domain</artifactId>
            <version>${{project.version}}</version>
        </dependency>
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-common-infrastructure</artifactId>
            <version>${{project.version}}</version>
        </dependency>
    </dependencies>
"""
            elif layer in ["application", "app"]:
                pom_content += f"""
    <dependencies>
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-{module_name}-domain</artifactId>
            <version>${{project.version}}</version>
        </dependency>
    </dependencies>
"""
            elif layer in ["interfaces", "adapter"]:
                pom_content += f"""
    <dependencies>
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-{module_name}-app</artifactId>
            <version>${{project.version}}</version>
        </dependency>
    </dependencies>
"""
            
            pom_content += "</project>\n"
            (sub_module_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
        
        # Module parent pom
        module_list = "\n".join(
            f"        <module>{artifact_id}-{module_name}-{layer_suffixes.get(layer, layer)}</module>"
            for layer in layers
        )
        module_pom = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-{module_name}</artifactId>
    <packaging>pom</packaging>

    <name>{artifact_id}-{module_name}</name>
    <description>{module_name.capitalize()} Business Module</description>

    <modules>
{module_list}
    </modules>
</project>
"""
        (module_dir / "pom.xml").write_text(module_pom, encoding="utf-8")
    
    def _create_start_module(
        self, project_path: Path, group_id: str, artifact_id: str,
        version: str, package_base: str, modules: List[str]
    ):
        """Create start module"""
        start_dir = project_path / f"{artifact_id}-start"
        start_dir.mkdir(parents=True, exist_ok=True)
        
        src_main_java = start_dir / "src" / "main" / "java" / package_base.replace(".", "/")
        src_main_java.mkdir(parents=True, exist_ok=True)
        
        app_class_name = self._to_class_name(artifact_id)
        self._create_application_class(src_main_java, package_base, app_class_name)
        
        src_main_resources = start_dir / "src" / "main" / "resources"
        src_main_resources.mkdir(parents=True, exist_ok=True)
        (src_main_resources / "application.yml").write_text("spring:\n  application:\n    name: " + artifact_id + "\n", encoding="utf-8")
        
        # Dependencies on all business modules
        dependencies = "\n".join(
            f"""        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-{module}-adapter</artifactId>
            <version>${{project.version}}</version>
        </dependency>"""
            for module in modules
        )
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{artifact_id}-start</artifactId>
    <packaging>jar</packaging>

    <name>{artifact_id}-start</name>
    <description>Application Start Module</description>

    <dependencies>
{dependencies}
        <dependency>
            <groupId>{group_id}</groupId>
            <artifactId>{artifact_id}-common-infrastructure</artifactId>
            <version>${{project.version}}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
"""
        (start_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_microservices_parent_pom(
        self, project_path: Path, group_id: str, artifact_id: str,
        version: str, parent_version: str, services: List[str]
    ):
        """Create parent pom.xml for microservices project"""
        service_modules = "\n".join(f"        <module>services/{service}</module>" for service in services)
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>ddd4j-cloud-parent</artifactId>
        <version>{parent_version}</version>
        <relativePath/>
    </parent>

    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
    <packaging>pom</packaging>

    <name>{artifact_id}</name>
    <description>DDD Microservices Platform</description>

    <modules>
        <module>platform-common</module>
{service_modules}
        <module>gateway</module>
    </modules>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
</project>
"""
        (project_path / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_platform_common(self, project_path: Path, group_id: str, artifact_id: str, version: str, package_base: str):
        """Create platform-common module"""
        common_dir = project_path / "platform-common"
        common_dir.mkdir(parents=True, exist_ok=True)
        
        src_main_java = common_dir / "src" / "main" / "java" / package_base.replace(".", "/") / "common"
        src_main_java.mkdir(parents=True, exist_ok=True)
        self._create_package_info(src_main_java, f"{package_base}.common")
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>platform-common</artifactId>
    <packaging>jar</packaging>

    <name>platform-common</name>
    <description>Platform Common Module</description>
</project>
"""
        (common_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
    
    def _create_service(
        self, services_dir: Path, group_id: str, artifact_id: str,
        version: str, package_base: str, service_name: str, architecture: str
    ):
        """Create microservice with all modules"""
        service_dir = services_dir / service_name
        service_dir.mkdir(parents=True, exist_ok=True)
        
        layers = self._get_layers(architecture)
        service_modules = ["api", "domain", "application", "infrastructure", "interfaces", "start"]
        
        for module_suffix in service_modules:
            module_dir = service_dir / f"{service_name}-{module_suffix}"
            module_dir.mkdir(parents=True, exist_ok=True)
            
            if module_suffix == "start":
                src_main_java = module_dir / "src" / "main" / "java" / package_base.replace(".", "/") / service_name.replace("-service", "")
                src_main_java.mkdir(parents=True, exist_ok=True)
                app_class_name = self._to_class_name(service_name.replace("-service", ""))
                self._create_application_class(src_main_java, f"{package_base}.{service_name.replace('-service', '')}", app_class_name)
            else:
                src_main_java = module_dir / "src" / "main" / "java" / package_base.replace(".", "/") / service_name.replace("-service", "") / module_suffix
                src_main_java.mkdir(parents=True, exist_ok=True)
                self._create_package_info(src_main_java, f"{package_base}.{service_name.replace('-service', '')}.{module_suffix}")
            
            pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{service_name}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{service_name}-{module_suffix}</artifactId>
    <packaging>jar</packaging>

    <name>{service_name}-{module_suffix}</name>
    <description>{service_name} {module_suffix.capitalize()} Module</description>
"""
            if module_suffix == "start":
                pom_content += """
    <dependencies>
        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>${service-name}-interfaces</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>${service-name}-application</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>${service-name}-infrastructure</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>platform-common</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
"""
            
            pom_content += "</project>\n"
            (module_dir / "pom.xml").write_text(pom_content, encoding="utf-8")
        
        # Service parent pom
        module_list = "\n".join(f"        <module>{service_name}-{module}</module>" for module in service_modules)
        service_pom = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>{service_name}</artifactId>
    <packaging>pom</packaging>

    <name>{service_name}</name>
    <description>{service_name.replace('-', ' ').title()} Microservice</description>

    <modules>
{module_list}
    </modules>
</project>
"""
        (service_dir / "pom.xml").write_text(service_pom, encoding="utf-8")
    
    def _create_gateway(self, project_path: Path, group_id: str, artifact_id: str, version: str, package_base: str):
        """Create gateway service"""
        gateway_dir = project_path / "gateway"
        gateway_dir.mkdir(parents=True, exist_ok=True)
        
        start_dir = gateway_dir / "gateway-start"
        start_dir.mkdir(parents=True, exist_ok=True)
        
        src_main_java = start_dir / "src" / "main" / "java" / package_base.replace(".", "/") / "gateway"
        src_main_java.mkdir(parents=True, exist_ok=True)
        
        app_class = src_main_java / "GatewayApplication.java"
        content = f"""package {package_base}.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Gateway Application
 */
@SpringBootApplication
public class GatewayApplication {{

    public static void main(String[] args) {{
        SpringApplication.run(GatewayApplication.class, args);
    }}
}}
"""
        app_class.write_text(content, encoding="utf-8")
        
        pom_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </parent>

    <artifactId>gateway</artifactId>
    <packaging>pom</packaging>

    <name>gateway</name>
    <description>API Gateway Service</description>

    <modules>
        <module>gateway-start</module>
    </modules>
</project>
"""
        (gateway_dir / "pom.xml").write_text(pom_content, encoding="utf-8")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: init_project.py <project-type> [options]", file=sys.stderr)
        print("Project types: single-module, multi-module, microservices", file=sys.stderr)
        sys.exit(1)
    
    project_type = sys.argv[1]
    
    # Parse configuration from JSON or command line
    if len(sys.argv) >= 3:
        config = json.loads(sys.argv[2])
    else:
        # Default configuration
        config = {
            "groupId": "io.ddd4j.base",
            "artifactId": "ddd4j-project",
            "version": "1.0.0-SNAPSHOT",
            "parentVersion": "2023.0.x.20251205-SNAPSHOT",
            "packageBase": "io.ddd4j.project",
            "architecture": "ddd-classic"
        }
    
    initializer = DDDProjectInitializer()
    
    if project_type == "single-module":
        result = initializer.init_single_module(
            config["groupId"],
            config["artifactId"],
            config["version"],
            config["parentVersion"],
            config["packageBase"],
            config.get("architecture", "ddd-classic")
        )
        print(json.dumps({"status": "success", "path": result}))
    
    elif project_type == "multi-module":
        modules = config.get("modules", ["api"])
        result = initializer.init_multi_module(
            config["groupId"],
            config["artifactId"],
            config["version"],
            config["parentVersion"],
            config["packageBase"],
            modules,
            config.get("architecture", "ddd-classic")
        )
        print(json.dumps({"status": "success", "path": result}))
    
    elif project_type == "microservices":
        services = config.get("services", ["user-service", "order-service"])
        result = initializer.init_microservices(
            config["groupId"],
            config["artifactId"],
            config["version"],
            config["parentVersion"],
            config["packageBase"],
            services,
            config.get("architecture", "ddd-classic")
        )
        print(json.dumps({"status": "success", "path": result}))
    
    else:
        print(json.dumps({"status": "error", "message": f"Unknown project type: {project_type}"}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
