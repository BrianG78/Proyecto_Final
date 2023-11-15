from django.shortcuts import render
from rest_framework.views import APIView



# Create your views here.

# class Home(APIView):
#    template_name='index.html'
#    def get(self,request):
#        return render(request,self.template_name)


class Login(APIView):
   template_name='login.html'
   def get(self,request):
       return render(request,self.template_name)
   
class Signup(APIView):
   template_name='Signup.html'
   def get(self,request):
       return render(request,self.template_name)  
    
class Index(APIView):
   template_name='index.html'
   def get(self,request):
       return render(request,self.template_name)
   
class stats(APIView):
   template_name='stats.html'
   def get(self,request):
       return render(request,self.template_name)     
     
   
     
   
   