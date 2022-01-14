import logging
import requests
import uuid
import datetime
import azure.functions as func
import json

def main(req: func.HttpRequest, documents: func.DocumentList) -> func.HttpResponse:
    
    if documents.__len__()==0:
        return func.HttpResponse(
              "No record found for this user.",
              status_code=400
         )

    doc = []
    for document in documents:
        print("Found ***********")
        apiresponse = {}
        apiresponse['id']= document['id']
        apiresponse['userId']=document['userId']
        apiresponse['productId']=document['productId']
        apiresponse['timestamp']=document['timestamp']
        apiresponse['locationName']=document['locationName']
        apiresponse['rating']=document['rating']
        apiresponse['userNotes']=document['userNotes']
        doc.append(apiresponse)
        
    json_data = json.dumps(doc)
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