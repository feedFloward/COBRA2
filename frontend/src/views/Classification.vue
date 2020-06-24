<template>
  <div class="home">
    <v-container fluid>
      <v-row>
        <v-col>
          <classDefinition :classes="classes"></classDefinition>
        </v-col>
        <v-col>
          <v-row>
            <inputspaceCanvas></inputspaceCanvas>
          </v-row>
        </v-col>
        <v-col></v-col>
      </v-row>
      <v-row>
        <v-col cols="2"><!--classifier definition here -->
          <classifierSelection></classifierSelection>
        </v-col>
        <v-col></v-col>
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
import { mapState } from 'vuex';
import { data } from '@/shared';

export default {
  name: "Classification",
  components: {
    inputspaceCanvas,
    classDefinition,
    classifierSelection,
  },
  data() {
    return {
    };
  },
methods: {
  async train() {
    let answer = await data.trainRequest(this.classes)
    console.log(answer)
  }
},
  computed: {
    ...mapState({
      classes: state => state.classes
    })
  },
};
</script>