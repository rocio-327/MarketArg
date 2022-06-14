<template>
<h2>Mi Carrito: </h2>
<div v-for="product in selected_products" :key="product.id">
  <h3>{{product.product_name}}</h3>
  <img :src="product.product_img" alt=""/>
  <button @click="removeProducts(product)" class="remove_button" >Eliminar producto</button>
  <h3>Contacto del vendedor : </h3>
  <img :src="contact_seller.seller_logo" alt="Sample photo">
  <h4><div> {{contact_seller.seller_email}}</div></h4>

</div>
</template>

<script>
export default {
    data() {
        return {
        selected_products: [],
        contact_seller: []
        }
    },
    mounted() {
        this.loadData()
        this.loadSeller()
    },

    methods: {
      async loadSeller(){
        let seller_id = await this.loadData()[0].seller_id
        let response = await fetch("http://localhost:5000/api/sellers/" + seller_id)
        let data = await response.json()
        this.contact_seller = data
        return data
      },

      loadData() {
        let products = localStorage.getItem("selectedProducts")
        let jsonProducts = JSON.parse(products)
        this.selected_products = jsonProducts
        return jsonProducts
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


div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>