<template>
  <div>
    <div class="card-header">
      <span>{{title}}</span>
    </div>
    <div class="card-content">
      <span class="num">{{count}}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Detail',
  props:[
    'title',
    'count'
  ]
}
</script>

<style scoped>
  .num{
    font-size: 25px;
    color: white;
    padding-right: 10px;
    text-align: center;
  };
  .card-content{
    justify-content: center;
    text-align: center;
  };
</style>
