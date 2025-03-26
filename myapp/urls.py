from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'rentals', views.RentalViewSet)
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path("", views.car_list, name="car_list"),
    path("rent/<int:car_id>/", views.rent_car, name="rent_car"),
    path("api/", include(router.urls)),
]
