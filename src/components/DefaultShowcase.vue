<template>
  <v-card
    class="ma-2 pa-6 mt-16"
    :color="color"
    elevation="0"
  >
    <v-row
      v-if="title != null"
    :justify="titlePosition"
    class="text-h4 pl-3 pr-3 mb-8 pt-8"
  >
    <v-hover>
      <template v-slot:default="{ isHovering, props }">
        <a
          v-bind="props"
          :class="['text-decoration-none', isHovering ? 'text-secondary' : 'text-secondary']"
        >
          {{ title }}
        </a>
      </template>
    </v-hover>
      
  </v-row>
  <v-card
    :color="color"
    class="pa-3 rounded-lg"
    min-width="100%"
    elevation=0
  >
    <v-row
      justify=center
    >
      <slot />
    </v-row>
  </v-card>
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