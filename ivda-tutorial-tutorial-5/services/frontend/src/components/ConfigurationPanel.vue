<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="2" class="sideBar">
          <v-row>
            <v-col cols="12" sm="12">
              <div class="control-panel-font">Company Overview</div>
            </v-col>
          </v-row> <!-- Company Overview -->
          <v-row>
            <v-col cols="12" sm="12">
              <v-select
                  :items="categories.values"
                  label="Select a category"
                  dense
                  v-model="categories.selectedValue"
              ></v-select>
            </v-col>
          </v-row> <!-- Category -->
          <v-row>
            <v-col cols="12" sm="12">
              <div class="control-panel-font">Profit View</div>
            </v-col>
          </v-row> <!-- Profit View -->
          <v-row>
            <v-col cols="12" sm="12">
              <v-select
                  :items="companies.values"
                  label="Select a company"
                  dense
                  v-model="companies.selectedValue"
              ></v-select>
            </v-col>
          </v-row> <!-- Select Company -->
          <v-row>
            <v-col cols="12" sm="12">
              <v-select
                  :items="algorithm.values"
                  label="Select an algorithm"
                  dense
                  v-model="algorithm.selectedValue"
              ></v-select>
            </v-col>
          </v-row> <!-- Select an algorithm -->
        </v-col>
        <v-col cols="12" md="5">
          <ScatterPlot/>
        </v-col>
        <v-col cols="12" md="5">
          <LinePlot/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>


<script>
import ScatterPlot from './ScatterPlot';
import LinePlot from './LinePlot';

export default {
  components: {ScatterPlot, LinePlot},
  data: () => ({
    categories: {
      values: ['All', 'tech', 'health', 'bank'],
      selectedValue: 'All'
    },
    companies: {
      values: [1, 2, 3, 4],
      selectedValue: 1
    },
    algorithm: {
      values: ['none', 'random', 'regression'],
      selectedValue: 'none'
    }
  }),
}
</script>

<style scoped>
.control-panel-font {
  font-family: "Open Sans", verdana, arial, sans-serif;
  align-items: center;
  font-size: 15px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  font-weight: 500;
  height: 40px;
}

.sideBar {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  background: #fafafa;
  padding-left: 17px;
  height: calc(100vh - 50px);

}
</style>
