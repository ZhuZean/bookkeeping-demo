"""Endpoint for bill
"""
from typing import Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Body, HTTPException, Query

from app.api import deps
from app.api.endpoints import bad_request, business_error
from app.helper.paginator import Paginator
from app.schemas.bill import (
    CreateBillResponse,
    CreateBillRequest,
    ListBillResponse,
    BillFormInfoResponse,
    BillSummaryResponse
)


router = APIRouter()


@router.post("", response_model=CreateBillResponse, status_code=201)
def create(
    params: CreateBillRequest = Body(...),
    db=Depends(deps.get_db_session),
    bill_business=Depends(deps.get_bill_business)
) -> Any:
    """ Create bill
    """
    try:
        return bill_business.create(params=params, db=db)
    except ValueError as ex:
        raise bad_request({'error': str(ex)})
    except Exception as ex:
        raise business_error({'error': str(ex)})


@router.get("", response_model=ListBillResponse)
def list_bills(
    page: int = Query(1),
    limit: int = Query(5),
    db=Depends(deps.get_db_session),
    bill_business=Depends(deps.get_bill_business)
) -> Any:
    """ Create bill
    """
    try:
        paginator = Paginator(limit, page)
        items = bill_business.get_bills(paginator=paginator, db=db)
        return {'items': items, 'pagination': paginator.get_info()}
    except Exception as ex:
        raise business_error({'error': str(ex)})


@router.get("/form-info", response_model=BillFormInfoResponse)
def form_info(
    db=Depends(deps.get_db_session),
    bill_business=Depends(deps.get_bill_business)
) -> Any:
    """ Get form field information
    """
    try:
        return bill_business.get_form_info(db=db)
    except Exception as ex:
        raise business_error({'error': str(ex)})


@router.get("/summary", response_model=BillSummaryResponse)
def summary(
    db=Depends(deps.get_db_session),
    bill_business=Depends(deps.get_bill_business)
) -> Any:
    """ Get bill summary data
    """
    try:
        return bill_business.get_summary(db=db)
    except Exception as ex:
        raise business_error({'error': str(ex)})