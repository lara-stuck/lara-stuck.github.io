<template>
  <default-page
    title="Mein Angebot"
    color="cardbackground"
  >
    <service-area
      v-for="serviceArea in serviceAreas"
      :key="serviceArea.title"
      :title="serviceArea.title"
      :introduction="serviceArea.introduction"
      :items="serviceArea.services"
    />

    <reference-area />

  </default-page>
</template>

<script>
import ServiceArea from '@/components/services/ServiceArea.vue'
import ReferenceArea from '@/components/services/ReferenceArea.vue'
export default {
  components: { ServiceArea, ReferenceArea },
  data: () => ({
    references: [
      {
        name: "Sam, The Fellowship of the Ring",
        quote: "I made a promise Mr Frodo. A promise. 'Don't you leave him Samwise Gamgee.' And I don't mean to. I don't mean to.",
      },
      {
        name: "Aragorn, The Fellowship of the Ring",
        quote: "I would have gone with you to the end, into the very fires of Mordor.”",
      },
      {
        name: "Smeagol, The Two Towers",
        quote: "What's taters, precious? What's taters, eh?",
      },
      {
        name: "Gollum, The Return of the King",
        quote: "She’s always hungry. She always needs to feed.",
      },
    ],
    serviceAreas: [
      {
        title: "Bereich A",
        introduction: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        services: [
          {
            title: "Leistung 1",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 2",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 3",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 4",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
        ]
      },
      {
        title: "Bereich B",
        introduction: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        services: [
          {
            title: "Leistung 1",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 2",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 3",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 4",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
          {
            title: "Leistung 5",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
          },
        ]
      },
    ],
  }),
}
</script>
