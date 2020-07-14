<template>
  <div class="home">
    <v-container fluid>
      <nav>
        <ul>
          <v-row>
            <v-col>
              <v-card to="/Classification" max-width="344">
              <v-img src="@/assets/Classification.png" height="200px"></v-img>
              Classification
              </v-card>
            </v-col>
            <v-col>Regression</v-col>
            <v-col>Clustering</v-col>
          </v-row>
        </ul>
      </nav>
    </v-container>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    addClass() {}
  }
};
</script>