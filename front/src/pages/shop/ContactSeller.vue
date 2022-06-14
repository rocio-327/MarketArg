<template>
<h1>Carrito</h1>
<div v-for="product in selected_products" :key="product.id">
  <h2>{{product.product_name}}</h2>
  <img :src="product.product_img" alt="">
  <button @click="removeProducts(product)" class="remove_button" >Eliminar producto</button>
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
    },
      removeProducts(product) {
        let index = this.selected_products.indexOf(product)
        this.selected_products.splice(index, 1)
    }
  }
}
</script>

<style>
img {
  width: 9rem;
}

</style>