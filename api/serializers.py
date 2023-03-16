from rest_framework.serializers import ModelSerializer
from main.models import ContactForm , CallBackForm ,    NewsLetter
class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactForm
        # fields = '__all__'
        exclude = ['user' , 'created_at' , 'contacted_status']
        
class CallBackFormSerializer(ModelSerializer):
    class Meta:
        model = CallBackForm
        exclude = ['user' , 'created_at' , 'contacted_status']
        
class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        # fields = '__all__'
        exclude = ['user' , 'created_at' ,]
        
