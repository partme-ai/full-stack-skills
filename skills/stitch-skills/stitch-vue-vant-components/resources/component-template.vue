<template>
  <div class="stitch-component">
    <!-- Replace with van-nav-bar, van-cell-group, van-button, etc. per references/contract.md -->
    <van-nav-bar title="StitchComponent" left-arrow />
    <van-cell-group inset>
      <van-cell title="Label" value="Content" />
    </van-cell-group>
    <div style="margin: 16px;">
      <van-button type="primary" block>Submit</van-button>
    </div>
  </div>
</template>

<script setup>
/**
 * Replace StitchComponent with actual component name.
 * Use Vant 4 components only; see references/contract.md.
 */
defineOptions({
  name: 'StitchComponent'
})
</script>

<style scoped>
.stitch-component {
  min-height: 100vh;
  background: #f7f8fa;
}
</style>
