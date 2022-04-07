<template>
    <main class="grid">
          <article v-for="seller in sellers" :key="seller.seller_id">
            <img :src="seller.seller_logo" alt="Sample photo">
            <div class="text">
              <h3>{{seller.seller_name}}</h3>
              <p>{{seller.seller_description}}</p>
              <button>Ver tienda</button>
            </div>
          </article>
        </main>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      sellers: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/sellers')
      this.sellers = await response.json()
    }
  }


}
</script>

<style scoped>
.grid {
  margin: 30px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 20px;
  align-items: stretch;
  }

.grid > article {
  border: 1px solid #ccc;
  box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);
  border-radius: 3px;
  text-align: center;
}

.grid > article:hover{
  transition: transform .1s ease-out;
  transform: translateY(5px);
}

.grid > article img {
  width: 40%;
}


.text {
  padding: 0 20px 20px;
}

.text > h3{
  text-transform: uppercase;
}

.text > button {
  background: linear-gradient(to right, #f030a7, #f0308d, #f03061);
  border-radius: 3px;
  border: 0;
  color: white;
  padding: 10px;
  width: 80%;
  font-weight: 600;
  text-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);
  text-transform: uppercase;
}


@media (max-width: 768px){
  .grid{
    grid-template-columns: repeat(2, 1fr);
    margin: 0;
  }
}

@media (max-width: 200px){
  .grid{
    grid-template-columns: repeat(1, 1fr);
    margin: 0;
  }

  .grid > article{
    text-align: center;
  }
}

</style>


