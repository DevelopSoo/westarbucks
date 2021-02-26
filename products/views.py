import json

from django.views import View
from django.http  import JsonResponse

from .models import *

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        menu_all = Menu.objects.all()

        result = []
        for category in categories:
            category_dict = {
                'name': category.name,
                'menu': category.menu.name
            }
            result.append(category_dict)

        return JsonResponse({'result': result}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)

        name = data["name"]
        menu = data["menu"]

        menu_id = Menu.objects.get(name=menu)
        
        Category.objects.create(name=name, menu=menu_id)

        return JsonResponse({'message': 'success'}, status=201)


class DrinkView(View):
    def get(self, request):
        drinks = Drink.objects.all()

        result = []
        for drink in drinks:
            drink_dict = {
                'korean_name': drink.korean_name,
                'english_name': drink.english_name,
                'description': drink.description,
                'category': drink.category.name

            }
            result.append(drink_dict)
        #print(result) (테스트용)
        return JsonResponse({'result': result}, status=200)

    def post(self, request):
        data = json.loads(request.body) # 요청 받은 정보(body)를 파이썬화시켜서 변수에 저장 - 딕셔너리 형태
        # print(data) 데이터가 잘 오는지 확인
        korean_name = data['korean_name'] # 저장한 데이터(딕셔너리)의 name 키 값의 value 값
        english_name = data['english_name']
        description = data['description']
        category = data['category'] # ??

        category_id = Category.objects.get(name=category)
        Drink.objects.create(korean_name=korean_name, english_name=english_name, description=description, category=category_id)

        # print(korean_name, english_name, description, category)
#         user = User.objects.get(name="")
#         Dog.objects.create(user=user)
        return JsonResponse({'message': 'success'}, status=201)
