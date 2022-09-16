from rest_framework import serializers
from account.models import account

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('ID', 'firstname', 'lastname', 'email', 'Email', 'Password', 'Contact_number', 'address')