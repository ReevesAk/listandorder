import re
from rest_framework  import serializers

# In-project imports.
from .models import ContactUs, Subscribe


class ContactUsSerializers(serializers.ModelSerializer):
    """ Serilaizers for sending email to the server for support. """

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone_number', 'label']

    
    def validate(self, attrs):

        email = attrs.get('email', '')

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email) == None:
            return serializers.ValidationError(
                'email: email is not valid'
            )

        return super().validate(attrs)


class SubscribeSerializers(serializers.ModelSerializer):
    """ Serilaizers for subscribing to graemart. """

    class Meta:
        model = Subscribe
        fields = ['email']


    def validate(self, attrs):

        email = attrs.get('email', '')

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email) == None:
            return serializers.ValidationError(
                'email: email is not valid'
            )

        return super().validate(attrs)
        