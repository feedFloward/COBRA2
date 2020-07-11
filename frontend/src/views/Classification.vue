<template>
  <div class="home">
    <v-container fluid>
      <v-row>
        <v-col>
          <classDefinition :classes="classes"></classDefinition>
        </v-col>
        <v-col>
          <v-row>
            <inputspaceCanvas ref="inputspaceCanvas"></inputspaceCanvas>
          </v-row>
        </v-col>
        <v-col></v-col>
      </v-row>
      <v-row>
        <v-col cols="2"><!--classifier definition here -->
          <classifierSelection></classifierSelection>
        </v-col>
        <v-col>
          <svmOptions v-if="selectedClassifier.value == 'svm'"></svmOptions>
        </v-col>
        <v-col>
          <v-btn @click="train" color="green white--text">train!</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import inputspaceCanvas from "@/components/classification/inputspace-canvas";
import classDefinition from "@/components/classification/class-definition";
import classifierSelection from "@/components/classification/classifier-selection";
import svmOptions from "@/components/classification/svm-options";
import { mapState } from 'vuex';
import { data } from '@/shared';

export default {
  name: "Classification",
  components: {
    inputspaceCanvas,
    classDefinition,
    classifierSelection,
    svmOptions,
  },
  data() {
    return {
    };
  },
methods: {
  async train() {
    //wie zeichnen?
    let answer = await data.trainRequest(this.classes, this.inputspace, this.selectedClassifier)
    this.$store.state.clfResponse = answer
    this.$refs.inputspaceCanvas.drawPredictions()
  }
},
  computed: {
    ...mapState({
      classes: state => state.classes,
      selectedClassifier: state => state.selectedClassifier,
      inputspace: state => state.inputspace,
    })
  },
};
</script>