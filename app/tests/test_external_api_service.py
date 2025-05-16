import pytest
from app.services.external_api_products import get_products_from_external_api

@pytest.mark.asyncio
async def test_get_products_from_external_api_real():
    # Act
    products = await get_products_from_external_api()

    # Assert
    assert products is not None, "Response should not be None"
    assert isinstance(products, list), "Response is not a list"
    if products:
        assert "id" in products[0], "Field 'id' is missing in the product"
        assert "title" in products[0], "Field 'title' is missing in the product"
        assert "price" in products[0], "Field 'price' is missing in the product"
        assert "description" in products[0], "Field 'description' is missing in the product"
        assert "category" in products[0], "Field 'category' is missing in the product"
        assert "image" in products[0], "Field 'image' is missing in the product"
