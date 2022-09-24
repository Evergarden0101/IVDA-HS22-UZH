### Tutorial-7 Plot Interaction

In this tutorial set, the goal is that a user can click on a company in the Company Overview which then reloads the Profit View with the clicked company.
To achieve this, we will implement a click event upon a click on a data point in the scatterplot. This click event will then trigger a change in the Profit View.

#### Prerequisite: Hoverinfo on Scatterplot points to show the Company Name
We would first like to know the company name when we hover over a point in the Company Overview.

1. Adjust the ScatterPlotData inside ScatterPlot.vue in the following way. We add an extra list for the names of the company.
```javascript
data: () => ({
    ScatterPlotData: {x: [], y: [], name: []},
  }),
```
2. Then, we will adjust the fetchData method in the following way. We will add the company names to the list.
```javascript
async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/companies?category=' + this.$props.selectedCategory
      console.log('ReqURL ' + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      // transform data to usable by scatterplot
      responseData.forEach((company) => {
        this.ScatterPlotData.name.push(company.name)
        this.ScatterPlotData.x.push(company.employees)
        this.ScatterPlotData.y.push(company.founding_year)
      })
      // after the data is loaded, draw the plot
      this.drawScatterPlot()
```
3. Add ``text: this.ScatterPlotData.name,`` to the trace1 inside the drawScatterPlot method.

#### Add a click event to the ScatterPlot
1. Adjust the drawScatterPlot() method in the following way. We (1) add a marker that sets the color of all data points to be black and of the same size. (2) We call a method after we created the plot which is responsible to handle the click events.
```Javascript
drawScatterPlot() {
      var trace1 = {
        x: this.ScatterPlotData.x,
        y: this.ScatterPlotData.y,
        mode: 'markers',
        type: 'scatter',
        text: this.ScatterPlotData.name,
        marker: {
          color: 'black',
          size: 12
        }
      };
      var data = [trace1];
      var layout = {}
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myScatterPlot', data, layout, config);
      this.clickScatterPlot()
    },
```
2. Create the clickScatterPlot method. Upon a click, retrieve the point number and then emit an event with (pn+1 = company id). Emitting an event will notify the parent (configuration panel) that the selected company has changed. Then, we revert all colors to black in case of previous clicks and change the current selection to blue. Then we call the Plotly.restyle function to update the plot.
```Javascript
clickScatterPlot() {
      var pn = 0
      var that = this
      var myPlot = document.getElementById('myScatterPlot')
      myPlot.on('plotly_click', function (data) {
        for (var i = 0; i < data.points.length; i++) {

          // get the index of point
          pn = data.points[i].pointNumber;

          // emit event to change the currently selected company in the a) configuration panel
          // and b) update the Profit View
          that.$emit('changeCurrentlySelectedCompany', pn + 1)

          // revert all colors
          var colors = ['#00000' * 15]

          // and change currently selected color to blue
          colors[pn] = '#3777ee';

          // update the marker and plot
          var update = {'marker': {color: colors, size: 12}};
          Plotly.restyle('myScatterPlot', update);
        }
      });
    }
```
3. In the ConfigurationPanel.vue add the following code to allow an emitted event from the child component (Company Overview) to the parent component (Configuration Panel).
```html
<ScatterPlot :key="scatterPlotId"
                 :selectedCategory="categories.selectedValue"
                 @changeCurrentlySelectedCompany="changeCurrentlySelectedCompany"
          />
          
```
4. Add the changeCurrentlySelectedCompany method in the method part of the configuration panel.
```javascript
methods: {
        ...
        changeCurrentlySelectedCompany(companyId) {
        this.companies.selectedValue = companyId
        this.changeCompany()
        },
...
}
```

#### References
[Vue JS 2 Tutorial #25 - The Event Bus](https://www.youtube.com/watch?v=jzh4zQcfB0o)
