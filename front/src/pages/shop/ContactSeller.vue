<template>
    <div> {{contact_info.seller_email}}</div>
    <div> {{contact_info.seller_id}}</div>
    <img :src="contact_info.seller_logo" alt="Sample photo">
  
</template>

<script>
export default {
    data() {
        return {
        contact_info: []
        }
    },
    mounted() {
        this.loadData()
    },

    methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/sellers/'+ this.$route.params.id)
      this.contact_info = await response.json()
    }

  }

}
</script>

<style>

</style>