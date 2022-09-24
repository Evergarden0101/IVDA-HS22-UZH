<template>
  <div style="height: 90vh">
    <div id='myScatterPlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';


export default {
  name: "ScatterPlot",
  data: () => ({
  }),
  mounted() {
    this.fetchData()
    this.drawScatterPlot()
  },
  methods: {
    drawScatterPlot() {
      var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        mode: 'markers',
        type: 'scatter'
      };

      var trace2 = {
        x: [2, 3, 4, 5],
        y: [16, 5, 11, 9],
        mode: 'lines',
        type: 'scatter'
      };

      var trace3 = {
        x: [1, 2, 3, 4],
        y: [12, 9, 15, 12],
        mode: 'lines+markers',
        type: 'scatter'
      };

      var data = [trace1, trace2, trace3];

      Plotly.newPlot('myScatterPlot', data);
    }

  }


}



</script>

<style scoped>

</style>
