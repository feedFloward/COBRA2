from .json_parser import JsonParser
from .models.classification import select_model
import json

def handle_request(request_body):
    request_dict = json.loads(request_body)
    print(request_dict)
    parsed_body = JsonParser(**request_dict)
    model = select_model(**parsed_body)