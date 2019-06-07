<template>
  <div>
    <ul>
      <li
        v-for="(item, index) of filterTodo"
        v-bind:key="item.id"
        v-bind:class="{ completed: item.isCompleted }"
        v-on:click="changeStatus(index)"
      >
        {{ item.title }}
        <button v-on:click="removeItem(index)">remove</button>
      </li>
    </ul>
  </div>
</template>
<script>
import Vue from "vue"
export default {
  name: "ListItem",
  props: ["todoItem", "filterTodo"],
  methods: {
    removeItem: function(index) {
      let tmp = this.todoItem
      tmp.splice(index, 1)
      this.$emit("update:todoItem", tmp)
    },
    changeStatus: function(index) {
      let tmp = this.todoItem
      // tmp[index].isComplete = true
      Vue.set(tmp, index, { ...tmp[index], isCompleted: true })
      this.$emit("update:todoItem", tmp)
    }
  }
}
</script>
<style>
  li {
    list-style: none;
  }

  .completed {
    text-decoration: line-through;
  }
</style>
