<template>
  <div class="stitch-component">
    <!-- Replace with b-container, b-row, b-col, b-card, b-button per references/contract.md -->
    <b-card title="StitchComponent" img-top>
      <b-card-text>
        <slot />
      </b-card-text>
      <b-button variant="primary">Action</b-button>
    </b-card>
  </div>
</template>

<script setup>
/**
 * Replace StitchComponent with actual component name.
 * Use Bootstrap Vue components only; see references/contract.md.
 */
defineOptions({
  name: 'StitchComponent'
})
</script>

<style scoped>
.stitch-component {
  /* Use Bootstrap utility classes; avoid hardcoded hex when token exists */
}
</style>
