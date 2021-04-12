from src.helpers import *
from src.serializers import UsersSerializer
from src.models import Users

model_fields = ["name", "phoneno"]
class UsersAPIController():
    def get(self, request_data):
        """
        :param request_data: Validate Request and Add User to DB and Generate Session 
        :return: {"user_info": "token": ""}
        """
        if "id" in request_data:        
            return UsersSerializer().get(id=request_data["id"])
        else:
            page_no = 1
            item_per_page = 1
            if "page_no" in request_data:
                try:
                    page_no = int(request_data["page_name"])
                except Exception as e:
                    page_no = 0
            if "item_per_page" in request_data:
                try:
                    item_per_page = int(request_data["item_per_page"])
                except Exception as e:
                    item_per_page = 0
            return UsersSerializer().get()
            
    def add(self, request_data):
        """
        :param request_data: Validate Request and Add User to DB and Generate Session 
        :return: {"user_info": "token": ""}
        """
        return UsersSerializer().add(request_data) 
            
    def modify(self, request_data):
        """
        :param request_data: Validate Request and Add User to DB and Generate Session 
        :return: {"user_info": "token": ""}
        """
        return UsersSerializer().modify(request_data)     
        
    def delete(self, request_data):
        """
        :param request_data: Validate Request and Add User to DB and Generate Session 
        :return: {"user_info": "token": ""}
        """
        return UsersSerializer().delete(request_data)                             
