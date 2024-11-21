from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import @api_viwe
from rest_framework.response import Response
from .filtters import ProductsFilter

from.models import Product
from.serializers import ProductSerializer




@api_view(['GET'])
def get_all_products(request):

   filterset = ProductsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
   count = filterset.qs.count()
   resPage = 12
   paginator = PageNumberPagination()
   paginator.page_size = resPage

   queryset =  paginator.paginate_queryset(filterset.qs, request)
   serializer = ProductSerializer(queryset,many=True)
   return Response({"products":serializer.data, "per page":resPage, "count":count})

@api_view(['GET'])
def get_by_id_product(request,pk):
    products = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(products,many=False)
    print(products)
    return Response({"product":serializer.data})








