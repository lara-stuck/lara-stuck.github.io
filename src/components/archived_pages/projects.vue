<template>
  <default-page
    title="Projekte"
    color="cardbackground"
  >
    <v-row>
      <v-col>
        <component
          v-for="item in items"
          :key="item.title"
          :is="item"
        />
      </v-col>
    </v-row>
  </default-page>
</template>

<script>
import { markRaw } from 'vue'

export default {
  data: () => ({
    items: [],
  }),
  mounted() {
    const modules = import.meta.glob('@/components/projects/examples/*.vue', { eager: true });
    const components = Object.values(modules).map((module) => markRaw(module.default));
    const sortedItems = components.sort((a, b) => new Date(b.data().date) - new Date(a.data().date));
    this.items = sortedItems
  }
}
</script>
