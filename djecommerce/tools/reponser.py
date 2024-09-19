import json
from django.http import JsonResponse

def JReponse(status_code: int):
# 2xx success
    if status_code == 200:
        return JsonResponse({
            "status": 200,
            "message": "Request successful",
            }) 
    if status_code == 201:
        return JsonResponse({
            "status": 201,
            "message": "Resource created successfully",
            }) 
    if status_code == 202:
        return JsonResponse({
            "status": 202,
            "message": "No content to return"
            }) 
# 4xx client errors
    if status_code == 400:
        return JsonResponse({
            "error": 400,
            "message": "Invalid request"
            })
    if status_code == 401:
        return JsonResponse({
            "error": 401,
            "message": "Authentication required"
            })
    if status_code == 403:
        return JsonResponse({
            "error": 403,
            "message": "Access denied"
            })
    if status_code == 404:
        return JsonResponse({
            "error": 404,
            "message": "Resource not found"
            })
    if status_code == 405:
        return JsonResponse({
            "error": 405,
            "message": "Method not allowed"
            })            
# 5xx server errors
    if status_code == 500:
        return JsonResponse({
            "error": 500,
            "message": "Server encountered an error"
            })
