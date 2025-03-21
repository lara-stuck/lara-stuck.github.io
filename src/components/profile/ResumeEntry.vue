<template>
  <blog-paragraph>
    {{ name }} - <span class="font-weight-bold">{{ years }}</span>
  </blog-paragraph>
</template>

<script>
export default {
  props: {
    name: String,
    years: String,
  }
}
</script>