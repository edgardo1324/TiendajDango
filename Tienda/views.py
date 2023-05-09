from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Tienda.models import Offer, Brand, Store, User
from .serializers import StoreSerializer, BrandSerializer, OfferSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET

class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class OfferList(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

@api_view(['POST'])
def login_register(request):
    username = request.data.get('username')
    otp = request.data.get('otp')

    # Verificar si el usuario ya existe
    user = User.objects.filter(username=username).first()

    if not user:
        # Si el usuario no existe, se crea uno nuevo
        user = User.objects.create(username=username)

    # Verificar el OTP y autenticar al usuario
    if otp == 'OTP_VALIDO':
        user = authenticate(request, username=username)
        if user:
            # Iniciar sesión y generar el token de acceso OAuth2
            login(request, user)
            return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)

    return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

def subscribe_user_to_store(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        store_id = request.POST.get('store_id')
        
        try:
            user = User.objects.get(username=username)
            store = Store.objects.get(id=store_id)
            
            user.favorite_store = store
            user.save()
            
            return JsonResponse({'success': True, 'message': 'User subscribed to store successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found.'})
        except Store.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Store not found.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@require_GET
def users_by_store(request, store_id):
    try:
        store = Store.objects.get(id=store_id)
        users = User.objects.filter(favorite_store=store)
        user_list = [user.username for user in users]
        return JsonResponse({'users': user_list})
    except Store.DoesNotExist:
        return JsonResponse({'error': 'Store not found'}, status=404)