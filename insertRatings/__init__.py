import logging
import requests
import uuid
import datetime
import azure.functions as func
import json

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    prodId = req.params.get('productId')
    print ("testing *********")
   
    if not prodId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            prodId = req_body.get('productId')
            userId = req_body.get('userId')
            rating = int(req_body.get('rating'))
            locationName = req_body.get('locationName')
            userNotes = req_body.get('userNotes')

    if prodId:
        queryGetProduct = {'productId':prodId}
        responseGetProduct = requests.get('https://serverlessohapi.azurewebsites.net/api/GetProduct', params=queryGetProduct)
        #print( responseGetProduct.status_code)
        if responseGetProduct.status_code==200:
            print ("Product Id Validated Successfully")
        else:
            return func.HttpResponse(f"Issue with Product Id",status_code=responseGetProduct.status_code)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a ProductId in the query string or in the request body for a personalized response.",
             status_code=400
        )

    if userId:
        queryGetUser = {'userId':userId}
        responseGetUser = requests.get('https://serverlessohapi.azurewebsites.net/api/GetUser', params=queryGetUser)
        print(responseGetUser.status_code)
        if responseGetUser.status_code==200:
           print ("User Id Validated Successfully")
        else:
            return func.HttpResponse(f"Issue with User Id",status_code=responseGetUser.status_code)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a UserId in the query string or in the request body for a personalized response.",
             status_code=400
        )    

    id=uuid.uuid4()
    timestamp=datetime.datetime.utcnow()
    if not 0<=rating<=5:
        return func.HttpResponse(f"Issue with Rating - It should be between 0 and 5",status_code=400)
   
    apiresponse = {}
    apiresponse['id']=str(id)
    apiresponse['userId']=userId
    apiresponse['productId']=prodId
    apiresponse['timestamp']=str(timestamp)
    apiresponse['locationName']=locationName
    apiresponse['rating']=rating
    apiresponse['userNotes']=userNotes
    json_data = json.dumps(apiresponse)
    print(json_data)
    doc.set(func.Document.from_json(json_data))

    return func.HttpResponse(json_data,status_code=200)