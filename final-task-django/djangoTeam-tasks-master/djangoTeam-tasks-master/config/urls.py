from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from library.apis.auth_api import auth_router
from library.apis.product_api import product_router

api = NinjaAPI()

api.add_router('Product', product_router)
api.add_router('Book_Auth', auth_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
