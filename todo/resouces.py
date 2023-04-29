from . import models
from import_export import resources 
from import_export.fields import Field 
from datetime import datetime as dt, date

class TableBasicResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    new_score_etc_identification = Field(attribute="new_score_etc_identification",column_name="new_score_etc_identification")
    new_score_etc = Field(attribute="new_score_etc",column_name="new_score_etc")
    old_score_etc_identification = Field(attribute="old_score_etc_identification",column_name="old_score_etc_identification")
    old_score_etc = Field(attribute="old_score_etc",column_name="old_score_etc")
    in_out_code = Field(attribute="in_out_code",column_name="in_out_code")
    late_elderly_medical_code = Field(attribute="late_elderly_medical_code",column_name="late_elderly_medical_code")
    time_add_code = Field(attribute="time_add_code",column_name="time_add_code")
    hospital_clinics_code = Field(attribute="hospital_clinics_code",column_name="hospital_clinics_code")
    nurse_add = Field(attribute="nurse_add",column_name="nurse_add")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    area_add = Field(attribute="area_add",column_name="area_add")
    injury_name_code = Field(attribute="injury_name_code",column_name="injury_name_code")
    drug_name_code = Field(attribute="drug_name_code",column_name="drug_name_code")
    number_of_bed_code = Field(attribute="number_of_bed_code",column_name="number_of_bed_code")
    notification = Field(attribute="notification",column_name="notification")
    future_hospital = Field(attribute="future_hospital",column_name="future_hospital")
    short_stay_surgery = Field(attribute="short_stay_surgery",column_name="short_stay_surgery")
    special_remarks = Field(attribute="special_remarks",column_name="special_remarks")
    Inspection_decision_code = Field(attribute="Inspection_decision_code",column_name="Inspection_decision_code")
    Inspection_decision_group_code = Field(attribute="Inspection_decision_group_code",column_name="Inspection_decision_group_code")
    diminution_code = Field(attribute="diminution_code",column_name="diminution_code")
    comprehensive_code = Field(attribute="comprehensive_code",column_name="comprehensive_code")
    base_conformance_code = Field(attribute="base_conformance_code",column_name="base_conformance_code")
    base_conformance_facility_standard = Field(attribute="base_conformance_facility_standard",column_name="base_conformance_facility_standard")
    facility_standard_code1 = Field(attribute="facility_standard_code1",column_name="facility_standard_code1")
    facility_standard_code2 = Field(attribute="facility_standard_code2",column_name="facility_standard_code2")
    facility_standard_code3 = Field(attribute="facility_standard_code3",column_name="facility_standard_code3")
    facility_standard_code4 = Field(attribute="facility_standard_code4",column_name="facility_standard_code4")
    facility_standard_code5 = Field(attribute="facility_standard_code5",column_name="facility_standard_code5")
    facility_standard_code6 = Field(attribute="facility_standard_code6",column_name="facility_standard_code6")
    facility_standard_code7 = Field(attribute="facility_standard_code7",column_name="facility_standard_code7")
    facility_standard_code8 = Field(attribute="facility_standard_code8",column_name="facility_standard_code8")
    facility_standard_code9 = Field(attribute="facility_standard_code9",column_name="facility_standard_code9")
    facility_standard_code10 = Field(attribute="facility_standard_code10",column_name="facility_standard_code10")
    general_rule_add_group = Field(attribute="general_rule_add_group",column_name="general_rule_add_group")
    basic_add_group = Field(attribute="basic_add_group",column_name="basic_add_group")
    annotation_add_group = Field(attribute="annotation_add_group",column_name="annotation_add_group")
    tech_materials_add_group = Field(attribute="tech_materials_add_group",column_name="tech_materials_add_group")
    calculation_limit_table_identification = Field(attribute="calculation_limit_table_identification",column_name="calculation_limit_table_identification")
    etch_table_identification = Field(attribute="etch_table_identification",column_name="etch_table_identification")
    age_limit_table_identification = Field(attribute="age_limit_table_identification",column_name="age_limit_table_identification")
    contradiction_table_identification = Field(attribute="contradiction_table_identification",column_name="contradiction_table_identification")
    days_table_identification = Field(attribute="days_table_identification",column_name="days_table_identification")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    prolonged_anesthesia_control_add = Field(attribute="prolonged_anesthesia_control_add",column_name="prolonged_anesthesia_control_add")
    cancer_pathological_specimen_add = Field(attribute="cancer_pathological_specimen_add",column_name="cancer_pathological_specimen_add")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    reserve6 = Field(attribute="reserve6",column_name="reserve6")
    reserve7 = Field(attribute="reserve7",column_name="reserve7")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    class Meta:
        model = models.TableBasic
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["new_score_etc_identification"] == "":
            row["new_score_etc_identification"]= None

        if row["new_score_etc"] == "":
            row["new_score_etc"]= None

        if row["old_score_etc_identification"] == "":
            row["old_score_etc_identification"]= None

        if row["old_score_etc"] == "":
            row["old_score_etc"]= None

        if row["in_out_code"] == "":
            row["in_out_code"]= None

        if row["late_elderly_medical_code"] == "":
            row["late_elderly_medical_code"]= None

        if row["time_add_code"] == "":
            row["time_add_code"]= None

        if row["hospital_clinics_code"] == "":
            row["hospital_clinics_code"]= None

        if row["nurse_add"] == "":
            row["nurse_add"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["area_add"] == "":
            row["area_add"]= None

        if row["injury_name_code"] == "":
            row["injury_name_code"]= None

        if row["drug_name_code"] == "":
            row["drug_name_code"]= None

        if row["number_of_bed_code"] == "":
            row["number_of_bed_code"]= None

        if row["notification"] == "":
            row["notification"]= None

        if row["future_hospital"] == "":
            row["future_hospital"]= None

        if row["short_stay_surgery"] == "":
            row["short_stay_surgery"]= None

        if row["special_remarks"] == "":
            row["special_remarks"]= None

        if row["Inspection_decision_code"] == "":
            row["Inspection_decision_code"]= None

        if row["Inspection_decision_group_code"] == "":
            row["Inspection_decision_group_code"]= None

        if row["diminution_code"] == "":
            row["diminution_code"]= None

        if row["comprehensive_code"] == "":
            row["comprehensive_code"]= None

        if row["base_conformance_code"] == "":
            row["base_conformance_code"]= None

        if row["base_conformance_facility_standard"] == "":
            row["base_conformance_facility_standard"]= None

        if row["facility_standard_code1"] == "":
            row["facility_standard_code1"]= None

        if row["facility_standard_code2"] == "":
            row["facility_standard_code2"]= None

        if row["facility_standard_code3"] == "":
            row["facility_standard_code3"]= None

        if row["facility_standard_code4"] == "":
            row["facility_standard_code4"]= None

        if row["facility_standard_code5"] == "":
            row["facility_standard_code5"]= None

        if row["facility_standard_code6"] == "":
            row["facility_standard_code6"]= None

        if row["facility_standard_code7"] == "":
            row["facility_standard_code7"]= None

        if row["facility_standard_code8"] == "":
            row["facility_standard_code8"]= None

        if row["facility_standard_code9"] == "":
            row["facility_standard_code9"]= None

        if row["facility_standard_code10"] == "":
            row["facility_standard_code10"]= None

        if row["calculation_limit_table_identification"] == "":
            row["calculation_limit_table_identification"]= None

        if row["etch_table_identification"] == "":
            row["etch_table_identification"]= None

        if row["age_limit_table_identification"] == "":
            row["age_limit_table_identification"]= None

        if row["contradiction_table_identification"] == "":
            row["contradiction_table_identification"]= None

        if row["days_table_identification"] == "":
            row["days_table_identification"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["reserve6"] == "":
            row["reserve6"]= None

        if row["reserve7"] == "":
            row["reserve7"]= None

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

class TableGeneralRuleAddItemAddResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    group_number = Field(attribute="group_number",column_name="group_number")
    general_rule_add_item_add_code = Field(attribute="general_rule_add_item_add_code",column_name="general_rule_add_item_add_code")
    general_rule_add_item_dental_practice_code = Field(attribute="general_rule_add_item_dental_practice_code",column_name="general_rule_add_item_dental_practice_code")
    general_rule_add_item_practice_bassic_name = Field(attribute="general_rule_add_item_practice_bassic_name",column_name="general_rule_add_item_practice_bassic_name")
    general_rule_add_item_add_identification = Field(attribute="general_rule_add_item_add_identification",column_name="general_rule_add_item_add_identification")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableGeneralRuleAddItemAdd
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["general_rule_add_item_dental_practice_code"] == "":
            row["general_rule_add_item_dental_practice_code"]= None

        if row["general_rule_add_item_add_identification"] == "":
            row["general_rule_add_item_add_identification"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableBasicAddItemAddResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    group_number = Field(attribute="group_number",column_name="group_number")
    basic_add_item_add_code = Field(attribute="basic_add_item_add_code",column_name="basic_add_item_add_code")
    basic_add_item_dental_practice_code = Field(attribute="basic_add_item_dental_practice_code",column_name="basic_add_item_dental_practice_code")
    basic_add_item_practice_bassic_name = Field(attribute="basic_add_item_practice_bassic_name",column_name="basic_add_item_practice_bassic_name")
    basic_add_item_add_identification = Field(attribute="basic_add_item_add_identification",column_name="basic_add_item_add_identification")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableBasicAddItemAdd
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["basic_add_item_dental_practice_code"] == "":
            row["basic_add_item_dental_practice_code"]= None

        if row["basic_add_item_add_identification"] == "":
            row["basic_add_item_add_identification"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableAnnotationAddItemAddResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    group_number = Field(attribute="group_number",column_name="group_number")
    annotation_add_item_add_code = Field(attribute="annotation_add_item_add_code",column_name="annotation_add_item_add_code")
    annotation_add_item_dental_practice_code = Field(attribute="annotation_add_item_dental_practice_code",column_name="annotation_add_item_dental_practice_code")
    annotation_add_item_practice_bassic_name = Field(attribute="annotation_add_item_practice_bassic_name",column_name="annotation_add_item_practice_bassic_name")
    annotation_add_item_add_identification = Field(attribute="annotation_add_item_add_identification",column_name="annotation_add_item_add_identification")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableAnnotationAddItemAdd
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["annotation_add_item_dental_practice_code"] == "":
            row["annotation_add_item_dental_practice_code"]= None

        if row["annotation_add_item_add_identification"] == "":
            row["annotation_add_item_add_identification"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableTechMaterialsAddItemResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    group_number = Field(attribute="group_number",column_name="group_number")
    tech_materials_add_item_add_code = Field(attribute="tech_materials_add_item_add_code",column_name="tech_materials_add_item_add_code")
    tech_materials_add_item_dental_practice_code = Field(attribute="tech_materials_add_item_dental_practice_code",column_name="tech_materials_add_item_dental_practice_code")
    tech_materials_add_item_practice_bassic_name = Field(attribute="tech_materials_add_item_practice_bassic_name",column_name="tech_materials_add_item_practice_bassic_name")
    tech_materials_add_item_add_identification = Field(attribute="tech_materials_add_item_add_identification",column_name="tech_materials_add_item_add_identification")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableTechMaterialsAddItem
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["tech_materials_add_item_dental_practice_code"] == "":
            row["tech_materials_add_item_dental_practice_code"]= None

        if row["tech_materials_add_item_add_identification"] == "":
            row["tech_materials_add_item_add_identification"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableCalculationLimitResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    calculation_unit = Field(attribute="calculation_unit",column_name="calculation_unit")
    calculation_limit = Field(attribute="calculation_limit",column_name="calculation_limit")
    upper_limit_error_process = Field(attribute="upper_limit_error_process",column_name="upper_limit_error_process")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableCalculationLimit
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["calculation_unit"] == "":
            row["calculation_unit"]= None

        if row["calculation_limit"] == "":
            row["calculation_limit"]= None

        if row["upper_limit_error_process"] == "":
            row["upper_limit_error_process"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableEtchResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    score_etc_identification = Field(attribute="score_etc_identification",column_name="score_etc_identification")
    score = Field(attribute="score",column_name="score")
    etch_score = Field(attribute="etch_score",column_name="etch_score")
    etch_lower_limit = Field(attribute="etch_lower_limit",column_name="etch_lower_limit")
    etch_upper_limit = Field(attribute="etch_upper_limit",column_name="etch_upper_limit")
    etch_value = Field(attribute="etch_value",column_name="etch_value")
    etch_score = Field(attribute="etch_score",column_name="etch_score")
    etch_limits_error_process = Field(attribute="etch_limits_error_process",column_name="etch_limits_error_process")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableEtch
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["score_etc_identification"] == "":
            row["score_etc_identification"]= None

        if row["score"] == "":
            row["score"]= None

        if row["etch_score"] == "":
            row["etch_score"]= None

        if row["etch_lower_limit"] == "":
            row["etch_lower_limit"]= None

        if row["etch_upper_limit"] == "":
            row["etch_upper_limit"]= None

        if row["etch_value"] == "":
            row["etch_value"]= None

        if row["etch_score"] == "":
            row["etch_score"]= None

        if row["etch_limits_error_process"] == "":
            row["etch_limits_error_process"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableAgeLimitResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    lower_age = Field(attribute="lower_age",column_name="lower_age")
    upper_age = Field(attribute="upper_age",column_name="upper_age")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableAgeLimit
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class TableFixCalculationContradictionResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    contradiction1_calculability = Field(attribute="contradiction1_calculability",column_name="contradiction1_calculability")
    contradiction1_dental_practice_code = Field(attribute="contradiction1_dental_practice_code",column_name="contradiction1_dental_practice_code")
    contradiction1_bulletin_number_type = Field(attribute="contradiction1_bulletin_number_type",column_name="contradiction1_bulletin_number_type")
    contradiction1_bulletin_number_type_number = Field(attribute="contradiction1_bulletin_number_type_number",column_name="contradiction1_bulletin_number_type_number")
    contradiction1_bulletin_number_branch_number = Field(attribute="contradiction1_bulletin_number_branch_number",column_name="contradiction1_bulletin_number_branch_number")
    contradiction1_bulletin_number_item_number = Field(attribute="contradiction1_bulletin_number_item_number",column_name="contradiction1_bulletin_number_item_number")
    contradiction1_add_code = Field(attribute="contradiction1_add_code",column_name="contradiction1_add_code")
    contradiction1_practice_bassic_name = Field(attribute="contradiction1_practice_bassic_name",column_name="contradiction1_practice_bassic_name")
    contradiction1_practice_abbreviation_name = Field(attribute="contradiction1_practice_abbreviation_name",column_name="contradiction1_practice_abbreviation_name")
    contradiction2_calculability = Field(attribute="contradiction2_calculability",column_name="contradiction2_calculability")
    contradiction2_dental_practice_code = Field(attribute="contradiction2_dental_practice_code",column_name="contradiction2_dental_practice_code")
    contradiction2_bulletin_number_type = Field(attribute="contradiction2_bulletin_number_type",column_name="contradiction2_bulletin_number_type")
    contradiction2_bulletin_number_type_number = Field(attribute="contradiction2_bulletin_number_type_number",column_name="contradiction2_bulletin_number_type_number")
    contradiction2_bulletin_number_branch_number = Field(attribute="contradiction2_bulletin_number_branch_number",column_name="contradiction2_bulletin_number_branch_number")
    contradiction2_bulletin_number_item_number = Field(attribute="contradiction2_bulletin_number_item_number",column_name="contradiction2_bulletin_number_item_number")
    contradiction2_add_code = Field(attribute="contradiction2_add_code",column_name="contradiction2_add_code")
    contradiction2_practice_bassic_name = Field(attribute="contradiction2_practice_bassic_name",column_name="contradiction2_practice_bassic_name")
    contradiction2_practice_abbreviation_name = Field(attribute="contradiction2_practice_abbreviation_name",column_name="contradiction2_practice_abbreviation_name")
    contradiction3_calculability = Field(attribute="contradiction3_calculability",column_name="contradiction3_calculability")
    contradiction3_dental_practice_code = Field(attribute="contradiction3_dental_practice_code",column_name="contradiction3_dental_practice_code")
    contradiction3_bulletin_number_type = Field(attribute="contradiction3_bulletin_number_type",column_name="contradiction3_bulletin_number_type")
    contradiction3_bulletin_number_type_number = Field(attribute="contradiction3_bulletin_number_type_number",column_name="contradiction3_bulletin_number_type_number")
    contradiction3_bulletin_number_branch_number = Field(attribute="contradiction3_bulletin_number_branch_number",column_name="contradiction3_bulletin_number_branch_number")
    contradiction3_bulletin_number_item_number = Field(attribute="contradiction3_bulletin_number_item_number",column_name="contradiction3_bulletin_number_item_number")
    contradiction3_add_code = Field(attribute="contradiction3_add_code",column_name="contradiction3_add_code")
    contradiction3_practice_bassic_name = Field(attribute="contradiction3_practice_bassic_name",column_name="contradiction3_practice_bassic_name")
    contradiction3_practice_abbreviation_name = Field(attribute="contradiction3_practice_abbreviation_name",column_name="contradiction3_practice_abbreviation_name")
    contradiction4_calculability = Field(attribute="contradiction4_calculability",column_name="contradiction4_calculability")
    contradiction4_dental_practice_code = Field(attribute="contradiction4_dental_practice_code",column_name="contradiction4_dental_practice_code")
    contradiction4_bulletin_number_type = Field(attribute="contradiction4_bulletin_number_type",column_name="contradiction4_bulletin_number_type")
    contradiction4_bulletin_number_type_number = Field(attribute="contradiction4_bulletin_number_type_number",column_name="contradiction4_bulletin_number_type_number")
    contradiction4_bulletin_number_branch_number = Field(attribute="contradiction4_bulletin_number_branch_number",column_name="contradiction4_bulletin_number_branch_number")
    contradiction4_bulletin_number_item_number = Field(attribute="contradiction4_bulletin_number_item_number",column_name="contradiction4_bulletin_number_item_number")
    contradiction4_add_code = Field(attribute="contradiction4_add_code",column_name="contradiction4_add_code")
    contradiction4_practice_bassic_name = Field(attribute="contradiction4_practice_bassic_name",column_name="contradiction4_practice_bassic_name")
    contradiction4_practice_abbreviation_name = Field(attribute="contradiction4_practice_abbreviation_name",column_name="contradiction4_practice_abbreviation_name")
    contradiction5_calculability = Field(attribute="contradiction5_calculability",column_name="contradiction5_calculability")
    contradiction5_dental_practice_code = Field(attribute="contradiction5_dental_practice_code",column_name="contradiction5_dental_practice_code")
    contradiction5_bulletin_number_type = Field(attribute="contradiction5_bulletin_number_type",column_name="contradiction5_bulletin_number_type")
    contradiction5_bulletin_number_type_number = Field(attribute="contradiction5_bulletin_number_type_number",column_name="contradiction5_bulletin_number_type_number")
    contradiction5_bulletin_number_branch_number = Field(attribute="contradiction5_bulletin_number_branch_number",column_name="contradiction5_bulletin_number_branch_number")
    contradiction5_bulletin_number_item_number = Field(attribute="contradiction5_bulletin_number_item_number",column_name="contradiction5_bulletin_number_item_number")
    contradiction5_add_code = Field(attribute="contradiction5_add_code",column_name="contradiction5_add_code")
    contradiction5_practice_bassic_name = Field(attribute="contradiction5_practice_bassic_name",column_name="contradiction5_practice_bassic_name")
    contradiction5_practice_abbreviation_name = Field(attribute="contradiction5_practice_abbreviation_name",column_name="contradiction5_practice_abbreviation_name")
    contradiction6_calculability = Field(attribute="contradiction6_calculability",column_name="contradiction6_calculability")
    contradiction6_dental_practice_code = Field(attribute="contradiction6_dental_practice_code",column_name="contradiction6_dental_practice_code")
    contradiction6_bulletin_number_type = Field(attribute="contradiction6_bulletin_number_type",column_name="contradiction6_bulletin_number_type")
    contradiction6_bulletin_number_type_number = Field(attribute="contradiction6_bulletin_number_type_number",column_name="contradiction6_bulletin_number_type_number")
    contradiction6_bulletin_number_branch_number = Field(attribute="contradiction6_bulletin_number_branch_number",column_name="contradiction6_bulletin_number_branch_number")
    contradiction6_bulletin_number_item_number = Field(attribute="contradiction6_bulletin_number_item_number",column_name="contradiction6_bulletin_number_item_number")
    contradiction6_add_code = Field(attribute="contradiction6_add_code",column_name="contradiction6_add_code")
    contradiction6_practice_bassic_name = Field(attribute="contradiction6_practice_bassic_name",column_name="contradiction6_practice_bassic_name")
    contradiction6_practice_abbreviation_name = Field(attribute="contradiction6_practice_abbreviation_name",column_name="contradiction6_practice_abbreviation_name")
    contradiction7_calculability = Field(attribute="contradiction7_calculability",column_name="contradiction7_calculability")
    contradiction7_dental_practice_code = Field(attribute="contradiction7_dental_practice_code",column_name="contradiction7_dental_practice_code")
    contradiction7_bulletin_number_type = Field(attribute="contradiction7_bulletin_number_type",column_name="contradiction7_bulletin_number_type")
    contradiction7_bulletin_number_type_number = Field(attribute="contradiction7_bulletin_number_type_number",column_name="contradiction7_bulletin_number_type_number")
    contradiction7_bulletin_number_branch_number = Field(attribute="contradiction7_bulletin_number_branch_number",column_name="contradiction7_bulletin_number_branch_number")
    contradiction7_bulletin_number_item_number = Field(attribute="contradiction7_bulletin_number_item_number",column_name="contradiction7_bulletin_number_item_number")
    contradiction7_add_code = Field(attribute="contradiction7_add_code",column_name="contradiction7_add_code")
    contradiction7_practice_bassic_name = Field(attribute="contradiction7_practice_bassic_name",column_name="contradiction7_practice_bassic_name")
    contradiction7_practice_abbreviation_name = Field(attribute="contradiction7_practice_abbreviation_name",column_name="contradiction7_practice_abbreviation_name")
    contradiction8_calculability = Field(attribute="contradiction8_calculability",column_name="contradiction8_calculability")
    contradiction8_dental_practice_code = Field(attribute="contradiction8_dental_practice_code",column_name="contradiction8_dental_practice_code")
    contradiction8_bulletin_number_type = Field(attribute="contradiction8_bulletin_number_type",column_name="contradiction8_bulletin_number_type")
    contradiction8_bulletin_number_type_number = Field(attribute="contradiction8_bulletin_number_type_number",column_name="contradiction8_bulletin_number_type_number")
    contradiction8_bulletin_number_branch_number = Field(attribute="contradiction8_bulletin_number_branch_number",column_name="contradiction8_bulletin_number_branch_number")
    contradiction8_bulletin_number_item_number = Field(attribute="contradiction8_bulletin_number_item_number",column_name="contradiction8_bulletin_number_item_number")
    contradiction8_add_code = Field(attribute="contradiction8_add_code",column_name="contradiction8_add_code")
    contradiction8_practice_bassic_name = Field(attribute="contradiction8_practice_bassic_name",column_name="contradiction8_practice_bassic_name")
    contradiction8_practice_abbreviation_name = Field(attribute="contradiction8_practice_abbreviation_name",column_name="contradiction8_practice_abbreviation_name")
    contradiction9_calculability = Field(attribute="contradiction9_calculability",column_name="contradiction9_calculability")
    contradiction9_dental_practice_code = Field(attribute="contradiction9_dental_practice_code",column_name="contradiction9_dental_practice_code")
    contradiction9_bulletin_number_type = Field(attribute="contradiction9_bulletin_number_type",column_name="contradiction9_bulletin_number_type")
    contradiction9_bulletin_number_type_number = Field(attribute="contradiction9_bulletin_number_type_number",column_name="contradiction9_bulletin_number_type_number")
    contradiction9_bulletin_number_branch_number = Field(attribute="contradiction9_bulletin_number_branch_number",column_name="contradiction9_bulletin_number_branch_number")
    contradiction9_bulletin_number_item_number = Field(attribute="contradiction9_bulletin_number_item_number",column_name="contradiction9_bulletin_number_item_number")
    contradiction9_add_code = Field(attribute="contradiction9_add_code",column_name="contradiction9_add_code")
    contradiction9_practice_bassic_name = Field(attribute="contradiction9_practice_bassic_name",column_name="contradiction9_practice_bassic_name")
    contradiction9_practice_abbreviation_name = Field(attribute="contradiction9_practice_abbreviation_name",column_name="contradiction9_practice_abbreviation_name")
    contradiction10_calculability = Field(attribute="contradiction10_calculability",column_name="contradiction10_calculability")
    contradiction10_dental_practice_code = Field(attribute="contradiction10_dental_practice_code",column_name="contradiction10_dental_practice_code")
    contradiction10_bulletin_number_type = Field(attribute="contradiction10_bulletin_number_type",column_name="contradiction10_bulletin_number_type")
    contradiction10_bulletin_number_type_number = Field(attribute="contradiction10_bulletin_number_type_number",column_name="contradiction10_bulletin_number_type_number")
    contradiction10_bulletin_number_branch_number = Field(attribute="contradiction10_bulletin_number_branch_number",column_name="contradiction10_bulletin_number_branch_number")
    contradiction10_bulletin_number_item_number = Field(attribute="contradiction10_bulletin_number_item_number",column_name="contradiction10_bulletin_number_item_number")
    contradiction10_add_code = Field(attribute="contradiction10_add_code",column_name="contradiction10_add_code")
    contradiction10_practice_bassic_name = Field(attribute="contradiction10_practice_bassic_name",column_name="contradiction10_practice_bassic_name")
    contradiction10_practice_abbreviation_name = Field(attribute="contradiction10_practice_abbreviation_name",column_name="contradiction10_practice_abbreviation_name")
    change_date = Field(attribute="change_date",column_name="change_date")
    abolition_date = Field(attribute="abolition_date",column_name="abolition_date")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    class Meta:
        model = models.TableFixCalculationContradiction
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["contradiction1_calculability"] == "":
            row["contradiction1_calculability"]= None

        if row["contradiction1_dental_practice_code"] == "":
            row["contradiction1_dental_practice_code"]= None

        if row["contradiction1_bulletin_number_type_number"] == "":
            row["contradiction1_bulletin_number_type_number"]= None

        if row["contradiction1_bulletin_number_branch_number"] == "":
            row["contradiction1_bulletin_number_branch_number"]= None

        if row["contradiction1_bulletin_number_item_number"] == "":
            row["contradiction1_bulletin_number_item_number"]= None

        if row["contradiction2_calculability"] == "":
            row["contradiction2_calculability"]= None

        if row["contradiction2_dental_practice_code"] == "":
            row["contradiction2_dental_practice_code"]= None

        if row["contradiction2_bulletin_number_type_number"] == "":
            row["contradiction2_bulletin_number_type_number"]= None

        if row["contradiction2_bulletin_number_branch_number"] == "":
            row["contradiction2_bulletin_number_branch_number"]= None

        if row["contradiction2_bulletin_number_item_number"] == "":
            row["contradiction2_bulletin_number_item_number"]= None

        if row["contradiction3_calculability"] == "":
            row["contradiction3_calculability"]= None

        if row["contradiction3_dental_practice_code"] == "":
            row["contradiction3_dental_practice_code"]= None

        if row["contradiction3_bulletin_number_type_number"] == "":
            row["contradiction3_bulletin_number_type_number"]= None

        if row["contradiction3_bulletin_number_branch_number"] == "":
            row["contradiction3_bulletin_number_branch_number"]= None

        if row["contradiction3_bulletin_number_item_number"] == "":
            row["contradiction3_bulletin_number_item_number"]= None

        if row["contradiction4_calculability"] == "":
            row["contradiction4_calculability"]= None

        if row["contradiction4_dental_practice_code"] == "":
            row["contradiction4_dental_practice_code"]= None

        if row["contradiction4_bulletin_number_type_number"] == "":
            row["contradiction4_bulletin_number_type_number"]= None

        if row["contradiction4_bulletin_number_branch_number"] == "":
            row["contradiction4_bulletin_number_branch_number"]= None

        if row["contradiction4_bulletin_number_item_number"] == "":
            row["contradiction4_bulletin_number_item_number"]= None

        if row["contradiction5_calculability"] == "":
            row["contradiction5_calculability"]= None

        if row["contradiction5_dental_practice_code"] == "":
            row["contradiction5_dental_practice_code"]= None

        if row["contradiction5_bulletin_number_type_number"] == "":
            row["contradiction5_bulletin_number_type_number"]= None

        if row["contradiction5_bulletin_number_branch_number"] == "":
            row["contradiction5_bulletin_number_branch_number"]= None

        if row["contradiction5_bulletin_number_item_number"] == "":
            row["contradiction5_bulletin_number_item_number"]= None

        if row["contradiction6_calculability"] == "":
            row["contradiction6_calculability"]= None

        if row["contradiction6_dental_practice_code"] == "":
            row["contradiction6_dental_practice_code"]= None

        if row["contradiction6_bulletin_number_type_number"] == "":
            row["contradiction6_bulletin_number_type_number"]= None

        if row["contradiction6_bulletin_number_branch_number"] == "":
            row["contradiction6_bulletin_number_branch_number"]= None

        if row["contradiction6_bulletin_number_item_number"] == "":
            row["contradiction6_bulletin_number_item_number"]= None

        if row["contradiction7_calculability"] == "":
            row["contradiction7_calculability"]= None

        if row["contradiction7_dental_practice_code"] == "":
            row["contradiction7_dental_practice_code"]= None

        if row["contradiction7_bulletin_number_type_number"] == "":
            row["contradiction7_bulletin_number_type_number"]= None

        if row["contradiction7_bulletin_number_branch_number"] == "":
            row["contradiction7_bulletin_number_branch_number"]= None

        if row["contradiction7_bulletin_number_item_number"] == "":
            row["contradiction7_bulletin_number_item_number"]= None

        if row["contradiction8_calculability"] == "":
            row["contradiction8_calculability"]= None

        if row["contradiction8_dental_practice_code"] == "":
            row["contradiction8_dental_practice_code"]= None

        if row["contradiction8_bulletin_number_type_number"] == "":
            row["contradiction8_bulletin_number_type_number"]= None

        if row["contradiction8_bulletin_number_branch_number"] == "":
            row["contradiction8_bulletin_number_branch_number"]= None

        if row["contradiction8_bulletin_number_item_number"] == "":
            row["contradiction8_bulletin_number_item_number"]= None

        if row["contradiction9_calculability"] == "":
            row["contradiction9_calculability"]= None

        if row["contradiction9_dental_practice_code"] == "":
            row["contradiction9_dental_practice_code"]= None

        if row["contradiction9_bulletin_number_type_number"] == "":
            row["contradiction9_bulletin_number_type_number"]= None

        if row["contradiction9_bulletin_number_branch_number"] == "":
            row["contradiction9_bulletin_number_branch_number"]= None

        if row["contradiction9_bulletin_number_item_number"] == "":
            row["contradiction9_bulletin_number_item_number"]= None

        if row["contradiction10_calculability"] == "":
            row["contradiction10_calculability"]= None

        if row["contradiction10_dental_practice_code"] == "":
            row["contradiction10_dental_practice_code"]= None

        if row["contradiction10_bulletin_number_type_number"] == "":
            row["contradiction10_bulletin_number_type_number"]= None

        if row["contradiction10_bulletin_number_branch_number"] == "":
            row["contradiction10_bulletin_number_branch_number"]= None

        if row["contradiction10_bulletin_number_item_number"] == "":
            row["contradiction10_bulletin_number_item_number"]= None

        if row["change_date"] == str(99999999):
            row["change_date"]= date.max
        elif row["change_date"] == "":
            row["change_date"]= None
        elif row["change_date"] == "0":
            row["change_date"]= None
        else:
            row["change_date"]=dt.strptime(row["change_date"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_date"] == str(99999999):
            row["abolition_date"]= date.max
        elif row["abolition_date"] == "":
            row["abolition_date"]= None
        elif row["abolition_date"] == "0":
            row["abolition_date"]= None
        else:
            row["abolition_date"]=dt.strptime(row["abolition_date"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

class TableRealDayResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    dental_practice_code = Field(attribute="dental_practice_code",column_name="dental_practice_code")
    bulletin_number_type = Field(attribute="bulletin_number_type",column_name="bulletin_number_type")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    add_code = Field(attribute="add_code",column_name="add_code")
    practice_bassic_name = Field(attribute="practice_bassic_name",column_name="practice_bassic_name")
    practice_abbreviation_name = Field(attribute="practice_abbreviation_name",column_name="practice_abbreviation_name")
    real_day = Field(attribute="real_day",column_name="real_day")
    days_or_times = Field(attribute="days_or_times",column_name="days_or_times")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    reserve = Field(attribute="reserve",column_name="reserve")
    class Meta:
        model = models.TableRealDay
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dental_practice_code"] == "":
            row["dental_practice_code"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["real_day"] == "":
            row["real_day"]= None

        if row["days_or_times"] == "":
            row["days_or_times"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["reserve"] == "":
            row["reserve"]= None

class MasterDiseaseResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    disease_name_code = Field(attribute="disease_name_code",column_name="disease_name_code")
    destination_code = Field(attribute="destination_code",column_name="destination_code")
    disease_bassic_name_digits = Field(attribute="disease_bassic_name_digits",column_name="disease_bassic_name_digits")
    disease_bassic_name = Field(attribute="disease_bassic_name",column_name="disease_bassic_name")
    disease_abbreviation_name_digits = Field(attribute="disease_abbreviation_name_digits",column_name="disease_abbreviation_name_digits")
    disease_abbreviation_name = Field(attribute="disease_abbreviation_name",column_name="disease_abbreviation_name")
    disease_cana_name_digits = Field(attribute="disease_cana_name_digits",column_name="disease_cana_name_digits")
    disease_cana_name = Field(attribute="disease_cana_name",column_name="disease_cana_name")
    disease_control_number = Field(attribute="disease_control_number",column_name="disease_control_number")
    adoption_type = Field(attribute="adoption_type",column_name="adoption_type")
    disease_name_exchange_code = Field(attribute="disease_name_exchange_code",column_name="disease_name_exchange_code")
    ICD_10_1 = Field(attribute="ICD_10_1",column_name="ICD_10_1")
    ICD_10_2 = Field(attribute="ICD_10_2",column_name="ICD_10_2")
    ICD_10_1_2013 = Field(attribute="ICD_10_1_2013",column_name="ICD_10_1_2013")
    ICD_10_2_2013 = Field(attribute="ICD_10_2_2013",column_name="ICD_10_2_2013")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    single_use_ban_type = Field(attribute="single_use_ban_type",column_name="single_use_ban_type")
    no_insurance_claim_type = Field(attribute="no_insurance_claim_type",column_name="no_insurance_claim_type")
    special_disease_target_type = Field(attribute="special_disease_target_type",column_name="special_disease_target_type")
    listing_day = Field(attribute="listing_day",column_name="listing_day")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    disease_bassic_name_change_info = Field(attribute="disease_bassic_name_change_info",column_name="disease_bassic_name_change_info")
    disease_abbreviation_name_change_info = Field(attribute="disease_abbreviation_name_change_info",column_name="disease_abbreviation_name_change_info")
    disease_cana_name_change_info = Field(attribute="disease_cana_name_change_info",column_name="disease_cana_name_change_info")
    adoption_type_change_info = Field(attribute="adoption_type_change_info",column_name="adoption_type_change_info")
    disease_name_exchange_code_change_info = Field(attribute="disease_name_exchange_code_change_info",column_name="disease_name_exchange_code_change_info")
    ICD_10_1_change_info = Field(attribute="ICD_10_1_change_info",column_name="ICD_10_1_change_info")
    ICD_10_2_change_info = Field(attribute="ICD_10_2_change_info",column_name="ICD_10_2_change_info")
    dental_disease_abbreviation_name_change_info = Field(attribute="dental_disease_abbreviation_name_change_info",column_name="dental_disease_abbreviation_name_change_info")
    intractable_disease_out_target_type_change_info = Field(attribute="intractable_disease_out_target_type_change_info",column_name="intractable_disease_out_target_type_change_info")
    dental_special_disease_target_type_change_info = Field(attribute="dental_special_disease_target_type_change_info",column_name="dental_special_disease_target_type_change_info")
    single_use_ban_type_change_info = Field(attribute="single_use_ban_type_change_info",column_name="single_use_ban_type_change_info")
    no_insurance_claim_type_change_info = Field(attribute="no_insurance_claim_type_change_info",column_name="no_insurance_claim_type_change_info")
    special_disease_target_type_change_info = Field(attribute="special_disease_target_type_change_info",column_name="special_disease_target_type_change_info")
    destination_disease_control_number = Field(attribute="destination_disease_control_number",column_name="destination_disease_control_number")
    dental_disease_abbreviation_name = Field(attribute="dental_disease_abbreviation_name",column_name="dental_disease_abbreviation_name")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    dental_disease_abbreviation_name_digits = Field(attribute="dental_disease_abbreviation_name_digits",column_name="dental_disease_abbreviation_name_digits")
    intractable_disease_out_target_type = Field(attribute="intractable_disease_out_target_type",column_name="intractable_disease_out_target_type")
    dental_special_disease_target_type = Field(attribute="dental_special_disease_target_type",column_name="dental_special_disease_target_type")
    ICD_10_1_2013_change_info = Field(attribute="ICD_10_1_2013_change_info",column_name="ICD_10_1_2013_change_info")
    ICD_10_2_2013_change_info = Field(attribute="ICD_10_2_2013_change_info",column_name="ICD_10_2_2013_change_info")
    class Meta:
        model = models.MasterDisease
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["disease_name_code"] == "":
            row["disease_name_code"]= None

        if row["destination_code"] == "":
            row["destination_code"]= None

        if row["disease_bassic_name_digits"] == "":
            row["disease_bassic_name_digits"]= None

        if row["disease_abbreviation_name_digits"] == "":
            row["disease_abbreviation_name_digits"]= None

        if row["disease_cana_name_digits"] == "":
            row["disease_cana_name_digits"]= None

        if row["disease_control_number"] == "":
            row["disease_control_number"]= None

        if row["adoption_type"] == "":
            row["adoption_type"]= None

        if row["single_use_ban_type"] == "":
            row["single_use_ban_type"]= None

        if row["no_insurance_claim_type"] == "":
            row["no_insurance_claim_type"]= None

        if row["special_disease_target_type"] == "":
            row["special_disease_target_type"]= None

        if row["listing_day"] == str(99999999):
            row["listing_day"]= date.max
        elif row["listing_day"] == "":
            row["listing_day"]= None
        elif row["listing_day"] == "0":
            row["listing_day"]= None
        else:
            row["listing_day"]=dt.strptime(row["listing_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["disease_bassic_name_change_info"] == "":
            row["disease_bassic_name_change_info"]= None

        if row["disease_abbreviation_name_change_info"] == "":
            row["disease_abbreviation_name_change_info"]= None

        if row["disease_cana_name_change_info"] == "":
            row["disease_cana_name_change_info"]= None

        if row["adoption_type_change_info"] == "":
            row["adoption_type_change_info"]= None

        if row["disease_name_exchange_code_change_info"] == "":
            row["disease_name_exchange_code_change_info"]= None

        if row["ICD_10_1_change_info"] == "":
            row["ICD_10_1_change_info"]= None

        if row["ICD_10_2_change_info"] == "":
            row["ICD_10_2_change_info"]= None

        if row["dental_disease_abbreviation_name_change_info"] == "":
            row["dental_disease_abbreviation_name_change_info"]= None

        if row["intractable_disease_out_target_type_change_info"] == "":
            row["intractable_disease_out_target_type_change_info"]= None

        if row["dental_special_disease_target_type_change_info"] == "":
            row["dental_special_disease_target_type_change_info"]= None

        if row["single_use_ban_type_change_info"] == "":
            row["single_use_ban_type_change_info"]= None

        if row["no_insurance_claim_type_change_info"] == "":
            row["no_insurance_claim_type_change_info"]= None

        if row["special_disease_target_type_change_info"] == "":
            row["special_disease_target_type_change_info"]= None

        if row["destination_disease_control_number"] == "":
            row["destination_disease_control_number"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["dental_disease_abbreviation_name_digits"] == "":
            row["dental_disease_abbreviation_name_digits"]= None

        if row["intractable_disease_out_target_type"] == "":
            row["intractable_disease_out_target_type"]= None

        if row["dental_special_disease_target_type"] == "":
            row["dental_special_disease_target_type"]= None

        if row["ICD_10_1_2013_change_info"] == "":
            row["ICD_10_1_2013_change_info"]= None

        if row["ICD_10_2_2013_change_info"] == "":
            row["ICD_10_2_2013_change_info"]= None

class MasterModifierResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    modifier_code = Field(attribute="modifier_code",column_name="modifier_code")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    modifier_name_digits = Field(attribute="modifier_name_digits",column_name="modifier_name_digits")
    modifier_name = Field(attribute="modifier_name",column_name="modifier_name")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    modifier_cana_name_digits = Field(attribute="modifier_cana_name_digits",column_name="modifier_cana_name_digits")
    modifier_cana_name = Field(attribute="modifier_cana_name",column_name="modifier_cana_name")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    modifier_name_change_info = Field(attribute="modifier_name_change_info",column_name="modifier_name_change_info")
    modifier_cana_name_change_info = Field(attribute="modifier_cana_name_change_info",column_name="modifier_cana_name_change_info")
    listing_day = Field(attribute="listing_day",column_name="listing_day")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    modifier_control_number = Field(attribute="modifier_control_number",column_name="modifier_control_number")
    modifier_exchange_code = Field(attribute="modifier_exchange_code",column_name="modifier_exchange_code")
    modifier_type = Field(attribute="modifier_type",column_name="modifier_type")
    class Meta:
        model = models.MasterModifier
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["modifier_code"] == "":
            row["modifier_code"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["modifier_name_digits"] == "":
            row["modifier_name_digits"]= None

        if row["modifier_cana_name_digits"] == "":
            row["modifier_cana_name_digits"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["modifier_name_change_info"] == "":
            row["modifier_name_change_info"]= None

        if row["modifier_cana_name_change_info"] == "":
            row["modifier_cana_name_change_info"]= None

        if row["listing_day"] == str(99999999):
            row["listing_day"]= date.max
        elif row["listing_day"] == "":
            row["listing_day"]= None
        elif row["listing_day"] == "0":
            row["listing_day"]= None
        else:
            row["listing_day"]=dt.strptime(row["listing_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["modifier_control_number"] == "":
            row["modifier_control_number"]= None

class MasterDentalResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    dentation_code = Field(attribute="dentation_code",column_name="dentation_code")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    dentation_name = Field(attribute="dentation_name",column_name="dentation_name")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    class Meta:
        model = models.MasterDental
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

class MasterDrugResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    drug_code = Field(attribute="drug_code",column_name="drug_code")
    drug_kanji_significant_digits = Field(attribute="drug_kanji_significant_digits",column_name="drug_kanji_significant_digits")
    drug_kanji_name = Field(attribute="drug_kanji_name",column_name="drug_kanji_name")
    drug_cana_significant_digits = Field(attribute="drug_cana_significant_digits",column_name="drug_cana_significant_digits")
    drug_cana_name = Field(attribute="drug_cana_name",column_name="drug_cana_name")
    unit_code = Field(attribute="unit_code",column_name="unit_code")
    unit_kanji_significant_digits = Field(attribute="unit_kanji_significant_digits",column_name="unit_kanji_significant_digits")
    unit_kanji_name = Field(attribute="unit_kanji_name",column_name="unit_kanji_name")
    new_cash_amount_type = Field(attribute="new_cash_amount_type",column_name="new_cash_amount_type")
    new_cash_new_cash = Field(attribute="new_cash_new_cash",column_name="new_cash_new_cash")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    special_drug = Field(attribute="special_drug",column_name="special_drug")
    neuroleptic = Field(attribute="neuroleptic",column_name="neuroleptic")
    biologics = Field(attribute="biologics",column_name="biologics")
    generic = Field(attribute="generic",column_name="generic")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    dental_special_drug = Field(attribute="dental_special_drug",column_name="dental_special_drug")
    contrast_drug = Field(attribute="contrast_drug",column_name="contrast_drug")
    Injection_volume = Field(attribute="Injection_volume",column_name="Injection_volume")
    listing_method_identification = Field(attribute="listing_method_identification",column_name="listing_method_identification")
    product_name_etc = Field(attribute="product_name_etc",column_name="product_name_etc")
    old_cash_amount_type = Field(attribute="old_cash_amount_type",column_name="old_cash_amount_type")
    old_cash_old_cash = Field(attribute="old_cash_old_cash",column_name="old_cash_old_cash")
    kanji_name_change_type = Field(attribute="kanji_name_change_type",column_name="kanji_name_change_type")
    cana_name_change_type = Field(attribute="cana_name_change_type",column_name="cana_name_change_type")
    dosage_form = Field(attribute="dosage_form",column_name="dosage_form")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    drug_price_bassic_listing_code = Field(attribute="drug_price_bassic_listing_code",column_name="drug_price_bassic_listing_code")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    expiry_day = Field(attribute="expiry_day",column_name="expiry_day")
    bassic_kanji_name = Field(attribute="bassic_kanji_name",column_name="bassic_kanji_name")
    class Meta:
        model = models.MasterDrug
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["drug_code"] == "":
            row["drug_code"]= None

        if row["drug_kanji_significant_digits"] == "":
            row["drug_kanji_significant_digits"]= None

        if row["drug_cana_significant_digits"] == "":
            row["drug_cana_significant_digits"]= None

        if row["unit_code"] == "":
            row["unit_code"]= None

        if row["unit_kanji_significant_digits"] == "":
            row["unit_kanji_significant_digits"]= None

        if row["new_cash_amount_type"] == "":
            row["new_cash_amount_type"]= None

        if row["new_cash_new_cash"] == "":
            row["new_cash_new_cash"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["special_drug"] == "":
            row["special_drug"]= None

        if row["neuroleptic"] == "":
            row["neuroleptic"]= None

        if row["biologics"] == "":
            row["biologics"]= None

        if row["generic"] == "":
            row["generic"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["dental_special_drug"] == "":
            row["dental_special_drug"]= None

        if row["contrast_drug"] == "":
            row["contrast_drug"]= None

        if row["Injection_volume"] == "":
            row["Injection_volume"]= None

        if row["listing_method_identification"] == "":
            row["listing_method_identification"]= None

        if row["product_name_etc"] == "":
            row["product_name_etc"]= None

        if row["old_cash_amount_type"] == "":
            row["old_cash_amount_type"]= None

        if row["old_cash_old_cash"] == "":
            row["old_cash_old_cash"]= None

        if row["kanji_name_change_type"] == "":
            row["kanji_name_change_type"]= None

        if row["cana_name_change_type"] == "":
            row["cana_name_change_type"]= None

        if row["dosage_form"] == "":
            row["dosage_form"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

        if row["expiry_day"] == str(99999999):
            row["expiry_day"]= date.max
        elif row["expiry_day"] == "":
            row["expiry_day"]= None
        elif row["expiry_day"] == "0":
            row["expiry_day"]= None
        else:
            row["expiry_day"]=dt.strptime(row["expiry_day"], "%Y%m%d").strftime("%Y-%m-%d")

class MasterSpecialEquipmentResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    special_equipment_code = Field(attribute="special_equipment_code",column_name="special_equipment_code")
    special_equipment_significant_digits = Field(attribute="special_equipment_significant_digits",column_name="special_equipment_significant_digits")
    special_equipment_kanji_name = Field(attribute="special_equipment_kanji_name",column_name="special_equipment_kanji_name")
    special_equipment_cana_significant_digits = Field(attribute="special_equipment_cana_significant_digits",column_name="special_equipment_cana_significant_digits")
    special_equipment_cana_name = Field(attribute="special_equipment_cana_name",column_name="special_equipment_cana_name")
    unit_code = Field(attribute="unit_code",column_name="unit_code")
    unit_kanji_significant_digits = Field(attribute="unit_kanji_significant_digits",column_name="unit_kanji_significant_digits")
    unit_kanji_name = Field(attribute="unit_kanji_name",column_name="unit_kanji_name")
    new_cash_amount_type = Field(attribute="new_cash_amount_type",column_name="new_cash_amount_type")
    new_cash_new_cash = Field(attribute="new_cash_new_cash",column_name="new_cash_new_cash")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    age_add_type = Field(attribute="age_add_type",column_name="age_add_type")
    age_limit_lower_limit = Field(attribute="age_limit_lower_limit",column_name="age_limit_lower_limit")
    age_limit_upper_limit = Field(attribute="age_limit_upper_limit",column_name="age_limit_upper_limit")
    old_cash_amount_type = Field(attribute="old_cash_amount_type",column_name="old_cash_amount_type")
    old_cash_old_cash = Field(attribute="old_cash_old_cash",column_name="old_cash_old_cash")
    kanji_name_change_type = Field(attribute="kanji_name_change_type",column_name="kanji_name_change_type")
    cana_name_change_type = Field(attribute="cana_name_change_type",column_name="cana_name_change_type")
    oxygen_type = Field(attribute="oxygen_type",column_name="oxygen_type")
    special_equipment_type = Field(attribute="special_equipment_type",column_name="special_equipment_type")
    upper_limit_price = Field(attribute="upper_limit_price",column_name="upper_limit_price")
    lower_limit_price = Field(attribute="lower_limit_price",column_name="lower_limit_price")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    abolition_new_etc = Field(attribute="abolition_new_etc",column_name="abolition_new_etc")
    change_day = Field(attribute="change_day",column_name="change_day")
    expiry_day = Field(attribute="expiry_day",column_name="expiry_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    bulletin_number_other_table_number = Field(attribute="bulletin_number_other_table_number",column_name="bulletin_number_other_table_number")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    dpc_type = Field(attribute="dpc_type",column_name="dpc_type")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    bassic_kanji_name = Field(attribute="bassic_kanji_name",column_name="bassic_kanji_name")
    class Meta:
        model = models.MasterSpecialEquipment
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["special_equipment_code"] == "":
            row["special_equipment_code"]= None

        if row["special_equipment_significant_digits"] == "":
            row["special_equipment_significant_digits"]= None

        if row["special_equipment_cana_significant_digits"] == "":
            row["special_equipment_cana_significant_digits"]= None

        if row["unit_code"] == "":
            row["unit_code"]= None

        if row["unit_kanji_significant_digits"] == "":
            row["unit_kanji_significant_digits"]= None

        if row["new_cash_amount_type"] == "":
            row["new_cash_amount_type"]= None

        if row["new_cash_new_cash"] == "":
            row["new_cash_new_cash"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["age_add_type"] == "":
            row["age_add_type"]= None

        if row["old_cash_amount_type"] == "":
            row["old_cash_amount_type"]= None

        if row["old_cash_old_cash"] == "":
            row["old_cash_old_cash"]= None

        if row["kanji_name_change_type"] == "":
            row["kanji_name_change_type"]= None

        if row["cana_name_change_type"] == "":
            row["cana_name_change_type"]= None

        if row["oxygen_type"] == "":
            row["oxygen_type"]= None

        if row["special_equipment_type"] == "":
            row["special_equipment_type"]= None

        if row["upper_limit_price"] == "":
            row["upper_limit_price"]= None

        if row["lower_limit_price"] == "":
            row["lower_limit_price"]= None

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

        if row["abolition_new_etc"] == "":
            row["abolition_new_etc"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["expiry_day"] == str(99999999):
            row["expiry_day"]= date.max
        elif row["expiry_day"] == "":
            row["expiry_day"]= None
        elif row["expiry_day"] == "0":
            row["expiry_day"]= None
        else:
            row["expiry_day"]=dt.strptime(row["expiry_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["bulletin_number_other_table_number"] == "":
            row["bulletin_number_other_table_number"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["dpc_type"] == "":
            row["dpc_type"]= None

class MasterCommentResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    type = Field(attribute="type",column_name="type")
    pattern = Field(attribute="pattern",column_name="pattern")
    serial_number = Field(attribute="serial_number",column_name="serial_number")
    comment_kanji_significant_digits = Field(attribute="comment_kanji_significant_digits",column_name="comment_kanji_significant_digits")
    comment_kanji_name = Field(attribute="comment_kanji_name",column_name="comment_kanji_name")
    comment_cana_significant_digits = Field(attribute="comment_cana_significant_digits",column_name="comment_cana_significant_digits")
    comment_cana_name = Field(attribute="comment_cana_name",column_name="comment_cana_name")
    receipt_edit_info_column1 = Field(attribute="receipt_edit_info_column1",column_name="receipt_edit_info_column1")
    receipt_edit_info_digits1 = Field(attribute="receipt_edit_info_digits1",column_name="receipt_edit_info_digits1")
    receipt_edit_info_column2 = Field(attribute="receipt_edit_info_column2",column_name="receipt_edit_info_column2")
    receipt_edit_info_digits2 = Field(attribute="receipt_edit_info_digits2",column_name="receipt_edit_info_digits2")
    receipt_edit_info_column3 = Field(attribute="receipt_edit_info_column3",column_name="receipt_edit_info_column3")
    receipt_edit_info_digits3 = Field(attribute="receipt_edit_info_digits3",column_name="receipt_edit_info_digits3")
    receipt_edit_info_column4 = Field(attribute="receipt_edit_info_column4",column_name="receipt_edit_info_column4")
    receipt_edit_info_digits4 = Field(attribute="receipt_edit_info_digits4",column_name="receipt_edit_info_digits4")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    choice_comment_identification = Field(attribute="choice_comment_identification",column_name="choice_comment_identification")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    commnet_code = Field(attribute="commnet_code",column_name="commnet_code")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    reserve6 = Field(attribute="reserve6",column_name="reserve6")
    reserve7 = Field(attribute="reserve7",column_name="reserve7")
    reserve8 = Field(attribute="reserve8",column_name="reserve8")
    class Meta:
        model = models.MasterComment
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["type"] == "":
            row["type"]= None

        if row["pattern"] == "":
            row["pattern"]= None

        if row["serial_number"] == "":
            row["serial_number"]= None

        if row["comment_kanji_significant_digits"] == "":
            row["comment_kanji_significant_digits"]= None

        if row["comment_cana_significant_digits"] == "":
            row["comment_cana_significant_digits"]= None

        if row["receipt_edit_info_column1"] == "":
            row["receipt_edit_info_column1"]= None

        if row["receipt_edit_info_digits1"] == "":
            row["receipt_edit_info_digits1"]= None

        if row["receipt_edit_info_column2"] == "":
            row["receipt_edit_info_column2"]= None

        if row["receipt_edit_info_digits2"] == "":
            row["receipt_edit_info_digits2"]= None

        if row["receipt_edit_info_column3"] == "":
            row["receipt_edit_info_column3"]= None

        if row["receipt_edit_info_digits3"] == "":
            row["receipt_edit_info_digits3"]= None

        if row["receipt_edit_info_column4"] == "":
            row["receipt_edit_info_column4"]= None

        if row["receipt_edit_info_digits4"] == "":
            row["receipt_edit_info_digits4"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["choice_comment_identification"] == "":
            row["choice_comment_identification"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["commnet_code"] == "":
            row["commnet_code"]= None

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["reserve6"] == "":
            row["reserve6"]= None

        if row["reserve7"] == "":
            row["reserve7"]= None

        if row["reserve8"] == "":
            row["reserve8"]= None

class MasterPracticeResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    practice_code = Field(attribute="practice_code",column_name="practice_code")
    practice_abbreviation_name_kanji_significant_digits = Field(attribute="practice_abbreviation_name_kanji_significant_digits",column_name="practice_abbreviation_name_kanji_significant_digits")
    practice_abbreviation_name_kanji_name = Field(attribute="practice_abbreviation_name_kanji_name",column_name="practice_abbreviation_name_kanji_name")
    practice_abbreviation_name_cana_significant_digits = Field(attribute="practice_abbreviation_name_cana_significant_digits",column_name="practice_abbreviation_name_cana_significant_digits")
    practice_abbreviation_name_cana_name = Field(attribute="practice_abbreviation_name_cana_name",column_name="practice_abbreviation_name_cana_name")
    data_code = Field(attribute="data_code",column_name="data_code")
    data_kanji_significant_digits = Field(attribute="data_kanji_significant_digits",column_name="data_kanji_significant_digits")
    data_kanji_name = Field(attribute="data_kanji_name",column_name="data_kanji_name")
    new_score_etc_identification = Field(attribute="new_score_etc_identification",column_name="new_score_etc_identification")
    new_score_etc = Field(attribute="new_score_etc",column_name="new_score_etc")
    in_out_code = Field(attribute="in_out_code",column_name="in_out_code")
    late_elderly_medical_code = Field(attribute="late_elderly_medical_code",column_name="late_elderly_medical_code")
    score_destination_identification_out = Field(attribute="score_destination_identification_out",column_name="score_destination_identification_out")
    comprehensive_inspection = Field(attribute="comprehensive_inspection",column_name="comprehensive_inspection")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    dpc_type = Field(attribute="dpc_type",column_name="dpc_type")
    hospital_type = Field(attribute="hospital_type",column_name="hospital_type")
    surgery_support_addition_type = Field(attribute="surgery_support_addition_type",column_name="surgery_support_addition_type")
    medical_observation_type = Field(attribute="medical_observation_type",column_name="medical_observation_type")
    nursing_addition = Field(attribute="nursing_addition",column_name="nursing_addition")
    anesthesia_identification_type = Field(attribute="anesthesia_identification_type",column_name="anesthesia_identification_type")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    disease_name_related_type = Field(attribute="disease_name_related_type",column_name="disease_name_related_type")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    real_day = Field(attribute="real_day",column_name="real_day")
    days_or_times = Field(attribute="days_or_times",column_name="days_or_times")
    drug_name_code = Field(attribute="drug_name_code",column_name="drug_name_code")
    etch_value_calculation_identification = Field(attribute="etch_value_calculation_identification",column_name="etch_value_calculation_identification")
    etch_lower_limit = Field(attribute="etch_lower_limit",column_name="etch_lower_limit")
    etch_upper_limit = Field(attribute="etch_upper_limit",column_name="etch_upper_limit")
    etch_value = Field(attribute="etch_value",column_name="etch_value")
    etch_value_score = Field(attribute="etch_value_score",column_name="etch_value_score")
    etch_limits_error_process = Field(attribute="etch_limits_error_process",column_name="etch_limits_error_process")
    upper_limit = Field(attribute="upper_limit",column_name="upper_limit")
    upper_limit_error_process = Field(attribute="upper_limit_error_process",column_name="upper_limit_error_process")
    annotation_add_item_add_code = Field(attribute="annotation_add_item_add_code",column_name="annotation_add_item_add_code")
    annotation_add_item_add_number = Field(attribute="annotation_add_item_add_number",column_name="annotation_add_item_add_number")
    general_rule_age = Field(attribute="general_rule_age",column_name="general_rule_age")
    etch_limits_lower_limit = Field(attribute="etch_limits_lower_limit",column_name="etch_limits_lower_limit")
    etch_limits_upper_limit = Field(attribute="etch_limits_upper_limit",column_name="etch_limits_upper_limit")
    time_addition_type = Field(attribute="time_addition_type",column_name="time_addition_type")
    base_conformance_code = Field(attribute="base_conformance_code",column_name="base_conformance_code")
    base_conformance_facility_standard = Field(attribute="base_conformance_facility_standard",column_name="base_conformance_facility_standard")
    treatment_infant_addition_type = Field(attribute="treatment_infant_addition_type",column_name="treatment_infant_addition_type")
    very_low_birth_weight_infant_addition_type = Field(attribute="very_low_birth_weight_infant_addition_type",column_name="very_low_birth_weight_infant_addition_type")
    basic_hospital_fee_deduction_identification = Field(attribute="basic_hospital_fee_deduction_identification",column_name="basic_hospital_fee_deduction_identification")
    donors_class_type = Field(attribute="donors_class_type",column_name="donors_class_type")
    judgment_class_inspections_type = Field(attribute="judgment_class_inspections_type",column_name="judgment_class_inspections_type")
    judgment_class_inspections_group_type = Field(attribute="judgment_class_inspections_group_type",column_name="judgment_class_inspections_group_type")
    diminution_code = Field(attribute="diminution_code",column_name="diminution_code")
    spinal_cord_evoked_potential_measurement_add_type = Field(attribute="spinal_cord_evoked_potential_measurement_add_type",column_name="spinal_cord_evoked_potential_measurement_add_type")
    neck_dissection_combined_addition_type = Field(attribute="neck_dissection_combined_addition_type",column_name="neck_dissection_combined_addition_type")
    auto_suturer_add_type = Field(attribute="auto_suturer_add_type",column_name="auto_suturer_add_type")
    out_management_add_type = Field(attribute="out_management_add_type",column_name="out_management_add_type")
    old_score_etc_identification = Field(attribute="old_score_etc_identification",column_name="old_score_etc_identification")
    old_score_etc = Field(attribute="old_score_etc",column_name="old_score_etc")
    kanji_name_change_type = Field(attribute="kanji_name_change_type",column_name="kanji_name_change_type")
    cana_name_change_type = Field(attribute="cana_name_change_type",column_name="cana_name_change_type")
    speciment_test_comment = Field(attribute="speciment_test_comment",column_name="speciment_test_comment")
    general_rule_add_score_type = Field(attribute="general_rule_add_score_type",column_name="general_rule_add_score_type")
    comprehensive_code = Field(attribute="comprehensive_code",column_name="comprehensive_code")
    ultrasonic_endoscope_add_type = Field(attribute="ultrasonic_endoscope_add_type",column_name="ultrasonic_endoscope_add_type")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    score_destination_identification_in = Field(attribute="score_destination_identification_in",column_name="score_destination_identification_in")
    auto_anastomosis_add_type = Field(attribute="auto_anastomosis_add_type",column_name="auto_anastomosis_add_type")
    bulletin_identification_type1 = Field(attribute="bulletin_identification_type1",column_name="bulletin_identification_type1")
    bulletin_identification_type2 = Field(attribute="bulletin_identification_type2",column_name="bulletin_identification_type2")
    area_add = Field(attribute="area_add",column_name="area_add")
    beds_type = Field(attribute="beds_type",column_name="beds_type")
    facility_standard_code1 = Field(attribute="facility_standard_code1",column_name="facility_standard_code1")
    facility_standard_code2 = Field(attribute="facility_standard_code2",column_name="facility_standard_code2")
    facility_standard_code3 = Field(attribute="facility_standard_code3",column_name="facility_standard_code3")
    facility_standard_code4 = Field(attribute="facility_standard_code4",column_name="facility_standard_code4")
    facility_standard_code5 = Field(attribute="facility_standard_code5",column_name="facility_standard_code5")
    facility_standard_code6 = Field(attribute="facility_standard_code6",column_name="facility_standard_code6")
    facility_standard_code7 = Field(attribute="facility_standard_code7",column_name="facility_standard_code7")
    facility_standard_code8 = Field(attribute="facility_standard_code8",column_name="facility_standard_code8")
    facility_standard_code9 = Field(attribute="facility_standard_code9",column_name="facility_standard_code9")
    facility_standard_code10 = Field(attribute="facility_standard_code10",column_name="facility_standard_code10")
    ultrasonic_coagulator_type = Field(attribute="ultrasonic_coagulator_type",column_name="ultrasonic_coagulator_type")
    short_stay_surgery = Field(attribute="short_stay_surgery",column_name="short_stay_surgery")
    dental_type = Field(attribute="dental_type",column_name="dental_type")
    code_table_number_alphabet = Field(attribute="code_table_number_alphabet",column_name="code_table_number_alphabet")
    bulletin_number_alphabet = Field(attribute="bulletin_number_alphabet",column_name="bulletin_number_alphabet")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    code_table_number_chapter = Field(attribute="code_table_number_chapter",column_name="code_table_number_chapter")
    code_table_number_department = Field(attribute="code_table_number_department",column_name="code_table_number_department")
    code_table_number_type_number = Field(attribute="code_table_number_type_number",column_name="code_table_number_type_number")
    code_table_number_branch_number = Field(attribute="code_table_number_branch_number",column_name="code_table_number_branch_number")
    code_table_number_item_number = Field(attribute="code_table_number_item_number",column_name="code_table_number_item_number")
    bulletin_number_chapter = Field(attribute="bulletin_number_chapter",column_name="bulletin_number_chapter")
    bulletin_number_department = Field(attribute="bulletin_number_department",column_name="bulletin_number_department")
    bulletin_number_type_number = Field(attribute="bulletin_number_type_number",column_name="bulletin_number_type_number")
    bulletin_number_branch_number = Field(attribute="bulletin_number_branch_number",column_name="bulletin_number_branch_number")
    bulletin_number_item_number = Field(attribute="bulletin_number_item_number",column_name="bulletin_number_item_number")
    age_add1_lower_age = Field(attribute="age_add1_lower_age",column_name="age_add1_lower_age")
    age_add1_upper_age = Field(attribute="age_add1_upper_age",column_name="age_add1_upper_age")
    age_add1_annotation_add_item_practice_code = Field(attribute="age_add1_annotation_add_item_practice_code",column_name="age_add1_annotation_add_item_practice_code")
    age_add2_lower_age = Field(attribute="age_add2_lower_age",column_name="age_add2_lower_age")
    age_add2_upper_age = Field(attribute="age_add2_upper_age",column_name="age_add2_upper_age")
    age_add2_annotation_add_item_practice_code = Field(attribute="age_add2_annotation_add_item_practice_code",column_name="age_add2_annotation_add_item_practice_code")
    age_add3_lower_age = Field(attribute="age_add3_lower_age",column_name="age_add3_lower_age")
    age_add3_upper_age = Field(attribute="age_add3_upper_age",column_name="age_add3_upper_age")
    age_add3_annotation_add_item_practice_code = Field(attribute="age_add3_annotation_add_item_practice_code",column_name="age_add3_annotation_add_item_practice_code")
    age_add4_lower_age = Field(attribute="age_add4_lower_age",column_name="age_add4_lower_age")
    age_add4_upper_age = Field(attribute="age_add4_upper_age",column_name="age_add4_upper_age")
    age_add4_annotation_add_item_practice_code = Field(attribute="age_add4_annotation_add_item_practice_code",column_name="age_add4_annotation_add_item_practice_code")
    transfer_related = Field(attribute="transfer_related",column_name="transfer_related")
    basic_kanji_name = Field(attribute="basic_kanji_name",column_name="basic_kanji_name")
    sinus_surgery_endoscope_addition = Field(attribute="sinus_surgery_endoscope_addition",column_name="sinus_surgery_endoscope_addition")
    sinus_surgery_tissue_resection_equipment_addition = Field(attribute="sinus_surgery_tissue_resection_equipment_addition",column_name="sinus_surgery_tissue_resection_equipment_addition")
    long_term_anesthesia_management_addition = Field(attribute="long_term_anesthesia_management_addition",column_name="long_term_anesthesia_management_addition")
    score_type_number = Field(attribute="score_type_number",column_name="score_type_number")
    monitoring_addition = Field(attribute="monitoring_addition",column_name="monitoring_addition")
    cryopreserved_allogeneic_tissue_addition = Field(attribute="cryopreserved_allogeneic_tissue_addition",column_name="cryopreserved_allogeneic_tissue_addition")
    malignant_tumor_histopathological_sample_addition = Field(attribute="malignant_tumor_histopathological_sample_addition",column_name="malignant_tumor_histopathological_sample_addition")
    external_fixator_addition = Field(attribute="external_fixator_addition",column_name="external_fixator_addition")
    ultrasonic_cutting_equipment_addition = Field(attribute="ultrasonic_cutting_equipment_addition",column_name="ultrasonic_cutting_equipment_addition")
    left_atrial_appendage_closure_surgery_addition = Field(attribute="left_atrial_appendage_closure_surgery_addition",column_name="left_atrial_appendage_closure_surgery_addition")
    improve_countermeasures_against_foreign_infections_additions = Field(attribute="improve_countermeasures_against_foreign_infections_additions",column_name="improve_countermeasures_against_foreign_infections_additions")
    otolaryngology_infant_treatment_addition = Field(attribute="otolaryngology_infant_treatment_addition",column_name="otolaryngology_infant_treatment_addition")
    otolaryngology_infant_treatment_drug_support_addition = Field(attribute="otolaryngology_infant_treatment_drug_support_addition",column_name="otolaryngology_infant_treatment_drug_support_addition")
    incision_local_negative_treatment_device_addition = Field(attribute="incision_local_negative_treatment_device_addition",column_name="incision_local_negative_treatment_device_addition")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    reserve6 = Field(attribute="reserve6",column_name="reserve6")
    reserve7 = Field(attribute="reserve7",column_name="reserve7")
    reserve8 = Field(attribute="reserve8",column_name="reserve8")
    reserve9 = Field(attribute="reserve9",column_name="reserve9")
    reserve10 = Field(attribute="reserve10",column_name="reserve10")
    reserve11 = Field(attribute="reserve11",column_name="reserve11")
    reserve12 = Field(attribute="reserve12",column_name="reserve12")
    reserve13 = Field(attribute="reserve13",column_name="reserve13")
    reserve14 = Field(attribute="reserve14",column_name="reserve14")
    reserve15 = Field(attribute="reserve15",column_name="reserve15")
    reserve16 = Field(attribute="reserve16",column_name="reserve16")
    reserve17 = Field(attribute="reserve17",column_name="reserve17")
    reserve18 = Field(attribute="reserve18",column_name="reserve18")
    reserve19 = Field(attribute="reserve19",column_name="reserve19")
    reserve20 = Field(attribute="reserve20",column_name="reserve20")
    reserve21 = Field(attribute="reserve21",column_name="reserve21")
    reserve22 = Field(attribute="reserve22",column_name="reserve22")
    reserve23 = Field(attribute="reserve23",column_name="reserve23")
    reserve24 = Field(attribute="reserve24",column_name="reserve24")
    reserve25 = Field(attribute="reserve25",column_name="reserve25")
    reserve26 = Field(attribute="reserve26",column_name="reserve26")
    reserve27 = Field(attribute="reserve27",column_name="reserve27")
    class Meta:
        model = models.MasterPractice
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["practice_code"] == "":
            row["practice_code"]= None

        if row["practice_abbreviation_name_kanji_significant_digits"] == "":
            row["practice_abbreviation_name_kanji_significant_digits"]= None

        if row["practice_abbreviation_name_cana_significant_digits"] == "":
            row["practice_abbreviation_name_cana_significant_digits"]= None

        if row["data_code"] == "":
            row["data_code"]= None

        if row["data_kanji_significant_digits"] == "":
            row["data_kanji_significant_digits"]= None

        if row["new_score_etc_identification"] == "":
            row["new_score_etc_identification"]= None

        if row["new_score_etc"] == "":
            row["new_score_etc"]= None

        if row["in_out_code"] == "":
            row["in_out_code"]= None

        if row["late_elderly_medical_code"] == "":
            row["late_elderly_medical_code"]= None

        if row["score_destination_identification_out"] == "":
            row["score_destination_identification_out"]= None

        if row["comprehensive_inspection"] == "":
            row["comprehensive_inspection"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["dpc_type"] == "":
            row["dpc_type"]= None

        if row["hospital_type"] == "":
            row["hospital_type"]= None

        if row["surgery_support_addition_type"] == "":
            row["surgery_support_addition_type"]= None

        if row["medical_observation_type"] == "":
            row["medical_observation_type"]= None

        if row["nursing_addition"] == "":
            row["nursing_addition"]= None

        if row["anesthesia_identification_type"] == "":
            row["anesthesia_identification_type"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["disease_name_related_type"] == "":
            row["disease_name_related_type"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["real_day"] == "":
            row["real_day"]= None

        if row["days_or_times"] == "":
            row["days_or_times"]= None

        if row["drug_name_code"] == "":
            row["drug_name_code"]= None

        if row["etch_value_calculation_identification"] == "":
            row["etch_value_calculation_identification"]= None

        if row["etch_lower_limit"] == "":
            row["etch_lower_limit"]= None

        if row["etch_upper_limit"] == "":
            row["etch_upper_limit"]= None

        if row["etch_value"] == "":
            row["etch_value"]= None

        if row["etch_value_score"] == "":
            row["etch_value_score"]= None

        if row["etch_limits_error_process"] == "":
            row["etch_limits_error_process"]= None

        if row["upper_limit"] == "":
            row["upper_limit"]= None

        if row["upper_limit_error_process"] == "":
            row["upper_limit_error_process"]= None

        if row["annotation_add_item_add_code"] == "":
            row["annotation_add_item_add_code"]= None

        if row["general_rule_age"] == "":
            row["general_rule_age"]= None

        if row["time_addition_type"] == "":
            row["time_addition_type"]= None

        if row["base_conformance_code"] == "":
            row["base_conformance_code"]= None

        if row["base_conformance_facility_standard"] == "":
            row["base_conformance_facility_standard"]= None

        if row["treatment_infant_addition_type"] == "":
            row["treatment_infant_addition_type"]= None

        if row["very_low_birth_weight_infant_addition_type"] == "":
            row["very_low_birth_weight_infant_addition_type"]= None

        if row["basic_hospital_fee_deduction_identification"] == "":
            row["basic_hospital_fee_deduction_identification"]= None

        if row["donors_class_type"] == "":
            row["donors_class_type"]= None

        if row["judgment_class_inspections_type"] == "":
            row["judgment_class_inspections_type"]= None

        if row["judgment_class_inspections_group_type"] == "":
            row["judgment_class_inspections_group_type"]= None

        if row["diminution_code"] == "":
            row["diminution_code"]= None

        if row["spinal_cord_evoked_potential_measurement_add_type"] == "":
            row["spinal_cord_evoked_potential_measurement_add_type"]= None

        if row["neck_dissection_combined_addition_type"] == "":
            row["neck_dissection_combined_addition_type"]= None

        if row["auto_suturer_add_type"] == "":
            row["auto_suturer_add_type"]= None

        if row["out_management_add_type"] == "":
            row["out_management_add_type"]= None

        if row["old_score_etc_identification"] == "":
            row["old_score_etc_identification"]= None

        if row["old_score_etc"] == "":
            row["old_score_etc"]= None

        if row["kanji_name_change_type"] == "":
            row["kanji_name_change_type"]= None

        if row["cana_name_change_type"] == "":
            row["cana_name_change_type"]= None

        if row["speciment_test_comment"] == "":
            row["speciment_test_comment"]= None

        if row["general_rule_add_score_type"] == "":
            row["general_rule_add_score_type"]= None

        if row["comprehensive_code"] == "":
            row["comprehensive_code"]= None

        if row["ultrasonic_endoscope_add_type"] == "":
            row["ultrasonic_endoscope_add_type"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["score_destination_identification_in"] == "":
            row["score_destination_identification_in"]= None

        if row["auto_anastomosis_add_type"] == "":
            row["auto_anastomosis_add_type"]= None

        if row["bulletin_identification_type1"] == "":
            row["bulletin_identification_type1"]= None

        if row["bulletin_identification_type2"] == "":
            row["bulletin_identification_type2"]= None

        if row["area_add"] == "":
            row["area_add"]= None

        if row["beds_type"] == "":
            row["beds_type"]= None

        if row["facility_standard_code1"] == "":
            row["facility_standard_code1"]= None

        if row["facility_standard_code2"] == "":
            row["facility_standard_code2"]= None

        if row["facility_standard_code3"] == "":
            row["facility_standard_code3"]= None

        if row["facility_standard_code4"] == "":
            row["facility_standard_code4"]= None

        if row["facility_standard_code5"] == "":
            row["facility_standard_code5"]= None

        if row["facility_standard_code6"] == "":
            row["facility_standard_code6"]= None

        if row["facility_standard_code7"] == "":
            row["facility_standard_code7"]= None

        if row["facility_standard_code8"] == "":
            row["facility_standard_code8"]= None

        if row["facility_standard_code9"] == "":
            row["facility_standard_code9"]= None

        if row["facility_standard_code10"] == "":
            row["facility_standard_code10"]= None

        if row["ultrasonic_coagulator_type"] == "":
            row["ultrasonic_coagulator_type"]= None

        if row["short_stay_surgery"] == "":
            row["short_stay_surgery"]= None

        if row["dental_type"] == "":
            row["dental_type"]= None

        if row["change_day"] == str(99999999):
            row["change_day"]= date.max
        elif row["change_day"] == "":
            row["change_day"]= None
        elif row["change_day"] == "0":
            row["change_day"]= None
        else:
            row["change_day"]=dt.strptime(row["change_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["abolition_day"] == str(99999999):
            row["abolition_day"]= date.max
        elif row["abolition_day"] == "":
            row["abolition_day"]= None
        elif row["abolition_day"] == "0":
            row["abolition_day"]= None
        else:
            row["abolition_day"]=dt.strptime(row["abolition_day"], "%Y%m%d").strftime("%Y-%m-%d")

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

        if row["code_table_number_chapter"] == "":
            row["code_table_number_chapter"]= None

        if row["code_table_number_department"] == "":
            row["code_table_number_department"]= None

        if row["code_table_number_type_number"] == "":
            row["code_table_number_type_number"]= None

        if row["code_table_number_branch_number"] == "":
            row["code_table_number_branch_number"]= None

        if row["code_table_number_item_number"] == "":
            row["code_table_number_item_number"]= None

        if row["bulletin_number_chapter"] == "":
            row["bulletin_number_chapter"]= None

        if row["bulletin_number_department"] == "":
            row["bulletin_number_department"]= None

        if row["bulletin_number_type_number"] == "":
            row["bulletin_number_type_number"]= None

        if row["bulletin_number_branch_number"] == "":
            row["bulletin_number_branch_number"]= None

        if row["bulletin_number_item_number"] == "":
            row["bulletin_number_item_number"]= None

        if row["age_add1_annotation_add_item_practice_code"] == "":
            row["age_add1_annotation_add_item_practice_code"]= None

        if row["age_add2_annotation_add_item_practice_code"] == "":
            row["age_add2_annotation_add_item_practice_code"]= None

        if row["age_add3_annotation_add_item_practice_code"] == "":
            row["age_add3_annotation_add_item_practice_code"]= None

        if row["age_add4_annotation_add_item_practice_code"] == "":
            row["age_add4_annotation_add_item_practice_code"]= None

        if row["transfer_related"] == "":
            row["transfer_related"]= None

        if row["external_fixator_addition"] == "":
            row["external_fixator_addition"]= None

        if row["ultrasonic_cutting_equipment_addition"] == "":
            row["ultrasonic_cutting_equipment_addition"]= None

        if row["left_atrial_appendage_closure_surgery_addition"] == "":
            row["left_atrial_appendage_closure_surgery_addition"]= None

        if row["improve_countermeasures_against_foreign_infections_additions"] == "":
            row["improve_countermeasures_against_foreign_infections_additions"]= None

        if row["otolaryngology_infant_treatment_addition"] == "":
            row["otolaryngology_infant_treatment_addition"]= None

        if row["otolaryngology_infant_treatment_drug_support_addition"] == "":
            row["otolaryngology_infant_treatment_drug_support_addition"]= None

        if row["incision_local_negative_treatment_device_addition"] == "":
            row["incision_local_negative_treatment_device_addition"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["reserve6"] == "":
            row["reserve6"]= None

        if row["reserve7"] == "":
            row["reserve7"]= None

        if row["reserve8"] == "":
            row["reserve8"]= None

        if row["reserve9"] == "":
            row["reserve9"]= None

        if row["reserve10"] == "":
            row["reserve10"]= None

        if row["reserve11"] == "":
            row["reserve11"]= None

        if row["reserve12"] == "":
            row["reserve12"]= None

        if row["reserve13"] == "":
            row["reserve13"]= None

        if row["reserve14"] == "":
            row["reserve14"]= None

        if row["reserve15"] == "":
            row["reserve15"]= None

        if row["reserve16"] == "":
            row["reserve16"]= None

        if row["reserve17"] == "":
            row["reserve17"]= None

        if row["reserve18"] == "":
            row["reserve18"]= None

        if row["reserve19"] == "":
            row["reserve19"]= None

        if row["reserve20"] == "":
            row["reserve20"]= None

        if row["reserve21"] == "":
            row["reserve21"]= None

        if row["reserve22"] == "":
            row["reserve22"]= None

        if row["reserve23"] == "":
            row["reserve23"]= None

        if row["reserve24"] == "":
            row["reserve24"]= None

        if row["reserve25"] == "":
            row["reserve25"]= None

        if row["reserve26"] == "":
            row["reserve26"]= None

        if row["reserve27"] == "":
            row["reserve27"]= None

class MasterDispensingResource(resources.ModelResource):
    change_type = Field(attribute="change_type",column_name="change_type")
    master_type = Field(attribute="master_type",column_name="master_type")
    dispensing_code = Field(attribute="dispensing_code",column_name="dispensing_code")
    dispensing_kanji_significant_digits = Field(attribute="dispensing_kanji_significant_digits",column_name="dispensing_kanji_significant_digits")
    dispensing_kanji_name = Field(attribute="dispensing_kanji_name",column_name="dispensing_kanji_name")
    dispensing_cana_significant_digits = Field(attribute="dispensing_cana_significant_digits",column_name="dispensing_cana_significant_digits")
    dispensing_cana_name = Field(attribute="dispensing_cana_name",column_name="dispensing_cana_name")
    receipt_mark_code = Field(attribute="receipt_mark_code",column_name="receipt_mark_code")
    receipt_display_order_code = Field(attribute="receipt_display_order_code",column_name="receipt_display_order_code")
    new_score_etc_identification = Field(attribute="new_score_etc_identification",column_name="new_score_etc_identification")
    dispensing_quantity_calculation_flag = Field(attribute="dispensing_quantity_calculation_flag",column_name="dispensing_quantity_calculation_flag")
    score_calculation_new_score = Field(attribute="score_calculation_new_score",column_name="score_calculation_new_score")
    score_calculation_etch_value_identification = Field(attribute="score_calculation_etch_value_identification",column_name="score_calculation_etch_value_identification")
    score_calculation_lower_limit = Field(attribute="score_calculation_lower_limit",column_name="score_calculation_lower_limit")
    score_calculation_upper_limit = Field(attribute="score_calculation_upper_limit",column_name="score_calculation_upper_limit")
    score_calculation_etch_value = Field(attribute="score_calculation_etch_value",column_name="score_calculation_etch_value")
    score_calculation_etch_score = Field(attribute="score_calculation_etch_score",column_name="score_calculation_etch_score")
    score_calculation_limits_error_process = Field(attribute="score_calculation_limits_error_process",column_name="score_calculation_limits_error_process")
    subtraction_act_type = Field(attribute="subtraction_act_type",column_name="subtraction_act_type")
    subtraction_subject_act_type = Field(attribute="subtraction_subject_act_type",column_name="subtraction_subject_act_type")
    dispensing_identification_type = Field(attribute="dispensing_identification_type",column_name="dispensing_identification_type")
    comprehensive_identification_code = Field(attribute="comprehensive_identification_code",column_name="comprehensive_identification_code")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    dispensing_type1 = Field(attribute="dispensing_type1",column_name="dispensing_type1")
    dispensing_type2 = Field(attribute="dispensing_type2",column_name="dispensing_type2")
    late_elderly_code = Field(attribute="late_elderly_code",column_name="late_elderly_code")
    facility_standard_code1 = Field(attribute="facility_standard_code1",column_name="facility_standard_code1")
    facility_standard_code2 = Field(attribute="facility_standard_code2",column_name="facility_standard_code2")
    facility_standard_code3 = Field(attribute="facility_standard_code3",column_name="facility_standard_code3")
    facility_standard_code4 = Field(attribute="facility_standard_code4",column_name="facility_standard_code4")
    facility_standard_code5 = Field(attribute="facility_standard_code5",column_name="facility_standard_code5")
    facility_standard_code6 = Field(attribute="facility_standard_code6",column_name="facility_standard_code6")
    facility_standard_code7 = Field(attribute="facility_standard_code7",column_name="facility_standard_code7")
    facility_standard_code8 = Field(attribute="facility_standard_code8",column_name="facility_standard_code8")
    facility_standard_code9 = Field(attribute="facility_standard_code9",column_name="facility_standard_code9")
    facility_standard_code10 = Field(attribute="facility_standard_code10",column_name="facility_standard_code10")
    receipt_unit_contradiction_type_code = Field(attribute="receipt_unit_contradiction_type_code",column_name="receipt_unit_contradiction_type_code")
    prescription_reception_unit_contradictory_type_code = Field(attribute="prescription_reception_unit_contradictory_type_code",column_name="prescription_reception_unit_contradictory_type_code")
    dispensing_unit_contraction_type_code = Field(attribute="dispensing_unit_contraction_type_code",column_name="dispensing_unit_contraction_type_code")
    special_drug = Field(attribute="special_drug",column_name="special_drug")
    time_add_code = Field(attribute="time_add_code",column_name="time_add_code")
    dosage_form = Field(attribute="dosage_form",column_name="dosage_form")
    receipt_unit_upper_limit = Field(attribute="receipt_unit_upper_limit",column_name="receipt_unit_upper_limit")
    receipt_unit_upper_limit_error_proces = Field(attribute="receipt_unit_upper_limit_error_proces",column_name="receipt_unit_upper_limit_error_proces")
    receipt_unit_lower_limit = Field(attribute="receipt_unit_lower_limit",column_name="receipt_unit_lower_limit")
    receipt_unit_lower_limit_error_proces = Field(attribute="receipt_unit_lower_limit_error_proces",column_name="receipt_unit_lower_limit_error_proces")
    annotation_add_code = Field(attribute="annotation_add_code",column_name="annotation_add_code")
    annotation_add_number = Field(attribute="annotation_add_number",column_name="annotation_add_number")
    limits_age_lower_age = Field(attribute="limits_age_lower_age",column_name="limits_age_lower_age")
    limits_age_upper_age = Field(attribute="limits_age_upper_age",column_name="limits_age_upper_age")
    pharmaceutical_management_fee_type = Field(attribute="pharmaceutical_management_fee_type",column_name="pharmaceutical_management_fee_type")
    bulletin_identification_type1 = Field(attribute="bulletin_identification_type1",column_name="bulletin_identification_type1")
    bulletin_identification_type2 = Field(attribute="bulletin_identification_type2",column_name="bulletin_identification_type2")
    old_score_etc_identification = Field(attribute="old_score_etc_identification",column_name="old_score_etc_identification")
    old_score_etc = Field(attribute="old_score_etc",column_name="old_score_etc")
    change_day = Field(attribute="change_day",column_name="change_day")
    abolition_day = Field(attribute="abolition_day",column_name="abolition_day")
    publication_order_number = Field(attribute="publication_order_number",column_name="publication_order_number")
    code_table_number = Field(attribute="code_table_number",column_name="code_table_number")
    bulletin_number = Field(attribute="bulletin_number",column_name="bulletin_number")
    transfer_related = Field(attribute="transfer_related",column_name="transfer_related")
    class Meta:
        model = models.MasterDispensing
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["change_type"] == "":
            row["change_type"]= None

        if row["dispensing_code"] == "":
            row["dispensing_code"]= None

        if row["dispensing_kanji_significant_digits"] == "":
            row["dispensing_kanji_significant_digits"]= None

        if row["dispensing_cana_significant_digits"] == "":
            row["dispensing_cana_significant_digits"]= None

        if row["receipt_mark_code"] == "":
            row["receipt_mark_code"]= None

        if row["receipt_display_order_code"] == "":
            row["receipt_display_order_code"]= None

        if row["new_score_etc_identification"] == "":
            row["new_score_etc_identification"]= None

        if row["dispensing_quantity_calculation_flag"] == "":
            row["dispensing_quantity_calculation_flag"]= None

        if row["score_calculation_new_score"] == "":
            row["score_calculation_new_score"]= None

        if row["score_calculation_etch_value_identification"] == "":
            row["score_calculation_etch_value_identification"]= None

        if row["score_calculation_lower_limit"] == "":
            row["score_calculation_lower_limit"]= None

        if row["score_calculation_upper_limit"] == "":
            row["score_calculation_upper_limit"]= None

        if row["score_calculation_etch_value"] == "":
            row["score_calculation_etch_value"]= None

        if row["score_calculation_etch_score"] == "":
            row["score_calculation_etch_score"]= None

        if row["score_calculation_limits_error_process"] == "":
            row["score_calculation_limits_error_process"]= None

        if row["subtraction_act_type"] == "":
            row["subtraction_act_type"]= None

        if row["subtraction_subject_act_type"] == "":
            row["subtraction_subject_act_type"]= None

        if row["dispensing_identification_type"] == "":
            row["dispensing_identification_type"]= None

        if row["comprehensive_identification_code"] == "":
            row["comprehensive_identification_code"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["dispensing_type1"] == "":
            row["dispensing_type1"]= None

        if row["dispensing_type2"] == "":
            row["dispensing_type2"]= None

        if row["late_elderly_code"] == "":
            row["late_elderly_code"]= None

        if row["facility_standard_code1"] == "":
            row["facility_standard_code1"]= None

        if row["facility_standard_code2"] == "":
            row["facility_standard_code2"]= None

        if row["facility_standard_code3"] == "":
            row["facility_standard_code3"]= None

        if row["facility_standard_code4"] == "":
            row["facility_standard_code4"]= None

        if row["facility_standard_code5"] == "":
            row["facility_standard_code5"]= None

        if row["facility_standard_code6"] == "":
            row["facility_standard_code6"]= None

        if row["facility_standard_code7"] == "":
            row["facility_standard_code7"]= None

        if row["facility_standard_code8"] == "":
            row["facility_standard_code8"]= None

        if row["facility_standard_code9"] == "":
            row["facility_standard_code9"]= None

        if row["facility_standard_code10"] == "":
            row["facility_standard_code10"]= None

        if row["receipt_unit_contradiction_type_code"] == "":
            row["receipt_unit_contradiction_type_code"]= None

        if row["prescription_reception_unit_contradictory_type_code"] == "":
            row["prescription_reception_unit_contradictory_type_code"]= None

        if row["dispensing_unit_contraction_type_code"] == "":
            row["dispensing_unit_contraction_type_code"]= None

        if row["special_drug"] == "":
            row["special_drug"]= None

        if row["time_add_code"] == "":
            row["time_add_code"]= None

        if row["dosage_form"] == "":
            row["dosage_form"]= None

        if row["receipt_unit_upper_limit"] == "":
            row["receipt_unit_upper_limit"]= None

        if row["receipt_unit_upper_limit_error_proces"] == "":
            row["receipt_unit_upper_limit_error_proces"]= None

        if row["receipt_unit_lower_limit"] == "":
            row["receipt_unit_lower_limit"]= None

        if row["receipt_unit_lower_limit_error_proces"] == "":
            row["receipt_unit_lower_limit_error_proces"]= None

        if row["annotation_add_code"] == "":
            row["annotation_add_code"]= None

        if row["pharmaceutical_management_fee_type"] == "":
            row["pharmaceutical_management_fee_type"]= None

        if row["bulletin_identification_type1"] == "":
            row["bulletin_identification_type1"]= None

        if row["bulletin_identification_type2"] == "":
            row["bulletin_identification_type2"]= None

        if row["old_score_etc_identification"] == "":
            row["old_score_etc_identification"]= None

        if row["old_score_etc"] == "":
            row["old_score_etc"]= None

        if row["change_day"] == "":
            row["change_day"]= None

        if row["abolition_day"] == "":
            row["abolition_day"]= None

        if row["publication_order_number"] == "":
            row["publication_order_number"]= None

        if row["code_table_number"] == "":
            row["code_table_number"]= None

        if row["bulletin_number"] == "":
            row["bulletin_number"]= None

        if row["transfer_related"] == "":
            row["transfer_related"]= None

class RecordReceiptInfoResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    examination_pay_institution = Field(attribute="examination_pay_institution",column_name="examination_pay_institution")
    prefectures = Field(attribute="prefectures",column_name="prefectures")
    score_sheet = Field(attribute="score_sheet",column_name="score_sheet")
    medical_institution_code = Field(attribute="medical_institution_code",column_name="medical_institution_code")
    reserve = Field(attribute="reserve",column_name="reserve")
    medical_institution_name = Field(attribute="medical_institution_name",column_name="medical_institution_name")
    billing_day = Field(attribute="billing_day",column_name="billing_day")
    notification = Field(attribute="notification",column_name="notification")
    multivolume_identifier_info = Field(attribute="multivolume_identifier_info",column_name="multivolume_identifier_info")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordReceiptInfo
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["examination_pay_institution"] == "":
            row["examination_pay_institution"]= None

        if row["prefectures"] == "":
            row["prefectures"]= None

        if row["score_sheet"] == "":
            row["score_sheet"]= None

        if row["medical_institution_code"] == "":
            row["medical_institution_code"]= None

        if row["reserve"] == "":
            row["reserve"]= None

        if row["billing_day"] == "":
            row["billing_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordMedicalInstitutionInfoResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    examination_pay_institution = Field(attribute="examination_pay_institution",column_name="examination_pay_institution")
    prefectures = Field(attribute="prefectures",column_name="prefectures")
    score_sheet = Field(attribute="score_sheet",column_name="score_sheet")
    medical_institution_code = Field(attribute="medical_institution_code",column_name="medical_institution_code")
    reserve = Field(attribute="reserve",column_name="reserve")
    billing_day = Field(attribute="billing_day",column_name="billing_day")
    phone_number = Field(attribute="phone_number",column_name="phone_number")
    notification = Field(attribute="notification",column_name="notification")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordMedicalInstitutionInfo
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["examination_pay_institution"] == "":
            row["examination_pay_institution"]= None

        if row["prefectures"] == "":
            row["prefectures"]= None

        if row["score_sheet"] == "":
            row["score_sheet"]= None

        if row["medical_institution_code"] == "":
            row["medical_institution_code"]= None

        if row["reserve"] == "":
            row["reserve"]= None

        if row["billing_day"] == "":
            row["billing_day"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordReceiptCommonResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    receipt_number = Field(attribute="receipt_number",column_name="receipt_number")
    receipt_identification = Field(attribute="receipt_identification",column_name="receipt_identification")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    sex_type = Field(attribute="sex_type",column_name="sex_type")
    birth_day = Field(attribute="birth_day",column_name="birth_day")
    benefit_ratio = Field(attribute="benefit_ratio",column_name="benefit_ratio")
    admission_day = Field(attribute="admission_day",column_name="admission_day")
    practice_start_day = Field(attribute="practice_start_day",column_name="practice_start_day")
    return_origin_yupe = Field(attribute="return_origin_yupe",column_name="return_origin_yupe")
    hospital_ward_type = Field(attribute="hospital_ward_type",column_name="hospital_ward_type")
    copayment = Field(attribute="copayment",column_name="copayment")
    receipt_special_remarks = Field(attribute="receipt_special_remarks",column_name="receipt_special_remarks")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    chart_number = Field(attribute="chart_number",column_name="chart_number")
    billing_info1 = Field(attribute="billing_info1",column_name="billing_info1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    future_hospital_billing = Field(attribute="future_hospital_billing",column_name="future_hospital_billing")
    search_number = Field(attribute="search_number",column_name="search_number")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    billing_info2 = Field(attribute="billing_info2",column_name="billing_info2")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    reserve6 = Field(attribute="reserve6",column_name="reserve6")
    cana_name = Field(attribute="cana_name",column_name="cana_name")
    patient_condition = Field(attribute="patient_condition",column_name="patient_condition")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordReceiptCommon
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["receipt_number"] == "":
            row["receipt_number"]= None

        if row["receipt_identification"] == "":
            row["receipt_identification"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["sex_type"] == "":
            row["sex_type"]= None

        if row["birth_day"] == "":
            row["birth_day"]= None

        if row["benefit_ratio"] == "":
            row["benefit_ratio"]= None

        if row["admission_day"] == "":
            row["admission_day"]= None

        if row["practice_start_day"] == "":
            row["practice_start_day"]= None

        if row["return_origin_yupe"] == "":
            row["return_origin_yupe"]= None

        if row["copayment"] == "":
            row["copayment"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["billing_info1"] == "":
            row["billing_info1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["future_hospital_billing"] == "":
            row["future_hospital_billing"]= None

        if row["search_number"] == "":
            row["search_number"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["reserve6"] == "":
            row["reserve6"]= None

        if row["patient_condition"] == "":
            row["patient_condition"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordInsurerResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    insurer_number = Field(attribute="insurer_number",column_name="insurer_number")
    insurer_card_code = Field(attribute="insurer_card_code",column_name="insurer_card_code")
    insurer_card_number = Field(attribute="insurer_card_number",column_name="insurer_card_number")
    practice_acrual_days = Field(attribute="practice_acrual_days",column_name="practice_acrual_days")
    total_score = Field(attribute="total_score",column_name="total_score")
    dietary_lifestyle_care_times = Field(attribute="dietary_lifestyle_care_times",column_name="dietary_lifestyle_care_times")
    dietary_lifestyle_care_total_amount = Field(attribute="dietary_lifestyle_care_total_amount",column_name="dietary_lifestyle_care_total_amount")
    professional_reasons = Field(attribute="professional_reasons",column_name="professional_reasons")
    certificate_number = Field(attribute="certificate_number",column_name="certificate_number")
    insurance_copayments = Field(attribute="insurance_copayments",column_name="insurance_copayments")
    exempt_type = Field(attribute="exempt_type",column_name="exempt_type")
    reduction_ratio = Field(attribute="reduction_ratio",column_name="reduction_ratio")
    reduction_amount = Field(attribute="reduction_amount",column_name="reduction_amount")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordInsurer
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_acrual_days"] == "":
            row["practice_acrual_days"]= None

        if row["total_score"] == "":
            row["total_score"]= None

        if row["dietary_lifestyle_care_times"] == "":
            row["dietary_lifestyle_care_times"]= None

        if row["dietary_lifestyle_care_total_amount"] == "":
            row["dietary_lifestyle_care_total_amount"]= None

        if row["professional_reasons"] == "":
            row["professional_reasons"]= None

        if row["certificate_number"] == "":
            row["certificate_number"]= None

        if row["insurance_copayments"] == "":
            row["insurance_copayments"]= None

        if row["exempt_type"] == "":
            row["exempt_type"]= None

        if row["reduction_ratio"] == "":
            row["reduction_ratio"]= None

        if row["reduction_amount"] == "":
            row["reduction_amount"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordPublicExpenseResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    payer_number = Field(attribute="payer_number",column_name="payer_number")
    recipient_number = Field(attribute="recipient_number",column_name="recipient_number")
    optional_benefit_type = Field(attribute="optional_benefit_type",column_name="optional_benefit_type")
    practice_acrual_days = Field(attribute="practice_acrual_days",column_name="practice_acrual_days")
    total_score = Field(attribute="total_score",column_name="total_score")
    copayment = Field(attribute="copayment",column_name="copayment")
    public_expense_benefit_copayment = Field(attribute="public_expense_benefit_copayment",column_name="public_expense_benefit_copayment")
    dietary_lifestyle_care_times = Field(attribute="dietary_lifestyle_care_times",column_name="dietary_lifestyle_care_times")
    dietary_lifestyle_care_total_amount = Field(attribute="dietary_lifestyle_care_total_amount",column_name="dietary_lifestyle_care_total_amount")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordPublicExpense
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["recipient_number"] == "":
            row["recipient_number"]= None

        if row["optional_benefit_type"] == "":
            row["optional_benefit_type"]= None

        if row["practice_acrual_days"] == "":
            row["practice_acrual_days"]= None

        if row["total_score"] == "":
            row["total_score"]= None

        if row["copayment"] == "":
            row["copayment"]= None

        if row["public_expense_benefit_copayment"] == "":
            row["public_expense_benefit_copayment"]= None

        if row["dietary_lifestyle_care_times"] == "":
            row["dietary_lifestyle_care_times"]= None

        if row["dietary_lifestyle_care_total_amount"] == "":
            row["dietary_lifestyle_care_total_amount"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordStatusCheckResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    payer_class = Field(attribute="payer_class",column_name="payer_class")
    confirmation_type = Field(attribute="confirmation_type",column_name="confirmation_type")
    insurer_number_etc = Field(attribute="insurer_number_etc",column_name="insurer_number_etc")
    insurer_card_code_status_check = Field(attribute="insurer_card_code_status_check",column_name="insurer_card_code_status_check")
    insurer_card_number_status_check = Field(attribute="insurer_card_number_status_check",column_name="insurer_card_number_status_check")
    branch_number = Field(attribute="branch_number",column_name="branch_number")
    recipient_id = Field(attribute="recipient_id",column_name="recipient_id")
    reserve = Field(attribute="reserve",column_name="reserve")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordStatusCheck
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["payer_class"] == "":
            row["payer_class"]= None

        if row["confirmation_type"] == "":
            row["confirmation_type"]= None

        if row["branch_number"] == "":
            row["branch_number"]= None

        if row["recipient_id"] == "":
            row["recipient_id"]= None

        if row["reserve"] == "":
            row["reserve"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordReceiptDayResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    info1 = Field(attribute="info1",column_name="info1")
    info2 = Field(attribute="info2",column_name="info2")
    info3 = Field(attribute="info3",column_name="info3")
    info4 = Field(attribute="info4",column_name="info4")
    info5 = Field(attribute="info5",column_name="info5")
    info6 = Field(attribute="info6",column_name="info6")
    info7 = Field(attribute="info7",column_name="info7")
    info8 = Field(attribute="info8",column_name="info8")
    info9 = Field(attribute="info9",column_name="info9")
    info10 = Field(attribute="info10",column_name="info10")
    info11 = Field(attribute="info11",column_name="info11")
    info12 = Field(attribute="info12",column_name="info12")
    info13 = Field(attribute="info13",column_name="info13")
    info14 = Field(attribute="info14",column_name="info14")
    info15 = Field(attribute="info15",column_name="info15")
    info16 = Field(attribute="info16",column_name="info16")
    info17 = Field(attribute="info17",column_name="info17")
    info18 = Field(attribute="info18",column_name="info18")
    info19 = Field(attribute="info19",column_name="info19")
    info20 = Field(attribute="info20",column_name="info20")
    info21 = Field(attribute="info21",column_name="info21")
    info22 = Field(attribute="info22",column_name="info22")
    info23 = Field(attribute="info23",column_name="info23")
    info24 = Field(attribute="info24",column_name="info24")
    info25 = Field(attribute="info25",column_name="info25")
    info26 = Field(attribute="info26",column_name="info26")
    info27 = Field(attribute="info27",column_name="info27")
    info28 = Field(attribute="info28",column_name="info28")
    info29 = Field(attribute="info29",column_name="info29")
    info30 = Field(attribute="info30",column_name="info30")
    info31 = Field(attribute="info31",column_name="info31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordReceiptDay
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["payer_type"] == "":
            row["payer_type"]= None

        if row["info1"] == "":
            row["info1"]= None

        if row["info2"] == "":
            row["info2"]= None

        if row["info3"] == "":
            row["info3"]= None

        if row["info4"] == "":
            row["info4"]= None

        if row["info5"] == "":
            row["info5"]= None

        if row["info6"] == "":
            row["info6"]= None

        if row["info7"] == "":
            row["info7"]= None

        if row["info8"] == "":
            row["info8"]= None

        if row["info9"] == "":
            row["info9"]= None

        if row["info10"] == "":
            row["info10"]= None

        if row["info11"] == "":
            row["info11"]= None

        if row["info12"] == "":
            row["info12"]= None

        if row["info13"] == "":
            row["info13"]= None

        if row["info14"] == "":
            row["info14"]= None

        if row["info15"] == "":
            row["info15"]= None

        if row["info16"] == "":
            row["info16"]= None

        if row["info17"] == "":
            row["info17"]= None

        if row["info18"] == "":
            row["info18"]= None

        if row["info19"] == "":
            row["info19"]= None

        if row["info20"] == "":
            row["info20"]= None

        if row["info21"] == "":
            row["info21"]= None

        if row["info22"] == "":
            row["info22"]= None

        if row["info23"] == "":
            row["info23"]= None

        if row["info24"] == "":
            row["info24"]= None

        if row["info25"] == "":
            row["info25"]= None

        if row["info26"] == "":
            row["info26"]= None

        if row["info27"] == "":
            row["info27"]= None

        if row["info28"] == "":
            row["info28"]= None

        if row["info29"] == "":
            row["info29"]= None

        if row["info30"] == "":
            row["info30"]= None

        if row["info31"] == "":
            row["info31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordCounterAmountResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    counter_amount_type = Field(attribute="counter_amount_type",column_name="counter_amount_type")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    reserve6 = Field(attribute="reserve6",column_name="reserve6")
    reserve7 = Field(attribute="reserve7",column_name="reserve7")
    reserve8 = Field(attribute="reserve8",column_name="reserve8")
    reserve9 = Field(attribute="reserve9",column_name="reserve9")
    reserve10 = Field(attribute="reserve10",column_name="reserve10")
    reserve11 = Field(attribute="reserve11",column_name="reserve11")
    reserve12 = Field(attribute="reserve12",column_name="reserve12")
    reserve13 = Field(attribute="reserve13",column_name="reserve13")
    reserve14 = Field(attribute="reserve14",column_name="reserve14")
    reserve15 = Field(attribute="reserve15",column_name="reserve15")
    reserve16 = Field(attribute="reserve16",column_name="reserve16")
    reserve17 = Field(attribute="reserve17",column_name="reserve17")
    reserve18 = Field(attribute="reserve18",column_name="reserve18")
    reserve19 = Field(attribute="reserve19",column_name="reserve19")
    reserve20 = Field(attribute="reserve20",column_name="reserve20")
    reserve21 = Field(attribute="reserve21",column_name="reserve21")
    reserve22 = Field(attribute="reserve22",column_name="reserve22")
    reserve23 = Field(attribute="reserve23",column_name="reserve23")
    reserve24 = Field(attribute="reserve24",column_name="reserve24")
    reserve25 = Field(attribute="reserve25",column_name="reserve25")
    reserve26 = Field(attribute="reserve26",column_name="reserve26")
    reserve27 = Field(attribute="reserve27",column_name="reserve27")
    reserve28 = Field(attribute="reserve28",column_name="reserve28")
    reserve29 = Field(attribute="reserve29",column_name="reserve29")
    reserve30 = Field(attribute="reserve30",column_name="reserve30")
    reserve31 = Field(attribute="reserve31",column_name="reserve31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordCounterAmount
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["counter_amount_type"] == "":
            row["counter_amount_type"]= None

        if row["reserve1"] == "":
            row["reserve1"]= None

        if row["reserve2"] == "":
            row["reserve2"]= None

        if row["reserve3"] == "":
            row["reserve3"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["reserve6"] == "":
            row["reserve6"]= None

        if row["reserve7"] == "":
            row["reserve7"]= None

        if row["reserve8"] == "":
            row["reserve8"]= None

        if row["reserve9"] == "":
            row["reserve9"]= None

        if row["reserve10"] == "":
            row["reserve10"]= None

        if row["reserve11"] == "":
            row["reserve11"]= None

        if row["reserve12"] == "":
            row["reserve12"]= None

        if row["reserve13"] == "":
            row["reserve13"]= None

        if row["reserve14"] == "":
            row["reserve14"]= None

        if row["reserve15"] == "":
            row["reserve15"]= None

        if row["reserve16"] == "":
            row["reserve16"]= None

        if row["reserve17"] == "":
            row["reserve17"]= None

        if row["reserve18"] == "":
            row["reserve18"]= None

        if row["reserve19"] == "":
            row["reserve19"]= None

        if row["reserve20"] == "":
            row["reserve20"]= None

        if row["reserve21"] == "":
            row["reserve21"]= None

        if row["reserve22"] == "":
            row["reserve22"]= None

        if row["reserve23"] == "":
            row["reserve23"]= None

        if row["reserve24"] == "":
            row["reserve24"]= None

        if row["reserve25"] == "":
            row["reserve25"]= None

        if row["reserve26"] == "":
            row["reserve26"]= None

        if row["reserve27"] == "":
            row["reserve27"]= None

        if row["reserve28"] == "":
            row["reserve28"]= None

        if row["reserve29"] == "":
            row["reserve29"]= None

        if row["reserve30"] == "":
            row["reserve30"]= None

        if row["reserve31"] == "":
            row["reserve31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordDiseasePositionResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    start_practice = Field(attribute="start_practice",column_name="start_practice")
    transcription_type = Field(attribute="transcription_type",column_name="transcription_type")
    dentation_code_diseaase = Field(attribute="dentation_code_diseaase",column_name="dentation_code_diseaase")
    disease_name_code = Field(attribute="disease_name_code",column_name="disease_name_code")
    modifier_code = Field(attribute="modifier_code",column_name="modifier_code")
    disease_name = Field(attribute="disease_name",column_name="disease_name")
    comorbidities_number = Field(attribute="comorbidities_number",column_name="comorbidities_number")
    disease_condition_transition = Field(attribute="disease_condition_transition",column_name="disease_condition_transition")
    major_disease = Field(attribute="major_disease",column_name="major_disease")
    comment_code = Field(attribute="comment_code",column_name="comment_code")
    supplementary_comment = Field(attribute="supplementary_comment",column_name="supplementary_comment")
    dentation_code_comment = Field(attribute="dentation_code_comment",column_name="dentation_code_comment")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordDiseasePosition
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["start_practice"] == "":
            row["start_practice"]= None

        if row["transcription_type"] == "":
            row["transcription_type"]= None

        if row["disease_name_code"] == "":
            row["disease_name_code"]= None

        if row["comorbidities_number"] == "":
            row["comorbidities_number"]= None

        if row["disease_condition_transition"] == "":
            row["disease_condition_transition"]= None

        if row["major_disease"] == "":
            row["major_disease"]= None

        if row["comment_code"] == "":
            row["comment_code"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordDentalPracticeResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    practice_identification = Field(attribute="practice_identification",column_name="practice_identification")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    practice_code = Field(attribute="practice_code",column_name="practice_code")
    practice_volume_data1 = Field(attribute="practice_volume_data1",column_name="practice_volume_data1")
    practice_volume_data2 = Field(attribute="practice_volume_data2",column_name="practice_volume_data2")
    add_code1 = Field(attribute="add_code1",column_name="add_code1")
    add_volume_data1 = Field(attribute="add_volume_data1",column_name="add_volume_data1")
    add_code2 = Field(attribute="add_code2",column_name="add_code2")
    add_volume_data2 = Field(attribute="add_volume_data2",column_name="add_volume_data2")
    add_code3 = Field(attribute="add_code3",column_name="add_code3")
    add_volume_data3 = Field(attribute="add_volume_data3",column_name="add_volume_data3")
    add_code4 = Field(attribute="add_code4",column_name="add_code4")
    add_volume_data4 = Field(attribute="add_volume_data4",column_name="add_volume_data4")
    add_code5 = Field(attribute="add_code5",column_name="add_code5")
    add_volume_data5 = Field(attribute="add_volume_data5",column_name="add_volume_data5")
    add_code6 = Field(attribute="add_code6",column_name="add_code6")
    add_volume_data6 = Field(attribute="add_volume_data6",column_name="add_volume_data6")
    add_code7 = Field(attribute="add_code7",column_name="add_code7")
    add_volume_data7 = Field(attribute="add_volume_data7",column_name="add_volume_data7")
    add_code8 = Field(attribute="add_code8",column_name="add_code8")
    add_volume_data8 = Field(attribute="add_volume_data8",column_name="add_volume_data8")
    add_code9 = Field(attribute="add_code9",column_name="add_code9")
    add_volume_data9 = Field(attribute="add_volume_data9",column_name="add_volume_data9")
    add_code10 = Field(attribute="add_code10",column_name="add_code10")
    add_volume_data10 = Field(attribute="add_volume_data10",column_name="add_volume_data10")
    add_code11 = Field(attribute="add_code11",column_name="add_code11")
    add_volume_data11 = Field(attribute="add_volume_data11",column_name="add_volume_data11")
    add_code12 = Field(attribute="add_code12",column_name="add_code12")
    add_volume_data12 = Field(attribute="add_volume_data12",column_name="add_volume_data12")
    add_code13 = Field(attribute="add_code13",column_name="add_code13")
    add_volume_data13 = Field(attribute="add_volume_data13",column_name="add_volume_data13")
    add_code14 = Field(attribute="add_code14",column_name="add_code14")
    add_volume_data14 = Field(attribute="add_volume_data14",column_name="add_volume_data14")
    add_code15 = Field(attribute="add_code15",column_name="add_code15")
    add_volume_data15 = Field(attribute="add_volume_data15",column_name="add_volume_data15")
    add_code16 = Field(attribute="add_code16",column_name="add_code16")
    add_volume_data16 = Field(attribute="add_volume_data16",column_name="add_volume_data16")
    add_code17 = Field(attribute="add_code17",column_name="add_code17")
    add_volume_data17 = Field(attribute="add_volume_data17",column_name="add_volume_data17")
    add_code18 = Field(attribute="add_code18",column_name="add_code18")
    add_volume_data18 = Field(attribute="add_volume_data18",column_name="add_volume_data18")
    add_code19 = Field(attribute="add_code19",column_name="add_code19")
    add_volume_data19 = Field(attribute="add_volume_data19",column_name="add_volume_data19")
    add_code20 = Field(attribute="add_code20",column_name="add_code20")
    add_volume_data20 = Field(attribute="add_volume_data20",column_name="add_volume_data20")
    add_code21 = Field(attribute="add_code21",column_name="add_code21")
    add_volume_data21 = Field(attribute="add_volume_data21",column_name="add_volume_data21")
    add_code22 = Field(attribute="add_code22",column_name="add_code22")
    add_volume_data22 = Field(attribute="add_volume_data22",column_name="add_volume_data22")
    add_code23 = Field(attribute="add_code23",column_name="add_code23")
    add_volume_data23 = Field(attribute="add_volume_data23",column_name="add_volume_data23")
    add_code24 = Field(attribute="add_code24",column_name="add_code24")
    add_volume_data24 = Field(attribute="add_volume_data24",column_name="add_volume_data24")
    add_code25 = Field(attribute="add_code25",column_name="add_code25")
    add_volume_data25 = Field(attribute="add_volume_data25",column_name="add_volume_data25")
    add_code26 = Field(attribute="add_code26",column_name="add_code26")
    add_volume_data26 = Field(attribute="add_volume_data26",column_name="add_volume_data26")
    add_code27 = Field(attribute="add_code27",column_name="add_code27")
    add_volume_data27 = Field(attribute="add_volume_data27",column_name="add_volume_data27")
    add_code28 = Field(attribute="add_code28",column_name="add_code28")
    add_volume_data28 = Field(attribute="add_volume_data28",column_name="add_volume_data28")
    add_code29 = Field(attribute="add_code29",column_name="add_code29")
    add_volume_data29 = Field(attribute="add_volume_data29",column_name="add_volume_data29")
    add_code30 = Field(attribute="add_code30",column_name="add_code30")
    add_volume_data30 = Field(attribute="add_volume_data30",column_name="add_volume_data30")
    add_code31 = Field(attribute="add_code31",column_name="add_code31")
    add_volume_data31 = Field(attribute="add_volume_data31",column_name="add_volume_data31")
    add_code32 = Field(attribute="add_code32",column_name="add_code32")
    add_volume_data32 = Field(attribute="add_volume_data32",column_name="add_volume_data32")
    add_code33 = Field(attribute="add_code33",column_name="add_code33")
    add_volume_data33 = Field(attribute="add_volume_data33",column_name="add_volume_data33")
    add_code34 = Field(attribute="add_code34",column_name="add_code34")
    add_volume_data34 = Field(attribute="add_volume_data34",column_name="add_volume_data34")
    add_code35 = Field(attribute="add_code35",column_name="add_code35")
    add_volume_data35 = Field(attribute="add_volume_data35",column_name="add_volume_data35")
    score = Field(attribute="score",column_name="score")
    count = Field(attribute="count",column_name="count")
    calculation_day_info1 = Field(attribute="calculation_day_info1",column_name="calculation_day_info1")
    calculation_day_info2 = Field(attribute="calculation_day_info2",column_name="calculation_day_info2")
    calculation_day_info3 = Field(attribute="calculation_day_info3",column_name="calculation_day_info3")
    calculation_day_info4 = Field(attribute="calculation_day_info4",column_name="calculation_day_info4")
    calculation_day_info5 = Field(attribute="calculation_day_info5",column_name="calculation_day_info5")
    calculation_day_info6 = Field(attribute="calculation_day_info6",column_name="calculation_day_info6")
    calculation_day_info7 = Field(attribute="calculation_day_info7",column_name="calculation_day_info7")
    calculation_day_info8 = Field(attribute="calculation_day_info8",column_name="calculation_day_info8")
    calculation_day_info9 = Field(attribute="calculation_day_info9",column_name="calculation_day_info9")
    calculation_day_info10 = Field(attribute="calculation_day_info10",column_name="calculation_day_info10")
    calculation_day_info11 = Field(attribute="calculation_day_info11",column_name="calculation_day_info11")
    calculation_day_info12 = Field(attribute="calculation_day_info12",column_name="calculation_day_info12")
    calculation_day_info13 = Field(attribute="calculation_day_info13",column_name="calculation_day_info13")
    calculation_day_info14 = Field(attribute="calculation_day_info14",column_name="calculation_day_info14")
    calculation_day_info15 = Field(attribute="calculation_day_info15",column_name="calculation_day_info15")
    calculation_day_info16 = Field(attribute="calculation_day_info16",column_name="calculation_day_info16")
    calculation_day_info17 = Field(attribute="calculation_day_info17",column_name="calculation_day_info17")
    calculation_day_info18 = Field(attribute="calculation_day_info18",column_name="calculation_day_info18")
    calculation_day_info19 = Field(attribute="calculation_day_info19",column_name="calculation_day_info19")
    calculation_day_info20 = Field(attribute="calculation_day_info20",column_name="calculation_day_info20")
    calculation_day_info21 = Field(attribute="calculation_day_info21",column_name="calculation_day_info21")
    calculation_day_info22 = Field(attribute="calculation_day_info22",column_name="calculation_day_info22")
    calculation_day_info23 = Field(attribute="calculation_day_info23",column_name="calculation_day_info23")
    calculation_day_info24 = Field(attribute="calculation_day_info24",column_name="calculation_day_info24")
    calculation_day_info25 = Field(attribute="calculation_day_info25",column_name="calculation_day_info25")
    calculation_day_info26 = Field(attribute="calculation_day_info26",column_name="calculation_day_info26")
    calculation_day_info27 = Field(attribute="calculation_day_info27",column_name="calculation_day_info27")
    calculation_day_info28 = Field(attribute="calculation_day_info28",column_name="calculation_day_info28")
    calculation_day_info29 = Field(attribute="calculation_day_info29",column_name="calculation_day_info29")
    calculation_day_info30 = Field(attribute="calculation_day_info30",column_name="calculation_day_info30")
    calculation_day_info31 = Field(attribute="calculation_day_info31",column_name="calculation_day_info31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordDentalPractice
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_identification"] == "":
            row["practice_identification"]= None

        if row["practice_code"] == "":
            row["practice_code"]= None

        if row["practice_volume_data1"] == "":
            row["practice_volume_data1"]= None

        if row["practice_volume_data2"] == "":
            row["practice_volume_data2"]= None

        if row["add_volume_data1"] == "":
            row["add_volume_data1"]= None

        if row["add_volume_data2"] == "":
            row["add_volume_data2"]= None

        if row["add_volume_data3"] == "":
            row["add_volume_data3"]= None

        if row["add_volume_data4"] == "":
            row["add_volume_data4"]= None

        if row["add_volume_data5"] == "":
            row["add_volume_data5"]= None

        if row["add_volume_data6"] == "":
            row["add_volume_data6"]= None

        if row["add_volume_data7"] == "":
            row["add_volume_data7"]= None

        if row["add_volume_data8"] == "":
            row["add_volume_data8"]= None

        if row["add_volume_data9"] == "":
            row["add_volume_data9"]= None

        if row["add_volume_data10"] == "":
            row["add_volume_data10"]= None

        if row["add_volume_data11"] == "":
            row["add_volume_data11"]= None

        if row["add_volume_data12"] == "":
            row["add_volume_data12"]= None

        if row["add_volume_data13"] == "":
            row["add_volume_data13"]= None

        if row["add_volume_data14"] == "":
            row["add_volume_data14"]= None

        if row["add_volume_data15"] == "":
            row["add_volume_data15"]= None

        if row["add_volume_data16"] == "":
            row["add_volume_data16"]= None

        if row["add_volume_data17"] == "":
            row["add_volume_data17"]= None

        if row["add_volume_data18"] == "":
            row["add_volume_data18"]= None

        if row["add_volume_data19"] == "":
            row["add_volume_data19"]= None

        if row["add_volume_data20"] == "":
            row["add_volume_data20"]= None

        if row["add_volume_data21"] == "":
            row["add_volume_data21"]= None

        if row["add_volume_data22"] == "":
            row["add_volume_data22"]= None

        if row["add_volume_data23"] == "":
            row["add_volume_data23"]= None

        if row["add_volume_data24"] == "":
            row["add_volume_data24"]= None

        if row["add_volume_data25"] == "":
            row["add_volume_data25"]= None

        if row["add_volume_data26"] == "":
            row["add_volume_data26"]= None

        if row["add_volume_data27"] == "":
            row["add_volume_data27"]= None

        if row["add_volume_data28"] == "":
            row["add_volume_data28"]= None

        if row["add_volume_data29"] == "":
            row["add_volume_data29"]= None

        if row["add_volume_data30"] == "":
            row["add_volume_data30"]= None

        if row["add_volume_data31"] == "":
            row["add_volume_data31"]= None

        if row["add_volume_data32"] == "":
            row["add_volume_data32"]= None

        if row["add_volume_data33"] == "":
            row["add_volume_data33"]= None

        if row["add_volume_data34"] == "":
            row["add_volume_data34"]= None

        if row["add_volume_data35"] == "":
            row["add_volume_data35"]= None

        if row["score"] == "":
            row["score"]= None

        if row["count"] == "":
            row["count"]= None

        if row["calculation_day_info1"] == "":
            row["calculation_day_info1"]= None

        if row["calculation_day_info2"] == "":
            row["calculation_day_info2"]= None

        if row["calculation_day_info3"] == "":
            row["calculation_day_info3"]= None

        if row["calculation_day_info4"] == "":
            row["calculation_day_info4"]= None

        if row["calculation_day_info5"] == "":
            row["calculation_day_info5"]= None

        if row["calculation_day_info6"] == "":
            row["calculation_day_info6"]= None

        if row["calculation_day_info7"] == "":
            row["calculation_day_info7"]= None

        if row["calculation_day_info8"] == "":
            row["calculation_day_info8"]= None

        if row["calculation_day_info9"] == "":
            row["calculation_day_info9"]= None

        if row["calculation_day_info10"] == "":
            row["calculation_day_info10"]= None

        if row["calculation_day_info11"] == "":
            row["calculation_day_info11"]= None

        if row["calculation_day_info12"] == "":
            row["calculation_day_info12"]= None

        if row["calculation_day_info13"] == "":
            row["calculation_day_info13"]= None

        if row["calculation_day_info14"] == "":
            row["calculation_day_info14"]= None

        if row["calculation_day_info15"] == "":
            row["calculation_day_info15"]= None

        if row["calculation_day_info16"] == "":
            row["calculation_day_info16"]= None

        if row["calculation_day_info17"] == "":
            row["calculation_day_info17"]= None

        if row["calculation_day_info18"] == "":
            row["calculation_day_info18"]= None

        if row["calculation_day_info19"] == "":
            row["calculation_day_info19"]= None

        if row["calculation_day_info20"] == "":
            row["calculation_day_info20"]= None

        if row["calculation_day_info21"] == "":
            row["calculation_day_info21"]= None

        if row["calculation_day_info22"] == "":
            row["calculation_day_info22"]= None

        if row["calculation_day_info23"] == "":
            row["calculation_day_info23"]= None

        if row["calculation_day_info24"] == "":
            row["calculation_day_info24"]= None

        if row["calculation_day_info25"] == "":
            row["calculation_day_info25"]= None

        if row["calculation_day_info26"] == "":
            row["calculation_day_info26"]= None

        if row["calculation_day_info27"] == "":
            row["calculation_day_info27"]= None

        if row["calculation_day_info28"] == "":
            row["calculation_day_info28"]= None

        if row["calculation_day_info29"] == "":
            row["calculation_day_info29"]= None

        if row["calculation_day_info30"] == "":
            row["calculation_day_info30"]= None

        if row["calculation_day_info31"] == "":
            row["calculation_day_info31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordPracticeResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    practice_identification = Field(attribute="practice_identification",column_name="practice_identification")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    practice_code = Field(attribute="practice_code",column_name="practice_code")
    volume_data = Field(attribute="volume_data",column_name="volume_data")
    score = Field(attribute="score",column_name="score")
    count = Field(attribute="count",column_name="count")
    calculation_day_info1 = Field(attribute="calculation_day_info1",column_name="calculation_day_info1")
    calculation_day_info2 = Field(attribute="calculation_day_info2",column_name="calculation_day_info2")
    calculation_day_info3 = Field(attribute="calculation_day_info3",column_name="calculation_day_info3")
    calculation_day_info4 = Field(attribute="calculation_day_info4",column_name="calculation_day_info4")
    calculation_day_info5 = Field(attribute="calculation_day_info5",column_name="calculation_day_info5")
    calculation_day_info6 = Field(attribute="calculation_day_info6",column_name="calculation_day_info6")
    calculation_day_info7 = Field(attribute="calculation_day_info7",column_name="calculation_day_info7")
    calculation_day_info8 = Field(attribute="calculation_day_info8",column_name="calculation_day_info8")
    calculation_day_info9 = Field(attribute="calculation_day_info9",column_name="calculation_day_info9")
    calculation_day_info10 = Field(attribute="calculation_day_info10",column_name="calculation_day_info10")
    calculation_day_info11 = Field(attribute="calculation_day_info11",column_name="calculation_day_info11")
    calculation_day_info12 = Field(attribute="calculation_day_info12",column_name="calculation_day_info12")
    calculation_day_info13 = Field(attribute="calculation_day_info13",column_name="calculation_day_info13")
    calculation_day_info14 = Field(attribute="calculation_day_info14",column_name="calculation_day_info14")
    calculation_day_info15 = Field(attribute="calculation_day_info15",column_name="calculation_day_info15")
    calculation_day_info16 = Field(attribute="calculation_day_info16",column_name="calculation_day_info16")
    calculation_day_info17 = Field(attribute="calculation_day_info17",column_name="calculation_day_info17")
    calculation_day_info18 = Field(attribute="calculation_day_info18",column_name="calculation_day_info18")
    calculation_day_info19 = Field(attribute="calculation_day_info19",column_name="calculation_day_info19")
    calculation_day_info20 = Field(attribute="calculation_day_info20",column_name="calculation_day_info20")
    calculation_day_info21 = Field(attribute="calculation_day_info21",column_name="calculation_day_info21")
    calculation_day_info22 = Field(attribute="calculation_day_info22",column_name="calculation_day_info22")
    calculation_day_info23 = Field(attribute="calculation_day_info23",column_name="calculation_day_info23")
    calculation_day_info24 = Field(attribute="calculation_day_info24",column_name="calculation_day_info24")
    calculation_day_info25 = Field(attribute="calculation_day_info25",column_name="calculation_day_info25")
    calculation_day_info26 = Field(attribute="calculation_day_info26",column_name="calculation_day_info26")
    calculation_day_info27 = Field(attribute="calculation_day_info27",column_name="calculation_day_info27")
    calculation_day_info28 = Field(attribute="calculation_day_info28",column_name="calculation_day_info28")
    calculation_day_info29 = Field(attribute="calculation_day_info29",column_name="calculation_day_info29")
    calculation_day_info30 = Field(attribute="calculation_day_info30",column_name="calculation_day_info30")
    calculation_day_info31 = Field(attribute="calculation_day_info31",column_name="calculation_day_info31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordPractice
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_identification"] == "":
            row["practice_identification"]= None

        if row["practice_code"] == "":
            row["practice_code"]= None

        if row["volume_data"] == "":
            row["volume_data"]= None

        if row["score"] == "":
            row["score"]= None

        if row["count"] == "":
            row["count"]= None

        if row["calculation_day_info1"] == "":
            row["calculation_day_info1"]= None

        if row["calculation_day_info2"] == "":
            row["calculation_day_info2"]= None

        if row["calculation_day_info3"] == "":
            row["calculation_day_info3"]= None

        if row["calculation_day_info4"] == "":
            row["calculation_day_info4"]= None

        if row["calculation_day_info5"] == "":
            row["calculation_day_info5"]= None

        if row["calculation_day_info6"] == "":
            row["calculation_day_info6"]= None

        if row["calculation_day_info7"] == "":
            row["calculation_day_info7"]= None

        if row["calculation_day_info8"] == "":
            row["calculation_day_info8"]= None

        if row["calculation_day_info9"] == "":
            row["calculation_day_info9"]= None

        if row["calculation_day_info10"] == "":
            row["calculation_day_info10"]= None

        if row["calculation_day_info11"] == "":
            row["calculation_day_info11"]= None

        if row["calculation_day_info12"] == "":
            row["calculation_day_info12"]= None

        if row["calculation_day_info13"] == "":
            row["calculation_day_info13"]= None

        if row["calculation_day_info14"] == "":
            row["calculation_day_info14"]= None

        if row["calculation_day_info15"] == "":
            row["calculation_day_info15"]= None

        if row["calculation_day_info16"] == "":
            row["calculation_day_info16"]= None

        if row["calculation_day_info17"] == "":
            row["calculation_day_info17"]= None

        if row["calculation_day_info18"] == "":
            row["calculation_day_info18"]= None

        if row["calculation_day_info19"] == "":
            row["calculation_day_info19"]= None

        if row["calculation_day_info20"] == "":
            row["calculation_day_info20"]= None

        if row["calculation_day_info21"] == "":
            row["calculation_day_info21"]= None

        if row["calculation_day_info22"] == "":
            row["calculation_day_info22"]= None

        if row["calculation_day_info23"] == "":
            row["calculation_day_info23"]= None

        if row["calculation_day_info24"] == "":
            row["calculation_day_info24"]= None

        if row["calculation_day_info25"] == "":
            row["calculation_day_info25"]= None

        if row["calculation_day_info26"] == "":
            row["calculation_day_info26"]= None

        if row["calculation_day_info27"] == "":
            row["calculation_day_info27"]= None

        if row["calculation_day_info28"] == "":
            row["calculation_day_info28"]= None

        if row["calculation_day_info29"] == "":
            row["calculation_day_info29"]= None

        if row["calculation_day_info30"] == "":
            row["calculation_day_info30"]= None

        if row["calculation_day_info31"] == "":
            row["calculation_day_info31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordDrugResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    practice_identification = Field(attribute="practice_identification",column_name="practice_identification")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    drug_code = Field(attribute="drug_code",column_name="drug_code")
    usage = Field(attribute="usage",column_name="usage")
    score = Field(attribute="score",column_name="score")
    count = Field(attribute="count",column_name="count")
    drug_type = Field(attribute="drug_type",column_name="drug_type")
    calculation_day_info1 = Field(attribute="calculation_day_info1",column_name="calculation_day_info1")
    calculation_day_info2 = Field(attribute="calculation_day_info2",column_name="calculation_day_info2")
    calculation_day_info3 = Field(attribute="calculation_day_info3",column_name="calculation_day_info3")
    calculation_day_info4 = Field(attribute="calculation_day_info4",column_name="calculation_day_info4")
    calculation_day_info5 = Field(attribute="calculation_day_info5",column_name="calculation_day_info5")
    calculation_day_info6 = Field(attribute="calculation_day_info6",column_name="calculation_day_info6")
    calculation_day_info7 = Field(attribute="calculation_day_info7",column_name="calculation_day_info7")
    calculation_day_info8 = Field(attribute="calculation_day_info8",column_name="calculation_day_info8")
    calculation_day_info9 = Field(attribute="calculation_day_info9",column_name="calculation_day_info9")
    calculation_day_info10 = Field(attribute="calculation_day_info10",column_name="calculation_day_info10")
    calculation_day_info11 = Field(attribute="calculation_day_info11",column_name="calculation_day_info11")
    calculation_day_info12 = Field(attribute="calculation_day_info12",column_name="calculation_day_info12")
    calculation_day_info13 = Field(attribute="calculation_day_info13",column_name="calculation_day_info13")
    calculation_day_info14 = Field(attribute="calculation_day_info14",column_name="calculation_day_info14")
    calculation_day_info15 = Field(attribute="calculation_day_info15",column_name="calculation_day_info15")
    calculation_day_info16 = Field(attribute="calculation_day_info16",column_name="calculation_day_info16")
    calculation_day_info17 = Field(attribute="calculation_day_info17",column_name="calculation_day_info17")
    calculation_day_info18 = Field(attribute="calculation_day_info18",column_name="calculation_day_info18")
    calculation_day_info19 = Field(attribute="calculation_day_info19",column_name="calculation_day_info19")
    calculation_day_info20 = Field(attribute="calculation_day_info20",column_name="calculation_day_info20")
    calculation_day_info21 = Field(attribute="calculation_day_info21",column_name="calculation_day_info21")
    calculation_day_info22 = Field(attribute="calculation_day_info22",column_name="calculation_day_info22")
    calculation_day_info23 = Field(attribute="calculation_day_info23",column_name="calculation_day_info23")
    calculation_day_info24 = Field(attribute="calculation_day_info24",column_name="calculation_day_info24")
    calculation_day_info25 = Field(attribute="calculation_day_info25",column_name="calculation_day_info25")
    calculation_day_info26 = Field(attribute="calculation_day_info26",column_name="calculation_day_info26")
    calculation_day_info27 = Field(attribute="calculation_day_info27",column_name="calculation_day_info27")
    calculation_day_info28 = Field(attribute="calculation_day_info28",column_name="calculation_day_info28")
    calculation_day_info29 = Field(attribute="calculation_day_info29",column_name="calculation_day_info29")
    calculation_day_info30 = Field(attribute="calculation_day_info30",column_name="calculation_day_info30")
    calculation_day_info31 = Field(attribute="calculation_day_info31",column_name="calculation_day_info31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordDrug
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_identification"] == "":
            row["practice_identification"]= None

        if row["drug_code"] == "":
            row["drug_code"]= None

        if row["score"] == "":
            row["score"]= None

        if row["count"] == "":
            row["count"]= None

        if row["calculation_day_info1"] == "":
            row["calculation_day_info1"]= None

        if row["calculation_day_info2"] == "":
            row["calculation_day_info2"]= None

        if row["calculation_day_info3"] == "":
            row["calculation_day_info3"]= None

        if row["calculation_day_info4"] == "":
            row["calculation_day_info4"]= None

        if row["calculation_day_info5"] == "":
            row["calculation_day_info5"]= None

        if row["calculation_day_info6"] == "":
            row["calculation_day_info6"]= None

        if row["calculation_day_info7"] == "":
            row["calculation_day_info7"]= None

        if row["calculation_day_info8"] == "":
            row["calculation_day_info8"]= None

        if row["calculation_day_info9"] == "":
            row["calculation_day_info9"]= None

        if row["calculation_day_info10"] == "":
            row["calculation_day_info10"]= None

        if row["calculation_day_info11"] == "":
            row["calculation_day_info11"]= None

        if row["calculation_day_info12"] == "":
            row["calculation_day_info12"]= None

        if row["calculation_day_info13"] == "":
            row["calculation_day_info13"]= None

        if row["calculation_day_info14"] == "":
            row["calculation_day_info14"]= None

        if row["calculation_day_info15"] == "":
            row["calculation_day_info15"]= None

        if row["calculation_day_info16"] == "":
            row["calculation_day_info16"]= None

        if row["calculation_day_info17"] == "":
            row["calculation_day_info17"]= None

        if row["calculation_day_info18"] == "":
            row["calculation_day_info18"]= None

        if row["calculation_day_info19"] == "":
            row["calculation_day_info19"]= None

        if row["calculation_day_info20"] == "":
            row["calculation_day_info20"]= None

        if row["calculation_day_info21"] == "":
            row["calculation_day_info21"]= None

        if row["calculation_day_info22"] == "":
            row["calculation_day_info22"]= None

        if row["calculation_day_info23"] == "":
            row["calculation_day_info23"]= None

        if row["calculation_day_info24"] == "":
            row["calculation_day_info24"]= None

        if row["calculation_day_info25"] == "":
            row["calculation_day_info25"]= None

        if row["calculation_day_info26"] == "":
            row["calculation_day_info26"]= None

        if row["calculation_day_info27"] == "":
            row["calculation_day_info27"]= None

        if row["calculation_day_info28"] == "":
            row["calculation_day_info28"]= None

        if row["calculation_day_info29"] == "":
            row["calculation_day_info29"]= None

        if row["calculation_day_info30"] == "":
            row["calculation_day_info30"]= None

        if row["calculation_day_info31"] == "":
            row["calculation_day_info31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordSpecialEquipmentResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    practice_identification = Field(attribute="practice_identification",column_name="practice_identification")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    special_equipment_code = Field(attribute="special_equipment_code",column_name="special_equipment_code")
    usage = Field(attribute="usage",column_name="usage")
    unit_code = Field(attribute="unit_code",column_name="unit_code")
    unit_cost = Field(attribute="unit_cost",column_name="unit_cost")
    special_equipment_add_code1 = Field(attribute="special_equipment_add_code1",column_name="special_equipment_add_code1")
    special_equipment_add_volume_data1 = Field(attribute="special_equipment_add_volume_data1",column_name="special_equipment_add_volume_data1")
    special_equipment_add_code2 = Field(attribute="special_equipment_add_code2",column_name="special_equipment_add_code2")
    special_equipment_add_volume_data2 = Field(attribute="special_equipment_add_volume_data2",column_name="special_equipment_add_volume_data2")
    standard_or_size = Field(attribute="standard_or_size",column_name="standard_or_size")
    score = Field(attribute="score",column_name="score")
    count = Field(attribute="count",column_name="count")
    calculation_day_info1 = Field(attribute="calculation_day_info1",column_name="calculation_day_info1")
    calculation_day_info2 = Field(attribute="calculation_day_info2",column_name="calculation_day_info2")
    calculation_day_info3 = Field(attribute="calculation_day_info3",column_name="calculation_day_info3")
    calculation_day_info4 = Field(attribute="calculation_day_info4",column_name="calculation_day_info4")
    calculation_day_info5 = Field(attribute="calculation_day_info5",column_name="calculation_day_info5")
    calculation_day_info6 = Field(attribute="calculation_day_info6",column_name="calculation_day_info6")
    calculation_day_info7 = Field(attribute="calculation_day_info7",column_name="calculation_day_info7")
    calculation_day_info8 = Field(attribute="calculation_day_info8",column_name="calculation_day_info8")
    calculation_day_info9 = Field(attribute="calculation_day_info9",column_name="calculation_day_info9")
    calculation_day_info10 = Field(attribute="calculation_day_info10",column_name="calculation_day_info10")
    calculation_day_info11 = Field(attribute="calculation_day_info11",column_name="calculation_day_info11")
    calculation_day_info12 = Field(attribute="calculation_day_info12",column_name="calculation_day_info12")
    calculation_day_info13 = Field(attribute="calculation_day_info13",column_name="calculation_day_info13")
    calculation_day_info14 = Field(attribute="calculation_day_info14",column_name="calculation_day_info14")
    calculation_day_info15 = Field(attribute="calculation_day_info15",column_name="calculation_day_info15")
    calculation_day_info16 = Field(attribute="calculation_day_info16",column_name="calculation_day_info16")
    calculation_day_info17 = Field(attribute="calculation_day_info17",column_name="calculation_day_info17")
    calculation_day_info18 = Field(attribute="calculation_day_info18",column_name="calculation_day_info18")
    calculation_day_info19 = Field(attribute="calculation_day_info19",column_name="calculation_day_info19")
    calculation_day_info20 = Field(attribute="calculation_day_info20",column_name="calculation_day_info20")
    calculation_day_info21 = Field(attribute="calculation_day_info21",column_name="calculation_day_info21")
    calculation_day_info22 = Field(attribute="calculation_day_info22",column_name="calculation_day_info22")
    calculation_day_info23 = Field(attribute="calculation_day_info23",column_name="calculation_day_info23")
    calculation_day_info24 = Field(attribute="calculation_day_info24",column_name="calculation_day_info24")
    calculation_day_info25 = Field(attribute="calculation_day_info25",column_name="calculation_day_info25")
    calculation_day_info26 = Field(attribute="calculation_day_info26",column_name="calculation_day_info26")
    calculation_day_info27 = Field(attribute="calculation_day_info27",column_name="calculation_day_info27")
    calculation_day_info28 = Field(attribute="calculation_day_info28",column_name="calculation_day_info28")
    calculation_day_info29 = Field(attribute="calculation_day_info29",column_name="calculation_day_info29")
    calculation_day_info30 = Field(attribute="calculation_day_info30",column_name="calculation_day_info30")
    calculation_day_info31 = Field(attribute="calculation_day_info31",column_name="calculation_day_info31")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordSpecialEquipment
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_identification"] == "":
            row["practice_identification"]= None

        if row["special_equipment_code"] == "":
            row["special_equipment_code"]= None

        if row["unit_code"] == "":
            row["unit_code"]= None

        if row["unit_cost"] == "":
            row["unit_cost"]= None

        if row["special_equipment_add_volume_data1"] == "":
            row["special_equipment_add_volume_data1"]= None

        if row["special_equipment_add_code2"] == "":
            row["special_equipment_add_code2"]= None

        if row["score"] == "":
            row["score"]= None

        if row["count"] == "":
            row["count"]= None

        if row["calculation_day_info1"] == "":
            row["calculation_day_info1"]= None

        if row["calculation_day_info2"] == "":
            row["calculation_day_info2"]= None

        if row["calculation_day_info3"] == "":
            row["calculation_day_info3"]= None

        if row["calculation_day_info4"] == "":
            row["calculation_day_info4"]= None

        if row["calculation_day_info5"] == "":
            row["calculation_day_info5"]= None

        if row["calculation_day_info6"] == "":
            row["calculation_day_info6"]= None

        if row["calculation_day_info7"] == "":
            row["calculation_day_info7"]= None

        if row["calculation_day_info8"] == "":
            row["calculation_day_info8"]= None

        if row["calculation_day_info9"] == "":
            row["calculation_day_info9"]= None

        if row["calculation_day_info10"] == "":
            row["calculation_day_info10"]= None

        if row["calculation_day_info11"] == "":
            row["calculation_day_info11"]= None

        if row["calculation_day_info12"] == "":
            row["calculation_day_info12"]= None

        if row["calculation_day_info13"] == "":
            row["calculation_day_info13"]= None

        if row["calculation_day_info14"] == "":
            row["calculation_day_info14"]= None

        if row["calculation_day_info15"] == "":
            row["calculation_day_info15"]= None

        if row["calculation_day_info16"] == "":
            row["calculation_day_info16"]= None

        if row["calculation_day_info17"] == "":
            row["calculation_day_info17"]= None

        if row["calculation_day_info18"] == "":
            row["calculation_day_info18"]= None

        if row["calculation_day_info19"] == "":
            row["calculation_day_info19"]= None

        if row["calculation_day_info20"] == "":
            row["calculation_day_info20"]= None

        if row["calculation_day_info21"] == "":
            row["calculation_day_info21"]= None

        if row["calculation_day_info22"] == "":
            row["calculation_day_info22"]= None

        if row["calculation_day_info23"] == "":
            row["calculation_day_info23"]= None

        if row["calculation_day_info24"] == "":
            row["calculation_day_info24"]= None

        if row["calculation_day_info25"] == "":
            row["calculation_day_info25"]= None

        if row["calculation_day_info26"] == "":
            row["calculation_day_info26"]= None

        if row["calculation_day_info27"] == "":
            row["calculation_day_info27"]= None

        if row["calculation_day_info28"] == "":
            row["calculation_day_info28"]= None

        if row["calculation_day_info29"] == "":
            row["calculation_day_info29"]= None

        if row["calculation_day_info30"] == "":
            row["calculation_day_info30"]= None

        if row["calculation_day_info31"] == "":
            row["calculation_day_info31"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordCommentResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    practice_identification = Field(attribute="practice_identification",column_name="practice_identification")
    payer_type = Field(attribute="payer_type",column_name="payer_type")
    comment_code = Field(attribute="comment_code",column_name="comment_code")
    character_data = Field(attribute="character_data",column_name="character_data")
    dentation_comment = Field(attribute="dentation_comment",column_name="dentation_comment")
    reserve1 = Field(attribute="reserve1",column_name="reserve1")
    reserve2 = Field(attribute="reserve2",column_name="reserve2")
    reserve3 = Field(attribute="reserve3",column_name="reserve3")
    reserve4 = Field(attribute="reserve4",column_name="reserve4")
    reserve5 = Field(attribute="reserve5",column_name="reserve5")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordComment
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["practice_identification"] == "":
            row["practice_identification"]= None

        if row["comment_code"] == "":
            row["comment_code"]= None

        if row["reserve4"] == "":
            row["reserve4"]= None

        if row["reserve5"] == "":
            row["reserve5"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordDetailSymptomsResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    detail_symptoms_type = Field(attribute="detail_symptoms_type",column_name="detail_symptoms_type")
    detail_symptoms_data = Field(attribute="detail_symptoms_data",column_name="detail_symptoms_data")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    name = Field(attribute="name",column_name="name")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordDetailSymptoms
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["detail_symptoms_type"] == "":
            row["detail_symptoms_type"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None

class RecordMedicalFeeClaimResource(resources.ModelResource):
    record_identification_info = Field(attribute="record_identification_info",column_name="record_identification_info")
    total_cases = Field(attribute="total_cases",column_name="total_cases")
    total_score = Field(attribute="total_score",column_name="total_score")
    multivolume_identification_info = Field(attribute="multivolume_identification_info",column_name="multivolume_identification_info")
    practice_day = Field(attribute="practice_day",column_name="practice_day")
    row_number = Field(attribute="row_number",column_name="row_number")
    class Meta:
        model = models.RecordMedicalFeeClaim
        skip_unchanged = True
        use_bulk = True
    def before_import_row(self, row, row_number=None, **kwargs):
        if row["total_cases"] == "":
            row["total_cases"]= None

        if row["total_score"] == "":
            row["total_score"]= None

        if row["multivolume_identification_info"] == "":
            row["multivolume_identification_info"]= None

        if row["practice_day"] == "":
            row["practice_day"]= None

        if row["row_number"] == "":
            row["row_number"]= None