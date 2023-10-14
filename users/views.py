from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout ,authenticate
from .forms import UserLoginForm ,UserRegisterForm
from django.urls import reverse_lazy
# Create your views here.



class UserRegisterView(CreateView):
    form_class = UserRegisterForm  
    template_name = 'register_user_view.html'  
    success_url = reverse_lazy('users:home')  
    def form_valid(self, form):
  
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  
        user.save()

      
        login(self.request, user)

        return super().form_valid(form) 
    


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login_user_view.html'
    success_url = reverse_lazy('users:home') 
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user) 
            return super().form_valid(form)  

        form.add_error(None, 'Invalid login credentials') 
        return self.form_invalid(form)  


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home.html')  

 
  
    


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,'home.html')
    login_url = "'/user/login/' "
    
   


        
        