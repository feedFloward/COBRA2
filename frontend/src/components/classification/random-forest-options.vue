<template>
  <div>
    <v-slider
    v-model="specs"
    min="1"
    max="200"
    label="number of estimators"
    thumb-label="always"
    ></v-slider>
  </div>
</template>


<script lang="ts">
import { randomForestMethods } from "../../store/helpers" // ts config oder so anpassen damit @/store.. funktioniert
    export default {
    name: "randomForestOptions",

    methods: {
        ...randomForestMethods,
    },

    computed: {
        // das so nochmal überdenken, WENN MÖGLICH IN HELPERS AUSLAGERN!!!!
        specs: {
        get() {
            return this.$store.state.selectedClassifier.specs.number_estimators;
        },
        set(numEstimators) {
            this.rfChooseNumEst(numEstimators)
        }
        }
    }
    };
</script>