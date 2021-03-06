from django.shortcuts import render,redirect
from .forms import Registration
from django.contrib import messages
from django.core.mail import send_mail
from college.models import College,Detail_college
from django.contrib.auth.models import User


def base(request):
    college = College.objects.all()
    college_count = College.objects.all().count()
    user_count = User.objects.count()
    context = {
        'college':college,
        'count':college_count,
        'ucount':user_count,
    }
    return render(request, 'pages/index.html',context)

def register(request):
    if request.method=='POST':
        form = Registration(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
#             send_mail(
#                 'Welcome to the this website',
#                 'thankyou for registering in this website, we will not disappoint you with our website.',
#                 '21b06project@gmail.com',
#                 [email],
#                 fail_silently=False,
# )
            messages.success(request,'You have successfully registered now please login')
            return redirect('login')
    else:
        form=Registration()
    return render(request, 'register/resgistration.html',{'form':form})
