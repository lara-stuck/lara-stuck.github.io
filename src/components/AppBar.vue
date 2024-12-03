<template>
  <v-app-bar
    app
    flat
    prominent
  >
    <template v-slot:prepend>
      <a href="/">
        <v-img
        src="@/assets/logo.png"
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
        :to="item.value"
        class="text-primary"
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
        :to="item.value"
        :title="item.text"
        class="text-primary"
      ></v-list-item>
    </v-navigation-drawer>
</template>

<script >
export default {
  data: () => ({
    drawer: false,
    bgColor: "transparent",
    navigationItems: [
      {
        text: "Startseite",
        value: "/"
      },
      {
        text: "Über mich",
        value: "/profile"
      },
      {
        text: "Blog",
        value: "/blog"
      },
      {
        text: "Mein Angebot",
        value: "/services"
      },
      {
        text: "Projekte",
        value: "/projects"
      },
      {
        text: "Kontakt",
        value: "/contact"
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
  },
}
</script>
