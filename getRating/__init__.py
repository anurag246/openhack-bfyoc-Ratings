import logging
import requests
import uuid
import datetime
import azure.functions as func
import json

def main(req: func.HttpRequest, ratingId: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    print(req.route_params)
    if not ratingId:
         return func.HttpResponse(
              "Pass a valid ratingID in the query string.",
              status_code=400
         )
    else:
        print("Found ***********")
        apiresponse = {}
        apiresponse['id']= ratingId[0]['id']
        apiresponse['userId']=ratingId[0]['userId']
        apiresponse['productId']=ratingId[0]['productId']
        apiresponse['timestamp']=ratingId[0]['timestamp']
        apiresponse['locationName']=ratingId[0]['locationName']
        apiresponse['rating']=ratingId[0]['rating']
        apiresponse['userNotes']=ratingId[0]['userNotes']
        json_data = json.dumps(apiresponse)
        print(json_data)
            

    
    # if rId:
    #     print("Found ***********")
    #     print(rId)

    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a ratingID in the query string or in the request body for a personalized response.",
    #          status_code=400
    #     )

    
    # apiresponse = {}
    # apiresponse['id']=str(id)
    # apiresponse['userId']=userId
    # apiresponse['productId']=prodId
    # apiresponse['timestamp']=str(timestamp)
    # apiresponse['locationName']=locationName
    # apiresponse['rating']=rating
    # apiresponse['userNotes']=userNotes
    # json_data = json.dumps(apiresponse)
    # print(json_data)
    # doc.set(func.Document.from_json(json_data))

    return func.HttpResponse(json_data,status_code=200)