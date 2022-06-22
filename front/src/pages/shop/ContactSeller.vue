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
      <h4><label> Enviar consulta: </label></h4>
      <br><textarea id="contenido" name="comment" cols="30" rows="5" v-model="client_request.user_request"> Ingresa aqui el mensaje...</textarea><br>
      <h4><label> Mi e-mail de contacto: </label></h4><br>
      <input id="email" name="email" type="text" v-model="client_request.user_email"/>
      <button type="button" @click="sendEmail"> Enviar </button>
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
        contact_seller: [],
        client_request : {seller_id : "" , user_request:"" , user_email : ""}
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
       async sendEmail(){
        const settings = {
        method: "POST",
        body: JSON.stringify(this.client_request),
        headers: {
        "Content-Type": "application/json",
    }
    }
        await fetch("http://localhost:5000/api/request", settings)
        alert("EMAIL ENVIADO")
      }

  }
}
</script>

<style scoped>


img {
  width: 9rem;
}
button {

  background: #eb94d0;
  background-image: -webkit-linear-gradient(top, #eb94d0, #2079b0);
  background-image: -moz-linear-gradient(top, #eb94d0, #2079b0);
  background-image: -ms-linear-gradient(top, #eb94d0, #2079b0);
  background-image: -o-linear-gradient(top, #eb94d0, #2079b0);
  background-image: linear-gradient(to bottom, #eb94d0, #2079b0);
  -webkit-border-radius: 25;
  -moz-border-radius: 23;
  border-radius: 25px;
  -webkit-box-shadow: 6px 5px 24px #666666;
  -moz-box-shadow: 6px 5px 24px #666666;
  box-shadow: 6px 5px 24px #666666;
  font-family: Arial;
  color: #fafafa;
  font-size: 20px;
  padding: 9px;
  text-decoration: none;
}
button:hover {
  background: #2079b0;
  background-image: -webkit-linear-gradient(top, #2079b0, #eb94d0);
  background-image: -moz-linear-gradient(top, #2079b0, #eb94d0);
  background-image: -ms-linear-gradient(top, #2079b0, #eb94d0);
  background-image: -o-linear-gradient(top, #2079b0, #eb94d0);
  background-image: linear-gradient(to bottom, #2079b0, #eb94d0);
  text-decoration: none;
}

div {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3px;
}


</style>