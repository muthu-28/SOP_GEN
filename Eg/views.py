from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm, SopForm, LastForm
from .models import UserProfile
from .utils.mail_send import send_mail

def login(request):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            # The form is valid, save the data to the database
            profile =form.save()
            # Redirect to the 'Next.html' page after successful form submission
            return redirect('next', profile.pk)  # Replace 'next_page_name' with the actual URL name for 'Next.html'
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})

def nextpage(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(UserProfile, id=pk)
        form = SopForm(request.POST or None, instance=instance)
        if form.is_valid():
            profile = form.save()
            # Redirect to the 'Next.html' page after successful form submission
            return redirect('last', profile.pk)  # Replace 'next_page_name' with the actual URL name for 'Next.html'
    else:
        form = SopForm()

    return render(request, 'Next.html', {'form': form})

def submit(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(UserProfile, id=pk)
        form = LastForm(request.POST or None, instance=instance)
        if form.is_valid():
            profile = form.save()
            return redirect('success', profile.pk)
    else:
        form=LastForm()
    return render(request,'regform.html',{'form':form})


def success(request, pk):
    instance = get_object_or_404(UserProfile, id=pk)
    # Here you can add SMTP call function
    print(instance.email)
    send_mail(instance)
    return render(request,'success.html', {"email":instance.email})


def favicon_view(request):
    # Handle favicon requests here
    # You can return an empty response or your custom favicon image
    return HttpResponse(status=204)
