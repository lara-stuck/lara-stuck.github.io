<template>
    <v-card
    class="rounded-lg"
    :to="link"
    elevation=0
  >
    <v-img
      :src="titleImage"
      min-width="100%"
      height=200
      cover
    >
    </v-img>
    <v-card-title
      class="text-secondary"
    >
      {{ title }}
    </v-card-title>
    <v-card-text>
      <p
        class="three-lines"
      >
        {{ summary }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    title: String,
    summary: String,
    titleImage: String,
    link: String
  }
}
</script>

<style scoped>
.three-lines {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  white-space: normal;
}
</style>