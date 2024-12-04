<template>
   <v-card
    flat
    class="ma-4 pa-4 rounded-lg"
  >
    <v-row
      align=center
    >
      <v-col
        cols=12
        md=6
        align=center
      >
        <v-img
          :src="titleImage"
          max-width=400
        />
      </v-col>
      <v-col
        cols=12
        md=6
      >
        <blog-paragraph
          class="text-h4 text-secondary"
        >
          {{ title }}
        </blog-paragraph>
        <blog-paragraph
          class="text-subtitle-3 font-weight-medium text-black"
        >
          {{ date.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) }}
        </blog-paragraph>
        <blog-paragraph
          class="text-subtitle-3 font-weight-medium text-black"
        >
          {{ summary }}
        </blog-paragraph>
        <slot />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: {
    title: String,
    titleImage: String,
    summary: String,
    date: Date
  }
}
</script>
