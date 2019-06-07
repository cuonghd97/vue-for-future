<template>
  <div id="app">
    <div class="range">
      <p>
        <input type="number" v-model="hue">
        <input type="range" min="0" max="360" v-model="hue">
      </p>
      <p>
        <input type="number" v-model="saturation">
        <input type="range" min="0" max="100" v-model="saturation">
      </p>
      <p>
        <input type="number" v-model="light">
        <input type="range" min="0" max="100" v-model="light">
      </p>
      <p>
        <input type="number" v-model="opacity">
        <input type="range" min="0" max="1" step="0.01" v-model="opacity">
      </p>
    </div>
    <div class="preview" v-bind:style="getHLS"></div>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data: function() {
    return {
      hue: 0,
      saturation: 0,
      light: 0,
      opacity: 1,
    }
  },
  computed: {
    getHLS: function() {
      return {"background-color": `hsla(${this.hue},${this.saturation}%,${this.light}%,${this.opacity})`}
    }
  }
}
</script>

<style>
#app {
  display: flex;
  justify-content: center;
}

.preview {
  width: 190px;
  height: 190px;
  border: solid black 1px;
}

</style>
