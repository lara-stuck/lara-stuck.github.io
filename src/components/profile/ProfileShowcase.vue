<template>
  <v-card
    color="transparent"
    elevation=0
    class="mb-4 rounded-lg"
  >
    <v-row
    align="end"
  >
    <v-col
      cols=12
      md=6
      class="split-view"
      @mousemove="updateClipPath"
      @touchmove.passive="updateClipPath"
      :style="{ height: '600px' }"
    >
    <!-- Vertical line to show mouse position -->
    <div class="vertical-line" :style="{ left: `${mouseX}px` }"></div>

    <!-- Bottom card -->
    <v-card
      class="layer mt-16 pa-4"
      :style="{ zIndex: 1 }"
      elevation=0
    >
      <v-row
          class="text-h1 text-primary font-weight-thin pl-6 pb-0 mt-16 mb-0"
        >
          Lara
        </v-row>
        <v-row
          class="text-h1 text-error font-weight-thin pl-6 pb-12 pt-0 mt-0"
        >
          Stuck
        </v-row>
        <v-card-subtitle
          class="text-subtitle-1"
        >
          Literarische Übersetzerin
        </v-card-subtitle>
        <v-card-text
          class="text-body-1"
        >
          Ich bin literarische Übersetzerin mit Sitz in Düsseldorf.
          Romane, Kinderbücher oder Gedichte.
          Englisch und Italienisch zu Deutsch.
        </v-card-text>
        <v-card-actions>
          <v-btn
            color="secondary"
            to="/profile"
          >
            Mehr über mich
          </v-btn>
        </v-card-actions>
    </v-card>

    <!-- Top card with clipping -->
    <v-card
      class="layer mt-16 pa-4"
      :style="{ clipPath: clipPathStyle, zIndex: 2 }"
      elevation=0
    >
      <v-row
          class="text-h1 text-secondary font-weight-thin pl-6 pb-0 mt-16 mb-0"
        >
          Lara
        </v-row>
        <v-row
          class="text-h1 text-success font-weight-thin pl-6 pb-12 pt-0 mt-0"
        >
          Stuck
        </v-row>
        <v-card-subtitle
          class="text-subtitle-1"
        >
          Litarary translator
        </v-card-subtitle>
        <v-card-text
          class="text-body-1"
        >
          I am a literary translator currently living in Düsseldorf.
          Novels, children's books or poems.
          From English and Italian to German.
        </v-card-text>
        <v-card-actions>
          <v-btn
            color="info"
            to="/profile"
          >
            More about me
          </v-btn>
        </v-card-actions>
    </v-card>
      
    </v-col>
    <v-col
      cols=12
      md=6
    >
      <v-img
        src="/images/lara.jpg"
        cover
        max-height=600
        ref="introductionImage"
        class="introduction-image"
      >
      </v-img>
    </v-col>
  </v-row>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      mouseX: 0, // Tracks the mouse X position
      clipPathStyle: "polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)", // Initial clip path
    };
  },
  methods: {
    updateClipPath(event) {
      const container = event.currentTarget;
      const rect = container.getBoundingClientRect();

      const clientX = event.touches ? event.touches[0].clientX : event.clientX;

      const xPercent = ((clientX - rect.left) / rect.width) * 100;
      const yPercent = 100;

      this.clipPathStyle = `polygon(0% 0%, ${xPercent}% 0%, ${xPercent}% ${yPercent}%, 0% ${yPercent}%)`;

      this.mouseX = clientX - rect.left;
    },
  },
};
</script>

<style>
.split-view {
  position: relative;
}
.layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
}
.vertical-line {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: red; /* Line color */
  z-index: 3; /* Above the cards */
  pointer-events: none; /* Allows interaction with the cards without blocking */
}
</style>
