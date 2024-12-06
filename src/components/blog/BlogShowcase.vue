<template>
  <card-carousel
    title="Blog"
r    :items="items"
    link="/blog"
  />
</template>

<script>
import CardCarousel from '../CardCarousel.vue';


  export default {
  components: { CardCarousel },
    data: () => ({
      items: [],
    }),
    mounted() {
      const modules = import.meta.glob('@/pages/blogs/*.vue', { eager: true });
      const components = Object.values(modules).map((module) => module.default);
      const componentData = components.map((component, index) => {
        let data =  component.data ? component.data() : {};
        data.link = Object.keys(modules)[index].replace("/src/pages", "").replace(".vue", "");
        return data;
      });
      const sortedItems = componentData.sort((a, b) => new Date(b.date) - new Date(a.date));
      this.items = sortedItems.slice(0, 5);
    }
  }
</script>
