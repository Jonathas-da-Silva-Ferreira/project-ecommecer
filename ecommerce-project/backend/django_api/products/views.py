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
    try:
         product = Product.objects.get(pk=pk)
         serializer = ProductSerializer(product)
         return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"Erro": "Produto não encontrado." }, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_product(request, pk):
    """Update a product by its ID"""
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"Erro": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_product(request, pk):
    """Delete a product by its ID"""
    try:
        product =  Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"Erro": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)