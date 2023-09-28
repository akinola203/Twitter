
from django.shortcuts import  redirect , render,  get_object_or_404
from django.contrib.auth.models import User
from .models import Profile , Post , Relationship
from .forms import UserRegisterForm, PostForm , ProfileUpdateForm , UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your views here.


def index(request):
    return render(request, 'events/index.html')

@login_required
def home(request):
    posts = Post.objects.all()
    form = PostForm()  

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'events/home.html', context)

def post(request):
    form = PostForm()
    


def profile(request):
    return render(request, 'events/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'events/register.html', context)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {
        'user':user,
        'posts':posts,

    }
    return render(request, 'events/profile.html', context)


@login_required
def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'events/edit.html', context)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()



@login_required
def follow(request, username):
    current_user = request.user
    to_user  = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('home')


@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = get_object_or_404(User, username=username) 
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user=current_user, to_user=to_user_id)  # Use the correct field names
    rel.delete()
    return redirect('home')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        user = User.objects.filter(username=searched)
        return render(request,'events/search.html',{'searched':'searched','user':user})
    else:
        return render(request,'events/search.html')


