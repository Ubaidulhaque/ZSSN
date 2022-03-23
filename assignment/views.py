from operator import length_hint
from time import process_time
from tkinter import EXCEPTION
from urllib import response
from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
  



from .models import Survivors

def home(request):
    
    return render(request, 'home.html')

@csrf_exempt 
def all_survivors(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))

       

        try:
            if 'name' not in data or 'age' not in data or 'gender' not in data or 'location' not in data:

                return JsonResponse({
                    'success':False,
                    'msg' : 'Required Data missing',
                })
            
            
            
           


            survivor = Survivors(name=data['name'], age=int(data['age']), gender=data['gender'], last_location=data['location'], infected= 1 if 'infected' in data and data['infected'] == 'yes' else 0, resources=data['resources'] if 'resources' in data else {})
            survivor.save()
            return JsonResponse({
                                'success':True, 
                                'msg': 'Survivor Added Successfully'
                                })
        
        except Exception as e:
            return JsonResponse({
                                'success':False,
                                'msg' : 'Data Base Error Occured',
                                'e':e
                                })

    if request.method != 'GET':
        return JsonResponse({
                    'success':False,
                    'msg' : 'Bad Request',
                })

    try:
        all_survivors = Survivors.objects.all()

        data = []
        for survivor in all_survivors:
            survivor_data = {}
            survivor_data['id']            = survivor.id
            survivor_data['name']          = survivor.name
            survivor_data['age']           = survivor.age
            survivor_data['gender']        = survivor.gender
            survivor_data['last_location'] = survivor.last_location
            survivor_data['infected']      = survivor.infected
            survivor_data['resources']     = survivor.resources

            data.append(survivor_data)
            


        return JsonResponse({
                            'success':True,
                            'msg' : 'All Survivors Data',
                            "data":data
                            })
    
    except:
        return JsonResponse({
                            'success':False,
                            'msg' : 'Data Base Error Occured'
                            })


@csrf_exempt 
def update_survivor(request, id):

    if request.method == 'PUT':

        try:
        
            data = json.loads(request.body.decode("utf-8"))

            if 'location' not in data:
                return JsonResponse({
                    'success':False,
                    'msg' : 'Required Data missing',
                })


        
            id = int(id)
            survivor = Survivors.objects.get(id=id)
            survivor.last_location = data['location']
            survivor.save()

            return JsonResponse({'success':True,'msg':'updated successfully'})
    

        except:
            return JsonResponse({
                    'success':False,
                    'msg' : 'Bad Request',
                })



        
        
    if id != 'reports' or request.method != 'GET':
        return JsonResponse({
                    'success':False,
                    'msg' : 'Bad Request',
                })


    total_survivor = len(Survivors.objects.all())
    infected_survivor = len(Survivors.objects.filter(infected=1))

    
    
    return JsonResponse({
                    'success':True,
                    'infected_users': str(round(((infected_survivor/total_survivor)*100),2))+ str('%'),
                    'non_infected users':str(round(100-((infected_survivor/total_survivor)*100),2))+ str('%')
                })