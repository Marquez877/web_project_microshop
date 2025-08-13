from sqlalchemy.orm import Mapped

from .base import Base


class Product(Base):
    __tablename__ = "Products"
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
