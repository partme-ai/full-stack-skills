---
name: react-native
description: "Provides comprehensive guidance for React Native development including components, navigation, native modules, platform-specific code, and mobile app development. Use when the user asks about React Native, needs to create mobile applications, implement React Native components, or work with React Native features."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build cross-platform mobile applications with React Native
- Create and style React Native components (View, Text, FlatList, ScrollView)
- Implement navigation with React Navigation
- Use platform-specific code for Android and iOS
- Integrate native modules and bridge native APIs
- Configure Metro bundler, debug tools, and build settings
- Optimize list performance and memory usage

## How to use this skill

### Workflow

1. **Identify the request area** (component creation, navigation, native modules, styling, etc.)
2. **Apply React Native conventions** for layout, styling, and platform handling
3. **Generate TypeScript/JSX code** using React Native core components
4. **Verify** the solution works on both Android and iOS

### 1. Core Component Example

```tsx
import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

interface User {
  id: string;
  name: string;
}

export function UserList({ users }: { users: User[] }) {
  return (
    <FlatList
      data={users}
      keyExtractor={item => item.id}
      renderItem={({ item }) => (
        <View style={styles.item}>
          <Text style={styles.name}>{item.name}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  item: { padding: 16, borderBottomWidth: 1, borderBottomColor: '#eee' },
  name: { fontSize: 16, fontWeight: '600' },
});
```

### 2. Navigation Setup

```tsx
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

### 3. Platform-Specific Code

```tsx
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 44 : 0,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 } },
      android: { elevation: 4 },
    }),
  },
});
```

## Best Practices

- Use `FlatList` (not `ScrollView`) for long lists; provide `keyExtractor` and `getItemLayout` for performance
- Avoid heavy computation on the main JavaScript thread; offload to native modules if needed
- Match native dependency versions with the React Native version to prevent build failures
- Test on both platforms early and often; use `Platform.select` for platform-specific styles
- Use `StyleSheet.create` for optimized style objects

## Resources

- Official documentation: https://reactnative.dev/docs/getting-started
- React Navigation: https://reactnavigation.org/
- Expo: https://docs.expo.dev/

## Keywords

react native, React Native, cross-platform, mobile, FlatList, React Navigation, Metro, native modules, iOS, Android, StyleSheet
