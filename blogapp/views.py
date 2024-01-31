from django.shortcuts import render, redirect
from .models import Article,Bio
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    acc=Article.objects.all()
    return render(request,'index.html',{'articles':acc})


@login_required
def profile(request):
    # acc=Article.objects.all()
    acc = Article.objects.filter(author=request.user)
    return render(request,'profile.html',{'articles':acc})

@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('arti')
        user = request.user 
        new_article = Article(title=title, content=content, author=user)
        new_article.save()
        return redirect('/')
    return render(request,'add.html')

def register(request):

    if request.method == 'POST':
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
                
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/') #home page

    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials...')
            return redirect("login")

    else:
        return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def update_bio(request):
    bio_text = request.POST.get('bio', '')

    if not bio_text:
        return JsonResponse({'error': 'Bio cannot be empty'})

    if len(bio_text) > 500:
        return JsonResponse({'error': 'Bio too long'})

    user = request.user

    # Assuming you have a Bio model associated with the User model
    bio_instance, created = Bio.objects.get_or_create(user=user)
    bio_instance.bio = bio_text  # Corrected field name
    bio_instance.save()

    return JsonResponse({'status': 'success'})