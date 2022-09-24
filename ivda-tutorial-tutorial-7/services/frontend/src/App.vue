<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h2>Example Project</h2>
    </v-app-bar>
    <v-main>
      <ConfigurationPanel/>
    </v-main>
  </v-app>
</template>

<script>
import ConfigurationPanel from './components/ConfigurationPanel';

export default {
  name: 'App',
  components: {
    ConfigurationPanel,
  },
  data: () => ({
    //
  }),
};
</script>
<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}

html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}
</style>

