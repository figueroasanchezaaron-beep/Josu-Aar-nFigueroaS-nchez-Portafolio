from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# ================================
# LOGIN
# ================================
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")  # Página de inicio del sistema
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "auth/login.html")


# ================================
# LOGOUT
# ================================
def logout_view(request):
    logout(request)
    return redirect("login")


# ================================
# REGISTRO DE USUARIO
# ================================
def registro_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("registro")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect("registro")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Usuario registrado correctamente.")
        return redirect("login")

    return render(request, "auth/registro.html")
