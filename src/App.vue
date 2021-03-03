<template>
  <div>
    <main-header></main-header>
    <maintodo></maintodo>
  </div>
</template>
<script>
  import './assets/styles/global.styl'
  import MainHeader from './components/MainHeader.vue'
  import Maintodo from './components/MainToDo/Maintodo.vue'

  export default {
    name: 'App',
    data() {
      return {
        info: null,
      }
    },
    components: {
      MainHeader: MainHeader,
      Maintodo,
    },
  }
</script>

<style lang="stylus" scoped></style>