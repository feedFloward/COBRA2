<template>
  <v-app>
    <v-app-bar app></v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>


<script lang="ts">

export default {
  name: 'App',
  data() {
    return {
    }
  },
}
</script>