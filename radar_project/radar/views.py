from django.shortcuts import render
from django.http import HttpResponse
from radar.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from radar.models import Post, Category, UserProfile


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'radar/category.html', context=context_dict)


def homepage1(request):
    return render(request, 'radar/homepage1.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('radar:homepage1'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'radar/login.html')


def signup(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'radar/signup.html', context={'user_form': user_form,
                                                         'profile_form': profile_form,
                                                         'registered': registered})


# @login_required
def account(request, current_user_slug):
    context_dict = {}
    current_user = request.user
    try:
        userProfile = UserProfile.objects.get(slug=current_user_slug)
        context_dict['user'] = userProfile
    except UserProfile.DoesNotExist:
        context_dict['user'] = None
    return render(request, 'radar/account.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('radar:homepage1'))


def addpage(request):
    return render(request, 'radar/addpage.html')


def viewpage(request):
    return render(request, 'radar/viewpage.html')
