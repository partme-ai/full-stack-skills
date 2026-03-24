# uView 2.0 Component Index (with official doc links)

**Use framework components when available; do not replace with generic `<view>`/`<text>` + custom class.** Use **u-cell-group** + **u-cell** for card-like blocks (no Card in uView 2), **u-text** for titles and hints, **u-line** / **u-divider** for dividers. Official overview: https://www.uviewui.com/components/intro.html

Each component links to its official doc below (Doc column). Base: https://www.uviewui.com/components/

## Basic

| Component | Tag | Doc |
|-----------|-----|-----|
| Color | theme variables | [color](https://www.uviewui.com/components/color.html) |
| Icon | `<u-icon name="photo" size="28">` | [icon](https://www.uviewui.com/components/icon.html) |
| Image | `<u-image src="..." width="200rpx">` | [image](https://www.uviewui.com/components/image.html) |
| Button | `<u-button type="primary" @click="submit">` | [button](https://www.uviewui.com/components/button.html) |
| Text | `<u-text text="Content">` | [text](https://www.uviewui.com/components/text.html) |
| Layout | `<u-row>`, `<u-col span="6">` | [layout](https://www.uviewui.com/components/layout.html) |
| Cell | `<u-cell title="Title" value="Value">` | [cell](https://www.uviewui.com/components/cell.html) |
| Badge | `<u-badge :value="9">` | [badge](https://www.uviewui.com/components/badge.html) |
| Tag | `<u-tag type="primary">` | [tag](https://www.uviewui.com/components/tag.html) |
| LoadingIcon | `<u-loading-icon>` | [loadingIcon](https://www.uviewui.com/components/loadingIcon.html) |
| LoadingPage | `<u-loading-page>` | [loadingPage](https://www.uviewui.com/components/loadingPage.html) |

## Form

| Component | Tag | Doc |
|-----------|-----|-----|
| Form | `<u--form :model="form" :rules="rules" ref="uForm">` | [form](https://www.uviewui.com/components/form.html) |
| Input | `<u--input v-model="form.name">` or `<u-input>` | [input](https://www.uviewui.com/components/input.html) |
| Textarea | `<u-textarea v-model="form.desc">` | [textarea](https://www.uviewui.com/components/textarea.html) |
| Calendar | `<u-calendar v-model="show">` | [calendar](https://www.uviewui.com/components/calendar.html) |
| Keyboard | `<u-keyboard>` | [keyboard](https://www.uviewui.com/components/keyboard.html) |
| Picker | `<u-picker>` | [picker](https://www.uviewui.com/components/picker.html) |
| DatetimePicker | `<u-datetime-picker>` | [datetimePicker](https://www.uviewui.com/components/datetimePicker.html) |
| Rate | `<u-rate v-model="score">` | [rate](https://www.uviewui.com/components/rate.html) |
| Search | `<u-search v-model="keyword">` | [search](https://www.uviewui.com/components/search.html) |
| NumberBox | `<u-number-box v-model="num">` | [numberBox](https://www.uviewui.com/components/numberBox.html) |
| Upload | `<u-upload>` | [upload](https://www.uviewui.com/components/upload.html) |
| Code | `<u-code :seconds="60">` | [code](https://www.uviewui.com/components/code.html) |
| Checkbox | `<u-checkbox>` | [checkbox](https://www.uviewui.com/components/checkbox.html) |
| Radio | `<u-radio-group>`, `<u-radio>` | [radio](https://www.uviewui.com/components/radio.html) |
| Switch | `<u-switch v-model="open">` | [switch](https://www.uviewui.com/components/switch.html) |
| Slider | `<u-slider v-model="value">` | [slider](https://www.uviewui.com/components/slider.html) |

## Data & List

| Component | Tag | Doc |
|-----------|-----|-----|
| List | `<u-list @scrolltolower="loadmore">` | [list](https://www.uviewui.com/components/list.html) |
| LineProgress | `<u-line-progress :percent="40">` | [lineProgress](https://www.uviewui.com/components/lineProgress.html) |
| CountDown | `<u-count-down :time="3600000">` | [countDown](https://www.uviewui.com/components/countDown.html) |
| CountTo | `<u-count-to :endVal="100">` | [countTo](https://www.uviewui.com/components/countTo.html) |

## Feedback

| Component | Tag | Doc |
|-----------|-----|-----|
| ActionSheet | `<u-action-sheet :list="list" v-model="show">` | [actionSheet](https://www.uviewui.com/components/actionSheet.html) |
| Alert | `<u-alert>` | [alert](https://www.uviewui.com/components/alert.html) |
| Toast | `<u-toast ref="uToast" />` | [toast](https://www.uviewui.com/components/toast.html) |
| NoticeBar | `<u-notice-bar text="...">` | [noticeBar](https://www.uviewui.com/components/noticeBar.html) |
| SwipeAction | `<u-swipe-action><u-swipe-action-item>` | [swipeAction](https://www.uviewui.com/components/swipeAction.html) |
| Collapse | `<u-collapse>`, `<u-collapse-item>` | [collapse](https://www.uviewui.com/components/collapse.html) |
| Popup | `<u-popup v-model="show" mode="bottom">` | [popup](https://www.uviewui.com/components/popup.html) |
| Modal | `<u-modal v-model="show" title="..." content="...">` | [modal](https://www.uviewui.com/components/modal.html) |

## Layout

| Component | Tag | Doc |
|-----------|-----|-----|
| Line | `<u-line>` | [line](https://www.uviewui.com/components/line.html) |
| Overlay | `<u-overlay>` | [overlay](https://www.uviewui.com/components/overlay.html) |
| NoNetwork | `<u-no-network>` | [noNetwork](https://www.uviewui.com/components/noNetwork.html) |
| Grid | `<u-grid>`, `<u-grid-item>` | [grid](https://www.uviewui.com/components/grid.html) |
| Swiper | `<u-swiper>` | [swiper](https://www.uviewui.com/components/swiper.html) |
| Skeleton | `<u-skeleton>` | [skeleton](https://www.uviewui.com/components/skeleton.html) |
| Sticky | `<u-sticky>` | [sticky](https://www.uviewui.com/components/sticky.html) |
| Divider | `<u-divider>` | [divider](https://www.uviewui.com/components/divider.html) |

## Navigation

| Component | Tag | Doc |
|-----------|-----|-----|
| Tabbar | `<u-tabbar v-model="current" :list="list">` | [tabbar](https://www.uviewui.com/components/tabbar.html) |
| BackTop | `<u-back-top>` | [backTop](https://www.uviewui.com/components/backTop.html) |
| Navbar | `<u-navbar title="Title" :autoBack="true">` | [navbar](https://www.uviewui.com/components/navbar.html) |
| Tabs | `<u-tabs :list="list1">` | [tabs](https://www.uviewui.com/components/tabs.html) |
| Subsection | `<u-subsection :list="['A','B']">` | [subsection](https://www.uviewui.com/components/subsection.html) |
| IndexList | `<u-index-list :indexList="indexList">` | [indexList](https://www.uviewui.com/components/indexList.html) |
| Steps | `<u-steps :current="1">` | [steps](https://www.uviewui.com/components/steps.html) |
| Empty | `<u-empty text="No data">` | [empty](https://www.uviewui.com/components/empty.html) |

## Other

| Component | Tag | Doc |
|-----------|-----|-----|
| Gap | `<u-gap height="20">` | [gap](https://www.uviewui.com/components/gap.html) |
| Avatar | `<u-avatar src="...">` | [avatar](https://www.uviewui.com/components/avatar.html) |
| Link | `<u-link href="...">` | [link](https://www.uviewui.com/components/link.html) |
| LoadMore | `<u-load-more>` | [loadMore](https://www.uviewui.com/components/loadMore.html) |
| ReadMore | `<u-read-more>` | [readMore](https://www.uviewui.com/components/readMore.html) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card-like section (title + content) | **u-cell-group** + **u-cell** or wrapper + **u-text** for title | view.card + card-header + text.card-title |
| Label hint / tip text (optional, unit) | **u-text** (per uView Text API) | text.label-optional, .tips-text, .unit |
| Divider line | **u-line** or **u-divider** | view with border only |
| Button, Form, Tabs, etc. | u-button, u-form, u-tabs, etc. | raw button, input, div tabs |

Consult this table and [contract.md](contract.md) when mapping Stitch HTML to uView 2 components.
