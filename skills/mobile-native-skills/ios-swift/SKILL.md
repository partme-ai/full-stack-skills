---
name: ios-swift
description: "Guides iOS app development with Swift including SwiftUI views, UIKit view controllers, navigation, async/await networking, Core Data persistence, Xcode project configuration, and App Store submission. Use when the user asks about iOS Swift development, needs to create iOS applications, implement SwiftUI or UIKit components, or configure Xcode signing and TestFlight."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create iOS applications using Swift with SwiftUI or UIKit
- Implement navigation, view controllers, or SwiftUI views and modifiers
- Use async/await, Combine, or URLSession for networking
- Configure Xcode project settings, signing, capabilities, or entitlements
- Persist data with Core Data, SwiftData, or UserDefaults
- Prepare for App Store submission via TestFlight

## How to use this skill

### 1. SwiftUI View

```swift
struct ContentView: View {
    @StateObject private var viewModel = ItemViewModel()

    var body: some View {
        NavigationStack {
            List(viewModel.items) { item in
                NavigationLink(item.name) {
                    DetailView(item: item)
                }
            }
            .navigationTitle("Items")
            .task { await viewModel.loadItems() }
        }
    }
}
```

### 2. ViewModel with async/await

```swift
@MainActor
class ItemViewModel: ObservableObject {
    @Published var items: [Item] = []

    func loadItems() async {
        let (data, _) = try await URLSession.shared.data(from: url)
        items = try JSONDecoder().decode([Item].self, from: data)
    }
}
```

### 3. Navigation (UIKit)

```swift
let detailVC = DetailViewController()
detailVC.item = selectedItem
navigationController?.pushViewController(detailVC, animated: true)
```

### 4. Xcode Configuration

- Set **Signing & Capabilities**: Team, Bundle ID, provisioning profile.
- Add capabilities (Push Notifications, Background Modes) in the Signing tab.
- Archive and upload via **Product -> Archive -> Distribute App**.

## Best Practices

- Perform all UI updates on `@MainActor`; use `[weak self]` in closures to avoid retain cycles.
- Add `NSCameraUsageDescription` and other privacy keys to Info.plist before requesting permissions.
- Test on real devices and via TestFlight before App Store submission.
- Follow Apple Human Interface Guidelines for layout, typography, and navigation patterns.

## Resources

- https://developer.apple.com/documentation/swift
- https://developer.apple.com/documentation/swiftui
- https://developer.apple.com/design/human-interface-guidelines

## Keywords

iOS, Swift, SwiftUI, UIKit, Xcode, async/await, Core Data, TestFlight, App Store
