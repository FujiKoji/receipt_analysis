from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index,name='index'),
    path('upload/', views.upload, name='upload'),
    path('csvexport/', views.csvexport, name='csvexport'),
    path('csvexport_summary/', views.csvexport_summary, name='csvexport_summary'),
    path('csvexport_practice/', views.csvexport_practice, name='csvexport_practice'),
    path('test/', views.test, name='test'),
    path('transform/', views.transform_practice_data, name='transform_practice_data'),
    path('analysis_monthly_data/', views.analysis_monthly_data, name='analysis_monthly_data'),
    path('yobou/', views.yobou, name='yobou'),
    path('export_patient_data/', views.export_patient_data,name='export_patient_data'),
    path('export_patient_data_set/', views.export_patient_data_set,name='export_patient_data_set'),
    path('export_prevent_set/', views.export_prevent_set,name='export_prevent_set'),
    path('transform_yobou/', views.transform_yobou,name='transform_yobou'),
    path('analysis_monthly_data_score/', views.analysis_monthly_data_score, name='analysis_monthly_data_score'),
    path('analysis_monthly_patient_stage/', views.analysis_monthly_patient_stage, name='analysis_monthly_patient_stage'),
    path('import_apodent_responsible_data/', views.import_apodent_responsible_data, name='import_apodent_responsible_data'),
    path('analysis_assess_responsible/', views.analysis_assess_responsible, name='analysis_assess_responsible'),
    path('assess_dh/', views.assess_dh, name='assess_dh'),
    path('import_cancel_csv/', views.import_cancel_csv, name='import_cancel_csv'),
    path('analysis_monthly_patient_v2/', views.analysis_monthly_patient_v2, name='analysis_monthly_patient_v2'),
    path('monthly_score/', views.monthly_score, name='monthly_score'),
    path('insurance_addition_simulation/', views.insurance_addition_simulation, name='insurance_addition_simulation'),
    path('import_apotool_responsible_data/', views.import_apotool_responsible_data, name='import_apotool_responsible_data'),
    path('assess_responsible/', views.assess_responsible, name='assess_responsible'),
    path('assess_responsible_cancel/', views.assess_responsible_cancel, name='assess_responsible_cancel'),
    path('assess_responsible_reserve/', views.assess_responsible_reserve, name='assess_responsible_reserve'),
    path('analysis_monthly_patient_stage_v2/', views.analysis_monthly_patient_stage_v2, name='analysis_monthly_patient_stage_v2'),
]