import json
from django.http import JsonResponse

def JReponse(status_code: int, message = object):
    if status_code == 201:
        return JsonResponse({
            "status": 201,
            "message": "The request has been fulfilled, resulting in the creation of a new resource.",
            "resource": f"{ message }"
            })   
    if status_code == 404:
        return JsonResponse({
            "status": 200,
            "message": { "error":"Bad Request"}
            })
    if status_code == 400:
        return JsonResponse({
            "status": 400,
            "message": { "error":"Bad Request"}
            })

