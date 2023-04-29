from django.contrib import admin
# Register your models here.
from . import models
from import_export.admin import ImportExportModelAdmin
from . import resouces

class TableBasicAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "new_score_etc_identification",
        "new_score_etc",
        "old_score_etc_identification",
        "old_score_etc",
        "in_out_code",
        "late_elderly_medical_code",
        "time_add_code",
        "hospital_clinics_code",
        "nurse_add",
        "reserve1",
        "reserve2",
        "area_add",
        "injury_name_code",
        "drug_name_code",
        "number_of_bed_code",
        "notification",
        "future_hospital",
        "short_stay_surgery",
        "special_remarks",
        "Inspection_decision_code",
        "Inspection_decision_group_code",
        "diminution_code",
        "comprehensive_code",
        "base_conformance_code",
        "base_conformance_facility_standard",
        "facility_standard_code1",
        "facility_standard_code2",
        "facility_standard_code3",
        "facility_standard_code4",
        "facility_standard_code5",
        "facility_standard_code6",
        "facility_standard_code7",
        "facility_standard_code8",
        "facility_standard_code9",
        "facility_standard_code10",
        "general_rule_add_group",
        "basic_add_group",
        "annotation_add_group",
        "tech_materials_add_group",
        "calculation_limit_table_identification",
        "etch_table_identification",
        "age_limit_table_identification",
        "contradiction_table_identification",
        "days_table_identification",
        "reserve3",
        "reserve4",
        "change_day",
        "abolition_day",
        "prolonged_anesthesia_control_add",
        "cancer_pathological_specimen_add",
        "reserve5",
        "reserve6",
        "reserve7",
        "publication_order_number",
    )
    resource_class = resouces.TableBasicResource


class TableGeneralRuleAddItemAddAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "group_number",
        "general_rule_add_item_add_code",
        "general_rule_add_item_dental_practice_code",
        "general_rule_add_item_practice_bassic_name",
        "general_rule_add_item_add_identification",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableGeneralRuleAddItemAddResource


class TableBasicAddItemAddAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "group_number",
        "basic_add_item_add_code",
        "basic_add_item_dental_practice_code",
        "basic_add_item_practice_bassic_name",
        "basic_add_item_add_identification",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableBasicAddItemAddResource


class TableAnnotationAddItemAddAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "group_number",
        "annotation_add_item_add_code",
        "annotation_add_item_dental_practice_code",
        "annotation_add_item_practice_bassic_name",
        "annotation_add_item_add_identification",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableAnnotationAddItemAddResource


class TableTechMaterialsAddItemAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "group_number",
        "tech_materials_add_item_add_code",
        "tech_materials_add_item_dental_practice_code",
        "tech_materials_add_item_practice_bassic_name",
        "tech_materials_add_item_add_identification",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableTechMaterialsAddItemResource


class TableCalculationLimitAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "calculation_unit",
        "calculation_limit",
        "upper_limit_error_process",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableCalculationLimitResource


class TableEtchAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "score_etc_identification",
        "score",
        "etch_score",
        "etch_lower_limit",
        "etch_upper_limit",
        "etch_value",
        "etch_score",
        "etch_limits_error_process",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableEtchResource


class TableAgeLimitAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "lower_age",
        "upper_age",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableAgeLimitResource


class TableFixCalculationContradictionAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "contradiction1_calculability",
        "contradiction1_dental_practice_code",
        "contradiction1_bulletin_number_type",
        "contradiction1_bulletin_number_type_number",
        "contradiction1_bulletin_number_branch_number",
        "contradiction1_bulletin_number_item_number",
        "contradiction1_add_code",
        "contradiction1_practice_bassic_name",
        "contradiction1_practice_abbreviation_name",
        "contradiction2_calculability",
        "contradiction2_dental_practice_code",
        "contradiction2_bulletin_number_type",
        "contradiction2_bulletin_number_type_number",
        "contradiction2_bulletin_number_branch_number",
        "contradiction2_bulletin_number_item_number",
        "contradiction2_add_code",
        "contradiction2_practice_bassic_name",
        "contradiction2_practice_abbreviation_name",
        "contradiction3_calculability",
        "contradiction3_dental_practice_code",
        "contradiction3_bulletin_number_type",
        "contradiction3_bulletin_number_type_number",
        "contradiction3_bulletin_number_branch_number",
        "contradiction3_bulletin_number_item_number",
        "contradiction3_add_code",
        "contradiction3_practice_bassic_name",
        "contradiction3_practice_abbreviation_name",
        "contradiction4_calculability",
        "contradiction4_dental_practice_code",
        "contradiction4_bulletin_number_type",
        "contradiction4_bulletin_number_type_number",
        "contradiction4_bulletin_number_branch_number",
        "contradiction4_bulletin_number_item_number",
        "contradiction4_add_code",
        "contradiction4_practice_bassic_name",
        "contradiction4_practice_abbreviation_name",
        "contradiction5_calculability",
        "contradiction5_dental_practice_code",
        "contradiction5_bulletin_number_type",
        "contradiction5_bulletin_number_type_number",
        "contradiction5_bulletin_number_branch_number",
        "contradiction5_bulletin_number_item_number",
        "contradiction5_add_code",
        "contradiction5_practice_bassic_name",
        "contradiction5_practice_abbreviation_name",
        "contradiction6_calculability",
        "contradiction6_dental_practice_code",
        "contradiction6_bulletin_number_type",
        "contradiction6_bulletin_number_type_number",
        "contradiction6_bulletin_number_branch_number",
        "contradiction6_bulletin_number_item_number",
        "contradiction6_add_code",
        "contradiction6_practice_bassic_name",
        "contradiction6_practice_abbreviation_name",
        "contradiction7_calculability",
        "contradiction7_dental_practice_code",
        "contradiction7_bulletin_number_type",
        "contradiction7_bulletin_number_type_number",
        "contradiction7_bulletin_number_branch_number",
        "contradiction7_bulletin_number_item_number",
        "contradiction7_add_code",
        "contradiction7_practice_bassic_name",
        "contradiction7_practice_abbreviation_name",
        "contradiction8_calculability",
        "contradiction8_dental_practice_code",
        "contradiction8_bulletin_number_type",
        "contradiction8_bulletin_number_type_number",
        "contradiction8_bulletin_number_branch_number",
        "contradiction8_bulletin_number_item_number",
        "contradiction8_add_code",
        "contradiction8_practice_bassic_name",
        "contradiction8_practice_abbreviation_name",
        "contradiction9_calculability",
        "contradiction9_dental_practice_code",
        "contradiction9_bulletin_number_type",
        "contradiction9_bulletin_number_type_number",
        "contradiction9_bulletin_number_branch_number",
        "contradiction9_bulletin_number_item_number",
        "contradiction9_add_code",
        "contradiction9_practice_bassic_name",
        "contradiction9_practice_abbreviation_name",
        "contradiction10_calculability",
        "contradiction10_dental_practice_code",
        "contradiction10_bulletin_number_type",
        "contradiction10_bulletin_number_type_number",
        "contradiction10_bulletin_number_branch_number",
        "contradiction10_bulletin_number_item_number",
        "contradiction10_add_code",
        "contradiction10_practice_bassic_name",
        "contradiction10_practice_abbreviation_name",
        "change_date",
        "abolition_date",
        "reserve1",
        "reserve2",
        "reserve3",
    )
    resource_class = resouces.TableFixCalculationContradictionResource


class TableRealDayAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "dental_practice_code",
        "bulletin_number_type",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "add_code",
        "practice_bassic_name",
        "practice_abbreviation_name",
        "real_day",
        "days_or_times",
        "change_day",
        "abolition_day",
        "reserve",
    )
    resource_class = resouces.TableRealDayResource


class MasterDiseaseAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "disease_name_code",
        "destination_code",
        "disease_bassic_name_digits",
        "disease_bassic_name",
        "disease_abbreviation_name_digits",
        "disease_abbreviation_name",
        "disease_cana_name_digits",
        "disease_cana_name",
        "disease_control_number",
        "adoption_type",
        "disease_name_exchange_code",
        "ICD_10_1",
        "ICD_10_2",
        "ICD_10_1_2013",
        "ICD_10_2_2013",
        "reserve1",
        "single_use_ban_type",
        "no_insurance_claim_type",
        "special_disease_target_type",
        "listing_day",
        "change_day",
        "abolition_day",
        "disease_bassic_name_change_info",
        "disease_abbreviation_name_change_info",
        "disease_cana_name_change_info",
        "adoption_type_change_info",
        "disease_name_exchange_code_change_info",
        "ICD_10_1_change_info",
        "ICD_10_2_change_info",
        "dental_disease_abbreviation_name_change_info",
        "intractable_disease_out_target_type_change_info",
        "dental_special_disease_target_type_change_info",
        "single_use_ban_type_change_info",
        "no_insurance_claim_type_change_info",
        "special_disease_target_type_change_info",
        "destination_disease_control_number",
        "dental_disease_abbreviation_name",
        "reserve2",
        "reserve3",
        "dental_disease_abbreviation_name_digits",
        "intractable_disease_out_target_type",
        "dental_special_disease_target_type",
        "ICD_10_1_2013_change_info",
        "ICD_10_2_2013_change_info",
    )
    resource_class = resouces.MasterDiseaseResource


class MasterModifierAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "modifier_code",
        "reserve1",
        "reserve2",
        "modifier_name_digits",
        "modifier_name",
        "reserve3",
        "modifier_cana_name_digits",
        "modifier_cana_name",
        "reserve4",
        "modifier_name_change_info",
        "modifier_cana_name_change_info",
        "listing_day",
        "change_day",
        "abolition_day",
        "modifier_control_number",
        "modifier_exchange_code",
        "modifier_type",
    )
    resource_class = resouces.MasterModifierResource


class MasterDentalAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "dentation_code",
        "reserve1",
        "dentation_name",
        "change_day",
        "abolition_day",
    )
    resource_class = resouces.MasterDentalResource


class MasterDrugAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "drug_code",
        "drug_kanji_significant_digits",
        "drug_kanji_name",
        "drug_cana_significant_digits",
        "drug_cana_name",
        "unit_code",
        "unit_kanji_significant_digits",
        "unit_kanji_name",
        "new_cash_amount_type",
        "new_cash_new_cash",
        "reserve1",
        "special_drug",
        "neuroleptic",
        "biologics",
        "generic",
        "reserve2",
        "dental_special_drug",
        "contrast_drug",
        "Injection_volume",
        "listing_method_identification",
        "product_name_etc",
        "old_cash_amount_type",
        "old_cash_old_cash",
        "kanji_name_change_type",
        "cana_name_change_type",
        "dosage_form",
        "reserve3",
        "change_day",
        "abolition_day",
        "drug_price_bassic_listing_code",
        "publication_order_number",
        "expiry_day",
        "bassic_kanji_name",
    )
    resource_class = resouces.MasterDrugResource


class MasterSpecialEquipmentAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "special_equipment_code",
        "special_equipment_significant_digits",
        "special_equipment_kanji_name",
        "special_equipment_cana_significant_digits",
        "special_equipment_cana_name",
        "unit_code",
        "unit_kanji_significant_digits",
        "unit_kanji_name",
        "new_cash_amount_type",
        "new_cash_new_cash",
        "reserve1",
        "age_add_type",
        "age_limit_lower_limit",
        "age_limit_upper_limit",
        "old_cash_amount_type",
        "old_cash_old_cash",
        "kanji_name_change_type",
        "cana_name_change_type",
        "oxygen_type",
        "special_equipment_type",
        "upper_limit_price",
        "lower_limit_price",
        "reserve2",
        "publication_order_number",
        "abolition_new_etc",
        "change_day",
        "expiry_day",
        "abolition_day",
        "bulletin_number_other_table_number",
        "bulletin_number_type_number",
        "dpc_type",
        "reserve3",
        "reserve4",
        "reserve5",
        "bassic_kanji_name",
    )
    resource_class = resouces.MasterSpecialEquipmentResource


class MasterCommentAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "type",
        "pattern",
        "serial_number",
        "comment_kanji_significant_digits",
        "comment_kanji_name",
        "comment_cana_significant_digits",
        "comment_cana_name",
        "receipt_edit_info_column1",
        "receipt_edit_info_digits1",
        "receipt_edit_info_column2",
        "receipt_edit_info_digits2",
        "receipt_edit_info_column3",
        "receipt_edit_info_digits3",
        "receipt_edit_info_column4",
        "receipt_edit_info_digits4",
        "reserve1",
        "reserve2",
        "choice_comment_identification",
        "change_day",
        "abolition_day",
        "commnet_code",
        "publication_order_number",
        "reserve3",
        "reserve4",
        "reserve5",
        "reserve6",
        "reserve7",
        "reserve8",
    )
    resource_class = resouces.MasterCommentResource


class MasterPracticeAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "practice_code",
        "practice_abbreviation_name_kanji_significant_digits",
        "practice_abbreviation_name_kanji_name",
        "practice_abbreviation_name_cana_significant_digits",
        "practice_abbreviation_name_cana_name",
        "data_code",
        "data_kanji_significant_digits",
        "data_kanji_name",
        "new_score_etc_identification",
        "new_score_etc",
        "in_out_code",
        "late_elderly_medical_code",
        "score_destination_identification_out",
        "comprehensive_inspection",
        "reserve1",
        "dpc_type",
        "hospital_type",
        "surgery_support_addition_type",
        "medical_observation_type",
        "nursing_addition",
        "anesthesia_identification_type",
        "reserve2",
        "disease_name_related_type",
        "reserve3",
        "real_day",
        "days_or_times",
        "drug_name_code",
        "etch_value_calculation_identification",
        "etch_lower_limit",
        "etch_upper_limit",
        "etch_value",
        "etch_value_score",
        "etch_limits_error_process",
        "upper_limit",
        "upper_limit_error_process",
        "annotation_add_item_add_code",
        "annotation_add_item_add_number",
        "general_rule_age",
        "etch_limits_lower_limit",
        "etch_limits_upper_limit",
        "time_addition_type",
        "base_conformance_code",
        "base_conformance_facility_standard",
        "treatment_infant_addition_type",
        "very_low_birth_weight_infant_addition_type",
        "basic_hospital_fee_deduction_identification",
        "donors_class_type",
        "judgment_class_inspections_type",
        "judgment_class_inspections_group_type",
        "diminution_code",
        "spinal_cord_evoked_potential_measurement_add_type",
        "neck_dissection_combined_addition_type",
        "auto_suturer_add_type",
        "out_management_add_type",
        "old_score_etc_identification",
        "old_score_etc",
        "kanji_name_change_type",
        "cana_name_change_type",
        "speciment_test_comment",
        "general_rule_add_score_type",
        "comprehensive_code",
        "ultrasonic_endoscope_add_type",
        "reserve4",
        "score_destination_identification_in",
        "auto_anastomosis_add_type",
        "bulletin_identification_type1",
        "bulletin_identification_type2",
        "area_add",
        "beds_type",
        "facility_standard_code1",
        "facility_standard_code2",
        "facility_standard_code3",
        "facility_standard_code4",
        "facility_standard_code5",
        "facility_standard_code6",
        "facility_standard_code7",
        "facility_standard_code8",
        "facility_standard_code9",
        "facility_standard_code10",
        "ultrasonic_coagulator_type",
        "short_stay_surgery",
        "dental_type",
        "code_table_number_alphabet",
        "bulletin_number_alphabet",
        "change_day",
        "abolition_day",
        "publication_order_number",
        "code_table_number_chapter",
        "code_table_number_department",
        "code_table_number_type_number",
        "code_table_number_branch_number",
        "code_table_number_item_number",
        "bulletin_number_chapter",
        "bulletin_number_department",
        "bulletin_number_type_number",
        "bulletin_number_branch_number",
        "bulletin_number_item_number",
        "age_add1_lower_age",
        "age_add1_upper_age",
        "age_add1_annotation_add_item_practice_code",
        "age_add2_lower_age",
        "age_add2_upper_age",
        "age_add2_annotation_add_item_practice_code",
        "age_add3_lower_age",
        "age_add3_upper_age",
        "age_add3_annotation_add_item_practice_code",
        "age_add4_lower_age",
        "age_add4_upper_age",
        "age_add4_annotation_add_item_practice_code",
        "transfer_related",
        "basic_kanji_name",
        "sinus_surgery_endoscope_addition",
        "sinus_surgery_tissue_resection_equipment_addition",
        "long_term_anesthesia_management_addition",
        "score_type_number",
        "monitoring_addition",
        "cryopreserved_allogeneic_tissue_addition",
        "malignant_tumor_histopathological_sample_addition",
        "external_fixator_addition",
        "ultrasonic_cutting_equipment_addition",
        "left_atrial_appendage_closure_surgery_addition",
        "improve_countermeasures_against_foreign_infections_additions",
        "otolaryngology_infant_treatment_addition",
        "otolaryngology_infant_treatment_drug_support_addition",
        "incision_local_negative_treatment_device_addition",
        "reserve5",
        "reserve6",
        "reserve7",
        "reserve8",
        "reserve9",
        "reserve10",
        "reserve11",
        "reserve12",
        "reserve13",
        "reserve14",
        "reserve15",
        "reserve16",
        "reserve17",
        "reserve18",
        "reserve19",
        "reserve20",
        "reserve21",
        "reserve22",
        "reserve23",
        "reserve24",
        "reserve25",
        "reserve26",
        "reserve27",
    )
    resource_class = resouces.MasterPracticeResource


class MasterDispensingAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "change_type",
        "master_type",
        "dispensing_code",
        "dispensing_kanji_significant_digits",
        "dispensing_kanji_name",
        "dispensing_cana_significant_digits",
        "dispensing_cana_name",
        "receipt_mark_code",
        "receipt_display_order_code",
        "new_score_etc_identification",
        "dispensing_quantity_calculation_flag",
        "score_calculation_new_score",
        "score_calculation_etch_value_identification",
        "score_calculation_lower_limit",
        "score_calculation_upper_limit",
        "score_calculation_etch_value",
        "score_calculation_etch_score",
        "score_calculation_limits_error_process",
        "subtraction_act_type",
        "subtraction_subject_act_type",
        "dispensing_identification_type",
        "comprehensive_identification_code",
        "reserve1",
        "reserve2",
        "reserve3",
        "reserve4",
        "reserve5",
        "dispensing_type1",
        "dispensing_type2",
        "late_elderly_code",
        "facility_standard_code1",
        "facility_standard_code2",
        "facility_standard_code3",
        "facility_standard_code4",
        "facility_standard_code5",
        "facility_standard_code6",
        "facility_standard_code7",
        "facility_standard_code8",
        "facility_standard_code9",
        "facility_standard_code10",
        "receipt_unit_contradiction_type_code",
        "prescription_reception_unit_contradictory_type_code",
        "dispensing_unit_contraction_type_code",
        "special_drug",
        "time_add_code",
        "dosage_form",
        "receipt_unit_upper_limit",
        "receipt_unit_upper_limit_error_proces",
        "receipt_unit_lower_limit",
        "receipt_unit_lower_limit_error_proces",
        "annotation_add_code",
        "annotation_add_number",
        "limits_age_lower_age",
        "limits_age_upper_age",
        "pharmaceutical_management_fee_type",
        "bulletin_identification_type1",
        "bulletin_identification_type2",
        "old_score_etc_identification",
        "old_score_etc",
        "change_day",
        "abolition_day",
        "publication_order_number",
        "code_table_number",
        "bulletin_number",
        "transfer_related",
    )
    resource_class = resouces.MasterDispensingResource


class RecordReceiptInfoAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "examination_pay_institution",
        "prefectures",
        "score_sheet",
        "medical_institution_code",
        "reserve",
        "medical_institution_name",
        "billing_day",
        "notification",
        "multivolume_identifier_info",
    )
    resource_class = resouces.RecordReceiptInfoResource


class RecordMedicalInstitutionInfoAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "examination_pay_institution",
        "prefectures",
        "score_sheet",
        "medical_institution_code",
        "reserve",
        "billing_day",
        "phone_number",
        "notification",
    )
    resource_class = resouces.RecordMedicalInstitutionInfoResource


class RecordReceiptCommonAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "receipt_number",
        "receipt_identification",
        "practice_day",
        "name",
        "sex_type",
        "birth_day",
        "benefit_ratio",
        "admission_day",
        "practice_start_day",
        "return_origin_yupe",
        "hospital_ward_type",
        "copayment",
        "receipt_special_remarks",
        "reserve1",
        "chart_number",
        "billing_info1",
        "reserve2",
        "future_hospital_billing",
        "search_number",
        "reserve3",
        "billing_info2",
        "reserve4",
        "reserve5",
        "reserve6",
        "cana_name",
        "patient_condition",
    )
    resource_class = resouces.RecordReceiptCommonResource


class RecordInsurerAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "insurer_number",
        "insurer_card_code",
        "insurer_card_number",
        "practice_acrual_days",
        "total_score",
        "dietary_lifestyle_care_times",
        "dietary_lifestyle_care_total_amount",
        "professional_reasons",
        "certificate_number",
        "insurance_copayments",
        "exempt_type",
        "reduction_ratio",
        "reduction_amount",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordInsurerResource


class RecordPublicExpenseAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "payer_number",
        "recipient_number",
        "optional_benefit_type",
        "practice_acrual_days",
        "total_score",
        "copayment",
        "public_expense_benefit_copayment",
        "dietary_lifestyle_care_times",
        "dietary_lifestyle_care_total_amount",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordPublicExpenseResource


class RecordStatusCheckAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "payer_class",
        "confirmation_type",
        "insurer_number_etc",
        "insurer_card_code_status_check",
        "insurer_card_number_status_check",
        "branch_number",
        "recipient_id",
        "reserve",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordStatusCheckResource


class RecordReceiptDayAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "payer_type",
        "info1",
        "info2",
        "info3",
        "info4",
        "info5",
        "info6",
        "info7",
        "info8",
        "info9",
        "info10",
        "info11",
        "info12",
        "info13",
        "info14",
        "info15",
        "info16",
        "info17",
        "info18",
        "info19",
        "info20",
        "info21",
        "info22",
        "info23",
        "info24",
        "info25",
        "info26",
        "info27",
        "info28",
        "info29",
        "info30",
        "info31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordReceiptDayResource


class RecordCounterAmountAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "counter_amount_type",
        "reserve1",
        "reserve2",
        "reserve3",
        "reserve4",
        "reserve5",
        "reserve6",
        "reserve7",
        "reserve8",
        "reserve9",
        "reserve10",
        "reserve11",
        "reserve12",
        "reserve13",
        "reserve14",
        "reserve15",
        "reserve16",
        "reserve17",
        "reserve18",
        "reserve19",
        "reserve20",
        "reserve21",
        "reserve22",
        "reserve23",
        "reserve24",
        "reserve25",
        "reserve26",
        "reserve27",
        "reserve28",
        "reserve29",
        "reserve30",
        "reserve31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordCounterAmountResource


class RecordDiseasePositionAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "start_practice",
        "transcription_type",
        "dentation_code_diseaase",
        "disease_name_code",
        "modifier_code",
        "disease_name",
        "comorbidities_number",
        "disease_condition_transition",
        "major_disease",
        "comment_code",
        "supplementary_comment",
        "dentation_code_comment",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordDiseasePositionResource


class RecordDentalPracticeAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "practice_identification",
        "payer_type",
        "practice_code",
        "practice_volume_data1",
        "practice_volume_data2",
        "add_code1",
        "add_volume_data1",
        "add_code2",
        "add_volume_data2",
        "add_code3",
        "add_volume_data3",
        "add_code4",
        "add_volume_data4",
        "add_code5",
        "add_volume_data5",
        "add_code6",
        "add_volume_data6",
        "add_code7",
        "add_volume_data7",
        "add_code8",
        "add_volume_data8",
        "add_code9",
        "add_volume_data9",
        "add_code10",
        "add_volume_data10",
        "add_code11",
        "add_volume_data11",
        "add_code12",
        "add_volume_data12",
        "add_code13",
        "add_volume_data13",
        "add_code14",
        "add_volume_data14",
        "add_code15",
        "add_volume_data15",
        "add_code16",
        "add_volume_data16",
        "add_code17",
        "add_volume_data17",
        "add_code18",
        "add_volume_data18",
        "add_code19",
        "add_volume_data19",
        "add_code20",
        "add_volume_data20",
        "add_code21",
        "add_volume_data21",
        "add_code22",
        "add_volume_data22",
        "add_code23",
        "add_volume_data23",
        "add_code24",
        "add_volume_data24",
        "add_code25",
        "add_volume_data25",
        "add_code26",
        "add_volume_data26",
        "add_code27",
        "add_volume_data27",
        "add_code28",
        "add_volume_data28",
        "add_code29",
        "add_volume_data29",
        "add_code30",
        "add_volume_data30",
        "add_code31",
        "add_volume_data31",
        "add_code32",
        "add_volume_data32",
        "add_code33",
        "add_volume_data33",
        "add_code34",
        "add_volume_data34",
        "add_code35",
        "add_volume_data35",
        "score",
        "count",
        "calculation_day_info1",
        "calculation_day_info2",
        "calculation_day_info3",
        "calculation_day_info4",
        "calculation_day_info5",
        "calculation_day_info6",
        "calculation_day_info7",
        "calculation_day_info8",
        "calculation_day_info9",
        "calculation_day_info10",
        "calculation_day_info11",
        "calculation_day_info12",
        "calculation_day_info13",
        "calculation_day_info14",
        "calculation_day_info15",
        "calculation_day_info16",
        "calculation_day_info17",
        "calculation_day_info18",
        "calculation_day_info19",
        "calculation_day_info20",
        "calculation_day_info21",
        "calculation_day_info22",
        "calculation_day_info23",
        "calculation_day_info24",
        "calculation_day_info25",
        "calculation_day_info26",
        "calculation_day_info27",
        "calculation_day_info28",
        "calculation_day_info29",
        "calculation_day_info30",
        "calculation_day_info31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordDentalPracticeResource


class RecordPracticeAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "practice_identification",
        "payer_type",
        "practice_code",
        "volume_data",
        "score",
        "count",
        "calculation_day_info1",
        "calculation_day_info2",
        "calculation_day_info3",
        "calculation_day_info4",
        "calculation_day_info5",
        "calculation_day_info6",
        "calculation_day_info7",
        "calculation_day_info8",
        "calculation_day_info9",
        "calculation_day_info10",
        "calculation_day_info11",
        "calculation_day_info12",
        "calculation_day_info13",
        "calculation_day_info14",
        "calculation_day_info15",
        "calculation_day_info16",
        "calculation_day_info17",
        "calculation_day_info18",
        "calculation_day_info19",
        "calculation_day_info20",
        "calculation_day_info21",
        "calculation_day_info22",
        "calculation_day_info23",
        "calculation_day_info24",
        "calculation_day_info25",
        "calculation_day_info26",
        "calculation_day_info27",
        "calculation_day_info28",
        "calculation_day_info29",
        "calculation_day_info30",
        "calculation_day_info31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordPracticeResource


class RecordDrugAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "practice_identification",
        "payer_type",
        "drug_code",
        "usage",
        "score",
        "count",
        "drug_type",
        "calculation_day_info1",
        "calculation_day_info2",
        "calculation_day_info3",
        "calculation_day_info4",
        "calculation_day_info5",
        "calculation_day_info6",
        "calculation_day_info7",
        "calculation_day_info8",
        "calculation_day_info9",
        "calculation_day_info10",
        "calculation_day_info11",
        "calculation_day_info12",
        "calculation_day_info13",
        "calculation_day_info14",
        "calculation_day_info15",
        "calculation_day_info16",
        "calculation_day_info17",
        "calculation_day_info18",
        "calculation_day_info19",
        "calculation_day_info20",
        "calculation_day_info21",
        "calculation_day_info22",
        "calculation_day_info23",
        "calculation_day_info24",
        "calculation_day_info25",
        "calculation_day_info26",
        "calculation_day_info27",
        "calculation_day_info28",
        "calculation_day_info29",
        "calculation_day_info30",
        "calculation_day_info31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordDrugResource


class RecordSpecialEquipmentAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "practice_identification",
        "payer_type",
        "special_equipment_code",
        "usage",
        "unit_code",
        "unit_cost",
        "special_equipment_add_code1",
        "special_equipment_add_volume_data1",
        "special_equipment_add_code2",
        "special_equipment_add_volume_data2",
        "standard_or_size",
        "score",
        "count",
        "calculation_day_info1",
        "calculation_day_info2",
        "calculation_day_info3",
        "calculation_day_info4",
        "calculation_day_info5",
        "calculation_day_info6",
        "calculation_day_info7",
        "calculation_day_info8",
        "calculation_day_info9",
        "calculation_day_info10",
        "calculation_day_info11",
        "calculation_day_info12",
        "calculation_day_info13",
        "calculation_day_info14",
        "calculation_day_info15",
        "calculation_day_info16",
        "calculation_day_info17",
        "calculation_day_info18",
        "calculation_day_info19",
        "calculation_day_info20",
        "calculation_day_info21",
        "calculation_day_info22",
        "calculation_day_info23",
        "calculation_day_info24",
        "calculation_day_info25",
        "calculation_day_info26",
        "calculation_day_info27",
        "calculation_day_info28",
        "calculation_day_info29",
        "calculation_day_info30",
        "calculation_day_info31",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordSpecialEquipmentResource


class RecordCommentAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "practice_identification",
        "payer_type",
        "comment_code",
        "character_data",
        "dentation_comment",
        "reserve1",
        "reserve2",
        "reserve3",
        "reserve4",
        "reserve5",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordCommentResource


class RecordDetailSymptomsAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "detail_symptoms_type",
        "detail_symptoms_data",
        "practice_day",
        "name",
    )
    resource_class = resouces.RecordDetailSymptomsResource


class RecordMedicalFeeClaimAdmin(ImportExportModelAdmin):
    from_encoding= "utf-8-sig"
    ordering = ["id"]
    list_display = (
        "record_identification_info",
        "total_cases",
        "total_score",
        "multivolume_identification_info",
        "practice_day",
    )
    resource_class = resouces.RecordMedicalFeeClaimResource


admin.site.register(models.TableBasic,TableBasicAdmin)
admin.site.register(models.TableGeneralRuleAddItemAdd,TableGeneralRuleAddItemAddAdmin)
admin.site.register(models.TableBasicAddItemAdd,TableBasicAddItemAddAdmin)
admin.site.register(models.TableAnnotationAddItemAdd,TableAnnotationAddItemAddAdmin)
admin.site.register(models.TableTechMaterialsAddItem,TableTechMaterialsAddItemAdmin)
admin.site.register(models.TableCalculationLimit,TableCalculationLimitAdmin)
admin.site.register(models.TableEtch,TableEtchAdmin)
admin.site.register(models.TableAgeLimit,TableAgeLimitAdmin)
admin.site.register(models.TableFixCalculationContradiction,TableFixCalculationContradictionAdmin)
admin.site.register(models.TableRealDay,TableRealDayAdmin)
admin.site.register(models.MasterDisease,MasterDiseaseAdmin)
admin.site.register(models.MasterModifier,MasterModifierAdmin)
admin.site.register(models.MasterDental,MasterDentalAdmin)
admin.site.register(models.MasterDrug,MasterDrugAdmin)
admin.site.register(models.MasterSpecialEquipment,MasterSpecialEquipmentAdmin)
admin.site.register(models.MasterComment,MasterCommentAdmin)
admin.site.register(models.MasterPractice,MasterPracticeAdmin)
admin.site.register(models.MasterDispensing,MasterDispensingAdmin)
admin.site.register(models.RecordReceiptInfo,RecordReceiptInfoAdmin)
admin.site.register(models.RecordMedicalInstitutionInfo,RecordMedicalInstitutionInfoAdmin)
admin.site.register(models.RecordReceiptCommon,RecordReceiptCommonAdmin)
admin.site.register(models.RecordInsurer,RecordInsurerAdmin)
admin.site.register(models.RecordPublicExpense,RecordPublicExpenseAdmin)
admin.site.register(models.RecordStatusCheck,RecordStatusCheckAdmin)
admin.site.register(models.RecordReceiptDay,RecordReceiptDayAdmin)
admin.site.register(models.RecordCounterAmount,RecordCounterAmountAdmin)
admin.site.register(models.RecordDiseasePosition,RecordDiseasePositionAdmin)
admin.site.register(models.RecordDentalPractice,RecordDentalPracticeAdmin)
admin.site.register(models.RecordPractice,RecordPracticeAdmin)
admin.site.register(models.RecordDrug,RecordDrugAdmin)
admin.site.register(models.RecordSpecialEquipment,RecordSpecialEquipmentAdmin)
admin.site.register(models.RecordComment,RecordCommentAdmin)
admin.site.register(models.RecordDetailSymptoms,RecordDetailSymptomsAdmin)
admin.site.register(models.RecordMedicalFeeClaim,RecordMedicalFeeClaimAdmin)
admin.site.register(models.PracticeRecord)
admin.site.register(models.PreventDentalPractice)

