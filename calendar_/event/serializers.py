from rest_framework import serializers
from .models import Event, Request
from rest_framework.fields import CurrentUserDefault

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','link','startdate','enddate','time']
    def save(self):
        user = self.context['request'].user
        name = self.validated_data['name']
        link = self.validated_data['link']
        startdate = self.validated_data['startdate']
        enddate = self.validated_data['enddate']
        time = self.validated_data['time']
        
        Event.objects.create(
            user=user,
            name=name,
            link=link,
            startdate=startdate,
            enddate=enddate,
            time=time
        )
    

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['event','status']
        model = Request
    def save(self):
        user = self.context['request'].user
        event = self.validated_data['event']
        status = self.validated_data['status']
        Request.objects.create(
            user=user,
            event=event,
            status=status
        )