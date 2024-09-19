from django.views.decorators.csrf import csrf_exempt
from djecommerce.tools.reponser import JReponse
from accounts.models import User
import json

def index(request):
    return HttpResponse("Hello, world. You're on the accounts page.")

@csrf_exempt
def register(request):
    
    if request.method != 'POST' or len(request.body) == 0:
        return JReponse(400)

    body = json.loads(request.body)

    if "name" not in body or "surname" not in body:  
        return JReponse(400)

    user = User(first_name=body["name"], last_name=body["surname"])
    return JReponse(201, user)
    


def login(request):
    if request.method != 'POST':
        return JReponse(400)
    return JReponse(201)