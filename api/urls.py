from django.urls import path
from .views import (
    RegisterView, PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView, MappingListCreateView,
    MappingPatientDetailView, MappingDeleteView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', MappingPatientDetailView.as_view(), name='mapping-patient-detail'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]