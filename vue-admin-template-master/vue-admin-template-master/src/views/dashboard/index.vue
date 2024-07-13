<template>
  <div class="top-card">
    <Card></Card>
    <Chart></Chart>
    <Map></Map>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from './Card/index'
import Chart from './Chart/index.vue'
import Map from './Map/index.vue'

export default {
  name: 'Dashboard',
  components: {
    Card,
    Chart,
    Map
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}

.top-card{
  padding-top: 15px;
}
</style>
