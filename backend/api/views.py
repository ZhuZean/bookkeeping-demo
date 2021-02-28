from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response

from api.models import Bill, Payment, Usage, Currency
from api.serializers import BillSerializer, BillSummarySerializer, BillInfoSerializer
from api.utils import get_current_month


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
            },
            'results': data
        })


class BillViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Bill endpoint to get the list of bills (current month)
    """
    queryset = Bill.objects.filter(
        created_at__month=get_current_month()
    ).order_by(
        '-created_at'
    )
    serializer_class = BillSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class BillInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Bill info endpoint to get the bill sub category information
    """
    serializer_class = BillInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        all_info = {
            'payment': self._get_all_payment_name(),
            'usage': self._get_all_usage_name(),
            'currency': self._get_all_currency_name(),
            'bill_type': self._get_all_bill_type()
        }

        serializer = BillInfoSerializer(all_info)
        return Response(serializer.data)

    def _get_all_payment_name(self):
        queryset = Payment.objects.order_by(
            'created_at'
        )
        return [obj.name for obj in queryset]

    def _get_all_usage_name(self):
        queryset = Usage.objects.order_by(
            'created_at'
        )
        return [obj.name for obj in queryset]

    def _get_all_currency_name(self):
        queryset = Currency.objects.order_by(
            'created_at'
        )
        return [obj.name for obj in queryset]

    def _get_all_bill_type(self):
        return ['Income', 'Expense']


class BillSummaryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Bill summary to get the total amount of income and expense (current month)
    """
    serializer_class = BillSummarySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        summary = self._get_summary()
        payment_detail = self._get_payment_details()
        result = {
            'summary': summary,
            'payment_detail': payment_detail
        }
        serializer = BillSummarySerializer(result)
        return Response(serializer.data)


    def _get_summary(self):
        result = {
            'total_expense': 0,
            'total_income': 0
        }

        queryset = Bill.objects.filter(
            created_at__month=get_current_month()
        ).order_by(
            'created_at'
        )

        for bill_obj in queryset:
            if (bill_obj.bill_type == 'EX'):
                result['total_expense'] += bill_obj.price
            if (bill_obj.bill_type == 'IN'):
                result['total_income'] += bill_obj.price
        return result

    def _get_payment_summary(self, payment):
        amount = 0

        queryset = Bill.objects.filter(
            created_at__month=get_current_month()
        ).filter(
            payment=payment
        ).order_by(
            'created_at'
        )

        for bill_obj in queryset:
            if (bill_obj.bill_type == 'EX'):
                amount -= bill_obj.price
            if (bill_obj.bill_type == 'IN'):
                amount += bill_obj.price

        return amount

    def _get_payment_details(self):
        payment_detail = []
        payments = Payment.objects.all().order_by('created_at')
        for payment_obj in payments:
            detail = {
                'name': payment_obj.name,
                'amount': self._get_payment_summary(payment_obj)
            }
            payment_detail.append(detail)

        return payment_detail
