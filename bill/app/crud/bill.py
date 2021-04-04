from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.bill import Bill as BillOrm
from app.schemas.orm.bill import BillCreate, BillUpdate


class CRUDBill(CRUDBase[BillOrm, BillCreate, BillUpdate]):
    def get_list(self, db: Session) -> List[BillOrm]:
        return db.query(self.model).order_by(self.model.updated_at.desc())


bill = CRUDBill(BillOrm)
