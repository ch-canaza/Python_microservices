from rest_framework import viewsets, status
from .models import Product, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
import random 
from .producers import publish


class ProductViewSet(viewsets.ViewSet):
    """ class to handel CRUD """

    def list(self, request): # /api/products
        """
            method to get a list of products,
            an array of objects
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)        
    
    def create(self, request): # /api/products 
        """ 
            method to post or create products
            receive a title and a image
        """
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None): # /api/products/<str:id>
        """
            method to get a product by id,
            a single object
        """
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def update(self, request, pk=None):
        """
            update a product by id, 
            raise an exception if the object is not valid,
            otherwise send it as a response
        """
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        """
            delete an element by id
        """
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserAPIView(APIView):
    """
        represents user views from database
        generates random users id 
    """
    def get(self, _):
        """
            method that retrieves a user randomly from users in database
        """
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
