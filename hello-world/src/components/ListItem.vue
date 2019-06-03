<template>
  <div>
    <ol>
      <ul
        v-for="(item, index) of todoItem"
        v-bind:key="item.id"
      >
        {{ item.title }}
        <button v-on:click="removeItem(index)">remove</button>
      </ul>
    </ol>
  </div>
</template>
<script>
export default {
  name: "ListItem",
  props: ["todoItem"],
  methods: {
    removeItem: function(index) {
      let tmp = this.todoItem
      tmp.splice(index, 1)
      this.$emit("update:todoItem", tmp)
    }
  }
}
</script>
