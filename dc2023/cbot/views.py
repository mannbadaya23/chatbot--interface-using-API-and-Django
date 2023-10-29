from rest_framework import generics
from django.http import JsonResponse
from fuzzywuzzy import fuzz
import requests
import re
# Create your views here.

class testview(generics.GenericAPIView):

    def get(self,request):
        return
    
    def post(self,request):
        print(request.data['prompt'])
        best_response = resgen(request.data['prompt'].lower(), response_dict)
        response = JsonResponse(
            {'response': best_response},status=200)
        return response

def resgen(input_text, response_dict):
    best_match = None
    best_score = -1
    for key, response in response_dict.items():
        similarity_score = fuzz.ratio(input_text, key)
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = response if isinstance(response, str) else response(input_text)

    return best_match

def jeepyqs():
    linkA= "https://nta.ac.in/Downloads"
    return linkA
    
def neetpyqs():
    linkB= "https://www.selfstudys.com/books/neet-previous-year-paper"
    return linkB 

response_dict = {
    "hello": "Hello, Which PYQ's do you want to solve: jee or neet.",
    "jee": "OK here you go:    " + jeepyqs() + "  .do you want me to open the link for you? if yes then type- yeah ",
    "neet": "OK here you go:    " + neetpyqs() + "  .do you want me to open the link for you? if yes then type- yep ",
    "yeah": "Its an  hell easy task you can also do it.",
    "yep": "Already provided.",
    "any other exam pyqs": "Soory sir but we have not anything else other than these right now, we are working on it.",
    "goodbye": "Goodbye! Have a great day.", 
}