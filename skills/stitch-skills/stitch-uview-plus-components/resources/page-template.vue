<template>
  <view class="page-shell">
    <up-status-bar v-if="useCustomStatusBar" />
    <up-navbar
      v-if="showNavbar"
      :title="pageTitle"
      :autoBack="true"
      placeholder
      bgColor="var(--up-navbar-bg-color)"
    />

    <scroll-view scroll-y class="page-shell__scroll">
      <view class="page-shell__content">
        <up-card :title="pageTitle" :border="false">
          <template #body>
            <view class="page-shell__body">
              <up-text
                text="Replace this scaffold with Stitch-derived content."
                color="var(--up-content-color)"
                size="28"
              />
            </view>
          </template>
        </up-card>

        <up-gap height="24" bgColor="transparent" />
      </view>
    </scroll-view>

    <view v-if="showBottomBar" class="page-shell__footer">
      <up-safe-bottom>
        <view class="page-shell__footer-inner">
          <up-button
            type="primary"
            :loading="submitting"
            shape="circle"
            @click="handlePrimaryAction"
          >
            {{ primaryActionText }}
          </up-button>
        </view>
      </up-safe-bottom>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const pageTitle = ref('Page Title')
const showNavbar = ref(true)
const useCustomStatusBar = ref(false)
const showBottomBar = ref(true)
const submitting = ref(false)
const primaryActionText = ref('Submit')

function handlePrimaryAction() {
  uni.$u.toast('Wire the primary action for this page')
}
</script>

<style lang="scss" scoped>
.page-shell {
  min-height: 100vh;
  background: var(--up-bg-color);
}

.page-shell__scroll {
  min-height: 100vh;
}

.page-shell__content {
  padding: 24rpx 24rpx 0;
}

.page-shell__body {
  display: flex;
  flex-direction: column;
  gap: 24rpx;
}

.page-shell__footer {
  position: sticky;
  bottom: 0;
}

.page-shell__footer-inner {
  padding: 16rpx 24rpx 24rpx;
  background: var(--up-bg-color);
  border-top: 1px solid var(--up-border-color);
}
</style>
