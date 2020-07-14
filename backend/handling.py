from .json_parser import JsonParser
from .models.classification import select_model
import json

#wieder rausnehmen, wenn answer_dict neu strukturiert wurde:
from .models.classification import answer_dict

def handle_request(request_body):
    request_dict = json.loads(request_body)
    parsed_body = JsonParser(**request_dict)
    model = select_model(**parsed_body)
    model.fit()
    model.predict_inputspace()
    model.evaluate()
    return json.dumps(answer_dict.response)
