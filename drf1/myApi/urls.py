from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('language', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]
