<template>
  <v-row
      v-if="title != null"
    :justify="titlePosition"
    class="text-h3 font-weight-light mt-16 mb-3"
  >
    <v-hover>
      <template v-slot:default="{ isHovering, props }">
        <a
          v-bind="props"
          :class="['text-decoration-none', isHovering ? 'text-secondary' : 'text-primary']"
          :href="link"
        >
          {{ title }}
        </a>
      </template>
    </v-hover>
      
  </v-row>
  <v-card
    :color="color"
    class="mb-16 pa-3 rounded-lg"
    min-width="100%"
    elevation=0
  >
    <v-row
      justify=center
    >
      <slot />
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: {
    title: String,
    color: String,
    titlePosition: String,
    link: String
  }
}
</script>