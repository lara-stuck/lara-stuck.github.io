<template>
  <v-app-bar
    app
    flat
    prominent
  >
    <template v-slot:prepend>
      <a href="/">
        <v-img
        src="/images/logo.png"
        width=50
        class="ml-3"
      />
      </a>
    </template>
    <template
      v-if="$vuetify.display.mdAndUp"
      v-slot:append
    >
      <v-btn
        v-for="item in navigationItems"
        :key="item.text"
        @click="clickNavBarLink(`#${item.value}`)"
        color="primary"
        :variant="item.variant"
        class="ma-2"
      >{{ item.text }}</v-btn>
    </template>
    <template
      v-else
      v-slot:append
    >
      <v-app-bar-nav-icon
        variant="text"
        @click.stop="drawer = !drawer"
      />
    </template>
  </v-app-bar>
  <v-navigation-drawer
      v-model="drawer"
      location="right"
      mobile
      temporary
    >
      <v-list-item
        v-for="item in navigationItems"
        :key="item.text"
        @click="clickNavBarLink(`#${item.value}`)"
        :title="item.text"
        class="text-primary"
      ></v-list-item>
    </v-navigation-drawer>
</template>

<script >
import { useGoTo } from 'vuetify'

export default {
  setup () {
    const goTo = useGoTo()
    return { goTo }
  },
  data: () => ({
    drawer: false,
    bgColor: "transparent",
    navigationItems: [
      {
        text: "Startseite",
        value: "profile-showcase",
        variant: "text"
      },
      {
        text: "Meine Übersetzungen",
        value: "services-showcase",
        variant: "text"
      },
      {
        text: "Mein Weg zum Übersetzen",
        value: "resume-showcase",
        variant: "text"
      },
      // {
      //   text: "Mein Angebot",
      //   value: "/services",
      //   variant: "text"
      // },
      // {
      //   text: "Projekte",
      //   value: "/projects",
      //   variant: "text"
      // },
      {
        text: "Kontakt",
        value: "contact-showcase",
        variant: "flat"
      }
    ],
  }),
  mounted() {
    window.onscroll = () => {
      this.changeColor();
    };
  },
  methods: {
    changeColor() {
      if (
        document.body.scrollTop > 10 ||
        document.documentElement.scrollTop > 10
      ) {
        this.bgColor = 'transparent';
      } else {
        this.bgColor = 'transparent';
      }
    },
    clickNavBarLink(scrollId) {
      if (this.$route.name !== '/') {
        this.$router.push(`/${scrollId}`)
      } else {
        this.goTo(scrollId, { offset: -64 })
      }
    }
  },
}
</script>
