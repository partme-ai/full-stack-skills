<template>
  <div class="stitch-component">
    <!-- Replace with el-row/el-col, el-card, el-button, etc. per references/contract.md -->
    <el-card shadow="hover">
      <template #header>
        <span>StitchComponent</span>
      </template>
      <slot />
    </el-card>
  </div>
</template>

<script setup>
/**
 * Replace StitchComponent with actual component name.
 * Use Element Plus components only; see references/contract.md.
 */
defineOptions({
  name: 'StitchComponent'
})
</script>

<style scoped>
.stitch-component {
  /* Use Element Plus design tokens; avoid hardcoded hex when token exists */
}
</style>
