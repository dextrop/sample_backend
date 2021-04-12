from rest_framework import serializers
from django.core.exceptions import ValidationError
from src.models import Users

model_fields = ["name", "phoneno"]

class UsersBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = '__all__'

class UsersSerializer():    
    def get(self, id=None, order_by_created=False, page_no=1, item_per_page=10):     
        # Returns user object from database based on filter configuration.
        if id != None:
            objects = Users.objects.filter(_id=id)
            if objects.count() < 1:
                return None
            return objects[0]
        
        start = ( page_no - 1 ) * item_per_page
        end = start + item_per_page
        
        if order_by_created:
            return Users.objects.all().order_by("-_created")[start:end]
        else:
            return Users.objects.all().order_by("-_updated")

    def add(self, data):
        # Validate object and add it to table.
        for field in model_fields:
            if field not in data:
                raise ValidationError("Missing key '{}'".format(field))
        user_obj = Users.objects.create(**data)

        return UsersBaseSerializer(user_obj, many=False).data

    def modify(self, data):
        # Modify an object based on ID.
        if "_id" not in data:
            raise ValidationError("Missing Object ID")
        obj = self.get(id=data["_id"])
        if obj == None:
            raise ValidationError("Object does not exits check if id is correct")
        for key in model_fields:
            if key != "_id" and key in data:
                setattr(obj, key, data[key])

        obj.save()
        obj = self.get(id=obj._id)
        return UsersBaseSerializer(obj, many=False).data

    def delete(self, data):
        # Delete an object based on ID.
        if "_id" not in data:
            raise ValidationError("Missing Object ID")
        Users.objects.filter(_id=data["_id"]).delete()
        return "Object Deleted Successfully"
