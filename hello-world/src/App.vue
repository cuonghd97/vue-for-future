<template>
  <div id="app">
    <AddTodo v-bind:todoItem.sync="todoItem"></AddTodo>
    <ListItem v-bind:todoItem.sync="todoItem"></ListItem>
    <span>{{ countLeftItem }} item left</span>
  </div>
</template>

<script>
import AddTodo from "./components/AddTodo"
import ListItem from "./components/ListItem"

export default {
  name: 'app',
  components: {
    AddTodo,
    ListItem
  },
  data: function() {
    return {
      addText: "",
      todoItem: [],
      leftItem: 0
    }
  },
  watch: {
    addText: function(newAddText) {
      console.log(newAddText);
    },
    todoItem: function(newTodoItem) {
      console.log(newTodoItem)
    }
  },
  computed: {
    countLeftItem: function() {
      return this.todoItem.length
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
