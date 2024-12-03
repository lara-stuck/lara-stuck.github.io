<template>
  <default-page
    title="Blog"
    color="cardbackground"
  >
    <v-row
      justify="center"
    >
      <v-col
        v-for="item in items"
        :key=item.title
        class="ma-4"
      >
          <blog-card
          :title=item.title
          :titleImage=item.titleImage
          :summary=item.summary
          :link="item.link"
          :min-width=300
        />
      </v-col>
    </v-row>
  </default-page>
</template>

<script>
import BlogCard from '@/components/blog/BlogCard.vue'


  export default {
  components: { BlogCard },
    data: () => ({
      items: [],
      numberRows: 0,
      numberColumns: 0,
    }),
    mounted() {
      const modules = import.meta.glob('@/pages/blogs/*.vue', { eager: true });
      const components = Object.values(modules).map((module) => module.default);
      const componentData = components.map((component, index) => {
        let data =  component.data ? component.data() : {};
        data.link = Object.keys(modules)[index].replace("/src/pages", "").replace(".vue", "");
        return data;
      });
      this.items = componentData.sort((a, b) => new Date(b.date) - new Date(a.date));
    }
  }
</script>
