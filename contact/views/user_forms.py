from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request=request, message='Usuário criado com sucesso!'
            )
            return redirect('contact:index')

    return render(
        request=request,
        template_name='contact/register.html',
        context={'form': form}
    )


def login_view(request):
    form = AuthenticationForm(request=request)

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request=request, user=user)
            messages.success(request=request, message='Logado com sucesso')
            return redirect('contact:index')
        messages.error(request=request, message='Login inválido!')

    return render(
        request=request,
        template_name='contact/login.html',
        context={'form': form}
    )


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request=request,
            template_name='contact/user_update.html',
            context={'form': form}
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request=request,
            template_name='contact/user_update.html',
            context={'form': form}
        )

    form.save()
    return redirect('contact:user_update')


def logout_view(request):
    auth.logout(request=request)
    return redirect('contact:login')
