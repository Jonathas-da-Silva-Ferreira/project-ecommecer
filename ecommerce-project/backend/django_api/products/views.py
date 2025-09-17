import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def list_products(request):
    """Lista todos os produtos"""
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.exception("Erro ao listar produtos")
        return Response({"error": "Erro ao listar produtos."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_product(request):
    """Cria um novo produto"""
    try:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception("Erro ao criar produto")
        return Response({"error": "Erro ao criar produto."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_product(request, pk):
    """Busca produto por ID"""
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("Erro ao buscar produto")
        return Response({"error": "Erro ao buscar produto."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_product(request, pk):
    """Atualiza produto por ID"""
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("Erro ao atualizar produto")
        return Response({"error": "Erro ao atualizar produto."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_product(request, pk):
    """Deleta produto por ID"""
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("Erro ao deletar produto")
        return Response({"error": "Erro ao deletar produto."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
