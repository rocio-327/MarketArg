<template>
<h1>Carrito</h1>
<div v-for="product in selected_products" :key="product.id"> 
  <h2>{{product.product_name}}</h2>
  <img :src="product.product_img" alt="">
</div>
</template>

<script>
export default {
    data() {
        return {
        selected_products: []
        }
    },
    mounted() {
        this.loadData()
    },

    methods: {
      loadData() {
        let products = localStorage.getItem("selectedProducts")
        let jsonProducts = JSON.parse(products)
        this.selected_products = jsonProducts
        console.log(products)
      // const response = await fetch('http://localhost:5000/api/sellers/'+ this.$route.params.id)
      // this.contact_info = await response.json()
    }

  }

}
</script>

<style>
img {
  width: 9rem;
}

</style>