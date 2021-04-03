from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import College,Detail_college,Line_Chart,College_Info,College_Courses 
from django.http import JsonResponse,HttpResponse
from django.contrib import messages

from django.core.mail import send_mail

from .forms import Years_of_experience,Email_send
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


dataset = pd.read_csv('college/Salary_predictor.csv')

@login_required
def genral_info(request):
    colleges = College.objects.all()

    context = {
        'colleges':colleges
    }
    return render(request,'colleges/genral.html',context)

@login_required
def dashboard(request,id):
    branch =  []
    placed =  []

    queryset = Line_Chart.objects.filter(name=id)

    colleges = College.objects.all()
    detail_college = get_object_or_404(College,id=id)

    y_pred = 0

    for total in queryset:
        branch.append(total.Branch)
        placed.append(total.placed)
    
    if request.method == 'POST':
        form = Years_of_experience(request.POST)
        if form.is_valid():
            years = form.cleaned_data['Years_of_experience']
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, 1].values

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


            regressor = LinearRegression()
            regressor.fit(X_train, y_train)

            y_pred = np.round_(regressor.predict(np.array(years).reshape(1, 1)),decimals=3)
            

            print("%.2f" % y_pred)

            # html = "<html><body>Your predicted salary is %s.</body></html>" % y_pred

            # return redirect('dashboard',id)

    else:
        form = Years_of_experience()
        # y_pred = None
        # regressor = None
    

    # if request.method == 'POST':
    #     email_form = Email_send(request.POST)
    #     if email_form.is_valid():
    #         college_email = email_form.cleaned_data['college_email']
    #         description = email_form.cleaned_data['description']

    #         send_mail(
    #             'Regarding College Information',
    #             description,
    #             '21b06project@gmail.com',
    #             [college_email],
    #             fail_silently=False,
    #         )
    #         return HttpResponse("<h1> Mail has been sent </h1>")



    # else:
    #     email_form = Email_send()  

    college_info_query = College_Info.objects.filter(name=id)


    college_course_query = College_Courses.objects.filter(name=id)

    context = {
        'branch':branch,
        'placed':placed,
        'detail_college': detail_college,
        'colleges':colleges,
        'form':form,
        'y_pred':y_pred,
        'college_info_query':college_info_query,
        'college_course_query':college_course_query,

    }
    return render(request , 'colleges/dashboard.html',context)

@login_required
def college_info(request,id):
    college = get_object_or_404(College,id=id)
    context = {
        'college':college
    }

    return render(request,'colleges/all_college.html',context)



def placement_chart(request,id):
    query_set = Detail_college.objects.filter(name = id)

    placements = []
    year       = []
    for entry in query_set:
        placements.append(entry.placement)
        year.append(entry.year)
    
    return JsonResponse(data={
        'placements': placements,
        'year': year,
    })


# def compare_colleges(request):
#     colleges = College_Info.objects.filter(city = "Kanpur")






