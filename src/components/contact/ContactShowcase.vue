<template>
  <default-showcase
    color="transparent"
  >
    <v-row
    class="pa-6"
    >
      <v-col
        cols=12
        sm=6
        md=6
        lg=5
        xl=5
        class="rounded-circle"
        align="center"
      >
        <v-img
          class="rounded-circle"
          src="@/assets/lara_portrait.jpg"
          max-width=300
        />
      </v-col>
      <v-col
        cols=12
        sm=5
        md=5../DefaultCard.vue
        lg=6./blog/Blo../BlogCard.vue
        xl=3
        align-self="center"
        class="mt-8 ml-4"
      >
        <v-row
          class="text-h6 font-weight-light mb-8"
          justify=start
        ><div>
          Interessiert an einem Austausch oder einer Zusammenarbeit? Melde dich bei mir!
        </div>
        </v-row>
        <v-row
          class="text-h4 font-weight-light mb-8"
          justify=start
        ><div>
          <span class="text-primary">Lara </span>
          <span class="text-error">Stuck</span>
        </div>
        </v-row>
        <v-row
          class="mb-3"
          justify=start
        >
          <a href="mailto:lara.stuck@outlook.com" target="_blank">
            <v-icon
              class="mr-2 pb-1"
              icon="mdi-email"
            >
            </v-icon>lara.stuck@outlook.com
          </a>
        </v-row>
        <v-row
              justify=start>
          <a href="https://www.linkedin.com/in/lara-stuck-042130216/" target="_blank">
            <v-icon
              class="mr-2 pb-1"
              icon="mdi-linkedin"
            >
            </v-icon>LinkedIn
          </a>
        </v-row>
      </v-col>
    </v-row>
  </default-showcase>
</template>
