<template>
  <div class="main-todo">
    <!-- el-input 要用 keyup.enter.native-->
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

  export default {
    name: 'Maintodo',
    data() {
      return {
        content: '',
        info: null,
        ID: '',
      }
    },
    components: {
      ToDoItem,
    },
    beforeMount: function () {
      setTimeout(() => {
        this.$axios.get('/GetID').then((response) => {
          this.ID = response.data[0]._id.$oid
          console.log('ID:' + this.ID)
          this.$axios
            .post('/search', {
              ID: this.ID,
            })
            .then((response) => (this.info = response.data))
        })
      }, 200)

      // setTimeout(() => {
      //   this.$axios
      //     .post('/search', {
      //       ID: this.ID,
      //     })
      //     .then((response) => (this.info = response.data))
      // }, 500)
    },
    methods: {
      addTodo() {
        if (this.content === '') return
        this.$axios
          .post('/add', {
            ID: this.ID,
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
            ID: this.ID,
            _id: id,
          })
          .then((response) => (this.info = response.data))
      },
      handleElement(data) {
        console.log('mainToDo:' + data)
        this.$axios
          .post('/change', {
            ID: this.ID,
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