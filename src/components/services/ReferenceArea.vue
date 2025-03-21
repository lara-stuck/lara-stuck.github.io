<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col
          class="pt-8 pl-8 pr-8 text-h5 text-primary font-weight-light"
          align=center
        >
          <div>Was Kolleg:innen, Übersetzer:innen und Dozent:innen über meine Arbeit sagen:</div>
        </v-col>
      </v-row>
      <v-row
        class="pl-6 pr-6 pb-6"
      >
        <v-col
          v-for="(reference, index) in references"
          :key="index"

          cols=12
          xs=12
          sm=12
          md=4
          lg=4
          xl=4
        >
          <reference-card
            :name="reference.name"
            :quote="reference.quote"
            :source="reference.source"
            :dense="dense"
          />
        </v-col>
      </v-row>
    </v-col>
    </v-row>
</template>



<script>
export default {
  props: {
    dense: Boolean
  },
  data: () => ({
    references: [
      {
        name: "Sam",
        source: "The Fellowship of the Ring",
        quote: "I made a promise Mr Frodo. A promise. 'Don't you leave him Samwise Gamgee.' And I don't mean to. I don't mean to.",
      },
      {
        name: "Aragorn",
        source: "(mensch)",
        quote: "I would have gone with you to the end, into the very fires of Mordor.",
      },
      {
        name: "Smeagol",
        source: "Hobbit",
        quote: "What's taters, precious? What's taters, eh?",
      },
    ],
  }),
}
</script>
