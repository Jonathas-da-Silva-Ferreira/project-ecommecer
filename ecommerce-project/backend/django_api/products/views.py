from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def list_products(request):
   """ List all products"""
   products = Product.objects.all()
   serializer = ProductSerializer(products, many=True)
   return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    """Create a new product"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_product(request, pk):
    """Retrieve a product by its ID"""
    