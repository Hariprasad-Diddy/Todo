from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from crm.models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def add_task(request):
    """
    The below function will create a New task 
    """
    if request.method == "POST":
        name = request.data.get('name')
        user = request.data.get('user')
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        todo_add = Todo.objects.create(name=name,user_id=user,start_date=start_date,end_date=end_date)
        return JsonResponse({'success':True,'data':'Todo added'})


@api_view(['PUT'])
def update_task(request):
    """
    The below function will update the existing task by providing ID of that task 
    """
    if request.method == "PUT":
        ID = request.data.get('id')
        name = request.data.get('name')
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        get_data = Todo.objects.get(id=ID)
        if name == None:
            name = get_data.name
        if start_date == None:
            start_date = get_data.start_date
        if end_date == None:
            end_date = get_data.end_date
        todo_update = Todo.objects.filter(id=ID).update(name=name,start_date=start_date,end_date=end_date)
        return JsonResponse({'success':True,'data':'Task Updated'})


@api_view(['DELETE'])
def remove_task(request):
    """
    The below function can delete the task from list by providing ID of the task
    """
    if request.method == "DELETE":
        ID = request.data.get("id")
        todo_delete = Todo.objects.filter(id=ID).delete()
        return JsonResponse({'success':True,"data":'Task deleted'})


@api_view(['GET'])
def show_task(request):
    """
    The below function can show all the task of particular use by providing that user id
    """
    if request.method == "GET":
        user_id = request.GET.get("id")
        todo_get = Todo.objects.filter(user_id=user_id)
        return JsonResponse({'success':True,'data':list(todo_get.values())})