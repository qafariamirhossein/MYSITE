from django.shortcuts import render,redirect,HttpResponse
from website.models import Contact
from django.contrib import messages
from website.forms import NameForm,ContactForm,NewsletterForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your ticket sent successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt sent successfuly')

    form = ContactForm
    return render(request,'website/contact.html',{'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return redirect('/')


def about_view(request):
    # return HttpResponse('<h1>This is --About-- page</h1>')
    return render(request,'website/about.html')

def index_view(request):
    # return HttpResponse('<h1>This is --About-- page</h1>')
    return render(request,'website/index.html')

def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name,message,email,subject)
            return HttpResponse('thanks')
        else:
            return HttpResponse('No thanks')
    form = NameForm
    return render(request,'test.html',{'form':form})