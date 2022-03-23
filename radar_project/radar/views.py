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


def like_post(request, pk):
    post = get_list_or_404(Post, id=request.POST.get('post_id'))[0]
    liked = False
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('homepage1'))


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


def homepage1(request):
    context_dict = {}
    current_user = request.user
    try:
        posts = Post.objects.all()
        context_dict['current_user'] = current_user.username.lower()
        for post in posts:
            post.set_total_likes()
        context_dict['posts'] = posts
        if(current_user.is_authenticated):
            context_dict['liked_posts'] = current_user.posts.all()

    except:
        context_dict['posts'] = None
    return render(request, 'radar/homepage1.html', context=context_dict)


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


# this will be implemented to be the only home page
def homepage(request):
    context_dict = {}
    try:
        posts = Post.objects.all()
        context_dict['posts'] = posts
    except:
        context_dict['posts'] = None
    return render(request, 'radar/header.html', context=context_dict)


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
    try:
        userProfile = UserProfile.objects.get(slug=current_user_slug)
        context_dict['user'] = userProfile
        user_liked_posts = current_user.posts.all()
        for post in user_liked_posts:
            post.set_total_likes()
    except UserProfile.DoesNotExist:
        context_dict['user'] = None
    context_dict['user_liked_posts'] = user_liked_posts
    print(user_liked_posts)
    return render(request, 'radar/account.html', context=context_dict)


@ login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('radar:homepage1'))


def testview(request):
    return render(request, 'radar/viewPost.html')


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
