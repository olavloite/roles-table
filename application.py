
import random
from typing import Optional

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.dialects import registry


class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    type: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(512))


def run_sample():
    engine = create_engine(
        "spanner:///projects/appdev-soda-spanner-staging/"
        "instances/knut-test-ycsb/"
        "databases/spring-data-jpa",
        echo=True,
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        role = Role(
            id=random.randint(1, 1000000),
            name="Test",
            type="Test",
            description="Test",
        )
        session.add(role)
        session.commit()

if __name__ == "__main__":
    registry.register(
        "spanner",
        "google.cloud.sqlalchemy_spanner.sqlalchemy_spanner",
        "SpannerDialect",
    )
    run_sample()
