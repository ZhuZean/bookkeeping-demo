from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.get_db_dsn(),
    pool_pre_ping=settings.db_pool_pre_ping
)

SessionLocal = sessionmaker(
    autocommit=settings.db_autocommit,
    autoflush=settings.db_autoflush,
    bind=engine
)
