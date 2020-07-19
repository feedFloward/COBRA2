<template>
  <div>
    <v-tooltip v-model="showTooltip" bottom>
      <template v-slot:activator="{ on, attrs}">
        <v-slider
        v-bind="attrs"
        v-on="on"
          v-model="specs"
          min="1"
          max="200"
          label="number of estimators"
          thumb-label="always"
        ></v-slider>
      </template>
      <span>This is basicaly a decision tree trained on a random dataset...</span>
    </v-tooltip>
  </div>
</template>


<script lang="ts">
import { randomForestMethods } from "../../store/helpers"; // ts config oder so anpassen damit @/store.. funktioniert
export default {
  name: "randomForestOptions",

  methods: {
    ...randomForestMethods
  },

  computed: {
    // das so nochmal überdenken, WENN MÖGLICH IN HELPERS AUSLAGERN!!!!
    specs: {
      get() : number {
        return this.$store.state.selectedClassifier.specs.number_estimators;
      },
      set(numEstimators: number) {
        this.rfChooseNumEst(numEstimators);
      }
    },
    showTooltip() {
        return this.specs == 1? true: false
    }
  }
};
</script>