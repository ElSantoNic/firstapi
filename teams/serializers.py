from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'url', 'name', 'standings', 'wins', 'draws', 'losses')