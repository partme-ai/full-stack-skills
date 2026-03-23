<template>
  <view class="page-stitch">
    <!-- Replace with u-navbar, u-row/u-col, u-button, etc. per references/contract.md -->
    <u-navbar title="StitchPage" :autoBack="true" @leftClick="onBack" />
    <u-cell-group>
      <u-cell title="Label" value="Content" />
    </u-cell-group>
    <u-button type="primary" text="Submit" @click="onSubmit" />
  </view>
</template>

<script>
/**
 * Replace StitchPage with actual page name.
 * Use uView 2 components only; see references/contract.md.
 */
export default {
  name: 'StitchPage',
  data() {
    return {}
  },
  methods: {
    onBack() {},
    onSubmit() {}
  }
}
</script>

<style lang="scss" scoped>
.page-stitch {
  min-height: 100vh;
  background: #f3f4f6;
}
</style>
