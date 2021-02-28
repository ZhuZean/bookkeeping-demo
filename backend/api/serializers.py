from api.models import Bill, Payment, Usage, Currency
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['name']


class UsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usage
        fields = ['name']


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['name']


class BillSerializer(serializers.HyperlinkedModelSerializer):
    payment = PaymentSerializer(many=False, read_only=False)
    usage = UsageSerializer(many=False, read_only=False)
    currency = CurrencySerializer(many=False, read_only=False)

    def create(self, validated_data):
        payment = Payment.objects.get(name=validated_data.pop('payment').get('name'))
        usage = Usage.objects.get(name=validated_data.pop('usage').get('name'))
        currency = Currency.objects.get(name=validated_data.pop('currency').get('name'))
        instance = Bill.objects.create(**validated_data, payment=payment, usage=usage, currency=currency)
        return instance

    class Meta:
        model = Bill
        fields = ['id', 'payment', 'bill_type', 'usage', 'currency', 'price', 'note', 'created_at']


class PaymentSummarySerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()


class BillSummarySerializer(serializers.Serializer):
    summary = serializers.DictField()
    payment_detail = PaymentSummarySerializer(many=True)


class BillInfoSerializer(serializers.Serializer):
    payment = serializers.ListField(
        child=serializers.CharField()
    )
    usage = serializers.ListField(
        child=serializers.CharField()
    )
    currency = serializers.ListField(
        child=serializers.CharField()
    )
    bill_type = serializers.ListField(
        child=serializers.CharField()
    )
