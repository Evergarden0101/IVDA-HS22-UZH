<template>
  <div style="height: 90vh">
    <div id='myLinePlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';


export default {
  name: "LinePlot",
  data: () => ({
  }),
  mounted() {
    this.drawLinePlot()
  },
  methods: {
    drawLinePlot() {
      var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        type: 'scatter'
      };

      var trace2 = {
        x: [1, 2, 3, 4],
        y: [16, 5, 11, 9],
        type: 'scatter'
      };

      var data = [trace1, trace2];

      Plotly.newPlot('myLinePlot', data);
    }

  }


}



</script>

<style scoped>

</style>
