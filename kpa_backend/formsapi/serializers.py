from rest_framework import serializers
from .models import WheelSpecification, BogieChecksheet

class WheelSpecificationSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(source="form_number")
    submittedBy = serializers.CharField(source="submitted_by")
    submittedDate = serializers.DateField(source="submitted_date")
    fields = serializers.JSONField()

    class Meta:
        model = WheelSpecification
        fields = ("formNumber", "submittedBy", "submittedDate", "fields")

class BogieChecksheetSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(source="form_number")
    inspectionBy = serializers.CharField(source="inspection_by")
    inspectionDate = serializers.DateField(source="inspection_date")
    bogieDetails = serializers.JSONField(source="bogie_details")
    bogieChecksheet = serializers.JSONField(source="bogie_checksheet")
    bmbcChecksheet = serializers.JSONField(source="bmbc_checksheet")

    class Meta:
        model = BogieChecksheet
        fields = (
            "formNumber", "inspectionBy", "inspectionDate", 
            "bogieDetails", "bogieChecksheet", "bmbcChecksheet"
        )
