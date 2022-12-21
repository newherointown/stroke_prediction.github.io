from django.urls import path
from . import views
from django.conf.urls.static import static
from stroke_prediction.settings import DEBUG, STATIC_URL, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT
urlpatterns = [
    path('',views.index , name='index'),
    path('quickpredict',views.quickpredict , name='quickpredict'),
    path('signup',views.signup , name='signup'),
    path('signin',views.signin , name='signin'),
    path('signout',views.signout , name='signout'),
    path('contact',views.contact , name='contact'),
    path('about',views.about , name='about'),
    path('record', views.record , name='record'),
    path('prevention', views.prevention , name='prevention'),
    path('doctorhospital', views.doctorhospital , name='doctorhospital'),
    path('heartdetail',views.heartdetail,name='heartdetail'),
    path('symptoms', views.symptoms, name='symptoms'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATICFILES_DIRS)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)