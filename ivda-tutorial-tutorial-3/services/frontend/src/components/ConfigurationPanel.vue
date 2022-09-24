<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="2">
          <v-card>
            Parameters go here
          </v-card>
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
  }),
}
</script>
