<template>
  <el-header height="120px" class="main-header">
    <el-row :gutter="20">
      <el-col :span="10"
        ><div class="grid-content bg-purple">
          <el-input placeholder="SessionID的值" v-model="session_ID">
            <template slot="prepend">SessionID</template>
          </el-input>
        </div></el-col
      >
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
    </el-row>

    <h1>ToDoList</h1>
  </el-header>
</template>

<script>
  export default {
    name: 'MainHeader',
    data() {
      return {
        cookie_flag: false,
        session_ID: '',
      }
    },
    created: function () {
      //this.cookie_flag = this.$cookies.remove('session')
      this.cookie_flag = this.$cookies.isKey('session')
      console.log(this.cookie_flag)
      if (!this.cookie_flag) {
        this.$axios.get('/SetID').then((response) => {
          console.log(response.data)
          this.$axios.get('/GetID').then((response) => {
            this.session_ID = response.data[0]._id.$oid
            console.log('Get:' + this.session_ID)
          })
        })
      } else {
        this.$axios.get('/GetID').then((response) => {
          this.session_ID = response.data[0]._id.$oid
          console.log('Get:' + this.session_ID)
        })
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .main-header
    text-align: center

    h1
      margin: 20px
      front-size: 100px
      front-weight: 100
      color: rgb(254, 67, 101)
</style>