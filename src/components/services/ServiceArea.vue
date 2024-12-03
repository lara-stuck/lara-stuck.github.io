<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col
          class="pt-8 pl-8 pr-8 text-h4 text-secondary"
        >
          {{ title }}
        </v-col>
      </v-row>
      <v-row>
        <v-col
          class="pt-6 pl-8 pr-8"
        >
          {{ introduction }}
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col
          class="ma-6"
        >
          <v-expansion-panels
            popout
            flat
          >
            <v-expansion-panel
              v-for="item in items"
              :key="item.title"
            >
              <v-expansion-panel-title>{{ item.title }}</v-expansion-panel-title>
              <v-expansion-panel-text>
                {{ item.description }}
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    title: String,
    introduction: String,
    items: Array
  }
}
</script>
