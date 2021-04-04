""" General configuration
"""
from pydantic import BaseSettings, PyObject


class Settings(BaseSettings):

    # Database
    environment: str
    db_pool_pre_ping: bool = True
    db_autocommit: bool = False
    db_autoflush: bool = False

    database_user: str
    database_pass: str
    database_host: str
    database_port: str
    database_name: str

    # API
    api_base_path: str = '/bill'

    # Business
    bill_business: PyObject = 'app.business.bill.BillBusiness'

    class Config:
        pass

    def get_db_dsn(self) -> str:
        return (
            f'postgresql://{self.database_user}:{self.database_pass}@' +
            f'{self.database_host}:{self.database_port}/{self.database_name}'
        )

settings = Settings()
