def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.seller import Seller, SellerRepository
    from src.domain.product import Product, ProductRepository

    database_path = "data/database.db"

    seller_repository = SellerRepository(database_path)
    product_repository = ProductRepository(database_path)

    seller1 = Seller(
        seller_id="Fedora",
        seller_name="Botxinche",
        seller_description="Moda infantil sostenible",
        seller_email="botintxe@gmail.com",
        seller_logo="https://cdn5.dibujos.net/dibujos/pintados/201229/mandela-51-mandalas-pintado-por-belinda99-9754275.jpg",
    )

    seller2 = Seller(
        seller_id="Eva",
        seller_name="Flashera",
        seller_description="Joyeria Contemporanea",
        seller_email="flashera@gmail.com",
        seller_logo="https://cdn5.dibujos.net/dibujos/pintados/201229/mandela-51-mandalas-pintado-por-belinda99-9754275.jpg",
    )
    seller3 = Seller(
        seller_id="Erika",
        seller_name="Tradiciones Argentinas",
        seller_description="Pasteleria típica",
        seller_email="tradiciones_arg@gmail.com",
        seller_logo="https://cdn5.dibujos.net/dibujos/pintados/201229/mandela-51-mandalas-pintado-por-belinda99-9754275.jpg",
    )
    seller4 = Seller(
        seller_id="Elias",
        seller_name="Manitas",
        seller_description="Muebles en madera",
        seller_email="elias@gmail.com",
        seller_logo="https://cdn5.dibujos.net/dibujos/pintados/201229/mandela-51-mandalas-pintado-por-belinda99-9754275.jpg",
    )

    product1 = Product(
        seller_id="Fedora",
        product_id="1",
        product_description="Peto infantil",
        product_name="Peto niño",
        product_price="5€",
        product_img="https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F57%2Fbf%2F57bffa3291cbd0185253d97a39638637f062a715.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVEDETAIL%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/fullscreen]",
    )

    seller_repository.save(seller1)
    seller_repository.save(seller2)
    seller_repository.save(seller3)
    seller_repository.save(seller4)
    product_repository.save(product1)

    print("Datos iniciales cargados (se ha ejecutado initial_data.py)")


main()
