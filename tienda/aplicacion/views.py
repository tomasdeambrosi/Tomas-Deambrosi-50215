from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView    


# Create your views here.

#____________________ Adicionales

def index(request):
    return render(request, "aplicacion/index.html")

def acerca_de(request):
    return render(request, "aplicacion/acerca_de.html")


#____________________ Artículos

class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["nombre", "categoria", "precio_compra", "precio_venta"]
    success_url = reverse_lazy("articulos")

class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ["nombre", "categoria", "precio_compra", "precio_venta"]
    success_url = reverse_lazy("articulos")

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy("articulos")

#____________________ Clientes

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "telefono"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")

#____________________ Ventas

class VentaList(LoginRequiredMixin, ListView):
    model = Venta

class VentaCreate(LoginRequiredMixin, CreateView):
    model = Venta
    fields = ["articulo", "cantidad"]
    success_url = reverse_lazy("ventas")

class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Venta
    fields = ["articulo", "cantidad"]
    success_url = reverse_lazy("ventas")

class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Venta
    success_url = reverse_lazy("ventas")


#____________________ Compras

class CompraList(LoginRequiredMixin, ListView):
    model = Compra

class CompraCreate(LoginRequiredMixin, CreateView):
    model = Compra
    fields = ["distribuidor", "articulo", "cantidad"]
    success_url = reverse_lazy("compras")

class CompraUpdate(LoginRequiredMixin, UpdateView):
    model = Compra
    fields = ["distribuidor", "articulo", "cantidad"]
    success_url = reverse_lazy("compras")

class CompraDelete(LoginRequiredMixin, DeleteView):
    model = Compra
    success_url = reverse_lazy("compras")

    
#____________________ Búsqueda

@login_required
def buscarArticulos(request):
    return render(request, "aplicacion/index.html")

@login_required
def encontrarArticulos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        articulo_list = Articulo.objects.filter(nombre__icontains=patron)
        contexto = {"articulo_list": articulo_list}
        return render(request, "aplicacion/articulo_list.html", contexto)

    return render(request, "aplicacion/index.html")

#____________________ Login

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
       miForm = AuthenticationForm()
    
    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('index'))
    else:
       miForm = RegistroForm()
    
    return render(request, "aplicacion/registro.html", {"form": miForm})

#____________________ Edición de perfil, Cambio de clave, Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.save()
            return redirect(reverse_lazy('index'))
    else:
       miForm = UserEditForm(instance=usuario)
    
    return render(request, "aplicacion/editar_perfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("index")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('index'))
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregar_avatar.html", {"form": miForm} )    