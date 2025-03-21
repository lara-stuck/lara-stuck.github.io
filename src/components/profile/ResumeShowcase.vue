<template>
  <default-showcase
    title="Mein Weg zum Übersetzen"
    link="/profile"
    titlePosition="left"
    color="transparent"
  >
    <v-row>
      <v-col
        class="pt-8"
      >
        <div
          class="text-left"
        >
          <blog-paragraph>

            Eine Sequenz aus schwarzen Buchstaben auf weißem Papier (oder etwas ungewöhnlicher aus weißen Buchstaben auf schwarzem Papier) lässt Leser:innen gespannt die Luft anhalten, laut auflachen oder den Tränen nahekommen.
          </blog-paragraph>
          <blog-paragraph>
            Texte faszinieren mich, seit ich lesen kann. In der Schule kam dann die Leidenschaft an Textanalysen dazu und im Bachelorstudium habe ich den Mix aus Kultur-, Literatur- und Sprachwissenschaft, der Übersetzen ist, als meinen Lieblingscocktail entdeckt. Mit meinem Masterstudium habe ich entschieden, das Übersetzen zu meinem Beruf zu machen.
          </blog-paragraph>
        </div>
        <div
          class="text-right pt-8"
        >
          <resume-entry
            name="Seminar zu “Kinderliteratur übersetzen” (Katharina Herzberger)"
            years="2024-2025"
          />
          <resume-entry
            name="M.A. Studium Literaturübersetzen, HHU Düsseldorf"
            years="seit 2024"
          />
          <resume-entry
            name="freiberufliche Übersetzerin"
            years="seit 2024"
          />
          <resume-entry
            name="Auslandsaufenthalt Bologna, Italien"
            years="2022"
          />
          <resume-entry
            name="selbständige Content-Managerin im Bereich Online Publishing"
            years="2021-2023"
          />
          <resume-entry
            name="B.A. Vergleichende Literaturwissenschaft, Universität Augsburg"
            years="2018-2023"
          />
          <resume-entry
            name="Auslandsaufenthalt Dublin, Irland"
            years="2017-2018"
          />
        </div>
        <blog-paragraph
          class="pt-8 text-h5 text-primary font-weight-light"
        >
          Mitglied im:
        </blog-paragraph>
        <ul>
          <li>Verband deutschsprachiger Übersetzer:innen literarischer und wissenschaftlicher Werke (VdÜ)</li>
          <li>Junge Verlags- und Medienmenschen (JVM)</li>
        </ul>
        <v-row
          class="pt-16"
        >
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
      </v-col>
    </v-row>

  </default-showcase>
</template>

<script>
export default {
  data: () => ({
    logos: [
      "/images/profile/vdue_logo.svg",
      "/images/profile/jvm.png",
      "/images/profile/unia_logo.svg",
      "/images/profile/hhu_logo.jpeg",
    ],
  }),
}
</script>
