---
name: flutter-project-creater
description: "Provides one-command project creation for Flutter including project initialization, configuration, and template generation. Use when the user asks about creating Flutter projects, needs to initialize a new Flutter project, or generate Flutter project structure."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create a new Flutter project from scratch
- Choose target platforms (Android, iOS, web, desktop)
- Configure organization name and package identifier
- Set up the initial project structure with dependencies
- Generate a Flutter project with a specific template

## How to use this skill

### Workflow

1. **Gather requirements**: project name, organization, target platforms, and any preferred packages
2. **Run `flutter create`** with the appropriate flags
3. **Configure `pubspec.yaml`** with initial dependencies and assets
4. **Verify** the project builds and runs with `flutter run`

### 1. Project Creation

```bash
# Basic project creation
flutter create my_app

# With organization and platform selection
flutter create my_app --org com.example --platforms android,ios,web

# Create a package or plugin
flutter create --template=package my_package
flutter create --template=plugin my_plugin --platforms android,ios
```

### 2. Project Structure

```
my_app/
├── lib/
│   └── main.dart          # Entry point
├── test/
│   └── widget_test.dart   # Widget tests
├── android/               # Android native code
├── ios/                   # iOS native code
├── pubspec.yaml           # Dependencies and metadata
└── README.md
```

### 3. Configure pubspec.yaml

```yaml
name: my_app
description: A new Flutter application.
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
  assets:
    - assets/images/
```

### 4. Initial Run

```bash
# Install dependencies
flutter pub get

# Run on connected device
flutter run

# Build release APK
flutter build apk --release
```

## Best Practices

- Use a consistent organization name (`--org`) across projects
- Lock dependency versions in `pubspec.yaml` for reproducible builds
- Remove default comments and sample code before expanding the project
- Run `flutter doctor` to verify the development environment is set up correctly
- Set up CI with `flutter test` and `flutter build` early in the project lifecycle

## Resources

- Getting started: https://docs.flutter.dev/get-started
- CLI reference: https://docs.flutter.dev/reference/flutter-cli

## Keywords

flutter create, project creation, initialization, cross-platform, pubspec, scaffolding, Flutter CLI
