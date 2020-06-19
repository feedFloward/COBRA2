<template>
  <div class="home">
    <v-container fluid>
      <v-row>
        <v-col>
          <v-btn @click="addClass">add class</v-btn>
          <classDefinition :classes="classes"></classDefinition>
        </v-col>
        <v-col>
          <v-row>
            <inputspaceCanvas></inputspaceCanvas>
          </v-row>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import inputspaceCanvas from "@/components/classification/inputspace-canvas";
import classDefinition from "@/components/classification/class-definition";
export default {
  name: "Classification",
  components: {
    inputspaceCanvas,
    classDefinition
  },
  data() {
    return {
      classes: []
    };
  },
  methods: {
    addClass() {
      if (this.classes.length < 5) {
        this.classes.push(1);
      }
    }
  }
};
</script>