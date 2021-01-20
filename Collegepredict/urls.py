from django.contrib import admin
from django.urls import path
from registration import views as reg
from college import views as coll
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from review import views as rev


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',reg.base , name='base'),
    path('registration/',reg.register , name='register'),
    path('dashboard/<int:id>',coll.dashboard,name='dashboard'),
    path('coll/detail/<int:id>',coll.college_info,name='info'),
    path('placement-chart/<int:id>', coll.placement_chart, name='placement-chart'),
    path('genral_info/',coll.genral_info , name='genral'),
    # path('Machine_learning/1/<int:id>',coll.ml_view,name="ml"),

    path('',reg.base,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html') , name='logout'),

    path('survey/',rev.review_view,name='survey'),
    path('help/secondary/',rev.secondary_view,name='secondary'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
