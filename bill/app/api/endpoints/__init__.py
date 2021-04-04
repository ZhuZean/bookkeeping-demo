""" Exceptions
"""
from typing import Dict

from fastapi import HTTPException


def bad_request(errors: Dict[str, str], code='validation_error'):
    """ Return HTTP 400 error
    """
    raise HTTPException(status_code=400, detail={
        'code': code,
        'reason': errors,
    })


def business_error(errors: Dict[str, str], code='internal_error'):
    """ Return HTTP 500 error
    """
    raise HTTPException(status_code=500, detail={
        'code': code,
        'reason': 'Server error',
    })