
<template>
<main>
<figure v-for="product in product_list" :key="product" class="snip1268">
  <div class="image">
    <img :src="product.product_img" alt="sq-sample4"/>
    <a class="add-to-cart" @click="addToCart(product)">Añadir al carrito</a>
     
  </div>
  <figcaption>
    <h2>{{product.product_name}}</h2>
    <p>{{product.product_description}}</p>
    <div class="price">{{product.product_price}} </div>
  </figcaption>
</figure>
<article>
<h2> Articulos en el carrito </h2>
<p v-for="selected_product in selected_products" :key="selected_product" > 
  {{selected_product.product_name}}</p>
<a href="cart/contact"> CONTACTAR CON EL VENDEDOR </a>
   </article>

</main>
</template>


<script>

export default {
  name: 'Stores',
  data() {
    return {
      product_list: [],
      selected_products: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/sellers/products/'+ this.$route.params.id)
      this.product_list = await response.json()
    },
    sendToContact() {
        this.$router.push("/shop/contact/" + this.$route.params.id)
    },
    addToCart(product) {
      this.selected_products.push(product)
      console.log(product)
      localStorage.setItem("selectedProducts", JSON.stringify(this.selected_products))
    }
  


  }
}
</script>



<style scoped>
*{
  padding:0;
  margin:0;
  box-sizing:border-box;
}

main {
  width: 100vw;
  display: grid;
  grid-template-columns:repeat(auto-fill, minmax(min(100%, 25rem), 1fr))
  }

@import url(https://fonts.googleapis.com/css?family=Raleway:400,500,700);
@import url(https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css);
.snip1268 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  margin: 10px;
  min-width: 220px;
  max-width: 310px;
  width: 100%;
  color: #333333;
  text-align: center;
  background-color: #ffffff;
  line-height: 1.6em;
}
.snip1268 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.6s ease;
  transition: all 0.6s ease;
}
.snip1268 .image {
  position: relative;
}
.snip1268 img {
  max-width: 100%;
  vertical-align: top;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}
.snip1268 .icons,
.snip1268 .add-to-cart {
  position: absolute;
  left: 20px;
  right: 20px;
  opacity: 0;
}
.snip1268 .icons {
  -webkit-transform: translateY(-100%);
  transform: translateY(-100%);
  top: 20px;
  display: flex;
  justify-content: space-between;
}
.snip1268 .icons a {
  width: 32.5%;
  background: #ffffff;
}
.snip1268 .icons a:hover {
  background: #000000;
}
.snip1268 .icons a:hover i {
  color: #ffffff;
  opacity: 1;
}
.snip1268 .icons i {
  line-height: 46px;
  font-size: 20px;
  color: #000000;
  text-align: center;
  opacity: 0.7;
  margin: 0;
}
.snip1268 .add-to-cart {
  position: absolute;
  bottom: 20px;
  -webkit-transform: translateY(100%);
  transform: translateY(100%);
  font-size: 0.8em;
  color: #000000;
  line-height: 46px;
  letter-spacing: 1.5px;
  background-color: #ffffff;
  font-weight: 700;
  text-decoration: none;
  text-transform: uppercase;
}
.snip1268 .add-to-cart:hover {
  background: #000000;
  color: #ffffff;
}
.snip1268 figcaption {
  padding: 20px 20px 30px;
}
.snip1268 h2,
.snip1268 p {
  margin: 0;
  text-align: left;
}
.snip1268 h2 {
  margin-bottom: 10px;
  font-weight: 700;
}
.snip1268 p {
  margin-bottom: 15px;
  font-size: 0.85em;
  font-weight: 500;
}
.snip1268 .price {
  font-size: 1.3em;
  opacity: 0.5;
  font-weight: 700;
  text-align: right;
}
.snip1268:hover img,
.snip1268.hover img {
  opacity: 0.8;
}
.snip1268:hover .icons,
.snip1268.hover .icons,
.snip1268:hover .add-to-cart,
.snip1268.hover .add-to-cart {
  -webkit-transform: translateY(0);
  transform: translateY(0);
  opacity: 1;
}
</style>