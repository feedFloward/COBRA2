<template>
  <div>
    <v-row>
      <v-col>
      <v-btn @click="addClass">add class</v-btn>
      </v-col>
    </v-row>

    <v-row class="ma-2">
      <v-col>
        <v-card height="400">
          <v-item-group multiple="false">
            <!-- multiple="false" mandatory -->
            <v-row wrap>
              <classCard
                v-for="cls in classes"
                :key="cls.index"
                :classIndex="cls.index"
                :color="cls.color"
              ></classCard>
            </v-row>
          </v-item-group>
        </v-card>
      </v-col>
    </v-row>

    <v-row align="end">
      <v-col>
        <v-slider
          v-model="trainTestSplit"
          min="0.05"
          max="0.5"
          step="0.01"
          label="test/train-split"
          thumb-label="always"
        ></v-slider>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import classCard from "@/components/classification/class-card";
import { classDefinitionComputed } from "@/store/helpers";
export default {
  name: "classDefinition",
  components: {
    classCard
  },
  data() {
    return {};
  },
  props: {
    classes: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    trainTestSplit: {
      get() {
        return this.$store.state.trainingSpecs.test_size;
      },
      set(trainTestSplit) {
        this.setTrainTestSplit(trainTestSplit);
      }
    }
  },
  methods: {
    ...classDefinitionComputed,
    addClass() {
      if (this.classes.length < 6) {
        this.$store.commit("addClass");
      }
    },
    selectClass() {}
  }
};
</script>