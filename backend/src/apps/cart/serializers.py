from rest_framework import serializers
from apps.cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'total_price']
        read_only_fields = ['product_name', 'product_price', 'total_price']
