from django.http import HttpResponse

import backend

import json

def classification_request(request):
    if request.method == 'POST':
        handler = backend.handle_request(request.body)
        

        
    return HttpResponse(json.dumps({'answer': 'hi ich komme aus dem backend'}), content_type='application/json')