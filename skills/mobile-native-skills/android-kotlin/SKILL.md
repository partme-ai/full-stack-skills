---
name: android-kotlin
description: "Guides Android app development with Kotlin including creating Activities, Fragments, ViewModels, Jetpack Compose UI, Navigation, Gradle configuration, and app signing. Use when the user asks about Android Kotlin development, needs to create Android applications, implement Jetpack components, or configure build variants."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create Android applications using Kotlin with Activities, Fragments, or Jetpack Compose
- Implement ViewModel, LiveData, StateFlow, or other Jetpack architecture components
- Configure Gradle build files (build.gradle.kts), dependencies, or build variants
- Set up navigation, permissions, or Android lifecycle handling
- Build and sign APK/AAB for release or configure ProGuard

## How to use this skill

### 1. Project Setup

Create a new project with Android Studio or configure build files:

```kotlin
// build.gradle.kts (app module)
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.7.0")
    implementation("androidx.navigation:navigation-fragment-ktx:2.7.6")
}
```

### 2. Architecture (MVVM with ViewModel)

```kotlin
class MainViewModel : ViewModel() {
    private val _items = MutableStateFlow<List<Item>>(emptyList())
    val items: StateFlow<List<Item>> = _items.asStateFlow()

    fun loadItems() {
        viewModelScope.launch {
            _items.value = repository.getItems()
        }
    }
}
```

### 3. UI with Jetpack Compose

```kotlin
@Composable
fun ItemList(viewModel: MainViewModel = viewModel()) {
    val items by viewModel.items.collectAsState()
    LazyColumn {
        items(items) { item ->
            Text(text = item.name, modifier = Modifier.padding(16.dp))
        }
    }
}
```

### 4. Navigation

Register destinations in the navigation graph and navigate programmatically:

```kotlin
findNavController().navigate(R.id.action_home_to_detail)
```

## Best Practices

- Use `viewModelScope` for coroutines tied to ViewModel lifecycle; avoid leaking activities.
- Save UI state with `SavedStateHandle` in ViewModel; handle process death gracefully.
- Use ViewBinding or Jetpack Compose instead of `findViewById`.
- Apply ProGuard/R8 rules for release builds; keep signing keys secure.
- Test with `@RunWith(AndroidJUnit4::class)` and Espresso for UI tests.

## Resources

- https://developer.android.com/kotlin
- https://developer.android.com/jetpack/compose
- https://developer.android.com/topic/architecture

## Keywords

android, Kotlin, Jetpack, Compose, ViewModel, Navigation, Gradle, AndroidManifest.xml
