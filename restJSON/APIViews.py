from django.http import HttpResponse 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json 

class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs["content_type"] = "application/json" 
        super(JSONResponse, self).__init__(content,**kwargs) 

@api_view(["GET"])
def get_courses_info(request):
    if request.method == "GET" :
        f = open("datas/final.json","r");
        content = f.read()
        f.close() 
        try : 
            return JSONResponse(json.loads(content))
        except ValueError :
            return JSONResponse({"error": "problem encoding json"});


@api_view(["GET"])
def get_news_info(request):
    if request.method == "GET" :
        f = open("datas/news.json","r");
        content = f.read()
        f.close() 
        try : 
            return JSONResponse(json.loads(content))
        except ValueError :
            return JSONResponse({"error": "problem encoding json"});

@api_view(["GET"])
def get_transfer(request): 
    if request.method == "GET" : 
        try : 
            if "course_id" in request.query_params : 
                f = open("datas/transfers/"+request.query_params["course_id"],"r"); 
            else: 
                f = open("datas/totaltrans.json","r");
            content = f.read();
            f.close() 
            return JSONResponse(json.loads(content))
        except (Exception) as e :
            print(e);
            return JSONResponse({"error": "problem generating json"});

@api_view(["GET"])
def get_room(request): 
    if request.method == "GET" : 
        try : 
            f = open("datas/days.json","r"); 
            content = f.read();
            f.close() 
            return JSONResponse(json.loads(content))
        except (Exception) as e :
            return JSONResponse({"error": "problem generating json"});

@api_view(["GET"])
def get_avail(request): 
    if request.method == "GET" : 
        try : 
            f = open("datas/avails.json","r"); 
            content = f.read();
            f.close() 
            return JSONResponse(json.loads(content))
        except (Exception) as e :
            return JSONResponse({"error": "problem generating json"});

