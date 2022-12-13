from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductModelSerializer
from .models import Product


# Create your views here.


class ProductAPIView(GenericAPIView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        filters = request.query_params.get('status')
        product_id = request.query_params.get('id')
        name = request.query_params.get('name')
        products = Product.objects.all()
        if filters:
            products = Product.objects.filter(status=filters)
        if product_id:
            products = Product.objects.filter(id=product_id)
        if name:
            products = self.filter_queryset(products, name)
        for product in products:
            print(product.image)
            image_name = str(product.image).rsplit('.', 1)
            data = {
                "path": f"{image_name[0]}",
                "formats": [
                    "png",
                    image_name[1],
                ]
            }
            product.image = data
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)

    def filter_queryset(self, queryset, name):
        return queryset.filter(name=name)
