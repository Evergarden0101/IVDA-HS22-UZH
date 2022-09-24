<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Profit View of Company: {{ $props.selectedCompany }}</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';


export default {
  name: "LinePlot",
  props: ["selectedCompany", "selectedAlgorithm"],
  data: () => ({
    LinePlotData: {x: [], y: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl = 'http://127.0.0.1:5000/companies/' + this.$props.selectedCompany +
          '?algorithm=' + this.$props.selectedAlgorithm
      console.log("ReqURL " + reqUrl)

      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      // transform data to usable by lineplot
      responseData.profit.forEach((profit) => {
        this.LinePlotData.x.push(profit.year)
        this.LinePlotData.y.push(profit.value)
      })

      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {
      var trace1 = {
        x: this.LinePlotData.x,
        y: this.LinePlotData.y,
        type: 'scatter'
      };
      var data = [trace1];
      var layout = {}
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myLinePlot', data, layout, config);
    }
  }
}


</script>

<style scoped>

</style>
