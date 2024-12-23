from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.cart.models import Cart
from apps.cart.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


    def get_queryset(self):

        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):

        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)


        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product_id=product_id,
            defaults={'quantity': quantity}
        )
        if not created:

            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)


        total_price = sum(item.total_price for item in queryset)
        return Response({
            "items": serializer.data,
            "total_price": total_price
        })
