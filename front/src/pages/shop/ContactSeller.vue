<template>
  
<h2 >Mi Carrito: </h2>
<div v-for="product in selected_products" :key="product.id">
  <h3>{{product.product_name}}</h3>
  <img :src="product.product_img" alt=""/>
  <button @click="removeProducts(product)" class="remove_button" >Eliminar producto</button>
  <h3>Contactar del vendedor : </h3>
</div>
  <form id="formulario">
    <div id="content">
      <h4><label> Enviar consulta: </label></h4><br>
      <textarea id="contenido" name="comment" cols="30" rows="5">Ingresa aqui el mensaje...</textarea><br>
      <label> Mi e-mail de contacto: </label><br>
      <input id="email" name="email" type="text" />
      <button @click="sendEmail"> Enviar </button>
    </div>
    <img :src="contact_seller.seller_logo" alt="Sample photo">
    <h4><div> {{contact_seller.seller_email}}</div></h4>
  </form>
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
    },
      sendEmail(){
        const request = {
          method: "POST",
          body: JSON.stringify(send),
          json_guardar_datos_email : {"mensaje":"", "email": "" }
          }
        fetch(`${config.API_PATH}/sellers`);

        alert("EMAIL ENVIADO")
      }

  }
}
</script>

<style scoped>


img {
  width: 9rem;
}


div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>