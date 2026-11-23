from sqlalchemy import CheckConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Resource(Base):
    __tablename__ = "resources"

    __table_args__ = (CheckConstraint("classification IN ('public', 'internal', 'confidential', 'secret')", name="ck_resources_classification",),)

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    classification: Mapped[str] = mapped_column(String(16))
    content: Mapped[str] = mapped_column(Text)
