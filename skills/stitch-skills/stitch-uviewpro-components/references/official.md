# uView Pro (Vue 3) Official References

- **Official**: https://uviewpro.cn/
- **Guide**: https://uviewpro.cn/zh/guide/intro.html
- **Components (overview)**: https://uviewpro.cn/zh/components/intro.html
- **Tools**: https://uviewpro.cn/zh/tools/intro.html
- **Layout / Templates**: https://uviewpro.cn/zh/layout/intro.html

## Per-component doc links (each component → official doc)

Base URL: `https://uviewpro.cn/zh/components/` + `{name}.html`

| Component | Doc |
|-----------|-----|
| Color | https://uviewpro.cn/zh/components/color.html |
| Icon | https://uviewpro.cn/zh/components/icon.html |
| Image | https://uviewpro.cn/zh/components/image.html |
| Button | https://uviewpro.cn/zh/components/button.html |
| Layout | https://uviewpro.cn/zh/components/layout.html |
| Cell | https://uviewpro.cn/zh/components/cell.html |
| Badge | https://uviewpro.cn/zh/components/badge.html |
| Tag | https://uviewpro.cn/zh/components/tag.html |
| Text | https://uviewpro.cn/zh/components/text.html |
| Fab | https://uviewpro.cn/zh/components/fab.html |
| Transition | https://uviewpro.cn/zh/components/transition.html |
| Gap | https://uviewpro.cn/zh/components/gap.html |
| Divider | https://uviewpro.cn/zh/components/divider.html |
| Form | https://uviewpro.cn/zh/components/form.html |
| Input | https://uviewpro.cn/zh/components/input.html |
| Textarea | https://uviewpro.cn/zh/components/textarea.html |
| Field | https://uviewpro.cn/zh/components/field.html |
| Calendar | https://uviewpro.cn/zh/components/calendar.html |
| Select | https://uviewpro.cn/zh/components/select.html |
| Picker | https://uviewpro.cn/zh/components/picker.html |
| Keyboard | https://uviewpro.cn/zh/components/keyboard.html |
| Rate | https://uviewpro.cn/zh/components/rate.html |
| Search | https://uviewpro.cn/zh/components/search.html |
| NumberBox | https://uviewpro.cn/zh/components/numberBox.html |
| Upload | https://uviewpro.cn/zh/components/upload.html |
| Code (VerificationCode) | https://uviewpro.cn/zh/components/code.html |
| Checkbox | https://uviewpro.cn/zh/components/checkbox.html |
| Radio | https://uviewpro.cn/zh/components/radio.html |
| Switch | https://uviewpro.cn/zh/components/switch.html |
| Slider | https://uviewpro.cn/zh/components/slider.html |
| CircleProgress | https://uviewpro.cn/zh/components/circleProgress.html |
| LineProgress | https://uviewpro.cn/zh/components/lineProgress.html |
| Table | https://uviewpro.cn/zh/components/table.html |
| CountDown | https://uviewpro.cn/zh/components/countDown.html |
| CountTo | https://uviewpro.cn/zh/components/countTo.html |
| ActionSheet | https://uviewpro.cn/zh/components/actionSheet.html |
| AlertTips | https://uviewpro.cn/zh/components/alertTips.html |
| Toast | https://uviewpro.cn/zh/components/toast.html |
| NoticeBar | https://uviewpro.cn/zh/components/noticeBar.html |
| TopTips | https://uviewpro.cn/zh/components/topTips.html |
| Collapse | https://uviewpro.cn/zh/components/collapse.html |
| Popup | https://uviewpro.cn/zh/components/popup.html |
| SwipeAction | https://uviewpro.cn/zh/components/swipeAction.html |
| Modal | https://uviewpro.cn/zh/components/modal.html |
| FullScreen | https://uviewpro.cn/zh/components/fullScreen.html |
| Line | https://uviewpro.cn/zh/components/line.html |
| Card | https://uviewpro.cn/zh/components/card.html |
| Mask | https://uviewpro.cn/zh/components/mask.html |
| NoNetwork | https://uviewpro.cn/zh/components/noNetwork.html |
| Grid | https://uviewpro.cn/zh/components/grid.html |
| Swiper | https://uviewpro.cn/zh/components/swiper.html |
| TimeLine | https://uviewpro.cn/zh/components/timeLine.html |
| Skeleton | https://uviewpro.cn/zh/components/skeleton.html |
| Sticky | https://uviewpro.cn/zh/components/sticky.html |
| Waterfall | https://uviewpro.cn/zh/components/waterfall.html |
| Dropdown | https://uviewpro.cn/zh/components/dropdown.html |
| Tabbar | https://uviewpro.cn/zh/components/tabbar.html |
| BackTop | https://uviewpro.cn/zh/components/backTop.html |
| Navbar | https://uviewpro.cn/zh/components/navbar.html |
| Tabs | https://uviewpro.cn/zh/components/tabs.html |
| TabsSwiper | https://uviewpro.cn/zh/components/tabsSwiper.html |
| Subsection | https://uviewpro.cn/zh/components/subsection.html |
| IndexList | https://uviewpro.cn/zh/components/indexList.html |
| Steps | https://uviewpro.cn/zh/components/steps.html |
| Empty | https://uviewpro.cn/zh/components/empty.html |
| Link | https://uviewpro.cn/zh/components/link.html |
| Section | https://uviewpro.cn/zh/components/section.html |
| Pagination | https://uviewpro.cn/zh/components/pagination.html |
| MessageInput | https://uviewpro.cn/zh/components/messageInput.html |
| Loadmore | https://uviewpro.cn/zh/components/loadmore.html |
| ReadMore | https://uviewpro.cn/zh/components/readMore.html |
| LazyLoad | https://uviewpro.cn/zh/components/lazyLoad.html |
| Avatar | https://uviewpro.cn/zh/components/avatar.html |
| Loading | https://uviewpro.cn/zh/components/loading.html |
| LoadingPopup | https://uviewpro.cn/zh/components/loadingPopup.html |
| safeAreaInset | https://uviewpro.cn/zh/components/safeAreaInset.html |

Full table with minimal usage: [component-index.md](component-index.md).

## Usage in This Skill

1. Map Stitch HTML to uView Pro (`u-*`) components (`u-row`, `u-col`, `u-navbar`, `u-button`, `u-form`, `u-input`, etc.) per [references/contract.md](contract.md). uView Pro uses the same tag prefix as uView 2; the package is `uview-pro` (Vue 3).
2. Use rpx for typography and spacing; rely on `uni.$u` for toast, route, http when documented.
3. Use `<script setup>` (Vue 3); register pages in `pages.json`.
