<template>
  <v-container
    class="mt-16"
    max-width="868"
  >
    <v-row>
      <v-col class="text-h2 text-secondary">
        {{ title }}
      </v-col>
    </v-row>
    <v-row>
      <v-col
        class='text-subtitle-1'
      >
        {{ date.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) }}
      </v-col>
    </v-row>
    <v-row>
      <v-col
        class='text-subtitle-1'
      >
        {{ summary }}
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-img
          :src='titleImage'
          max-height=600
          width=100%
          cover
        ></v-img>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <slot />
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
export default {
  props: {
    title: String,
    summary: String,
    titleImage: String,
    date: Date
  }
}
</script>
