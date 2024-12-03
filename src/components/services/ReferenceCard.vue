<template>
  <v-card
    flat
    :class="dense ? 'pa-1' : 'pa-4'"
    color="white"
  >
    <blockquote
      class="pl-3 pr-3 pb-3"
    >
      <cite>”{{ quote }}”</cite>
    </blockquote>
    <p><span class="font-weight-medium">{{ name }}</span>,  <span>{{ source }}</span></p>
  </v-card>
</template>

<script>
export default {
  props: {
    name: String,
    source: String,
    quote: String,
    dense: Boolean
  }
}
</script>
