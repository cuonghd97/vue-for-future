<template>
  <div>
    <input
      type="text"
      v-model="value"
      v-on:keyup.enter="addTodoItem"
    >
  </div>
</template>
<script>
export default {
  name: "AddTodo",
  props: ["todoItem"],
  data: function() {
    return {
      value: "",
    }
  },
  methods: {
    addTodoItem: function() {
      let tmp = this.todoItem;
      tmp.push({ title: this.value, isCompleted: false })
      this.$emit("update:todoItem", tmp)
      this.value=""
    }
  }
}
</script>
