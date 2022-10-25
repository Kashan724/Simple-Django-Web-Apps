from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("kashan",views.kashan,name="kashan"),
    path("david",views.david,name="david")

]