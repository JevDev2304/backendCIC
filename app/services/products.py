from sqlmodel import Session, select
from app.models import Products, ProductCreate, ProductUpdate
from app.database import engine 
from typing import Optional, List

def get_products() -> List[Products]:
    with Session(engine) as session:
        return session.exec(select(Products)).all()

def get_product(Products_id: int) -> Optional[Products]:
    with Session(engine) as session:
        return session.get(Products, Products_id)
    
def get_product_by_title_and_price(title: str, price: float) -> Optional[Products]:
    with Session(engine) as session:
        statement = select(Products).where(
            (Products.title == title) &
            (Products.price == price)
        )
        return session.exec(statement).first()

def create_product(Products_create: ProductCreate) -> Products:
    with Session(engine) as session:
        db_Products = Products(**Products_create.dict())
        session.add(db_Products)
        session.commit()
        session.refresh(db_Products)
        return db_Products

def update_product(Products_id: int, Products_update: ProductUpdate) -> Optional[Products]:
    with Session(engine) as session:
        db_Products = session.get(Products, Products_id)
        if not db_Products:
            return None
        Products_data = Products_update.dict(exclude_unset=True)
        for key, value in Products_data.items():
            setattr(db_Products, key, value)
        session.add(db_Products)
        session.commit()
        session.refresh(db_Products)
        return db_Products

def delete_product(Products_id: int) -> bool:
    with Session(engine) as session:
        db_Products = session.get(Products, Products_id)
        if not db_Products:
            return False
        session.delete(db_Products)
        session.commit()
        return True
