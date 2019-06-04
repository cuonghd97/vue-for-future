<template>
  <div id="app">
    <AddTodo v-bind:todoItem.sync="todoItem"></AddTodo>
    <ListItem
      v-bind:todoItem.sync="todoItem"
      v-bind:filterTodo.sync="filterTodo"
    ></ListItem>
    <div>
      <span>{{ countLeftItem }} item left</span>
      <button v-on:click="changeTypeFilterToAll">All</button>
      <button v-on:click="changeTypeFilterToActive">Active</button>
      <button v-on:click="changeTypeFilterToCompleted">Completed</button>
      <button
        v-show="hasCompleted"
        v-on:click="clearCompleted"
      >Clear completed</button>
    </div>
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
      typeFilter: "all"
    }
  },
  methods: {
    changeTypeFilterToAll: function() {
      this.typeFilter = "all"
    },
    changeTypeFilterToActive: function() {
      this.typeFilter = "active"
    },
    changeTypeFilterToCompleted: function() {
      this.typeFilter = "completed"
    },
    clearCompleted: function() {
      let tmp = this.todoItem.filter(item => (
        !item.isCompleted
      ))
      this.todoItem = tmp
    }
  },
  watch: {
    addText: function(newAddText) {
      console.log(newAddText);
    },
    todoItem: function(newTodoItem) {
      console.log(newTodoItem)
    },
    typeFilter: function(val) {
      console.log(val)
    }
  },
  computed: {
    countLeftItem: function() {
      const listTodo = this.todoItem
      let count = 0
      for (let todo of listTodo) {
        if (!todo.isCompleted) {
          count += 1
        }
      }
      return count
    },
    hasCompleted: function() {
      const listTodo = this.todoItem
      let count = 0
      for (let todo of listTodo) {
        if (todo.isCompleted) {
          count += 1
        }
      }
      return count > 0 ? true : false
    },
    filterTodo: function() {
      if (this.typeFilter === "all") {
        return this.todoItem
      }
      if (this.typeFilter === "active") {
        return this.todoItem.filter(item => (
          !item.isCompleted
        ))
      }
      if (this.typeFilter === "completed") {
        return this.todoItem.filter(item => (
          item.isCompleted
        ))
      }
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
