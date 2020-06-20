<template>
    <v-item>
        <v-card
        :active="isActive"
        width="150"
        height="150"
        :color="color"
        class="text-center ma-2"
        :class="isActive? 'darken-5' : 'lighten-5'"
        :elevation="isActive? 24 : 3"
        >
          <v-card-text @click="selectClass">
            <p>class {{ classIndex }}</p>
            <p>#samples</p>
          </v-card-text>
          <v-card-actions>
            <v-btn small class="red white--text" @click="removeClass">delete</v-btn>
          </v-card-actions>
        </v-card>
    </v-item>
</template>

<script>
export default {
  name: "classCard",
  props: {
    classIndex: {
      type: Number
    },
    color: {
        type: String
    }
  },
  data() {
    return {
    };
  },
  methods: {
    removeClass() {
      this.$store.commit("removeClass", this.classIndex);
    },
    selectClass() {
        this.$store.commit("selectClass", this.classIndex-1)
    }
  },
  mounted() {
      this.selectClass()
  },
  destroyed () {
      this.$store.state.currentClass = {};
  },
  computed: {
      isActive() {
          return this.$store.getters.getCurrentClassIndex == this.classIndex ? true : false
      }
  },
};
</script>