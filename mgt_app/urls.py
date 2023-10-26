from django.urls import path
from . import views

app_name = "mgt_app"
urlpatterns = [

    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("customers/<str:pk>/", views.customers, name="customers"),
    path("createorder/<str:pk>/", views.createOrder, name="createorder"),
    path("update_order/<str:pk>/", views.updateOrder, name="update_order"),
    path("delete_order/<str:pk>/", views.deleteOrder, name="delete_order"),
    
]
