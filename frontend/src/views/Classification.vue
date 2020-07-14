<template>
  <div class="home">
    <v-container fluid>
      <v-row>
        <v-col>
          <classDefinition :classes="classes"></classDefinition>
        </v-col>
        <v-col>
            <inputspaceCanvas ref="inputspaceCanvas"></inputspaceCanvas>
        </v-col>
        <v-col></v-col>
      </v-row>
      <v-row>
        <v-col cols="2"><!--classifier definition here -->
          <classifierSelection></classifierSelection>
        </v-col>
        <v-col>
          <svmOptions v-if="selectedClassifier.value == 'svm'"></svmOptions>
          <randomForestOptions v-else-if="selectedClassifier.value == 'random_forest'"/>
        </v-col>
        <v-col>
          <v-btn @click="train" color="green white--text">train!</v-btn>
        </v-col>
      </v-row>
    </v-container>
    <v-overlay :value="overlayLoading">
      
    </v-overlay>
  </div>
</template>

<script>
import inputspaceCanvas from "@/components/classification/inputspace-canvas";
import classDefinition from "@/components/classification/class-definition";
import classifierSelection from "@/components/classification/classifier-selection";
import svmOptions from "@/components/classification/svm-options";
import randomForestOptions from "@/components/classification/random-forest-options";
import { mapState } from 'vuex';
import { data } from '@/shared';
import axios from 'axios';

export default {
  name: "Classification",
  components: {
    inputspaceCanvas,
    classDefinition,
    classifierSelection,
    svmOptions,
    randomForestOptions,
  },
  data() {
    return {
      overlayLoading: false,
    };
  },
methods: {
  async train() {
    //wie zeichnen?
    let answer = await data.trainRequest(this.classes, this.inputspace, this.selectedClassifier, this.trainingSpecs)
    this.$store.state.clfResponse = answer
    this.$refs.inputspaceCanvas.drawPredictions()
  }
},
  computed: {
    ...mapState({
      classes: state => state.classes,
      selectedClassifier: state => state.selectedClassifier,
      inputspace: state => state.inputspace,
      trainingSpecs: state => state.trainingSpecs
    })
  },
created() {
  axios.interceptors.request.use((config) => {
    this.overlayLoading = true
    return config;
  }, (error) => {
    this.overlayLoading = false
    return Promise.reject(error);
  });

  axios.interceptors.response.use((response) => {
    this.overlayLoading = false
    return response;
  }, (error) => {
    this.overlayLoading = false
    return Promise.reject(error);
  });
}
};
</script>