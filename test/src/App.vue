<template>
  <div id="app">
    <p>{{ count }}</p>
    <Test v-on:counter="countPlus"></Test>
    <Test v-on:counter="countPlus"></Test>
    <hr/>
    <router-link to="/home">Home</router-link>
    <router-link to="/users/:Id">User</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
import Test from "./components/Test";

export default {
  name: "app",
  components: {
    Test
  },
  data: function() {
    return {
      count: 0
    };
  },
  methods: {
    countPlus: function() {
      this.count += 1;
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
