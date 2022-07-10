import requests 
import json
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from .models import Article

class NPRAPIView(APIView):
    """using APIView for get the contents from NPR and save it in the database"""
    def get(self, request, format=None):
        #results = self.request.query_params.get('type')
        response = {}
        r = requests.get("https://feeds.npr.org/1004/feed.json")
        r_status = r.status_code
        if r_status == 200:
            data = r.json()
            items = data['items']
        
        
            for i in items[:5]:
                article_data= Article(
                    id_number = i['id'],
                    url = i["url"],
                    title = i["title"],
                    content_html = i["content_html"],
                    summary = i["summary"],
                    date_published = i["date_published"],   
                )
                article_data.save()
                
                
                response['status'] = 200
                response['message'] = "success"
                response['article'] = items
            
        else:
            response['status'] = r.status_code
            response['message'] = "failed"
            response['article'] = {} 
            
        return Response(response)          
        
        