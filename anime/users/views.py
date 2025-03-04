from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout

# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("blog:home")
        else:
            print(form.errors)  # In lỗi ra console

    return render(request, "users/login.html", {"form": form})
    


def logout_view(request):
    logout(request)
    return redirect('blog:home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})
