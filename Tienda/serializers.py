from rest_framework import serializers
from .models import Store, Brand, Offer,User, UserStore


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

# crearusuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
#endpoint 5 usuarios y tienda
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'brand', 'identifier', 'name', 'address']

class UserStoreSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    store = StoreSerializer()

    class Meta:
        model = UserStore
        fields = ['user', 'store']