from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Products, ProductCreate, ProductUpdate
from app.database import get_session
from app.services.products import get_product, get_products, create_product, update_product, delete_product
from app.services.external_api_products import sync_products_from_external_api
router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[Products])
def get_all_products():
    return get_products()

@router.get("/{product_id}", response_model=Products)
def get_product_by_id(product_id: int):
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Products)
def post_product(product: ProductCreate):
    product = Products(**product.dict())
    db_product=create_product(product)
    return db_product

@router.put("/{product_id}", response_model=Products)
def put_product(product_id: int, product: ProductUpdate):
    db_product =update_product(product_id,product)
    return db_product

@router.delete("/{product_id}")
def del_product(product_id: int):
    is_deleted=delete_product(product_id)
    if (is_deleted):
        return {"ok": True}
    else:
        raise HTTPException(status_code=400, detail="Cannot delete the product")

@router.post("/sync")
async def sync_products():
    try:
        await sync_products_from_external_api()
        return get_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error syncing products: {str(e)}")