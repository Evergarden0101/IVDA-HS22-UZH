<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Overview of {{ $props.selectedCategory }} Companies</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myScatterPlot' style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';


export default {
  name: "ScatterPlot",
  props: [
    "selectedCategory"
  ],
  data: () => ({
    ScatterPlotData: {x: [], y: []}
  }),
  mounted() {
    console.log(this.$props.selectedCategory);
    this.fetchData()
  },
  methods: {
    async fetchData() {

      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/companies?category=' + this.$props.selectedCategory
      console.log("ReqURL " + reqUrl)

      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      // transform data to usable by scatterplot
      responseData.forEach((company) => {
        this.ScatterPlotData.x.push(company.employees)
        this.ScatterPlotData.y.push(company.founding_year)
      })

      // after the data is loaded, draw the plot
      this.drawScatterPlot()
    },
    drawScatterPlot() {
      var trace1 = {
        x: this.ScatterPlotData.x,
        y: this.ScatterPlotData.y,
        mode: 'markers',
        type: 'scatter'
      };
      var data = [trace1];
      var layout = {}
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myScatterPlot', data, layout, config);
    }
  }
}


</script>

<style scoped>

</style>
