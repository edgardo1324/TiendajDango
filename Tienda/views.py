from rest_framework import generics
from Tienda.models import Offer, Brand, Store, UserStore
from .serializers import StoreSerializer, BrandSerializer, OfferSerializer
from django.contrib.auth import get_user_model
from .serializers import  StoreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, StoreSerializer, UserStoreSerializer
User = get_user_model()


class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class OfferList(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
#crear usarios
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#endpoint 5 usuarios y tienda
class UserStoreSelectionView(APIView):
    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

        try:
            store = Store.objects.get(name=name)
        except Store.DoesNotExist:
            return Response("Store not found.", status=status.HTTP_404_NOT_FOUND)

        user_store = UserStore(user_id=user.id, store_id=store.id)
        user_store.save()

        serializer = UserStoreSerializer(user_store)
        return Response(serializer.data, status=status.HTTP_201_CREATED)