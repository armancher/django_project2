from typing import Any
from django.db import models
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderForm,InventoryForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list_view.html'
    context_object_name = 'orders'

    def get_queryset(self):
        inventory_id = self.kwargs['inventory_id']
     
        return Order.objects.filter(product__inventory__pk=inventory_id)

    
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail_view.html'
    context_object_name = 'order'  

    def get_object(self, queryset=None):
        return get_object_or_404(Order, pk=self.kwargs['order_id']) 
  


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form_view.html' 
    def get_success_url(self):
        
        return reverse_lazy('inventory:order_list', kwargs={'inventory_id': self.object.product.inventory.pk})

    def form_valid(self, form):
       
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    def get_object(self):
        inventory_id = self.kwargs['inventory_id']
        order_id = self.kwargs['order_id']
       
        order = get_object_or_404(Order, pk=order_id)
        return order

    
        
    def get_success_url(self):
        return reverse_lazy('inventory:order_list', kwargs={'inventory_id': self.object.product.inventory.pk})
 
 
class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    
    def get_object(self):
        inventory_id = self.kwargs['inventory_id']
        order_id = self.kwargs['order_id']
       
        order = get_object_or_404(Order, pk=order_id)
        return order

    def get_success_url(self):
        inventory_id = self.kwargs['inventory_id']
        return reverse_lazy('inventory:order_list', kwargs={'inventory_id': inventory_id})