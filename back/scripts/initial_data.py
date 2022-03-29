def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.seller import Seller, SellerRepository

    database_path = "data/database.db"

    seller_repository = SellerRepository(database_path)

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
        seller_description="Joyeria",
        seller_email="flashera@gmail.com",
        seller_logo="https://cdn5.dibujos.net/dibujos/pintados/201229/mandela-51-mandalas-pintado-por-belinda99-9754275.jpg",
    )

    seller_repository.save(seller1)
    seller_repository.save(seller2)

    print("Datos iniciales cargados (se ha ejecutado initial_data.py)")


main()
