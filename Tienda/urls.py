from django.urls import include, path
from oauth2_provider.views import TokenView
from .views import StoreList, BrandList, OfferList, login_register, users_by_store
from . import views

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/', TokenView.as_view(), name='token'),
    path('stores/', StoreList.as_view(), name='store-list'),
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('offers/', OfferList.as_view(), name='offer-list'),
    path('login-register/', login_register, name='login_register'),
    path('subscribe/', views.subscribe_user_to_store, name='subscribe_user_to_store'),
    path('stores/<int:store_id>/users/', users_by_store, name='users_by_store'),
]
