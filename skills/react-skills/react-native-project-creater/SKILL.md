---
name: react-native-project-creater
description: "Provides one-command project creation for React Native including project initialization, configuration, and template generation. Use when the user asks about creating React Native projects, needs to initialize a new React Native project, or generate React Native project structure."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create a new React Native project from scratch
- Choose between React Native CLI and Expo for project initialization
- Configure TypeScript, bundler, and native dependencies
- Set up the initial project structure with navigation and state management

## How to use this skill

### Workflow

1. **Gather requirements**: project name, organization, TypeScript preference, Expo vs bare CLI
2. **Run the initialization command** with appropriate options
3. **Install initial dependencies** (navigation, state management, etc.)
4. **Verify** the project builds and runs on a simulator or device

### 1. Project Creation (CLI)

```bash
# Using React Native Community CLI
npx @react-native-community/cli init MyApp

# With TypeScript template
npx @react-native-community/cli init MyApp --template react-native-template-typescript
```

### 2. Project Creation (Expo)

```bash
# Using Expo (recommended for new projects)
npx create-expo-app MyApp --template blank-typescript
```

### 3. Project Structure

```
MyApp/
├── App.tsx            # Entry point
├── android/           # Android native project
├── ios/               # iOS native project
├── src/               # Application source code
│   ├── screens/
│   ├── components/
│   └── navigation/
├── package.json
├── tsconfig.json
└── metro.config.js    # Metro bundler configuration
```

### 4. Initial Setup

```bash
# Install dependencies
npm install

# iOS: install CocoaPods
cd ios && pod install && cd ..

# Run on simulators
npx react-native run-ios
npx react-native run-android
```

## Best Practices

- Use consistent naming and package identifiers across platforms
- Lock Node.js and React Native versions for reproducible builds
- Run `pod install` after adding any native dependency on iOS
- Start with the default template, verify it runs, then incrementally add features
- Set up CI early with both `npx react-native run-android` and `run-ios` build steps

## Resources

- Environment setup: https://reactnative.dev/docs/environment-setup
- Expo getting started: https://docs.expo.dev/get-started/create-a-project/

## Keywords

react native init, project creation, Expo, React Native CLI, initialization, cross-platform, TypeScript, scaffolding
