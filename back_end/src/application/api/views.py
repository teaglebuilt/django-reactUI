from rest_framework.generics import ListAPIView, RetrieveAPIView
from application.models import Customer, ProductType, Product, PaymentType, Orders
from .serializers import CustomerSerializer, ProductTypeSerializer, ProductSerializer, PaymentTypeSerializer, OrdersSerializer


class CustomerViewSet(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Returning customers that have not yet placed an active order
    def get_queryset(self):
        queryset = Customer.objects.all()

        if self.request.GET.get('active') == 'false':
            print('if statement')
            queryset = queryset.filter(active= False)
        return queryset


class CustomerDetailView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductTypeViewSet(ListAPIView):
    queryset= ProductType.objects.all()
    serializer_class = ProductTypeSerializer



class ProductViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class PaymentTypeViewSet(ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer



class OrdersViewSet(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


