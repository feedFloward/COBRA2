from django.http import HttpResponse

import json

def classification_request(request):
    if request.method == 'POST':
        print(request.body)
        
    return HttpResponse(json.dumps({'answer': 'hi ich komme aus dem backend'}), content_type='application/json')