<template>
  <div class="main-todo">
    <!-- el-input 要用 keyup.enter.native ，有坑-->
    <el-input
      placeholder="请输入内容"
      suffix-icon="el-icon-date"
      v-model="content"
      @keyup.enter.native="addTodo"
    >
    </el-input>
    <to-do-item
      v-for="(item, index) in info"
      :key="index"
      :todo="item"
      @del="handleDelet"
      @change_element="handleElement"
    ></to-do-item>
  </div>
</template>

<script>
  import ToDoItem from './coms/ToDoItem.vue'

  var ip = returnCitySN['cip']
  console.log(ip)

  export default {
    name: 'Maintodo',
    data() {
      return {
        content: '',
        info: null,
      }
    },
    components: {
      ToDoItem,
    },
    created: function () {
      //this.$axios.get('/search').then((response) => (this.info = response.data))
      this.$axios
        .post('/search', {
          IP: ip,
        })
        .then((response) => (this.info = response.data))
    },
    methods: {
      addTodo() {
        if (this.content === '') return
        this.$axios
          .post('/add', {
            IP: ip,
            PMcontent: this.content,
            PMflag: true,
            PMcompleted: '',
            PMdatatime: '',
          })
          .then((response) => (this.info = response.data))
        this.content = ''
      },
      handleDelet(id) {
        console.log('mainToDo:' + id)
        this.$axios
          .post('/delete', {
            IP: ip,
            _id: id,
          })
          .then((response) => (this.info = response.data))
      },
      handleElement(data) {
        console.log('mainToDo:' + data)
        this.$axios
          .post('/change', {
            IP: ip,
            _id: data._id,
            PMflag: data.PMflag,
            PMdatatime: data.PMdatatime,
            PMcompleted: data.PMcompleted,
          })
          .then((response) => (this.info = response.data))
      },
    },
  }
</script>
<style lang="stylus" scoped>
  .main-todo
    width: 1000px
    margin: 0 auto
</style>