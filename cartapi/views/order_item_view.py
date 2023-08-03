from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from cartapi.models import OrderItem, Product, Order, User

class OrderItemView(ViewSet):

    def create(self, request):
        """POST request for order_item or 'cart item' for user's cart
        Two conditions for this method: a user already has an open order, or a user does not have an open order and one must be created"""
        user = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        product = Product.objects.get(pk=request.data["productId"])
        order_item = {
            'product': product
        }
        try:
            order = Order.objects.get(is_open=True, buyer=user)
            order_item['order'] = order
        except Order.DoesNotExist:
            new_order = Order(buyer=user)
            new_order.save()
            order_item['order'] = new_order

        OrderItem.objects.create(
            order = order_item['order'],
            product = order_item['product']
        )

        return Response({'message': f'{product.name} added to cart!'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to remove item from cart
        handles two conditions: removing a single item from cart, and removing all instances of product from cart
        pk=product id"""
        user = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        order = Order.objects.get(buyer=user, is_open=True)
        product = Product.objects.get(pk=pk)
        order_items = OrderItem.objects.filter(product=product, order=order)
        try:
            request.META['HTTP_DECREMENT']
            order_items[0].delete()
            return Response({'message': f'1 {product.name} removed from cart!'}, status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            for item in order_items:
                item.delete()
        return Response({'message': f'{product.name} removed from cart!'}, status=status.HTTP_204_NO_CONTENT)
