import json
from urllib import response
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from radar.forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from radar.models import Post, Category, UserProfile
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class LikePostView(View):
    @ method_decorator(login_required)
    def get(self, request):
        post_id = request.GET['post_id']
        try:
            post = Post.objects.get(id=int(post_id))
            liked = False
            if post.likes.filter(id=request.user.id):
                post.likes.remove(request.user)
                liked = False
            else:
                post.likes.add(request.user)
                liked = True
        except Category.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        post.set_total_likes()
        post.save()
        context_dict = {"total_likes": post.total_likes,
                        "liked": liked, 'post_id': post.id}
        return HttpResponse(json.dumps(context_dict), content_type='application/json')


def show_category(request, category_name_slug):
    context_dict = {}
    current_user = request.user
    context_dict['current_user'] = current_user
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['posts'] = None
    return render(request, 'radar/category.html', context=context_dict)


def show_post(request, post_title_slug):
    context_dict = {}
    context_dict['current_user'] = request.user
    try:
        post = Post.objects.get(slug=post_title_slug)
        post.views += 1
        post.save()
        context_dict['post'] = post
    except Post.DoesNotExist:
        context_dict['post'] = None

    return render(request, 'radar/viewPost.html', context=context_dict)


def homepage(request):
    context_dict = {}
    current_user = request.user
    try:
        posts = Post.objects.all()
        context_dict['current_user'] = current_user.username.lower()
        for post in posts:
            post.set_total_likes()
        context_dict['posts'] = posts
        if(current_user.is_authenticated):
            user_profile = UserProfile.objects.get(user=current_user)
            context_dict['liked_posts'] = current_user.posts.all()
            context_dict['user_profile'] = user_profile

    except:
        context_dict['posts'] = None
    return render(request, 'radar/homepage.html', context=context_dict)


def search_results(request):
    context_dict = {}
    if request.method == 'GET':
        searched = request.GET['searched']
        posts = Post.objects.filter(title__contains=searched)
        context_dict['searched'] = searched
        context_dict['posts'] = posts
        return render(request, 'radar/search_results.html', context=context_dict)
    else:
        return render(request, 'radar/search_results.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('radar:homepage'))
            else:
                return HttpResponse("Your Radar account is disabled.")
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


@ login_required
def account(request, current_user_slug):
    context_dict = {}
    current_user = request.user
    context_dict['current_user'] = current_user
    user_liked_posts = current_user.posts.all()
    try:
        userProfile = UserProfile.objects.get(slug=current_user_slug)
        context_dict['user_profile'] = userProfile
        for post in user_liked_posts:
            post.set_total_likes()
    except UserProfile.DoesNotExist:
        context_dict['user'] = None
    context_dict['user_liked_posts'] = user_liked_posts

    return render(request, 'radar/account.html', context=context_dict)


@ login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('radar:homepage'))


@ login_required
def add_post(request):
    submitted = False
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/radar/addPost?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True

    context_dict = {}
    context_dict['form'] = form
    context_dict['submitted'] = submitted
    context_dict['current_user'] = current_user

    return render(request, 'radar/addPost.html', context_dict)
