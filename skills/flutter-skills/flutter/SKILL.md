---
name: flutter
description: "Provides comprehensive guidance for Flutter development including widgets, state management, navigation, platform channels, and mobile app development. Use when the user asks about Flutter, needs to create Flutter applications, implement Flutter widgets, or work with Flutter features."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build cross-platform mobile, web, or desktop applications with Flutter
- Create and compose Flutter widgets (StatelessWidget, StatefulWidget)
- Implement state management (setState, Provider, Riverpod, Bloc)
- Set up navigation and routing in Flutter apps
- Configure themes, assets, and platform-specific settings
- Use platform channels for native interop
- Optimize Flutter app performance (const widgets, keys, build methods)
- Debug and hot-reload Flutter applications

## How to use this skill

### Workflow

1. **Identify the request area** (widget creation, state management, navigation, platform integration, etc.)
2. **Apply Flutter/Dart best practices** following official guidelines
3. **Generate Dart code** using Flutter widget conventions
4. **Verify** the widget tree is correct and state management is properly scoped

### 1. Project Setup

```bash
# Create a new Flutter project
flutter create my_app --org com.example --platforms android,ios

# Run the app with hot reload
flutter run
```

### 2. StatelessWidget Example

```dart
import 'package:flutter/material.dart';

class UserCard extends StatelessWidget {
  final String name;
  final String email;

  const UserCard({super.key, required this.name, required this.email});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        leading: const Icon(Icons.person),
        title: Text(name),
        subtitle: Text(email),
      ),
    );
  }
}
```

### 3. StatefulWidget with State Management

```dart
import 'package:flutter/material.dart';

class CounterPage extends StatefulWidget {
  const CounterPage({super.key});

  @override
  State<CounterPage> createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  int _count = 0;

  void _increment() {
    setState(() => _count++);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(child: Text('Count: $_count', style: Theme.of(context).textTheme.headlineMedium)),
      floatingActionButton: FloatingActionButton(
        onPressed: _increment,
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

### 4. Navigation

```dart
// Named routes
MaterialApp(
  routes: {
    '/': (context) => const HomePage(),
    '/details': (context) => const DetailsPage(),
  },
);

// Programmatic navigation
Navigator.pushNamed(context, '/details');
```

## Best Practices

- Use `const` constructors wherever possible to optimize rebuilds
- Split large widgets into smaller, reusable components
- Use `Key` on list items for correct reconciliation
- Choose a consistent state management approach (Provider/Riverpod for most apps)
- Test on both Android and iOS; handle platform differences explicitly
- Follow the Flutter performance best practices (avoid expensive builds in `build()`)

## Resources

- Official documentation: https://docs.flutter.dev/
- Widget catalog: https://docs.flutter.dev/ui/widgets
- Pub.dev packages: https://pub.dev/

## Keywords

flutter, Dart, cross-platform, Widget, StatelessWidget, StatefulWidget, Provider, Riverpod, navigation, hot reload, mobile development, Material Design, Cupertino
