from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ContactFormViewSet , CallBackFormViewSet , NewsLetterViewSet
router= DefaultRouter()
router.register('', ContactFormViewSet)
router.register('', CallBackFormViewSet)
router.register('', NewsLetterViewSet)

urlpatterns = [
    path('contact/<int:pk>' , include(router.urls)),
    path('callback/<int:pk>' , include(router.urls)),
    path('newsletter/<int:pk>' , include(router.urls)),
]

