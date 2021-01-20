from django.shortcuts import render,redirect
from .forms import Review_Form,Seconday_form
from django.contrib import messages

def review_view(request):
    if request.method == "POST":
        form = Review_Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.reviewer = request.user
            instance.save()
            messages.success(request,'Thank you for your review,your review is submitted.')
            return redirect('dashboard')
    else:
        form = Review_Form()
    
    context = {
        'form':form
    }

    return render(request,'review/review.html',context)


def secondary_view(request):
    if request.method == "POST":
        form = Secondary_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            messages.success(request,'Thank you for your review,your review is submitted.')
            return redirect('index')
    else:
        form = Seconday_form()
    context = {
        'form':form
    }
    return render(request,'help/secondary.html',context)

