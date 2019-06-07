<template>
  <button v-on:click="numberPlus">{{ count }}</button>
</template>
<script>
export default {
  name: "test-component",
  data: function() {
    return {
      count: 0
    };
  },
  methods: {
    numberPlus: function() {
      this.count += 1;
      this.$emit("counter");
    }
  }
};
</script>
