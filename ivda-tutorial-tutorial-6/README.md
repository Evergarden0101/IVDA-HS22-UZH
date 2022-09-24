### Tutorial-6: Dropdown Interactions

In this tutorial, we would like to achieve the following. A user makes a change in the configuration panel. Then, the Company Overview and Profit View should update accordingly.
In order to achieve this, we have to adapt the backend and the frontend.

#### Switch between categories in the dropdown and automatically trigger a change in the Company Overview
1. Update the backend to accept categories as arguments by adapting the CompaniesList class. Hint: Don't forget the import statement
```python
# add the request import
from flask import request
...

class CompaniesList(Resource):
    def get(self, args=None):
        # retrieve the arguments and convert to a dict
        args = request.args.to_dict()
        print(args)
        # If the user specified category is "All" we retrieve all companies
        if args['category'] == 'All':
            cursor = companies.find()
        # In any other case, we only return the companies where the category applies
        else:
            cursor = companies.find(args)
        # we return all companies as json
        return [Company(**doc).to_json() for doc in cursor]
...
```

2. Next, we switch to the frontend. Here, we call a new method that is triggered whenever the user switches between categories in the dropdown. We adapt the html in the following way.
```html
<v-select
    :items="categories.values"
    label="Select a category"
    dense
    v-model="categories.selectedValue"
    @change="changeCategory"
    ></v-select>
```
3. Next, we create the "changeCategory" method in the methods object in the javascript code.
```javascript
data: () => ({
  scatterPlotId: 0,
  ...
}),
methods: {
changeCategory() {
      this.scatterPlotId += 1
    },
...
}
```
4. The Scatterplot component accepts a key and selected Category arg.
The Key args is a special argument which triggers the component to reload when changed.
The selectedCategory is the current selection of the dropdown (default: All).
```html
<ScatterPlot :key="scatterPlotId" :selectedCategory="categories.selectedValue"/>
```
5. In the ScatterPlot.vue component, we have to accept the incoming argument selectedCategory like this.
```javascript
export default {
  name: "ScatterPlot",
  props: [
    "selectedCategory"
  ],
  ...
}
```

6. Now, we can use the parameter "selectedCategory" inside the ScatterPlot.vue Component. We can change the title of the component. It will now be e.g. Overview of All Companies depending on the chosen parameter (All, tech, health, bank).
```html
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
```

7. Adjust the ReqURL like this. We will use request args to chain the user params which we can receive as a dict in the backend (see previous step).
```Javascript
async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/companies?category=' + this.$props.selectedCategory
      console.log("ReqURL " + reqUrl)
...
}
```
8. Try the implemented change: You should be able to change the selection from the categories dropdown and trigger the ScatterPlot.vue component to reload and hence make a API call with the chosen parameter. You should see that the Company Overview only shows the companies from the respective category.
Remember: Run ``npm run serve`` for the frontend (terminal in webstorm) and ``python app.py run`` to run the backend.


#### Switch between company IDs and algorithms in the dropdown and automatically trigger a change in the Profit View

1. Add an \@change method to the existing v-selectors in the ConfigurationPanel.vue
```html
<v-row>
    <v-col cols="12" sm="12">
      <v-select
          :items="companies.values"
          label="Select a company"
          dense
          v-model="companies.selectedValue"
          @change="changeCompany"
      ></v-select>
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="12" sm="12">
      <v-select
          :items="algorithm.values"
          label="Select an algorithm"
          dense
          v-model="algorithm.selectedValue"
          @change="changeAlgorithm"
      ></v-select>
    </v-col>
  </v-row>
```
2. Add the two methods:
```
data: () => ({
    ...
    linePlotId: 0,
    ...
},
methods: {
    ...
    changeCompany() {
          this.linePlotId += 1
    },
    changeAlgorithm() {
          this.linePlotId += 1
    }
    ...
}
```
3. Adjust the LinePlot tag to accept the key.
```html
<LinePlot :key="linePlotId"
            :selectedCompany="companies.selectedValue"
            :selectedAlgorithm="algorithm.selectedValue"/>
```
4. Accept the props inside the LinePlot.vue Component
```javascript
export default {
  name: "LinePlot",
  props: ["selectedCompany", "selectedAlgorithm"],
  ...
}
```
5. Add a title to Profit View depending on the currently selected company.
```html
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
```
6. Adjust the ReqUrl in the following way in the LinePlot javascript code. Note: We will implement the backend for the algorithm part in a future tutorial.
```javascript
var reqUrl = 'http://127.0.0.1:5000/companies/' + this.$props.selectedCompany +
          '?algorithm=' + this.$props.selectedAlgorithm
```

#### References
[Vue JS 2 Tutorial #24 - Events (child to parent)](https://www.youtube.com/watch?v=5pvG6fzkdFM)
