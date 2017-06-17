from rest_framework import serializers
from app.models import UpComingEvents

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpComingEvents
        fields = ('EventDate','EventName','EventVenue','EventImage','EventOrganiser','ShowCategory','EventContact','EventLink')
