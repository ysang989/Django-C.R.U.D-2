import json

from django.views import View
from django.http import JsonResponse

from .models import Owner, Dog

"""
input : {
    name : 박상연
    age : 25
    email : ysh959@naver.com
}
logic

    post
    1) 주인테이블에 신규주인(이름, 나이, 이메일)을 추가한다.
    output: 신규등록 : 성공
    2) 강아지테이블에 신규강아지(이름, 나이, 주인 id)를 추가한다.
    output: 신규등록 : 성공


"""

class OwnersViews(View):
    def get(self, request):
        results=[]
        owners = Owner.objects.all()
        dogs = Dog.objects.all()

        # for owner,dog in owners,dogs:
        #     results.append({
        #         "name" : owner.name,
        #         "email": owner.email,
        #         "age" : owner.age,
        #         "dog_name": dog.name,
        #         "dog_age": dog.age
        # })
        for owner in owners:
            dogs_list=[]
            dogs = Dog.objects.filter(owner_id=owner.id)
            for dog in dogs:
                dogs_list.append({
                    'name' : dog.name,
                    'age': dog.age
                })
            results.append({
                'name' : owner.name,
                'email': owner.email,
                'age': owner.age,
                'dogs_list' : dogs_list,
            })


        return JsonResponse({"owners":results}, status=200)


    def post(self,request):
        input_data = json.loads(request.body)
        owner = Owner.objects.create(name=input_data["name"], age = input_data['age'], email=input_data['email'])

        return JsonResponse({"new_owner":"SUCCESS"},status=201)

class DogViews(View):
    def get(self,request):
        results=[]
        dogs = Dog.objects.all()

        for dog in dogs:
            results.append({
                "name": dog.name,
                "owner's name": dog.id
            })
        return JsonResponse({"dogs":results}, status=200)

    def post(self,request):
        """
        이름 : 해피
        나이 : 5
        owner_id : 1
        """
        input_data = json.loads(request.body)

        owner = Owner.objects.get(id=input_data["owner_id"])

        dog = Dog.objects.create(name=input_data["name"], age=input_data["age"], owner_id = owner.id)

        return JsonResponse({"new_dog":"SUCCESS"},status=201)


        

# from django.shortcuts import render


# Create your views here.
