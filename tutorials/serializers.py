from rest_framework import serializers 
from tutorials.models import Tutorial, Student
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','nim','generation','email','avatar','major','address','city','province','postal_code','create_at','updated_at')