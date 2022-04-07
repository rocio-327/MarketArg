from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.seller import SellerRepository, Seller


def test_should_return_empty_database():
    seller_repository = SellerRepository(temp_file())
    app = create_app(repositories={"sellers": seller_repository})
    client = app.test_client()

    response = client.get("/api/sellers")
    assert response.json == []


def test_should_return_seller_in_database():
    seller_repository = SellerRepository(temp_file())
    app = create_app(repositories={"sellers": seller_repository})
    client = app.test_client()
    seller1 = Seller(
        seller_id="seller_id",
        seller_name="seller_name",
        seller_description="seller_description",
        seller_logo="seller_logo",
        seller_email="seller_email",
    )
    seller_repository.save(seller1)

    response = client.get("/api/sellers")
    assert response.json == [
        {
            "seller_id": "seller_id",
            "seller_name": "seller_name",
            "seller_description": "seller_description",
            "seller_logo": "seller_logo",
            "seller_email": "seller_email",
        }
    ]
