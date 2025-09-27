# myapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products_Fake
from .serializers import ProductsFakeSerializer
from django.db.models import Q

@api_view(['GET'])
def search_products(request):
    search = request.GET.get('search', None) 
    if search:
        products = Products_Fake.objects.filter(
              Q(product_name__icontains=search)
            | Q(product_description__icontains=search)
            | Q(product_category__icontains=search)
            )
    else:
        products = Products_Fake.objects.all()
    
    serializer = ProductsFakeSerializer(products, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Products_Fake.objects.get(pk=pk)
    except Products_Fake.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductsFakeSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Products_Fake.objects.get(pk=pk)
    except Products_Fake.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)