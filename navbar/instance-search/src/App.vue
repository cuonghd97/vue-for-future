<template>
  <div>
    <input type="text" v-model="searchText">
    <div>
      <ul>
        <li v-for="item in filterData">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data: function() {
    return {
      searchText: "",
      listData: [
        {
          name: "cuong"
        },
        {
          name: "asndkalsd"
        },
        {
          name: "knibuyhgqtwdqw"
        }
      ]
    }
  },
  computed: {
    filterData: function() {
      const searchText = this.searchText
      const listData = this.listData
      if (searchText === "") {
        return listData
      }

      return listData.filter(function(item) {
        return item.name.indexOf(searchText) !== -1
      })
    }
  }
}
</script>

<style>
</style>
