<template>
  <div class="todo-item">
    <el-row :gutter="10">
      <el-col :span="5"
        ><div class="grid-content bg-purple">
          <el-checkbox
            size="medium"
            v-model="todo.PMflag"
            @change="change_flag"
            border
            >{{ todo.PMcontent }}</el-checkbox
          >
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <el-select
            v-model="todo.PMcompleted"
            placeholder="重要程度"
            @change="change_select"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select></div
      ></el-col>
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <el-date-picker
            v-model="todo.PMdatatime"
            type="datetime"
            placeholder="选择截止时间"
            @change="change_time"
          >
          </el-date-picker></div
      ></el-col>
      <el-col :span="5"
        ><div class="grid-content bg-purple">
          <el-button @click="delItem">删除</el-button>
        </div></el-col
      >
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'ToDoItem',
    props: {
      todo: Object,
    },
    data() {
      return {
        options: [
          {
            value: '选项1',
            label: '不重要',
          },
          {
            value: '选项2',
            label: '重要',
          },
          {
            value: '选项3',
            label: '非常重要',
          },
        ],
      }
    },
    methods: {
      delItem() {
        this.$emit('del', this.todo._id.$oid)
      },
      change_flag() {
        this.$emit('change_element', {
          _id: this.todo._id.$oid,
          PMflag: this.todo.PMflag,
        })
        console.log('todoItem:' + this.todo.PMflag)
      },
      change_time() {
        this.$emit('change_element', {
          _id: this.todo._id.$oid,
          PMdatatime: this.todo.PMdatatime,
        })
        console.log('todoItem:' + this.todo.PMdatatime)
      },
      change_select() {
        this.$emit('change_element', {
          _id: this.todo._id.$oid,
          PMcompleted: this.todo.PMcompleted,
        })
        console.log('todoItem:' + this.todo.PMcompleted)
      },
    },
  }
</script>

<style lang="stylus" scoped>
  // .todo.item
  // display: flex
  // justify-content: space--between
  // padding: 10px
  .el-row
    margin-bottom: 20px

    &:last-child
      margin-bottom: 0

  .el-col
    border-radius: 4px

  .bg-purple-dark
    background: Transparent

  .bg-purple
    background: Transparent

  .bg-purple-light
    background: Transparent

  .grid-content
    border-radius: 4px
    min-height: 36px

  .row-bg
    padding: 10px 0
    background-color: Transparent
</style>