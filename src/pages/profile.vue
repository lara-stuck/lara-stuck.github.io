<template>
  <default-page
    title="Über mich"
    color="cardbackground"
  >
    <v-row>
      <v-img
        src="/images/profile.jpeg"
      />
    </v-row>
    <v-row>
      <v-col
        class="pl-8 pr-8"
      >
        <blog-paragraph>
          Ich habe mein Bachelorstudium im Fach Vergleichende Literaturwissenschaft/Europäische Literaturen abgeschlossen und dort meine Liebe zu detailgenauen Textanalysen und Übersetzungen entdeckt. Drei Jahre lang habe ich Artikel für Webseiten übersetzt. Jetzt nähere ich mich wieder meinem Studium an und widme mich dem Übersetzen von englischsprachiger Literatur ins Deutsche.
        </blog-paragraph>
          
        <blog-paragraph>
          Kontaktiert mich gerne für Arbeitsproben oder eine Zusammenarbeit, ich freue mich über jeden Austausch!
        </blog-paragraph>
      </v-col>
    </v-row>
    <template
      v-slot:append
    >
      <v-row>
        <v-col
          v-for="logo in logos"
          :key="logo"
        >
          <v-img
            :src="logo"
            height=50
          />
        </v-col>
      </v-row>
    </template>
  </default-page>
</template>

<script>
import ServiceArea from '@/components/services/ServiceArea.vue'
export default {
  components: { ServiceArea },
  data: () => ({
    logos: [
      "/images/vdue_logo.svg",
      "/images/unia_logo.svg",
      "/images/hhu_logo.png",
    ],
  }),
}
</script>
