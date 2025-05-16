from sqlmodel import select, Session
from app.database import engine
from app.models import Products
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_LINK = os.getenv("EXTERNAL_API_LINK")

async def get_products_from_external_api():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{API_LINK}/products")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

from sqlalchemy.exc import IntegrityError

async def sync_products_from_external_api():
    added_products = []
    external_products = await get_products_from_external_api()

    if not external_products:
        return added_products

    with Session(engine) as session:
        for ext_prod in external_products:
            try:
                new_product = Products(
                    title=ext_prod["title"],
                    price=ext_prod["price"],
                    description=ext_prod["description"],
                    category=ext_prod["category"],
                    image=ext_prod["image"],
                )
                session.add(new_product)
                session.flush()
                session.commit()  # intenta insertar inmediatamente

                added_products.append(new_product)
            except IntegrityError as e:
                session.rollback()  # hace rollback solo de esta inserción
                print(f"[WARN] Duplicated Product {ext_prod['title']} -> {e.orig}")
            except Exception as e:
                session.rollback()
                print(f"[ERROR] Internal Server Error {ext_prod['title']} -> {e}")

          # guarda los que sí se insertaron bien

    return added_products
