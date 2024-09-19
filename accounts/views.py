from django.views.decorators.csrf import csrf_exempt
from djecommerce.tools.reponser import JReponse
from accounts.models import User
import json

def index(request):
    return HttpResponse("Hello, world. You're on the accounts page.")

@csrf_exempt
def register(request):
    
    if request.method != 'POST':
        return JReponse(405)
    if len(request.body) == 0:
        return JReponse(405)
    body = json.loads(request.body)

    if "first_name" not in body or "last_name" not in body or "email" not in body or "password" not in body:  
        return JReponse(400)

    user = User(first_name=body["first_name"], last_name=body["last_name"])
    return JReponse(201, user)
    


def login(request):
    if request.method != 'POST':
        return JReponse(400)
    return JReponse(201)