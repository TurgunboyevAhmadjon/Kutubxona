from django.contrib import admin
from django.urls import path
from mashq_uchun.views import *
from Badiiy_kitoblar.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('bosh/', bosh),
    path('oquvchilar/', oquvchilar),
    path('oquvchi/<str:ism>/', oquvchi),
    path('books/', all_kitoblar),
    path('kitob/<int:pk>/edit/', kitob_edit),
    path('muallif/', mualliflar),
    path('mualliflar/<int:pk>/edit/', muallif_edit),
    path('students/', all_students),
    path('studentlar/<int:pk>/', bitta_student),
    path('records/', record),
    path('student/<int:pk>/edit/', student_tahrirlash),
    path('student/<int:pk>/', student_del),
]
