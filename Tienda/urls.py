from django.urls import include, path
from oauth2_provider.views import TokenView
from .views import StoreList, BrandList, OfferList
from .views import UserRegistrationView,UserStoreSelectionView



urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/', TokenView.as_view(), name='token'),
    path('stores/', StoreList.as_view(), name='store-list'),
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('offers/', OfferList.as_view(), name='offer-list'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('select-store/', UserStoreSelectionView.as_view(), name='user-store-selection'),

]
