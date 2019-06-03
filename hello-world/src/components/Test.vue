<template>
  <div>
    <h3>{{ message }}</h3>
  </div>
</template>
<script>
  export default {
    name: "Test",
    props: {
      message: String
    }
  }
</script>
