from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification, BogieChecksheet
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer

# Handle POST and GET for /api/forms/wheel-specifications
class WheelSpecificationView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": obj.form_number,
                    "status": "Saved",
                    "submittedBy": obj.submitted_by,
                    "submittedDate": obj.submitted_date.strftime("%Y-%m-%d"),
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        filters = {}
        if 'formNumber' in request.GET:
            filters['form_number'] = request.GET.get('formNumber')
        if 'submittedBy' in request.GET:
            filters['submitted_by'] = request.GET.get('submittedBy')
        if 'submittedDate' in request.GET:
            filters['submitted_date'] = request.GET.get('submittedDate')
        queryset = WheelSpecification.objects.filter(**filters)
        data = [
            {
                "formNumber": obj.form_number,
                "submittedBy": obj.submitted_by,
                "submittedDate": obj.submitted_date.strftime("%Y-%m-%d"),
                "fields": obj.fields,
            }
            for obj in queryset
        ]
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": data
        })

# Handle POST for /api/forms/bogie-checksheet
class BogieChecksheetView(APIView):
    def post(self, request):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({
                "success": True,
                "message": "Bogie checksheet submitted successfully.",
                "data": {
                    "formNumber": obj.form_number,
                    "inspectionBy": obj.inspection_by,
                    "inspectionDate": obj.inspection_date.strftime("%Y-%m-%d"),
                    "status": obj.status,
                },
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
