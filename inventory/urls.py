from django.urls import path

from inventory.views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, OrderDetailView

app_name = 'inventory'
urlpatterns = [
    path('order/<int:inventory_id>/list', OrderListView.as_view(), name='order_list'),
    path('order/<int:inventory_id>/detail/<int:order_id>', OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:inventory_id>/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:inventory_id>/update/<int:order_id>', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:inventory_id>/delete/<int:order_id>', OrderDeleteView.as_view(), name='order_delete'),
]
