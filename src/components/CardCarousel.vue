<template>
  <default-showcase
    :title="title"
    :transparent="transparent"
    titlePosition="center"
    :link=link
  >
    <v-slide-group
      v-model="model"
      center-active
      show-arrows
    >
        <v-slide-group-item
          v-for="(item, index) in items"
          :key="index"
        >
          <v-col>
            <blog-card
              :title="item.title"
              :summary="item.summary"
              :titleImage="item.titleImage"
              :link="item.link"
              :width=300
            />
          </v-col>
        </v-slide-group-item>
    </v-slide-group>
  </default-showcase>
</template>

<script>
import DefaultShowcase from './DefaultShowcase.vue'


export default {
  props: {
    title: String,
    transparent: Boolean,
    items: Array,
    link: String
  },
  data: () => ({
      model: null,
    }),
  components: { DefaultShowcase },
}
</script>
