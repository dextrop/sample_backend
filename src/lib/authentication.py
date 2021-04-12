from rest_framework import authentication
from rest_framework import exceptions

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # write your auth code here.
        return None

    def authenticate_header(self, request):
        # declare all your herders here
        return []