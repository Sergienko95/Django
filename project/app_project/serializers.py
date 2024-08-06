from rest_framework import serializers
from .models import Organization, Period, Line, Form, Data


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
