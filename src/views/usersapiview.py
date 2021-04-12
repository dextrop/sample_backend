from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse
from src.lib.loggingmixin import LoggingMixin
from src.controllers import UsersAPIController


class UsersAPIView(LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin):
    
    
    def get(self, requests):
        # GET api view
        Response = UsersAPIController().get(request_data=requests.GET)
        return CustomResponse(message="UsersAPI GET Api view", payload=Response, code=HTTP_200_OK)

    def post(self, requests):
        # POST api view
        Response = UsersAPIController().add(request_data=requests.data)
        return CustomResponse(message="UsersAPI POST Api view", payload=Response, code=HTTP_200_OK)

    def put(self, requests):
        # PUT api view
        Response = UsersAPIController().modify(request_data=requests.data)
        return CustomResponse(message="UsersAPI PUT Api view", payload=Response, code=HTTP_200_OK)

    def delete(self, requests):
        # DELETE api view
        Response = UsersAPIController().delete(request_data=requests.data)
        return CustomResponse(message="UsersAPI DELETE Api view", payload=Response, code=HTTP_200_OK)                        
