<template>
  <v-container>

    <v-row
      class="text-h2 text-primary font-weight-normal mt-8 mb-8"
    >
      <v-col
        align="center"
      >
        {{ title }}
      </v-col>
    </v-row>
    <v-card
      elevation=0
      class="pa-4 rounded-lg"
      :color=color
    >
      <v-row>
          <slot />
      </v-row>
    </v-card>

    <v-row
      class="mt-8"
    >
      <v-col>
        <slot
          name="append"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    props: {
      title: String,
      color: String
    }
  }
</script>