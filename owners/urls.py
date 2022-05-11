from django.urls import path
from .views import OwnersViews, DogViews

urlpatterns=[
    # HTTP GET METHOD -> get
    # GET :8000/owners/owners
    # POST :8000/owners/owners
    # GET :8000/products : products 리스트 요청
    # ProductView(View):
    # ProductDetailView(View):

    path("owners", OwnersViews.as_view()),
    path("dogs", DogViews.as_view()),
]