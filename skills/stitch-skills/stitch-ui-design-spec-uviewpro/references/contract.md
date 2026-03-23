# uView Pro Design Contract (Vue 3 / uni-app)

## 1. Design Tokens (Hard Constraints)

### Colors (Standard Theme)
- **Primary**: `#3c9cff` (Blue)
- **Success**: `#5ac725` (Green)
- **Warning**: `#f9ae3d` (Orange)
- **Danger**: `#f56c6c` (Red)
- **Info**: `#909399` (Gray)
- **Main Text**: `#303133`
- **Content Text**: `#606266`
- **Tips Text**: `#909399`
- **Light Text**: `#c0c4cc`
- **Border**: `#dadbde`
- **Background**: `#f3f4f6`

### Typography
- **Unit**: `rpx` (Responsive Pixel) is standard for mobile.
- **Sizes**:
  - Main Title: `32rpx` or `36rpx` (Bold)
  - Content: `28rpx` (Base)
  - Tips/Secondary: `24rpx`
  - Small: `20rpx`

### Radius & Spacing
- **Radius**: `8rpx` (Small), `16rpx` (Card), `9999px` (Circle/Pill).
- **Spacing**: Use `gap` in flex layouts or utility classes if available.

## 2. Component Contracts

**IMPORTANT**: uView Pro components use the `u-` prefix (same as uView 2; package is `uview-pro`, easycom: `^u-(.*)` → `uview-pro/components/u-$1`). Example: `<u-button>`.

### Layout
- **Flex Grid**: `<u-row>` and `<u-col span="6">`.
- **Gap**: `<u-gap height="20" bgColor="#f3f4f6"></u-gap>` for vertical spacing.
- **Divider**: `<u-divider text="End"></u-divider>`.

### Buttons
- **Tag**: `<u-button>`
- **Props**: `type="primary"`, `shape="circle"`, `size="normal"`, `plain`.

### Forms
- **Wrapper**: `<u-form :model="form" ref="uForm">`
- **Item**: `<u-form-item label="Name" prop="name" borderBottom>`
- **Input**: `<u-input v-model="form.name" border="none" placeholder="Please input"></u-input>`
- **Upload**: `<u-upload :fileList="fileList1" @afterRead="afterRead" ...></u-upload>`

### Navigation
- **Navbar**: `<u-navbar title="Home" @leftClick="leftClick" :autoBack="true">`
- **Tabs**: `<u-tabs :list="list1" @click="click"></u-tabs>`
- **IndexList**: `<u-index-list :indexList="indexList">...</u-index-list>` (Contact list style)

### List & Data
- **SwipeAction**: `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>`
- **List**: `<u-list @scrolltolower="scrolltolower">...</u-list>` (Load more)
- **Grid Menu**: `<u-grid :col="3">...</u-grid>`
- **Waterfall**: `<u-waterfall v-model="flowList">...</u-waterfall>` (Masonry layout)

### Feedback
- **Toast**: `<u-toast ref="uToast"></u-toast>`
- **JS Usage**: `uni.$u.toast('Hello')` (Note: uView Pro hangs tools on `uni.$u`)
- **Code**: `<u-code :seconds="60" @end="end"></u-code>` (SMS verification countdown)

## 3. Icons
- **Tag**: `<u-icon name="photo" color="#2979ff" size="28"></u-icon>`
- **Library**: Built-in uView Pro icons.

## 4. JS Utilities (`uni.$u`)
- **Trim**: `uni.$u.trim(str)`
- **Test**: `uni.$u.test.mobile(str)` (Validation)
- **Route**: `uni.$u.route('/pages/index/index')`
- **Request**: `uni.$u.http.post(...)`

## 5. Script Setup (Vue 3)
- Use `<script setup lang="ts">`.
- Import hooks and utils from `uview-pro` if needed, or rely on global `uni.$u`.
