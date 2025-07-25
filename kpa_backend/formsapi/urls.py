from django.urls import path
from .views import WheelSpecificationView, BogieChecksheetView

urlpatterns = [
    path('api/forms/wheel-specifications', WheelSpecificationView.as_view()),
    path('api/forms/bogie-checksheet', BogieChecksheetView.as_view()),
]
