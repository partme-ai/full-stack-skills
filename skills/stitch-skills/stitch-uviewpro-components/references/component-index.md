# uView Pro Component Index (Full List)

**Use framework components when available; do not replace with generic `<view>`/`<text>` + custom class.** When generating pages **you must prefer u-\* components from this table**; avoid using native `<button>`, `<input>`, `<div>` as substitutes. Do not use custom `.card` / `.card-header` / `.card-title` when **u-card** and **u-section** exist; do not use custom label/tips classes when **u-text** exists; do not use custom divider when **u-line** / **u-divider** exist. Official overview: https://uviewpro.cn/zh/components/intro.html

Each component links to its official doc below (Doc column).

## Basic

| Component | Tag | Minimal example / notes | Doc |
|-----------|-----|-------------------------|-----|
| Color | — | Theme variables for customStyle / theme | [color](https://uviewpro.cn/zh/components/color.html) |
| Icon | `<u-icon name="photo" size="28" color="#2979ff">` | name, size, color | [icon](https://uviewpro.cn/zh/components/icon.html) |
| Image | `<u-image src="/static/xx.png" width="200rpx" height="200rpx">` | src, width, height, mode | [image](https://uviewpro.cn/zh/components/image.html) |
| Button | `<u-button type="primary" @click="submit">Submit</u-button>` | type; size; shape: circle/round | [button](https://uviewpro.cn/zh/components/button.html) |
| Layout | `<u-row><u-col span="6">...</u-col></u-row>` | u-row, u-col span | [layout](https://uviewpro.cn/zh/components/layout.html) |
| Cell | `<u-cell title="Title" value="Value" @click="fn"></u-cell>` | title, value, label, isLink, url | [cell](https://uviewpro.cn/zh/components/cell.html) |
| Badge | `<u-badge :value="9"><u-icon name="bell"></u-icon></u-badge>` | value, max, dot | [badge](https://uviewpro.cn/zh/components/badge.html) |
| Tag | `<u-tag type="primary" text="Tag">` | type, text, plain, size | [tag](https://uviewpro.cn/zh/components/tag.html) |
| Text | `<u-text text="Content" type="primary" size="28">` | text, type, size | [text](https://uviewpro.cn/zh/components/text.html) |
| Fab | `<u-fab :list="fabList" @click="fabClick">` | Floating action button | [fab](https://uviewpro.cn/zh/components/fab.html) |
| Transition | `<u-transition mode="fade">...</u-transition>` | mode: fade/slide | [transition](https://uviewpro.cn/zh/components/transition.html) |
| Gap | `<u-gap height="20" bgColor="#f3f4f6">` | height, bgColor | [gap](https://uviewpro.cn/zh/components/gap.html) |
| Divider | `<u-divider text="Divider">` | text, dashed, dot | [divider](https://uviewpro.cn/zh/components/divider.html) |

## Form

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| Form | `<u-form :model="form" ref="uForm">` | model, ref; validate(), resetFields() | [form](https://uviewpro.cn/zh/components/form.html) |
| Input | `<u-input v-model="form.name" placeholder="Please input" border="none">` | type=select: use :select-open + @click; pair with u-picker | [input](https://uviewpro.cn/zh/components/input.html) |
| Textarea | `<u-textarea v-model="form.desc" placeholder="Multi-line">` | v-model, maxlength, count | [textarea](https://uviewpro.cn/zh/components/textarea.html) |
| Field | `<u-field v-model="val" label="Name" placeholder="Please input">` | Input with label | [field](https://uviewpro.cn/zh/components/field.html) |
| Calendar | `<u-calendar v-model="show" @confirm="onConfirm">` | Date picker | [calendar](https://uviewpro.cn/zh/components/calendar.html) |
| Select | `<u-select v-model="val" :list="options">` | Column selector | [select](https://uviewpro.cn/zh/components/select.html) |
| Picker | `<u-picker v-model="show" mode="selector" :range="options" @confirm="onConfirm">` | **v-model** (not :show); **:range** = 1D array (e.g. `['A','B']`), not :columns or 2D | [picker](https://uviewpro.cn/zh/components/picker.html) |
| Keyboard | `<u-keyboard v-model="show" @confirm="onConfirm">` | Number / secure keyboard | [keyboard](https://uviewpro.cn/zh/components/keyboard.html) |
| Rate | `<u-rate v-model="score" count="5">` | Star rating | [rate](https://uviewpro.cn/zh/components/rate.html) |
| Search | `<u-search v-model="keyword" placeholder="Search" @search="search">` | Search box | [search](https://uviewpro.cn/zh/components/search.html) |
| NumberBox | `<u-number-box v-model="num" :min="0" :max="99">` | Stepper | [numberBox](https://uviewpro.cn/zh/components/numberBox.html) |
| Upload | `<u-upload :fileList="fileList" @afterRead="afterRead" @delete="onDelete">` | Image/file upload | [upload](https://uviewpro.cn/zh/components/upload.html) |
| VerificationCode | `<u-code :seconds="60" @end="end" @start="start">` | SMS countdown | [code](https://uviewpro.cn/zh/components/code.html) |
| Checkbox | `<u-checkbox v-model="checked" label="Option">` | Checkbox | [checkbox](https://uviewpro.cn/zh/components/checkbox.html) |
| Radio | `<u-radio-group v-model="val"><u-radio label="A" value="a"></u-radio></u-radio-group>` | value (not name); label for display | [radio](https://uviewpro.cn/zh/components/radio.html) |
| Switch | `<u-switch v-model="open" activeColor="#3c9cff">` | Switch | [switch](https://uviewpro.cn/zh/components/switch.html) |
| Slider | `<u-slider v-model="value" :min="0" :max="100">` | Slider | [slider](https://uviewpro.cn/zh/components/slider.html) |

## Data

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| CircleProgress | `<u-circle-progress :percent="60">` | percent | [circleProgress](https://uviewpro.cn/zh/components/circleProgress.html) |
| LineProgress | `<u-line-progress :percent="40" activeColor="#3c9cff">` | percent | [lineProgress](https://uviewpro.cn/zh/components/lineProgress.html) |
| Table | `<u-table :columns="columns" :data="list">` | Table | [table](https://uviewpro.cn/zh/components/table.html) |
| CountDown | `<u-count-down :time="3600 * 1000" @finish="finish">` | Countdown | [countDown](https://uviewpro.cn/zh/components/countDown.html) |
| CountTo | `<u-count-to :endVal="100">` | Number animation | [countTo](https://uviewpro.cn/zh/components/countTo.html) |

## Feedback

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| ActionSheet | `<u-action-sheet :list="actionList" v-model="show" @click="onClick">` | Bottom action menu | [actionSheet](https://uviewpro.cn/zh/components/actionSheet.html) |
| AlertTips | `<u-alert-tips type="warning" title="Tip">` | Alert bar | [alertTips](https://uviewpro.cn/zh/components/alertTips.html) |
| Toast | `<u-toast ref="uToast">` + `uni.$u.toast('msg')` | Light toast | [toast](https://uviewpro.cn/zh/components/toast.html) |
| NoticeBar | `<u-notice-bar text="Notice content" scrollable>` | Top scroll notice | [noticeBar](https://uviewpro.cn/zh/components/noticeBar.html) |
| TopTips | `<u-top-tips type="success" text="Success">` | Top short tip | [topTips](https://uviewpro.cn/zh/components/topTips.html) |
| Collapse | `<u-collapse><u-collapse-item title="Title">Content</u-collapse-item></u-collapse>` | Accordion | [collapse](https://uviewpro.cn/zh/components/collapse.html) |
| Popup | `<u-popup v-model="show" mode="bottom"><view>Content</view></u-popup>` | mode: center/bottom/top/left/right | [popup](https://uviewpro.cn/zh/components/popup.html) |
| SwipeAction | `<u-swipe-action><u-swipe-action-item :options="options">...</u-swipe-action-item></u-swipe-action>` | Swipe actions | [swipeAction](https://uviewpro.cn/zh/components/swipeAction.html) |
| Modal | `<u-modal v-model="show" title="Title" content="Content" @confirm="ok">` | Confirm dialog | [modal](https://uviewpro.cn/zh/components/modal.html) |
| FullScreen | `<u-full-screen v-model="show">...</u-full-screen>` | Full-screen overlay | [fullScreen](https://uviewpro.cn/zh/components/fullScreen.html) |

## Layout

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| Line | `<u-line color="#eee" margin="20rpx 0">` | Divider line | [line](https://uviewpro.cn/zh/components/line.html) |
| Card | `<u-card title="Title" :padding="20">Content</u-card>` | Card container | [card](https://uviewpro.cn/zh/components/card.html) |
| Mask | `<u-mask :show="show" @click="show=false">` | Mask overlay | [mask](https://uviewpro.cn/zh/components/mask.html) |
| NoNetwork | `<u-no-network @retry="retry">` | No-network hint | [noNetwork](https://uviewpro.cn/zh/components/noNetwork.html) |
| Grid | `<u-grid :col="3"><u-grid-item v-for="...">` | Grid menu | [grid](https://uviewpro.cn/zh/components/grid.html) |
| Swiper | `<u-swiper :list="bannerList" keyName="url">` | Carousel | [swiper](https://uviewpro.cn/zh/components/swiper.html) |
| TimeLine | `<u-time-line><u-time-line-item>...</u-time-line-item></u-time-line>` | Timeline | [timeLine](https://uviewpro.cn/zh/components/timeLine.html) |
| Skeleton | `<u-skeleton rows="3" loading>` | Skeleton | [skeleton](https://uviewpro.cn/zh/components/skeleton.html) |
| Sticky | `<u-sticky><u-navbar title="Sticky">` | Sticky container | [sticky](https://uviewpro.cn/zh/components/sticky.html) |
| Waterfall | `<u-waterfall v-model="flowList">...</u-waterfall>` | Waterfall | [waterfall](https://uviewpro.cn/zh/components/waterfall.html) |

## Navigation

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| Dropdown | `<u-dropdown :options="options" @click="onClick">` | Dropdown menu | [dropdown](https://uviewpro.cn/zh/components/dropdown.html) |
| Tabbar | `<u-tabbar v-model="current" :list="tabList">` | Bottom tab bar | [tabbar](https://uviewpro.cn/zh/components/tabbar.html) |
| BackTop | `<u-back-top :scrollTop="scrollTop">` | Back to top | [backTop](https://uviewpro.cn/zh/components/backTop.html) |
| Navbar | `<u-navbar title="Page Title" @leftClick="back" :autoBack="true">` | Top bar | [navbar](https://uviewpro.cn/zh/components/navbar.html) |
| Tabs | `<u-tabs :list="list1" :current="current" @change="(i)=>current=i" active-color="#2979ff" inactive-color="#606266">` | **Always use for tab switchers**; list: [{name:'A'},...]; @change(index); do not use custom view/div tabs | [tabs](https://uviewpro.cn/zh/components/tabs.html) |
| TabsSwiper | `<u-tabs-swiper :list="list" ref="tabs">` | Full-screen tabs + swiper | [tabsSwiper](https://uviewpro.cn/zh/components/tabsSwiper.html) |
| Subsection | `<u-subsection :list="['Tab1','Tab2']" @change="change">` | Segmented control | [subsection](https://uviewpro.cn/zh/components/subsection.html) |
| IndexList | `<u-index-list :indexList="indexList">...</u-index-list>` | Index list (e.g. contacts) | [indexList](https://uviewpro.cn/zh/components/indexList.html) |
| Steps | `<u-steps :current="1" :list="steps">` | Steps | [steps](https://uviewpro.cn/zh/components/steps.html) |
| Empty | `<u-empty text="No data" mode="data">` | Empty state | [empty](https://uviewpro.cn/zh/components/empty.html) |
| Link | `<u-link href="/pages/xx" text="Link">` | Link | [link](https://uviewpro.cn/zh/components/link.html) |
| Section | `<u-section title="Title" rightText="More" @click="more">` | Section header | [section](https://uviewpro.cn/zh/components/section.html) |
| Pagination | `<u-pagination v-model="current" :total="total" @change="change">` | Pagination | [pagination](https://uviewpro.cn/zh/components/pagination.html) |

## Other

| Component | Tag | Minimal example | Doc |
|-----------|-----|-----------------|-----|
| MessageInput | `<u-message-input v-model="code" :maxlength="6">` | Verification code input | [messageInput](https://uviewpro.cn/zh/components/messageInput.html) |
| Loadmore | `<u-loadmore :status="status" @loadmore="loadmore">` | List load more | [loadmore](https://uviewpro.cn/zh/components/loadmore.html) |
| ReadMore | `<u-read-more :toggle="true" :content="longText">` | Expand/collapse | [readMore](https://uviewpro.cn/zh/components/readMore.html) |
| LazyLoad | `<u-lazy-load :imageUrl="url">` | Image lazy load | [lazyLoad](https://uviewpro.cn/zh/components/lazyLoad.html) |
| Avatar | `<u-avatar src="/static/avatar.png" size="80">` | Avatar | [avatar](https://uviewpro.cn/zh/components/avatar.html) |
| Loading | `<u-loading mode="circle" size="40">` | Loading spinner | [loading](https://uviewpro.cn/zh/components/loading.html) |
| LoadingPopup | `<u-loading-popup v-model="show" title="Loading">` | Full-screen loading | [loadingPopup](https://uviewpro.cn/zh/components/loadingPopup.html) |
| safeAreaInset | `<safe-area-inset type="bottom">` | Bottom safe area | [safeAreaInset](https://uviewpro.cn/zh/components/safeAreaInset.html) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card / section with title only | **u-card** with `title="..."` and `:padding="32"` | view.card + card-header + text.card-title |
| Card / section with title + right content (switch, link) | **u-card** + **u-section** with `title` and **#right** slot | view.card-header-row + custom spec-label |
| Section header | **u-section** (title, rightText or #right) | view + text with custom class |
| Secondary label / hint (e.g. optional, display-only, no limit) | **u-text** `text=" (optional)"` `type="info"` `size="24"` | text.label-optional / .label-hint |
| Tips / notice under upload or form | **u-text** type="info" or type="warning", size="24", block | .tips-text, .tips-warn |
| Unit text (e.g. yuan, piece) next to input | **u-text** `text="yuan"` type="info" size="28" | text.unit |
| Divider line | **u-line** or **u-divider** | view with border-top/border-bottom only |
| Button | u-button | raw button / view |
| Input / search box | u-input, u-field, u-search | raw input |
| Form (multiple fields) | u-form + u-form-item + u-input/u-select/u-switch etc. | — |
| List item (swipe to delete/action) | u-swipe-action + u-swipe-action-item | — |
| Bottom sheet / action menu | u-action-sheet or u-popup mode="bottom" | — |
| Dialog / modal | u-modal or u-popup | — |
| Date / time picker | u-calendar, u-picker | — |
| Tab switcher | **u-tabs** or u-tabs-swiper | custom view tab-item |
| Top bar / back | u-navbar | — |
| Bottom tab bar | u-tabbar | — |
| Card list / grid | u-card, u-grid | — |
| Empty state | u-empty | — |
| Loading | u-loading or u-loading-popup | — |
| Toast | u-toast / uni.$u.toast | — |
| Avatar | u-avatar | — |
| Badge / dot | u-badge | — |

**Consult this table before writing templates**; do not hand-write div/button/input in place of u-\* components. **Vue 3 slots**: use **#label**, **#suffix**, **#right**, **v-slot:label** etc., never `slot="label"` or `slot="suffix"`.
