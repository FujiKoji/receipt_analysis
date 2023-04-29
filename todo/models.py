from django.db import models
# Create your models here.

class TableBasic(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_区分枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_区分項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    new_score_etc_identification = models.IntegerField(
        verbose_name = "新又は現点数_点数等識別",
        blank = True,
        null = True,
        default = None
    )
    new_score_etc = models.DecimalField(
        verbose_name = "新又は現点数_点数等",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    old_score_etc_identification = models.IntegerField(
        verbose_name = "旧点数_点数等識別",
        blank = True,
        null = True,
        default = None
    )
    old_score_etc = models.DecimalField(
        verbose_name = "旧点数_点数等",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    in_out_code = models.IntegerField(
        verbose_name = "入外適用区分",
        blank = True,
        null = True,
        default = None
    )
    late_elderly_medical_code = models.IntegerField(
        verbose_name = "後期高齢者医療適用区分",
        blank = True,
        null = True,
        default = None
    )
    time_add_code = models.IntegerField(
        verbose_name = "時間加算区分",
        blank = True,
        null = True,
        default = None
    )
    hospital_clinics_code = models.IntegerField(
        verbose_name = "病院・診療所区分",
        blank = True,
        null = True,
        default = None
    )
    nurse_add = models.IntegerField(
        verbose_name = "看護加算",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    area_add = models.IntegerField(
        verbose_name = "地域加算",
        blank = True,
        null = True,
        default = None
    )
    injury_name_code = models.IntegerField(
        verbose_name = "傷病名関連区分",
        blank = True,
        null = True,
        default = None
    )
    drug_name_code = models.IntegerField(
        verbose_name = "医薬品関連区分",
        blank = True,
        null = True,
        default = None
    )
    number_of_bed_code = models.IntegerField(
        verbose_name = "病床数区分",
        blank = True,
        null = True,
        default = None
    )
    notification = models.IntegerField(
        verbose_name = "届出",
        blank = True,
        null = True,
        default = None
    )
    future_hospital = models.IntegerField(
        verbose_name = "未来院",
        blank = True,
        null = True,
        default = None
    )
    short_stay_surgery = models.IntegerField(
        verbose_name = "短期滞在手術",
        blank = True,
        null = True,
        default = None
    )
    special_remarks = models.IntegerField(
        verbose_name = "特記事項",
        blank = True,
        null = True,
        default = None
    )
    Inspection_decision_code = models.IntegerField(
        verbose_name = "検査等実施判断区分",
        blank = True,
        null = True,
        default = None
    )
    Inspection_decision_group_code = models.IntegerField(
        verbose_name = "検査等実施判断グループ区分",
        blank = True,
        null = True,
        default = None
    )
    diminution_code = models.IntegerField(
        verbose_name = "逓減対象区分",
        blank = True,
        null = True,
        default = None
    )
    comprehensive_code = models.IntegerField(
        verbose_name = "包括逓減区分",
        blank = True,
        null = True,
        default = None
    )
    base_conformance_code = models.IntegerField(
        verbose_name = "基準適合識別_適合区分",
        blank = True,
        null = True,
        default = None
    )
    base_conformance_facility_standard = models.IntegerField(
        verbose_name = "基準適合識別_対象施設基準",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code1 = models.IntegerField(
        verbose_name = "施設基準コード①",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code2 = models.IntegerField(
        verbose_name = "施設基準コード②",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code3 = models.IntegerField(
        verbose_name = "施設基準コード③",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code4 = models.IntegerField(
        verbose_name = "施設基準コード④",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code5 = models.IntegerField(
        verbose_name = "施設基準コード⑤",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code6 = models.IntegerField(
        verbose_name = "施設基準コード⑥",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code7 = models.IntegerField(
        verbose_name = "施設基準コード⑦",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code8 = models.IntegerField(
        verbose_name = "施設基準コード⑧",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code9 = models.IntegerField(
        verbose_name = "施設基準コード⑨",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code10 = models.IntegerField(
        verbose_name = "施設基準コード⑩",
        blank = True,
        null = True,
        default = None
    )
    general_rule_add_group = models.CharField(
        verbose_name = "通則加算グループ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    basic_add_group = models.CharField(
        verbose_name = "基本加算グループ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    annotation_add_group = models.CharField(
        verbose_name = "注加算グループ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    tech_materials_add_group = models.CharField(
        verbose_name = "手技・材料加算グループ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    calculation_limit_table_identification = models.IntegerField(
        verbose_name = "算定回数限度テーブル関連識別",
        blank = True,
        null = True,
        default = None
    )
    etch_table_identification = models.IntegerField(
        verbose_name = "きざみテーブル関連識別",
        blank = True,
        null = True,
        default = None
    )
    age_limit_table_identification = models.IntegerField(
        verbose_name = "年齢制限テーブル関連識別",
        blank = True,
        null = True,
        default = None
    )
    contradiction_table_identification = models.IntegerField(
        verbose_name = "併算定背反テーブル関連識別",
        blank = True,
        null = True,
        default = None
    )
    days_table_identification = models.IntegerField(
        verbose_name = "実日数テーブル関連識別",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    prolonged_anesthesia_control_add = models.CharField(
        verbose_name = "長時間麻酔管理加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    cancer_pathological_specimen_add = models.CharField(
        verbose_name = "悪性腫瘍病理組織標本加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備３",
        blank = True,
        null = True,
        default = None
    )
    reserve6 = models.IntegerField(
        verbose_name = "予備４",
        blank = True,
        null = True,
        default = None
    )
    reserve7 = models.IntegerField(
        verbose_name = "予備５",
        blank = True,
        null = True,
        default = None
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_basic"
        verbose_name_plural = "T:基本テーブル"

class TableGeneralRuleAddItemAdd(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    group_number = models.CharField(
        verbose_name = "グループ番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    general_rule_add_item_add_code = models.CharField(
        verbose_name = "通則加算項目_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    general_rule_add_item_dental_practice_code = models.IntegerField(
        verbose_name = "通則加算項目_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    general_rule_add_item_practice_bassic_name = models.CharField(
        verbose_name = "通則加算項目_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    general_rule_add_item_add_identification = models.IntegerField(
        verbose_name = "通則加算項目_加算識別",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_general_rule_add_item_add"
        verbose_name_plural = "T:通則加算対応テーブル"

class TableBasicAddItemAdd(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    group_number = models.CharField(
        verbose_name = "グループ番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    basic_add_item_add_code = models.CharField(
        verbose_name = "基本加算項目_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    basic_add_item_dental_practice_code = models.IntegerField(
        verbose_name = "基本加算項目_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    basic_add_item_practice_bassic_name = models.CharField(
        verbose_name = "基本加算項目_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    basic_add_item_add_identification = models.IntegerField(
        verbose_name = "基本加算項目_加算識別",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_basic_add_item_add"
        verbose_name_plural = "T:基本加算対応テーブル"

class TableAnnotationAddItemAdd(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    group_number = models.CharField(
        verbose_name = "グループ番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    annotation_add_item_add_code = models.CharField(
        verbose_name = "注加算項目_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    annotation_add_item_dental_practice_code = models.IntegerField(
        verbose_name = "注加算項目_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    annotation_add_item_practice_bassic_name = models.CharField(
        verbose_name = "注加算項目_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    annotation_add_item_add_identification = models.IntegerField(
        verbose_name = "注加算項目_加算識別",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_annotation_add_item_add"
        verbose_name_plural = "T:注加算対応テーブル"

class TableTechMaterialsAddItem(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    group_number = models.CharField(
        verbose_name = "グループ番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    tech_materials_add_item_add_code = models.CharField(
        verbose_name = "手技・材料加算項目_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    tech_materials_add_item_dental_practice_code = models.IntegerField(
        verbose_name = "手技・材料加算項目_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    tech_materials_add_item_practice_bassic_name = models.CharField(
        verbose_name = "手技・材料加算項目_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    tech_materials_add_item_add_identification = models.IntegerField(
        verbose_name = "手技・材料加算項目_加算識別",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_tech_materials_add_item"
        verbose_name_plural = "T:手技・材料加算対応テーブル"

class TableCalculationLimit(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    calculation_unit = models.IntegerField(
        verbose_name = "算定単位",
        blank = True,
        null = True,
        default = None
    )
    calculation_limit = models.IntegerField(
        verbose_name = "算定回数限度",
        blank = True,
        null = True,
        default = None
    )
    upper_limit_error_process = models.IntegerField(
        verbose_name = "上限回数エラー処理",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_calculation_limit"
        verbose_name_plural = "T:算定回数限度テーブル"

class TableEtch(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    score_etc_identification = models.IntegerField(
        verbose_name = "点数等識別",
        blank = True,
        null = True,
        default = None
    )
    score = models.DecimalField(
        verbose_name = "点数",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    etch_score = models.IntegerField(
        verbose_name = "きざみ単位",
        blank = True,
        null = True,
        default = None
    )
    etch_lower_limit = models.IntegerField(
        verbose_name = "きざみ下限値",
        blank = True,
        null = True,
        default = None
    )
    etch_upper_limit = models.IntegerField(
        verbose_name = "きざみ上限値",
        blank = True,
        null = True,
        default = None
    )
    etch_value = models.IntegerField(
        verbose_name = "きざみ値",
        blank = True,
        null = True,
        default = None
    )
    etch_score = models.DecimalField(
        verbose_name = "きざみ点数",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    etch_limits_error_process = models.IntegerField(
        verbose_name = "きざみ上下限エラー処理",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_etch"
        verbose_name_plural = "T:きざみテーブル"

class TableAgeLimit(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    lower_age = models.CharField(
        verbose_name = "下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    upper_age = models.CharField(
        verbose_name = "上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_age_limit"
        verbose_name_plural = "T:年齢制限テーブル"

class TableFixCalculationContradiction(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction1_calculability = models.IntegerField(
        verbose_name = "背反1_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction1_dental_practice_code = models.IntegerField(
        verbose_name = "背反1_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction1_bulletin_number_type = models.CharField(
        verbose_name = "背反1_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction1_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反1_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction1_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反1_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction1_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反1_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction1_add_code = models.CharField(
        verbose_name = "背反1_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction1_practice_bassic_name = models.CharField(
        verbose_name = "背反1_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction1_practice_abbreviation_name = models.CharField(
        verbose_name = "背反1_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction2_calculability = models.IntegerField(
        verbose_name = "背反2_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction2_dental_practice_code = models.IntegerField(
        verbose_name = "背反2_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction2_bulletin_number_type = models.CharField(
        verbose_name = "背反2_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction2_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反2_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction2_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反2_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction2_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反2_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction2_add_code = models.CharField(
        verbose_name = "背反2_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction2_practice_bassic_name = models.CharField(
        verbose_name = "背反2_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction2_practice_abbreviation_name = models.CharField(
        verbose_name = "背反2_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction3_calculability = models.IntegerField(
        verbose_name = "背反3_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction3_dental_practice_code = models.IntegerField(
        verbose_name = "背反3_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction3_bulletin_number_type = models.CharField(
        verbose_name = "背反3_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction3_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反3_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction3_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反3_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction3_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反3_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction3_add_code = models.CharField(
        verbose_name = "背反3_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction3_practice_bassic_name = models.CharField(
        verbose_name = "背反3_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction3_practice_abbreviation_name = models.CharField(
        verbose_name = "背反3_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction4_calculability = models.IntegerField(
        verbose_name = "背反4_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction4_dental_practice_code = models.IntegerField(
        verbose_name = "背反4_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction4_bulletin_number_type = models.CharField(
        verbose_name = "背反4_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction4_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反4_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction4_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反4_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction4_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反4_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction4_add_code = models.CharField(
        verbose_name = "背反4_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction4_practice_bassic_name = models.CharField(
        verbose_name = "背反4_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction4_practice_abbreviation_name = models.CharField(
        verbose_name = "背反4_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction5_calculability = models.IntegerField(
        verbose_name = "背反5_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction5_dental_practice_code = models.IntegerField(
        verbose_name = "背反5_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction5_bulletin_number_type = models.CharField(
        verbose_name = "背反5_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction5_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反5_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction5_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反5_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction5_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反5_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction5_add_code = models.CharField(
        verbose_name = "背反5_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction5_practice_bassic_name = models.CharField(
        verbose_name = "背反5_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction5_practice_abbreviation_name = models.CharField(
        verbose_name = "背反5_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction6_calculability = models.IntegerField(
        verbose_name = "背反6_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction6_dental_practice_code = models.IntegerField(
        verbose_name = "背反6_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction6_bulletin_number_type = models.CharField(
        verbose_name = "背反6_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction6_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反6_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction6_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反6_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction6_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反6_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction6_add_code = models.CharField(
        verbose_name = "背反6_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction6_practice_bassic_name = models.CharField(
        verbose_name = "背反6_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction6_practice_abbreviation_name = models.CharField(
        verbose_name = "背反6_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction7_calculability = models.IntegerField(
        verbose_name = "背反7_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction7_dental_practice_code = models.IntegerField(
        verbose_name = "背反7_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction7_bulletin_number_type = models.CharField(
        verbose_name = "背反7_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction7_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反7_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction7_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反7_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction7_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反7_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction7_add_code = models.CharField(
        verbose_name = "背反7_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction7_practice_bassic_name = models.CharField(
        verbose_name = "背反7_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction7_practice_abbreviation_name = models.CharField(
        verbose_name = "背反7_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction8_calculability = models.IntegerField(
        verbose_name = "背反8_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction8_dental_practice_code = models.IntegerField(
        verbose_name = "背反8_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction8_bulletin_number_type = models.CharField(
        verbose_name = "背反8_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction8_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反8_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction8_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反8_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction8_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反8_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction8_add_code = models.CharField(
        verbose_name = "背反8_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction8_practice_bassic_name = models.CharField(
        verbose_name = "背反8_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction8_practice_abbreviation_name = models.CharField(
        verbose_name = "背反8_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction9_calculability = models.IntegerField(
        verbose_name = "背反9_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction9_dental_practice_code = models.IntegerField(
        verbose_name = "背反9_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction9_bulletin_number_type = models.CharField(
        verbose_name = "背反9_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction9_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反9_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction9_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反9_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction9_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反9_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction9_add_code = models.CharField(
        verbose_name = "背反9_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction9_practice_bassic_name = models.CharField(
        verbose_name = "背反9_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction9_practice_abbreviation_name = models.CharField(
        verbose_name = "背反9_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction10_calculability = models.IntegerField(
        verbose_name = "背反10_算定可否",
        blank = True,
        null = True,
        default = None
    )
    contradiction10_dental_practice_code = models.IntegerField(
        verbose_name = "背反10_歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    contradiction10_bulletin_number_type = models.CharField(
        verbose_name = "背反10_告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction10_bulletin_number_type_number = models.IntegerField(
        verbose_name = "背反10_告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    contradiction10_bulletin_number_branch_number = models.IntegerField(
        verbose_name = "背反10_告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    contradiction10_bulletin_number_item_number = models.IntegerField(
        verbose_name = "背反10_告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    contradiction10_add_code = models.CharField(
        verbose_name = "背反10_加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction10_practice_bassic_name = models.CharField(
        verbose_name = "背反10_診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    contradiction10_practice_abbreviation_name = models.CharField(
        verbose_name = "背反10_診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    change_date = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_date = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_fix_calculation_contradiction"
        verbose_name_plural = "T:併算定背反テーブル"

class TableRealDay(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type = models.CharField(
        verbose_name = "告示番号_区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号_区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示番号_枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示番号_項番",
        blank = True,
        null = True,
        default = None
    )
    add_code = models.CharField(
        verbose_name = "加算コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_bassic_name = models.CharField(
        verbose_name = "診療行為名称_基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name = models.CharField(
        verbose_name = "診療行為名称_省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    real_day = models.IntegerField(
        verbose_name = "実日数",
        blank = True,
        null = True,
        default = None
    )
    days_or_times = models.IntegerField(
        verbose_name = "日数・回数",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "table_real_day"
        verbose_name_plural = "T:実日数関連テーブル"

class MasterDisease(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_name_code = models.IntegerField(
        verbose_name = "傷病名コード",
        blank = True,
        null = True,
        default = None
    )
    destination_code = models.IntegerField(
        verbose_name = "移行先コード",
        blank = True,
        null = True,
        default = None
    )
    disease_bassic_name_digits = models.IntegerField(
        verbose_name = "傷病名基本名称桁数",
        blank = True,
        null = True,
        default = None
    )
    disease_bassic_name = models.CharField(
        verbose_name = "傷病名基本名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_abbreviation_name_digits = models.IntegerField(
        verbose_name = "傷病名省略名称桁数",
        blank = True,
        null = True,
        default = None
    )
    disease_abbreviation_name = models.CharField(
        verbose_name = "傷病名省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_cana_name_digits = models.IntegerField(
        verbose_name = "傷病名カナ名称桁数",
        blank = True,
        null = True,
        default = None
    )
    disease_cana_name = models.CharField(
        verbose_name = "傷病名カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_control_number = models.IntegerField(
        verbose_name = "病名管理番号",
        blank = True,
        null = True,
        default = None
    )
    adoption_type = models.IntegerField(
        verbose_name = "採択区分",
        blank = True,
        null = True,
        default = None
    )
    disease_name_exchange_code = models.CharField(
        verbose_name = "病名交換用コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    ICD_10_1 = models.CharField(
        verbose_name = "ICD-10-1",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    ICD_10_2 = models.CharField(
        verbose_name = "ICD-10-2",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    ICD_10_1_2013 = models.CharField(
        verbose_name = "ICD-10-1(2013)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    ICD_10_2_2013 = models.CharField(
        verbose_name = "ICD-10-2(2013)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve1 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    single_use_ban_type = models.IntegerField(
        verbose_name = "単独使用禁止区分",
        blank = True,
        null = True,
        default = None
    )
    no_insurance_claim_type = models.IntegerField(
        verbose_name = "保険請求外区分",
        blank = True,
        null = True,
        default = None
    )
    special_disease_target_type = models.IntegerField(
        verbose_name = "特定疾患等対象区分",
        blank = True,
        null = True,
        default = None
    )
    listing_day = models.DateField(
        verbose_name = "収載年月日",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    disease_bassic_name_change_info = models.IntegerField(
        verbose_name = "傷病名基本名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    disease_abbreviation_name_change_info = models.IntegerField(
        verbose_name = "傷病名省略名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    disease_cana_name_change_info = models.IntegerField(
        verbose_name = "傷病名カナ名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    adoption_type_change_info = models.IntegerField(
        verbose_name = "採択区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    disease_name_exchange_code_change_info = models.IntegerField(
        verbose_name = "病名交換用コード（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    ICD_10_1_change_info = models.IntegerField(
        verbose_name = "ICD-10-1（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    ICD_10_2_change_info = models.IntegerField(
        verbose_name = "ICD-10-2（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    dental_disease_abbreviation_name_change_info = models.IntegerField(
        verbose_name = "歯科傷病名省略名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    intractable_disease_out_target_type_change_info = models.IntegerField(
        verbose_name = "難病外来対象区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    dental_special_disease_target_type_change_info = models.IntegerField(
        verbose_name = "歯科特定疾患対象区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    single_use_ban_type_change_info = models.IntegerField(
        verbose_name = "単独使用禁止区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    no_insurance_claim_type_change_info = models.IntegerField(
        verbose_name = "保険請求外区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    special_disease_target_type_change_info = models.IntegerField(
        verbose_name = "特定疾患対象区分（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    destination_disease_control_number = models.IntegerField(
        verbose_name = "移行先病名管理番号",
        blank = True,
        null = True,
        default = None
    )
    dental_disease_abbreviation_name = models.CharField(
        verbose_name = "歯科傷病名省略名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve2 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    dental_disease_abbreviation_name_digits = models.IntegerField(
        verbose_name = "歯科傷病名省略名称桁数",
        blank = True,
        null = True,
        default = None
    )
    intractable_disease_out_target_type = models.IntegerField(
        verbose_name = "難病外来対象区分",
        blank = True,
        null = True,
        default = None
    )
    dental_special_disease_target_type = models.IntegerField(
        verbose_name = "歯科特定疾患対象区分",
        blank = True,
        null = True,
        default = None
    )
    ICD_10_1_2013_change_info = models.IntegerField(
        verbose_name = "ICD-10_1(2013)(変更情報)",
        blank = True,
        null = True,
        default = None
    )
    ICD_10_2_2013_change_info = models.IntegerField(
        verbose_name = "ICD-10_2(2013)(変更情報)",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "master_disease"
        verbose_name_plural = "M:傷病名マスター"

class MasterModifier(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    modifier_code = models.IntegerField(
        verbose_name = "修飾語コード",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    modifier_name_digits = models.IntegerField(
        verbose_name = "修飾語名称桁数",
        blank = True,
        null = True,
        default = None
    )
    modifier_name = models.CharField(
        verbose_name = "修飾語名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve3 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    modifier_cana_name_digits = models.IntegerField(
        verbose_name = "修飾語カナ名称桁数",
        blank = True,
        null = True,
        default = None
    )
    modifier_cana_name = models.CharField(
        verbose_name = "修飾語カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    modifier_name_change_info = models.IntegerField(
        verbose_name = "修飾語名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    modifier_cana_name_change_info = models.IntegerField(
        verbose_name = "修飾語カナ名称（変更情報）",
        blank = True,
        null = True,
        default = None
    )
    listing_day = models.DateField(
        verbose_name = "収載年月日",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    modifier_control_number = models.IntegerField(
        verbose_name = "修飾語管理番号",
        blank = True,
        null = True,
        default = None
    )
    modifier_exchange_code = models.CharField(
        verbose_name = "修飾語交換用コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    modifier_type = models.CharField(
        verbose_name = "修飾語区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    class Meta:
        db_table = "master_modifier"
        verbose_name_plural = "M:修飾語マスター"

class MasterDental(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dentation_code = models.CharField(
        verbose_name = "歯式コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    dentation_name = models.CharField(
        verbose_name = "歯式名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "master_dental"
        verbose_name_plural = "M:歯式マスター"

class MasterDrug(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    drug_code = models.IntegerField(
        verbose_name = "医薬品コード",
        blank = True,
        null = True,
        default = None
    )
    drug_kanji_significant_digits = models.IntegerField(
        verbose_name = "医薬品名・規格名＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    drug_kanji_name = models.CharField(
        verbose_name = "医薬品名・規格名＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    drug_cana_significant_digits = models.IntegerField(
        verbose_name = "医薬品名・規格名＿カナ有効桁数",
        blank = True,
        null = True,
        default = None
    )
    drug_cana_name = models.CharField(
        verbose_name = "医薬品名・規格名＿カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    unit_code = models.IntegerField(
        verbose_name = "単位＿コード",
        blank = True,
        null = True,
        default = None
    )
    unit_kanji_significant_digits = models.IntegerField(
        verbose_name = "単位＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    unit_kanji_name = models.CharField(
        verbose_name = "単位＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    new_cash_amount_type = models.IntegerField(
        verbose_name = "新又は現金額＿金額種別",
        blank = True,
        null = True,
        default = None
    )
    new_cash_new_cash = models.DecimalField(
        verbose_name = "新又は現金額＿新又は現金額",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    special_drug = models.IntegerField(
        verbose_name = "麻薬・毒薬・覚醒剤原料・向精神薬",
        blank = True,
        null = True,
        default = None
    )
    neuroleptic = models.IntegerField(
        verbose_name = "神経破壊剤",
        blank = True,
        null = True,
        default = None
    )
    biologics = models.IntegerField(
        verbose_name = "生物学的製薬",
        blank = True,
        null = True,
        default = None
    )
    generic = models.IntegerField(
        verbose_name = "後発品",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    dental_special_drug = models.IntegerField(
        verbose_name = "歯科特定薬剤",
        blank = True,
        null = True,
        default = None
    )
    contrast_drug = models.IntegerField(
        verbose_name = "造影（補助）剤",
        blank = True,
        null = True,
        default = None
    )
    Injection_volume = models.IntegerField(
        verbose_name = "注射容量",
        blank = True,
        null = True,
        default = None
    )
    listing_method_identification = models.IntegerField(
        verbose_name = "収載方式等識別",
        blank = True,
        null = True,
        default = None
    )
    product_name_etc = models.IntegerField(
        verbose_name = "商品名等関連",
        blank = True,
        null = True,
        default = None
    )
    old_cash_amount_type = models.IntegerField(
        verbose_name = "旧金額＿金額種別",
        blank = True,
        null = True,
        default = None
    )
    old_cash_old_cash = models.DecimalField(
        verbose_name = "旧金額＿旧金額",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    kanji_name_change_type = models.IntegerField(
        verbose_name = "漢字名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    cana_name_change_type = models.IntegerField(
        verbose_name = "カナ名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    dosage_form = models.IntegerField(
        verbose_name = "剤形",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    drug_price_bassic_listing_code = models.CharField(
        verbose_name = "薬価基準収載医薬品コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    expiry_day = models.DateField(
        verbose_name = "経過措置年月日又は商品名医薬品コード使用期限",
        blank = True,
        null = True,
        default = None
    )
    bassic_kanji_name = models.CharField(
        verbose_name = "基本漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    class Meta:
        db_table = "master_drug"
        verbose_name_plural = "M:医薬品マスター"

class MasterSpecialEquipment(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    special_equipment_code = models.IntegerField(
        verbose_name = "特定器材コード",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_significant_digits = models.IntegerField(
        verbose_name = "特定器材名・規格名＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_kanji_name = models.CharField(
        verbose_name = "特定器材名・規格名＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    special_equipment_cana_significant_digits = models.IntegerField(
        verbose_name = "特定器材名・規格名＿カナ有効桁数",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_cana_name = models.CharField(
        verbose_name = "特定器材名・規格名＿カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    unit_code = models.IntegerField(
        verbose_name = "単位＿コード",
        blank = True,
        null = True,
        default = None
    )
    unit_kanji_significant_digits = models.IntegerField(
        verbose_name = "単位＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    unit_kanji_name = models.CharField(
        verbose_name = "単位＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    new_cash_amount_type = models.IntegerField(
        verbose_name = "新又は現金額＿金額種別",
        blank = True,
        null = True,
        default = None
    )
    new_cash_new_cash = models.DecimalField(
        verbose_name = "新又は現金額＿新又は現金額",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    age_add_type = models.IntegerField(
        verbose_name = "年齢加算区分",
        blank = True,
        null = True,
        default = None
    )
    age_limit_lower_limit = models.CharField(
        verbose_name = "上下限年齢＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_limit_upper_limit = models.CharField(
        verbose_name = "上下限年齢＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    old_cash_amount_type = models.IntegerField(
        verbose_name = "旧金額＿金額種別",
        blank = True,
        null = True,
        default = None
    )
    old_cash_old_cash = models.DecimalField(
        verbose_name = "旧金額＿旧金額",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    kanji_name_change_type = models.IntegerField(
        verbose_name = "漢字名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    cana_name_change_type = models.IntegerField(
        verbose_name = "カナ名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    oxygen_type = models.IntegerField(
        verbose_name = "酸素等区分",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_type = models.IntegerField(
        verbose_name = "特定器材種別",
        blank = True,
        null = True,
        default = None
    )
    upper_limit_price = models.IntegerField(
        verbose_name = "上限価格",
        blank = True,
        null = True,
        default = None
    )
    lower_limit_price = models.IntegerField(
        verbose_name = "上限点数",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    abolition_new_etc = models.IntegerField(
        verbose_name = "廃止・新設関連",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    expiry_day = models.DateField(
        verbose_name = "経過措置年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_other_table_number = models.IntegerField(
        verbose_name = "告示番号＿別表番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示番号＿区分番号",
        blank = True,
        null = True,
        default = None
    )
    dpc_type = models.IntegerField(
        verbose_name = "DPC適用区分",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve4 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve5 = models.CharField(
        verbose_name = "予備",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bassic_kanji_name = models.CharField(
        verbose_name = "基本漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    class Meta:
        db_table = "master_special_equipment"
        verbose_name_plural = "M:特定器材マスター"

class MasterComment(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    type = models.IntegerField(
        verbose_name = "区分",
        blank = True,
        null = True,
        default = None
    )
    pattern = models.IntegerField(
        verbose_name = "パターン",
        blank = True,
        null = True,
        default = None
    )
    serial_number = models.IntegerField(
        verbose_name = "一連番号",
        blank = True,
        null = True,
        default = None
    )
    comment_kanji_significant_digits = models.IntegerField(
        verbose_name = "コメント文＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    comment_kanji_name = models.CharField(
        verbose_name = "コメント文＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    comment_cana_significant_digits = models.IntegerField(
        verbose_name = "コメント文＿カナ有効桁数",
        blank = True,
        null = True,
        default = None
    )
    comment_cana_name = models.CharField(
        verbose_name = "コメント文＿カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    receipt_edit_info_column1 = models.IntegerField(
        verbose_name = "レセプト編集情報１＿カラム位置",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_digits1 = models.IntegerField(
        verbose_name = "レセプト編集情報１＿桁数",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_column2 = models.IntegerField(
        verbose_name = "レセプト編集情報２＿カラム位置",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_digits2 = models.IntegerField(
        verbose_name = "レセプト編集情報２＿桁数",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_column3 = models.IntegerField(
        verbose_name = "レセプト編集情報３＿カラム位置",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_digits3 = models.IntegerField(
        verbose_name = "レセプト編集情報３＿桁数",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_column4 = models.IntegerField(
        verbose_name = "レセプト編集情報４＿カラム位置",
        blank = True,
        null = True,
        default = None
    )
    receipt_edit_info_digits4 = models.IntegerField(
        verbose_name = "レセプト編集情報４＿桁数",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    choice_comment_identification = models.IntegerField(
        verbose_name = "選択式コメント識別",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    commnet_code = models.IntegerField(
        verbose_name = "コメントコード",
        blank = True,
        null = True,
        default = None
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve6 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve7 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve8 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "master_comment"
        verbose_name_plural = "M:コメントマスター"

class MasterPractice(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_code = models.IntegerField(
        verbose_name = "診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    practice_abbreviation_name_kanji_significant_digits = models.IntegerField(
        verbose_name = "診療行為省略名称＿省略漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    practice_abbreviation_name_kanji_name = models.CharField(
        verbose_name = "診療行為省略名称＿省略漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_abbreviation_name_cana_significant_digits = models.IntegerField(
        verbose_name = "診療行為省略名称＿省略カナ有効桁数",
        blank = True,
        null = True,
        default = None
    )
    practice_abbreviation_name_cana_name = models.CharField(
        verbose_name = "診療行為省略名称＿省略カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    data_code = models.IntegerField(
        verbose_name = "データ規格コード",
        blank = True,
        null = True,
        default = None
    )
    data_kanji_significant_digits = models.IntegerField(
        verbose_name = "データ規格名＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    data_kanji_name = models.CharField(
        verbose_name = "データ規格名＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    new_score_etc_identification = models.IntegerField(
        verbose_name = "新又は現点数＿点数識別",
        blank = True,
        null = True,
        default = None
    )
    new_score_etc = models.DecimalField(
        verbose_name = "新又は現点数＿新又は現点数",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    in_out_code = models.IntegerField(
        verbose_name = "入外適用区分",
        blank = True,
        null = True,
        default = None
    )
    late_elderly_medical_code = models.IntegerField(
        verbose_name = "後期高齢者医療適用区分",
        blank = True,
        null = True,
        default = None
    )
    score_destination_identification_out = models.IntegerField(
        verbose_name = "点数欄集計先識別（入院外）",
        blank = True,
        null = True,
        default = None
    )
    comprehensive_inspection = models.IntegerField(
        verbose_name = "包括対象検査",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    dpc_type = models.IntegerField(
        verbose_name = "DPC適用区分",
        blank = True,
        null = True,
        default = None
    )
    hospital_type = models.IntegerField(
        verbose_name = "病院・診療所区分",
        blank = True,
        null = True,
        default = None
    )
    surgery_support_addition_type = models.IntegerField(
        verbose_name = "画像等手術支援加算区分",
        blank = True,
        null = True,
        default = None
    )
    medical_observation_type = models.IntegerField(
        verbose_name = "医療観察法対象区分",
        blank = True,
        null = True,
        default = None
    )
    nursing_addition = models.IntegerField(
        verbose_name = "看護加算",
        blank = True,
        null = True,
        default = None
    )
    anesthesia_identification_type = models.IntegerField(
        verbose_name = "麻酔識別区分",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    disease_name_related_type = models.IntegerField(
        verbose_name = "傷病名関連区分",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    real_day = models.IntegerField(
        verbose_name = "実日数",
        blank = True,
        null = True,
        default = None
    )
    days_or_times = models.IntegerField(
        verbose_name = "日数・回数",
        blank = True,
        null = True,
        default = None
    )
    drug_name_code = models.IntegerField(
        verbose_name = "医薬品関連区分",
        blank = True,
        null = True,
        default = None
    )
    etch_value_calculation_identification = models.IntegerField(
        verbose_name = "きざみ値＿きざみ値計算識別",
        blank = True,
        null = True,
        default = None
    )
    etch_lower_limit = models.IntegerField(
        verbose_name = "きざみ値＿下限値",
        blank = True,
        null = True,
        default = None
    )
    etch_upper_limit = models.IntegerField(
        verbose_name = "きざみ値＿上限値",
        blank = True,
        null = True,
        default = None
    )
    etch_value = models.IntegerField(
        verbose_name = "きざみ値＿きざみ値",
        blank = True,
        null = True,
        default = None
    )
    etch_value_score = models.DecimalField(
        verbose_name = "きざみ値＿きざみ点数",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    etch_limits_error_process = models.IntegerField(
        verbose_name = "きざみ値＿上下限エラー処理",
        blank = True,
        null = True,
        default = None
    )
    upper_limit = models.IntegerField(
        verbose_name = "上限回数＿上限回数",
        blank = True,
        null = True,
        default = None
    )
    upper_limit_error_process = models.IntegerField(
        verbose_name = "上限回数＿上限回数エラー処理",
        blank = True,
        null = True,
        default = None
    )
    annotation_add_item_add_code = models.IntegerField(
        verbose_name = "注加算＿注加算コード",
        blank = True,
        null = True,
        default = None
    )
    annotation_add_item_add_number = models.CharField(
        verbose_name = "注加算＿注加算通番",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    general_rule_age = models.IntegerField(
        verbose_name = "通則年齢",
        blank = True,
        null = True,
        default = None
    )
    etch_limits_lower_limit = models.CharField(
        verbose_name = "上下限年齢＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    etch_limits_upper_limit = models.CharField(
        verbose_name = "上下限年齢＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    time_addition_type = models.IntegerField(
        verbose_name = "時間加算区分",
        blank = True,
        null = True,
        default = None
    )
    base_conformance_code = models.IntegerField(
        verbose_name = "基準適合識別＿適合区分",
        blank = True,
        null = True,
        default = None
    )
    base_conformance_facility_standard = models.IntegerField(
        verbose_name = "基準適合識別＿対象施設基準",
        blank = True,
        null = True,
        default = None
    )
    treatment_infant_addition_type = models.IntegerField(
        verbose_name = "処置乳幼児加算区分",
        blank = True,
        null = True,
        default = None
    )
    very_low_birth_weight_infant_addition_type = models.IntegerField(
        verbose_name = "極低出生体重児加算区分",
        blank = True,
        null = True,
        default = None
    )
    basic_hospital_fee_deduction_identification = models.IntegerField(
        verbose_name = "入院基本料減算対象識別",
        blank = True,
        null = True,
        default = None
    )
    donors_class_type = models.IntegerField(
        verbose_name = "ドナー分集計区分",
        blank = True,
        null = True,
        default = None
    )
    judgment_class_inspections_type = models.IntegerField(
        verbose_name = "検査等実施判断区分",
        blank = True,
        null = True,
        default = None
    )
    judgment_class_inspections_group_type = models.IntegerField(
        verbose_name = "検査等実施判断グループ区分",
        blank = True,
        null = True,
        default = None
    )
    diminution_code = models.IntegerField(
        verbose_name = "逓減対象区分",
        blank = True,
        null = True,
        default = None
    )
    spinal_cord_evoked_potential_measurement_add_type = models.IntegerField(
        verbose_name = "脊髄誘発電位測定等加算区分",
        blank = True,
        null = True,
        default = None
    )
    neck_dissection_combined_addition_type = models.IntegerField(
        verbose_name = "頸部郭清術併施加算区分 ",
        blank = True,
        null = True,
        default = None
    )
    auto_suturer_add_type = models.IntegerField(
        verbose_name = "自動縫合器加算区分",
        blank = True,
        null = True,
        default = None
    )
    out_management_add_type = models.IntegerField(
        verbose_name = "外来管理加算区分 ",
        blank = True,
        null = True,
        default = None
    )
    old_score_etc_identification = models.IntegerField(
        verbose_name = "旧点数＿点数識別",
        blank = True,
        null = True,
        default = None
    )
    old_score_etc = models.DecimalField(
        verbose_name = "旧点数＿旧点数",
        blank = True,
        null = True,
        max_digits=12,
        decimal_places=2,
        default = None
    )
    kanji_name_change_type = models.IntegerField(
        verbose_name = "漢字名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    cana_name_change_type = models.IntegerField(
        verbose_name = "カナ名称変更区分",
        blank = True,
        null = True,
        default = None
    )
    speciment_test_comment = models.IntegerField(
        verbose_name = "検体検査コメント",
        blank = True,
        null = True,
        default = None
    )
    general_rule_add_score_type = models.IntegerField(
        verbose_name = "通則加算所定点数対象区分",
        blank = True,
        null = True,
        default = None
    )
    comprehensive_code = models.IntegerField(
        verbose_name = "包括逓減区分",
        blank = True,
        null = True,
        default = None
    )
    ultrasonic_endoscope_add_type = models.IntegerField(
        verbose_name = "超音波内視鏡加算区分",
        blank = True,
        null = True,
        default = None
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    score_destination_identification_in = models.IntegerField(
        verbose_name = "点数欄集計先識別（入院）",
        blank = True,
        null = True,
        default = None
    )
    auto_anastomosis_add_type = models.IntegerField(
        verbose_name = "自動吻合器加算区分",
        blank = True,
        null = True,
        default = None
    )
    bulletin_identification_type1 = models.IntegerField(
        verbose_name = "告示等識別区分（１）",
        blank = True,
        null = True,
        default = None
    )
    bulletin_identification_type2 = models.IntegerField(
        verbose_name = "告示等識別区分（２）",
        blank = True,
        null = True,
        default = None
    )
    area_add = models.IntegerField(
        verbose_name = "地域加算",
        blank = True,
        null = True,
        default = None
    )
    beds_type = models.IntegerField(
        verbose_name = "病床数区分",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code1 = models.IntegerField(
        verbose_name = "施設基準１＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code2 = models.IntegerField(
        verbose_name = "施設基準２＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code3 = models.IntegerField(
        verbose_name = "施設基準３＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code4 = models.IntegerField(
        verbose_name = "施設基準４＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code5 = models.IntegerField(
        verbose_name = "施設基準５＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code6 = models.IntegerField(
        verbose_name = "施設基準６＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code7 = models.IntegerField(
        verbose_name = "施設基準７＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code8 = models.IntegerField(
        verbose_name = "施設基準８＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code9 = models.IntegerField(
        verbose_name = "施設基準９＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code10 = models.IntegerField(
        verbose_name = "施設基準１０＿施設基準コード",
        blank = True,
        null = True,
        default = None
    )
    ultrasonic_coagulator_type = models.IntegerField(
        verbose_name = "超音波凝固切開装置等加算区分",
        blank = True,
        null = True,
        default = None
    )
    short_stay_surgery = models.IntegerField(
        verbose_name = "短期滞在手術",
        blank = True,
        null = True,
        default = None
    )
    dental_type = models.IntegerField(
        verbose_name = "歯科適用区分",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_alphabet = models.CharField(
        verbose_name = "コード表用番号（アルファベット部）",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    bulletin_number_alphabet = models.CharField(
        verbose_name = "告示・通知関連番号（アルファベット部）",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    change_day = models.DateField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.DateField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_chapter = models.IntegerField(
        verbose_name = "コード表用番号＿章",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_department = models.IntegerField(
        verbose_name = "コード表用番号＿部",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_type_number = models.IntegerField(
        verbose_name = "コード表用番号＿区分番号",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_branch_number = models.IntegerField(
        verbose_name = "コード表用番号＿枝番",
        blank = True,
        null = True,
        default = None
    )
    code_table_number_item_number = models.IntegerField(
        verbose_name = "コード表用番号＿項番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_chapter = models.IntegerField(
        verbose_name = "告示・通知関連番号＿章",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_department = models.IntegerField(
        verbose_name = "告示・通知関連番号＿部",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_type_number = models.IntegerField(
        verbose_name = "告示・通知関連番号＿区分番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_branch_number = models.IntegerField(
        verbose_name = "告示・通知関連番号＿枝番",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number_item_number = models.IntegerField(
        verbose_name = "告示・通知関連番号＿項番",
        blank = True,
        null = True,
        default = None
    )
    age_add1_lower_age = models.CharField(
        verbose_name = "年齢加算１＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add1_upper_age = models.CharField(
        verbose_name = "年齢加算１＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add1_annotation_add_item_practice_code = models.IntegerField(
        verbose_name = "年齢加算１＿注加算診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    age_add2_lower_age = models.CharField(
        verbose_name = "年齢加算２＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add2_upper_age = models.CharField(
        verbose_name = "年齢加算２＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add2_annotation_add_item_practice_code = models.IntegerField(
        verbose_name = "年齢加算２＿注加算診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    age_add3_lower_age = models.CharField(
        verbose_name = "年齢加算３＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add3_upper_age = models.CharField(
        verbose_name = "年齢加算３＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add3_annotation_add_item_practice_code = models.IntegerField(
        verbose_name = "年齢加算３＿注加算診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    age_add4_lower_age = models.CharField(
        verbose_name = "年齢加算４＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add4_upper_age = models.CharField(
        verbose_name = "年齢加算４＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    age_add4_annotation_add_item_practice_code = models.IntegerField(
        verbose_name = "年齢加算４＿注加算診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    transfer_related = models.IntegerField(
        verbose_name = "異動関連",
        blank = True,
        null = True,
        default = None
    )
    basic_kanji_name = models.CharField(
        verbose_name = "基本漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    sinus_surgery_endoscope_addition = models.CharField(
        verbose_name = "副鼻腔手術用内視鏡加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    sinus_surgery_tissue_resection_equipment_addition = models.CharField(
        verbose_name = "副鼻腔手術用骨軟部組織切除機器加算 ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    long_term_anesthesia_management_addition = models.CharField(
        verbose_name = "長時間麻酔管理加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    score_type_number = models.CharField(
        verbose_name = "点数表区分番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    monitoring_addition = models.CharField(
        verbose_name = "モニタリング加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    cryopreserved_allogeneic_tissue_addition = models.CharField(
        verbose_name = "凍結保存同種組織加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    malignant_tumor_histopathological_sample_addition = models.CharField(
        verbose_name = "悪性腫瘍病理組織標本加算",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    external_fixator_addition = models.IntegerField(
        verbose_name = "創外固定器加算",
        blank = True,
        null = True,
        default = None
    )
    ultrasonic_cutting_equipment_addition = models.IntegerField(
        verbose_name = "超音波切削機器加算",
        blank = True,
        null = True,
        default = None
    )
    left_atrial_appendage_closure_surgery_addition = models.IntegerField(
        verbose_name = "左心耳閉鎖術併施加算",
        blank = True,
        null = True,
        default = None
    )
    improve_countermeasures_against_foreign_infections_additions = models.IntegerField(
        verbose_name = "外来感染対策向上加算等",
        blank = True,
        null = True,
        default = None
    )
    otolaryngology_infant_treatment_addition = models.IntegerField(
        verbose_name = "耳鼻咽喉科乳幼児処置加算",
        blank = True,
        null = True,
        default = None
    )
    otolaryngology_infant_treatment_drug_support_addition = models.IntegerField(
        verbose_name = "耳鼻咽喉科小児抗菌薬適正使用支援加算",
        blank = True,
        null = True,
        default = None
    )
    incision_local_negative_treatment_device_addition = models.IntegerField(
        verbose_name = "切開創局所陰圧閉鎖処置機器加算",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve6 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve7 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve8 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve9 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve10 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve11 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve12 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve13 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve14 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve15 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve16 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve17 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve18 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve19 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve20 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve21 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve22 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve23 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve24 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve25 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve26 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve27 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "master_practice"
        verbose_name_plural = "M:医科診療行為マスター"

class MasterDispensing(models.Model):
    change_type = models.IntegerField(
        verbose_name = "変更区分",
        blank = True,
        null = True,
        default = None
    )
    master_type = models.CharField(
        verbose_name = "マスター種別",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dispensing_code = models.IntegerField(
        verbose_name = "調剤行為コード",
        blank = True,
        null = True,
        default = None
    )
    dispensing_kanji_significant_digits = models.IntegerField(
        verbose_name = "調剤行為名称＿漢字有効桁数",
        blank = True,
        null = True,
        default = None
    )
    dispensing_kanji_name = models.CharField(
        verbose_name = "調剤行為名称＿漢字名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dispensing_cana_significant_digits = models.IntegerField(
        verbose_name = "調剤行為名称＿カナ有効桁数",
        blank = True,
        null = True,
        default = None
    )
    dispensing_cana_name = models.CharField(
        verbose_name = "調剤行為名称＿カナ名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    receipt_mark_code = models.IntegerField(
        verbose_name = "レセプト表示用記号コード",
        blank = True,
        null = True,
        default = None
    )
    receipt_display_order_code = models.IntegerField(
        verbose_name = "レセプト表示順番号",
        blank = True,
        null = True,
        default = None
    )
    new_score_etc_identification = models.IntegerField(
        verbose_name = "新又は現点数識別",
        blank = True,
        null = True,
        default = None
    )
    dispensing_quantity_calculation_flag = models.IntegerField(
        verbose_name = "調剤数量計算フラグ",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_new_score = models.IntegerField(
        verbose_name = "点数計算＿新又は現点数（基本点数）",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_etch_value_identification = models.IntegerField(
        verbose_name = "点数計算＿きざみ値計算識別",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_lower_limit = models.IntegerField(
        verbose_name = "点数計算＿下限値",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_upper_limit = models.IntegerField(
        verbose_name = "点数計算＿上限値",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_etch_value = models.IntegerField(
        verbose_name = "点数計算＿きざみ値",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_etch_score = models.IntegerField(
        verbose_name = "点数計算＿きざみ点数",
        blank = True,
        null = True,
        default = None
    )
    score_calculation_limits_error_process = models.IntegerField(
        verbose_name = "点数計算＿上下限エラー処理",
        blank = True,
        null = True,
        default = None
    )
    subtraction_act_type = models.IntegerField(
        verbose_name = "減算行為区分",
        blank = True,
        null = True,
        default = None
    )
    subtraction_subject_act_type = models.IntegerField(
        verbose_name = "減算対象行為区分",
        blank = True,
        null = True,
        default = None
    )
    dispensing_identification_type = models.IntegerField(
        verbose_name = "調剤行為識別区分",
        blank = True,
        null = True,
        default = None
    )
    comprehensive_identification_code = models.IntegerField(
        verbose_name = "包括識別区分",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    dispensing_type1 = models.IntegerField(
        verbose_name = "調剤行為種類（１）",
        blank = True,
        null = True,
        default = None
    )
    dispensing_type2 = models.IntegerField(
        verbose_name = "調剤行為種類（２）",
        blank = True,
        null = True,
        default = None
    )
    late_elderly_code = models.IntegerField(
        verbose_name = "後期高齢者適用区分",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code1 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード①",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code2 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード②",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code3 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード③",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code4 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード④",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code5 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑤",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code6 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑥",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code7 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑦",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code8 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑧",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code9 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑨",
        blank = True,
        null = True,
        default = None
    )
    facility_standard_code10 = models.IntegerField(
        verbose_name = "施設基準＿施設基準コード⑩",
        blank = True,
        null = True,
        default = None
    )
    receipt_unit_contradiction_type_code = models.IntegerField(
        verbose_name = "レセプト単位背反区分コード",
        blank = True,
        null = True,
        default = None
    )
    prescription_reception_unit_contradictory_type_code = models.IntegerField(
        verbose_name = "処方箋受付回単位背反区分コード",
        blank = True,
        null = True,
        default = None
    )
    dispensing_unit_contraction_type_code = models.IntegerField(
        verbose_name = "調剤単位背反区分コード",
        blank = True,
        null = True,
        default = None
    )
    special_drug = models.IntegerField(
        verbose_name = "麻薬・毒薬・覚醒剤原料・向精神薬",
        blank = True,
        null = True,
        default = None
    )
    time_add_code = models.IntegerField(
        verbose_name = "時間加算区分",
        blank = True,
        null = True,
        default = None
    )
    dosage_form = models.IntegerField(
        verbose_name = "剤形",
        blank = True,
        null = True,
        default = None
    )
    receipt_unit_upper_limit = models.IntegerField(
        verbose_name = "レセプト単位＿上限回数",
        blank = True,
        null = True,
        default = None
    )
    receipt_unit_upper_limit_error_proces = models.IntegerField(
        verbose_name = "レセプト単位＿上限回数エラー処理",
        blank = True,
        null = True,
        default = None
    )
    receipt_unit_lower_limit = models.IntegerField(
        verbose_name = "処方箋受付回単位＿上限回数",
        blank = True,
        null = True,
        default = None
    )
    receipt_unit_lower_limit_error_proces = models.IntegerField(
        verbose_name = "処方箋受付回単位＿上限回数エラー処理",
        blank = True,
        null = True,
        default = None
    )
    annotation_add_code = models.IntegerField(
        verbose_name = "注加算＿コード",
        blank = True,
        null = True,
        default = None
    )
    annotation_add_number = models.CharField(
        verbose_name = "注加算＿通番",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    limits_age_lower_age = models.CharField(
        verbose_name = "上下限年齢＿下限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    limits_age_upper_age = models.CharField(
        verbose_name = "上下限年齢＿上限年齢",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    pharmaceutical_management_fee_type = models.IntegerField(
        verbose_name = "薬学管理料区分",
        blank = True,
        null = True,
        default = None
    )
    bulletin_identification_type1 = models.IntegerField(
        verbose_name = "告示等識別区分（１）",
        blank = True,
        null = True,
        default = None
    )
    bulletin_identification_type2 = models.IntegerField(
        verbose_name = "告示等識別区分（２）",
        blank = True,
        null = True,
        default = None
    )
    old_score_etc_identification = models.IntegerField(
        verbose_name = "旧点数＿点数識別",
        blank = True,
        null = True,
        default = None
    )
    old_score_etc = models.IntegerField(
        verbose_name = "旧点数＿旧点数",
        blank = True,
        null = True,
        default = None
    )
    change_day = models.IntegerField(
        verbose_name = "変更年月日",
        blank = True,
        null = True,
        default = None
    )
    abolition_day = models.IntegerField(
        verbose_name = "廃止年月日",
        blank = True,
        null = True,
        default = None
    )
    publication_order_number = models.IntegerField(
        verbose_name = "公表順序番号",
        blank = True,
        null = True,
        default = None
    )
    code_table_number = models.IntegerField(
        verbose_name = "コード表用番号",
        blank = True,
        null = True,
        default = None
    )
    bulletin_number = models.IntegerField(
        verbose_name = "告示・通知関連番号",
        blank = True,
        null = True,
        default = None
    )
    transfer_related = models.IntegerField(
        verbose_name = "異動関連",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "master_dispensing"
        verbose_name_plural = "M:調剤行為マスター"

class RecordReceiptInfo(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    prefectures = models.IntegerField(
        verbose_name = "都道府県",
        blank = True,
        null = True,
        default = None
    )
    score_sheet = models.IntegerField(
        verbose_name = "点数表",
        blank = True,
        null = True,
        default = None
    )
    medical_institution_code = models.IntegerField(
        verbose_name = "医療機関コード",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    medical_institution_name = models.CharField(
        verbose_name = "医療機関名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    billing_day = models.IntegerField(
        verbose_name = "請求年月",
        blank = True,
        null = True,
        default = None
    )
    notification = models.CharField(
        verbose_name = "届出",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    multivolume_identifier_info = models.CharField(
        verbose_name = "マルチボリューム識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_receipt_info"
        verbose_name_plural = "R:受付情報レコード"

class RecordMedicalInstitutionInfo(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機",
        blank = True,
        null = True,
        default = None
    )
    prefectures = models.IntegerField(
        verbose_name = "都道府県",
        blank = True,
        null = True,
        default = None
    )
    score_sheet = models.IntegerField(
        verbose_name = "点数表",
        blank = True,
        null = True,
        default = None
    )
    medical_institution_code = models.IntegerField(
        verbose_name = "医療機関コード",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    billing_day = models.IntegerField(
        verbose_name = "請求年月",
        blank = True,
        null = True,
        default = None
    )
    phone_number = models.CharField(
        verbose_name = "電話番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    notification = models.CharField(
        verbose_name = "届出",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_medical_institution_info"
        verbose_name_plural = "R:医療機関情報レコード"

class RecordReceiptCommon(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    receipt_number = models.IntegerField(
        verbose_name = "レセプト番号",
        blank = True,
        null = True,
        default = None
    )
    receipt_identification = models.IntegerField(
        verbose_name = "レセプト種別",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    sex_type = models.IntegerField(
        verbose_name = "男女区分",
        blank = True,
        null = True,
        default = None
    )
    birth_day = models.IntegerField(
        verbose_name = "生年月日",
        blank = True,
        null = True,
        default = None
    )
    benefit_ratio = models.IntegerField(
        verbose_name = "給付割合",
        blank = True,
        null = True,
        default = None
    )
    admission_day = models.IntegerField(
        verbose_name = "入院年月日",
        blank = True,
        null = True,
        default = None
    )
    practice_start_day = models.IntegerField(
        verbose_name = "診療開始日",
        blank = True,
        null = True,
        default = None
    )
    return_origin_yupe = models.IntegerField(
        verbose_name = "転帰区分",
        blank = True,
        null = True,
        default = None
    )
    hospital_ward_type = models.CharField(
        verbose_name = "病棟区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    copayment = models.IntegerField(
        verbose_name = "一部負担金・食事療養費・生活療養費標準負担額区分",
        blank = True,
        null = True,
        default = None
    )
    receipt_special_remarks = models.CharField(
        verbose_name = "レセプト特記事項",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    chart_number = models.CharField(
        verbose_name = "カルテ番号等",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    billing_info1 = models.IntegerField(
        verbose_name = "請求情報1",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    future_hospital_billing = models.IntegerField(
        verbose_name = "未来院請求",
        blank = True,
        null = True,
        default = None
    )
    search_number = models.IntegerField(
        verbose_name = "検索番号",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備_1",
        blank = True,
        null = True,
        default = None
    )
    billing_info2 = models.CharField(
        verbose_name = "請求情報2",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備_2",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備_3",
        blank = True,
        null = True,
        default = None
    )
    reserve6 = models.IntegerField(
        verbose_name = "予備_4",
        blank = True,
        null = True,
        default = None
    )
    cana_name = models.CharField(
        verbose_name = "カタカナ(氏名)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    patient_condition = models.IntegerField(
        verbose_name = "患者の状態",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_receipt_common"
        verbose_name_plural = "R:レセプト共通レコード"

class RecordInsurer(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    insurer_number = models.CharField(
        verbose_name = "保険者番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    insurer_card_code = models.CharField(
        verbose_name = "被保険者証(手帳)等の記号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    insurer_card_number = models.CharField(
        verbose_name = "被保険者証(手帳)等の番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_acrual_days = models.IntegerField(
        verbose_name = "診療実日数",
        blank = True,
        null = True,
        default = None
    )
    total_score = models.IntegerField(
        verbose_name = "合計点数",
        blank = True,
        null = True,
        default = None
    )
    dietary_lifestyle_care_times = models.IntegerField(
        verbose_name = "食事療養・生活療養回数",
        blank = True,
        null = True,
        default = None
    )
    dietary_lifestyle_care_total_amount = models.IntegerField(
        verbose_name = "食事療養・生活療養合計金額",
        blank = True,
        null = True,
        default = None
    )
    professional_reasons = models.IntegerField(
        verbose_name = "職務上の事由",
        blank = True,
        null = True,
        default = None
    )
    certificate_number = models.IntegerField(
        verbose_name = "証明書番号",
        blank = True,
        null = True,
        default = None
    )
    insurance_copayments = models.IntegerField(
        verbose_name = "医療保険一部負担金額",
        blank = True,
        null = True,
        default = None
    )
    exempt_type = models.IntegerField(
        verbose_name = "減免区分",
        blank = True,
        null = True,
        default = None
    )
    reduction_ratio = models.IntegerField(
        verbose_name = "減額割合",
        blank = True,
        null = True,
        default = None
    )
    reduction_amount = models.IntegerField(
        verbose_name = "減額金額",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_insurer"
        verbose_name_plural = "R:保険者レコード"

class RecordPublicExpense(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    payer_number = models.CharField(
        verbose_name = "負担者番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    recipient_number = models.IntegerField(
        verbose_name = "受給者番号",
        blank = True,
        null = True,
        default = None
    )
    optional_benefit_type = models.IntegerField(
        verbose_name = "任意給付区分",
        blank = True,
        null = True,
        default = None
    )
    practice_acrual_days = models.IntegerField(
        verbose_name = "診療実日数",
        blank = True,
        null = True,
        default = None
    )
    total_score = models.IntegerField(
        verbose_name = "合計点数",
        blank = True,
        null = True,
        default = None
    )
    copayment = models.IntegerField(
        verbose_name = "負担金額",
        blank = True,
        null = True,
        default = None
    )
    public_expense_benefit_copayment = models.IntegerField(
        verbose_name = "公費給付対象一部負担金",
        blank = True,
        null = True,
        default = None
    )
    dietary_lifestyle_care_times = models.IntegerField(
        verbose_name = "食事療養・生活療養回数",
        blank = True,
        null = True,
        default = None
    )
    dietary_lifestyle_care_total_amount = models.IntegerField(
        verbose_name = "食事療養・生活療養合計金額",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_public_expense"
        verbose_name_plural = "R:公費レコード"

class RecordStatusCheck(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    payer_class = models.IntegerField(
        verbose_name = "負担者種別",
        blank = True,
        null = True,
        default = None
    )
    confirmation_type = models.IntegerField(
        verbose_name = "確認区分",
        blank = True,
        null = True,
        default = None
    )
    insurer_number_etc = models.CharField(
        verbose_name = "保険者番号等(資格確認)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    insurer_card_code_status_check = models.CharField(
        verbose_name = "被保険者証(手帳)等の記号(資格確認)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    insurer_card_number_status_check = models.CharField(
        verbose_name = "被保険者証(手帳)等の番号(資格確認)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    branch_number = models.IntegerField(
        verbose_name = "枝番",
        blank = True,
        null = True,
        default = None
    )
    recipient_id = models.IntegerField(
        verbose_name = "受給者番号",
        blank = True,
        null = True,
        default = None
    )
    reserve = models.IntegerField(
        verbose_name = "予備",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_status_check"
        verbose_name_plural = "R:資格確認レコード"

class RecordReceiptDay(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    payer_type = models.IntegerField(
        verbose_name = "負担者種別",
        blank = True,
        null = True,
        default = None
    )
    info1 = models.IntegerField(
        verbose_name = "1日の情報",
        blank = True,
        null = True,
        default = None
    )
    info2 = models.IntegerField(
        verbose_name = "2日の情報",
        blank = True,
        null = True,
        default = None
    )
    info3 = models.IntegerField(
        verbose_name = "3日の情報",
        blank = True,
        null = True,
        default = None
    )
    info4 = models.IntegerField(
        verbose_name = "4日の情報",
        blank = True,
        null = True,
        default = None
    )
    info5 = models.IntegerField(
        verbose_name = "5日の情報",
        blank = True,
        null = True,
        default = None
    )
    info6 = models.IntegerField(
        verbose_name = "6日の情報",
        blank = True,
        null = True,
        default = None
    )
    info7 = models.IntegerField(
        verbose_name = "7日の情報",
        blank = True,
        null = True,
        default = None
    )
    info8 = models.IntegerField(
        verbose_name = "8日の情報",
        blank = True,
        null = True,
        default = None
    )
    info9 = models.IntegerField(
        verbose_name = "9日の情報",
        blank = True,
        null = True,
        default = None
    )
    info10 = models.IntegerField(
        verbose_name = "10日の情報",
        blank = True,
        null = True,
        default = None
    )
    info11 = models.IntegerField(
        verbose_name = "11日の情報",
        blank = True,
        null = True,
        default = None
    )
    info12 = models.IntegerField(
        verbose_name = "12日の情報",
        blank = True,
        null = True,
        default = None
    )
    info13 = models.IntegerField(
        verbose_name = "13日の情報",
        blank = True,
        null = True,
        default = None
    )
    info14 = models.IntegerField(
        verbose_name = "14日の情報",
        blank = True,
        null = True,
        default = None
    )
    info15 = models.IntegerField(
        verbose_name = "15日の情報",
        blank = True,
        null = True,
        default = None
    )
    info16 = models.IntegerField(
        verbose_name = "16日の情報",
        blank = True,
        null = True,
        default = None
    )
    info17 = models.IntegerField(
        verbose_name = "17日の情報",
        blank = True,
        null = True,
        default = None
    )
    info18 = models.IntegerField(
        verbose_name = "18日の情報",
        blank = True,
        null = True,
        default = None
    )
    info19 = models.IntegerField(
        verbose_name = "19日の情報",
        blank = True,
        null = True,
        default = None
    )
    info20 = models.IntegerField(
        verbose_name = "20日の情報",
        blank = True,
        null = True,
        default = None
    )
    info21 = models.IntegerField(
        verbose_name = "21日の情報",
        blank = True,
        null = True,
        default = None
    )
    info22 = models.IntegerField(
        verbose_name = "22日の情報",
        blank = True,
        null = True,
        default = None
    )
    info23 = models.IntegerField(
        verbose_name = "23日の情報",
        blank = True,
        null = True,
        default = None
    )
    info24 = models.IntegerField(
        verbose_name = "24日の情報",
        blank = True,
        null = True,
        default = None
    )
    info25 = models.IntegerField(
        verbose_name = "25日の情報",
        blank = True,
        null = True,
        default = None
    )
    info26 = models.IntegerField(
        verbose_name = "26日の情報",
        blank = True,
        null = True,
        default = None
    )
    info27 = models.IntegerField(
        verbose_name = "27日の情報",
        blank = True,
        null = True,
        default = None
    )
    info28 = models.IntegerField(
        verbose_name = "28日の情報",
        blank = True,
        null = True,
        default = None
    )
    info29 = models.IntegerField(
        verbose_name = "29日の情報",
        blank = True,
        null = True,
        default = None
    )
    info30 = models.IntegerField(
        verbose_name = "30日の情報",
        blank = True,
        null = True,
        default = None
    )
    info31 = models.IntegerField(
        verbose_name = "31日の情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_receipt_day"
        verbose_name_plural = "R:受診日等レコード"

class RecordCounterAmount(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    counter_amount_type = models.IntegerField(
        verbose_name = "窓口負担額区分",
        blank = True,
        null = True,
        default = None
    )
    reserve1 = models.IntegerField(
        verbose_name = "予備1",
        blank = True,
        null = True,
        default = None
    )
    reserve2 = models.IntegerField(
        verbose_name = "予備2",
        blank = True,
        null = True,
        default = None
    )
    reserve3 = models.IntegerField(
        verbose_name = "予備3",
        blank = True,
        null = True,
        default = None
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備4",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備5",
        blank = True,
        null = True,
        default = None
    )
    reserve6 = models.IntegerField(
        verbose_name = "予備6",
        blank = True,
        null = True,
        default = None
    )
    reserve7 = models.IntegerField(
        verbose_name = "予備7",
        blank = True,
        null = True,
        default = None
    )
    reserve8 = models.IntegerField(
        verbose_name = "予備8",
        blank = True,
        null = True,
        default = None
    )
    reserve9 = models.IntegerField(
        verbose_name = "予備9",
        blank = True,
        null = True,
        default = None
    )
    reserve10 = models.IntegerField(
        verbose_name = "予備10",
        blank = True,
        null = True,
        default = None
    )
    reserve11 = models.IntegerField(
        verbose_name = "予備11",
        blank = True,
        null = True,
        default = None
    )
    reserve12 = models.IntegerField(
        verbose_name = "予備12",
        blank = True,
        null = True,
        default = None
    )
    reserve13 = models.IntegerField(
        verbose_name = "予備13",
        blank = True,
        null = True,
        default = None
    )
    reserve14 = models.IntegerField(
        verbose_name = "予備14",
        blank = True,
        null = True,
        default = None
    )
    reserve15 = models.IntegerField(
        verbose_name = "予備15",
        blank = True,
        null = True,
        default = None
    )
    reserve16 = models.IntegerField(
        verbose_name = "予備16",
        blank = True,
        null = True,
        default = None
    )
    reserve17 = models.IntegerField(
        verbose_name = "予備17",
        blank = True,
        null = True,
        default = None
    )
    reserve18 = models.IntegerField(
        verbose_name = "予備18",
        blank = True,
        null = True,
        default = None
    )
    reserve19 = models.IntegerField(
        verbose_name = "予備19",
        blank = True,
        null = True,
        default = None
    )
    reserve20 = models.IntegerField(
        verbose_name = "予備20",
        blank = True,
        null = True,
        default = None
    )
    reserve21 = models.IntegerField(
        verbose_name = "予備21",
        blank = True,
        null = True,
        default = None
    )
    reserve22 = models.IntegerField(
        verbose_name = "予備22",
        blank = True,
        null = True,
        default = None
    )
    reserve23 = models.IntegerField(
        verbose_name = "予備23",
        blank = True,
        null = True,
        default = None
    )
    reserve24 = models.IntegerField(
        verbose_name = "予備24",
        blank = True,
        null = True,
        default = None
    )
    reserve25 = models.IntegerField(
        verbose_name = "予備25",
        blank = True,
        null = True,
        default = None
    )
    reserve26 = models.IntegerField(
        verbose_name = "予備26",
        blank = True,
        null = True,
        default = None
    )
    reserve27 = models.IntegerField(
        verbose_name = "予備27",
        blank = True,
        null = True,
        default = None
    )
    reserve28 = models.IntegerField(
        verbose_name = "予備28",
        blank = True,
        null = True,
        default = None
    )
    reserve29 = models.IntegerField(
        verbose_name = "予備29",
        blank = True,
        null = True,
        default = None
    )
    reserve30 = models.IntegerField(
        verbose_name = "予備30",
        blank = True,
        null = True,
        default = None
    )
    reserve31 = models.IntegerField(
        verbose_name = "予備31",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_counter_amount"
        verbose_name_plural = "R:窓口負担額レコード"

class RecordDiseasePosition(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    start_practice = models.IntegerField(
        verbose_name = "診療開始日",
        blank = True,
        null = True,
        default = None
    )
    transcription_type = models.IntegerField(
        verbose_name = "転記区分",
        blank = True,
        null = True,
        default = None
    )
    dentation_code_diseaase = models.CharField(
        verbose_name = "歯式コード(傷病名)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_name_code = models.IntegerField(
        verbose_name = "傷病名コード",
        blank = True,
        null = True,
        default = None
    )
    modifier_code = models.CharField(
        verbose_name = "修飾語コード",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    disease_name = models.CharField(
        verbose_name = "傷病名称",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    comorbidities_number = models.IntegerField(
        verbose_name = "併存傷病名数",
        blank = True,
        null = True,
        default = None
    )
    disease_condition_transition = models.IntegerField(
        verbose_name = "病態移行",
        blank = True,
        null = True,
        default = None
    )
    major_disease = models.IntegerField(
        verbose_name = "主傷病",
        blank = True,
        null = True,
        default = None
    )
    comment_code = models.IntegerField(
        verbose_name = "コメントコード",
        blank = True,
        null = True,
        default = None
    )
    supplementary_comment = models.CharField(
        verbose_name = "補足コメント",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dentation_code_comment = models.CharField(
        verbose_name = "歯式コード(補足コメント)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_disease_position"
        verbose_name_plural = "R:傷病名部位レコード"

class RecordDentalPractice(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_identification = models.IntegerField(
        verbose_name = "診療識別",
        blank = True,
        null = True,
        default = None
    )
    payer_type = models.CharField(
        verbose_name = "負担区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_code = models.IntegerField(
        verbose_name = "診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    practice_volume_data1 = models.IntegerField(
        verbose_name = "診療行為数量データ1",
        blank = True,
        null = True,
        default = None
    )
    practice_volume_data2 = models.IntegerField(
        verbose_name = "診療行為数量データ2",
        blank = True,
        null = True,
        default = None
    )
    add_code1 = models.CharField(
        verbose_name = "加算コード1",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data1 = models.IntegerField(
        verbose_name = "加算数量データ1",
        blank = True,
        null = True,
        default = None
    )
    add_code2 = models.CharField(
        verbose_name = "加算コード2",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data2 = models.IntegerField(
        verbose_name = "加算数量データ2",
        blank = True,
        null = True,
        default = None
    )
    add_code3 = models.CharField(
        verbose_name = "加算コード3",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data3 = models.IntegerField(
        verbose_name = "加算数量データ3",
        blank = True,
        null = True,
        default = None
    )
    add_code4 = models.CharField(
        verbose_name = "加算コード4",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data4 = models.IntegerField(
        verbose_name = "加算数量データ4",
        blank = True,
        null = True,
        default = None
    )
    add_code5 = models.CharField(
        verbose_name = "加算コード5",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data5 = models.IntegerField(
        verbose_name = "加算数量データ5",
        blank = True,
        null = True,
        default = None
    )
    add_code6 = models.CharField(
        verbose_name = "加算コード6",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data6 = models.IntegerField(
        verbose_name = "加算数量データ6",
        blank = True,
        null = True,
        default = None
    )
    add_code7 = models.CharField(
        verbose_name = "加算コード7",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data7 = models.IntegerField(
        verbose_name = "加算数量データ7",
        blank = True,
        null = True,
        default = None
    )
    add_code8 = models.CharField(
        verbose_name = "加算コード8",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data8 = models.IntegerField(
        verbose_name = "加算数量データ8",
        blank = True,
        null = True,
        default = None
    )
    add_code9 = models.CharField(
        verbose_name = "加算コード9",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data9 = models.IntegerField(
        verbose_name = "加算数量データ9",
        blank = True,
        null = True,
        default = None
    )
    add_code10 = models.CharField(
        verbose_name = "加算コード10",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data10 = models.IntegerField(
        verbose_name = "加算数量データ10",
        blank = True,
        null = True,
        default = None
    )
    add_code11 = models.CharField(
        verbose_name = "加算コード11",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data11 = models.IntegerField(
        verbose_name = "加算数量データ11",
        blank = True,
        null = True,
        default = None
    )
    add_code12 = models.CharField(
        verbose_name = "加算コード12",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data12 = models.IntegerField(
        verbose_name = "加算数量データ12",
        blank = True,
        null = True,
        default = None
    )
    add_code13 = models.CharField(
        verbose_name = "加算コード13",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data13 = models.IntegerField(
        verbose_name = "加算数量データ13",
        blank = True,
        null = True,
        default = None
    )
    add_code14 = models.CharField(
        verbose_name = "加算コード14",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data14 = models.IntegerField(
        verbose_name = "加算数量データ14",
        blank = True,
        null = True,
        default = None
    )
    add_code15 = models.CharField(
        verbose_name = "加算コード15",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data15 = models.IntegerField(
        verbose_name = "加算数量データ15",
        blank = True,
        null = True,
        default = None
    )
    add_code16 = models.CharField(
        verbose_name = "加算コード16",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data16 = models.IntegerField(
        verbose_name = "加算数量データ16",
        blank = True,
        null = True,
        default = None
    )
    add_code17 = models.CharField(
        verbose_name = "加算コード17",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data17 = models.IntegerField(
        verbose_name = "加算数量データ17",
        blank = True,
        null = True,
        default = None
    )
    add_code18 = models.CharField(
        verbose_name = "加算コード18",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data18 = models.IntegerField(
        verbose_name = "加算数量データ18",
        blank = True,
        null = True,
        default = None
    )
    add_code19 = models.CharField(
        verbose_name = "加算コード19",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data19 = models.IntegerField(
        verbose_name = "加算数量データ19",
        blank = True,
        null = True,
        default = None
    )
    add_code20 = models.CharField(
        verbose_name = "加算コード20",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data20 = models.IntegerField(
        verbose_name = "加算数量データ20",
        blank = True,
        null = True,
        default = None
    )
    add_code21 = models.CharField(
        verbose_name = "加算コード21",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data21 = models.IntegerField(
        verbose_name = "加算数量データ21",
        blank = True,
        null = True,
        default = None
    )
    add_code22 = models.CharField(
        verbose_name = "加算コード22",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data22 = models.IntegerField(
        verbose_name = "加算数量データ22",
        blank = True,
        null = True,
        default = None
    )
    add_code23 = models.CharField(
        verbose_name = "加算コード23",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data23 = models.IntegerField(
        verbose_name = "加算数量データ23",
        blank = True,
        null = True,
        default = None
    )
    add_code24 = models.CharField(
        verbose_name = "加算コード24",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data24 = models.IntegerField(
        verbose_name = "加算数量データ24",
        blank = True,
        null = True,
        default = None
    )
    add_code25 = models.CharField(
        verbose_name = "加算コード25",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data25 = models.IntegerField(
        verbose_name = "加算数量データ25",
        blank = True,
        null = True,
        default = None
    )
    add_code26 = models.CharField(
        verbose_name = "加算コード26",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data26 = models.IntegerField(
        verbose_name = "加算数量データ26",
        blank = True,
        null = True,
        default = None
    )
    add_code27 = models.CharField(
        verbose_name = "加算コード27",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data27 = models.IntegerField(
        verbose_name = "加算数量データ27",
        blank = True,
        null = True,
        default = None
    )
    add_code28 = models.CharField(
        verbose_name = "加算コード28",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data28 = models.IntegerField(
        verbose_name = "加算数量データ28",
        blank = True,
        null = True,
        default = None
    )
    add_code29 = models.CharField(
        verbose_name = "加算コード29",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data29 = models.IntegerField(
        verbose_name = "加算数量データ29",
        blank = True,
        null = True,
        default = None
    )
    add_code30 = models.CharField(
        verbose_name = "加算コード30",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data30 = models.IntegerField(
        verbose_name = "加算数量データ30",
        blank = True,
        null = True,
        default = None
    )
    add_code31 = models.CharField(
        verbose_name = "加算コード31",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data31 = models.IntegerField(
        verbose_name = "加算数量データ31",
        blank = True,
        null = True,
        default = None
    )
    add_code32 = models.CharField(
        verbose_name = "加算コード32",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data32 = models.IntegerField(
        verbose_name = "加算数量データ32",
        blank = True,
        null = True,
        default = None
    )
    add_code33 = models.CharField(
        verbose_name = "加算コード33",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data33 = models.IntegerField(
        verbose_name = "加算数量データ33",
        blank = True,
        null = True,
        default = None
    )
    add_code34 = models.CharField(
        verbose_name = "加算コード34",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data34 = models.IntegerField(
        verbose_name = "加算数量データ34",
        blank = True,
        null = True,
        default = None
    )
    add_code35 = models.CharField(
        verbose_name = "加算コード35",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    add_volume_data35 = models.IntegerField(
        verbose_name = "加算数量データ35",
        blank = True,
        null = True,
        default = None
    )
    score = models.IntegerField(
        verbose_name = "点数",
        blank = True,
        null = True,
        default = None
    )
    count = models.IntegerField(
        verbose_name = "回数",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info1 = models.IntegerField(
        verbose_name = "算定日情報_1日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info2 = models.IntegerField(
        verbose_name = "算定日情報_2日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info3 = models.IntegerField(
        verbose_name = "算定日情報_3日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info4 = models.IntegerField(
        verbose_name = "算定日情報_4日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info5 = models.IntegerField(
        verbose_name = "算定日情報_5日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info6 = models.IntegerField(
        verbose_name = "算定日情報_6日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info7 = models.IntegerField(
        verbose_name = "算定日情報_7日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info8 = models.IntegerField(
        verbose_name = "算定日情報_8日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info9 = models.IntegerField(
        verbose_name = "算定日情報_9日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info10 = models.IntegerField(
        verbose_name = "算定日情報_10日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info11 = models.IntegerField(
        verbose_name = "算定日情報_11日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info12 = models.IntegerField(
        verbose_name = "算定日情報_12日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info13 = models.IntegerField(
        verbose_name = "算定日情報_13日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info14 = models.IntegerField(
        verbose_name = "算定日情報_14日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info15 = models.IntegerField(
        verbose_name = "算定日情報_15日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info16 = models.IntegerField(
        verbose_name = "算定日情報_16日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info17 = models.IntegerField(
        verbose_name = "算定日情報_17日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info18 = models.IntegerField(
        verbose_name = "算定日情報_18日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info19 = models.IntegerField(
        verbose_name = "算定日情報_19日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info20 = models.IntegerField(
        verbose_name = "算定日情報_20日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info21 = models.IntegerField(
        verbose_name = "算定日情報_21日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info22 = models.IntegerField(
        verbose_name = "算定日情報_22日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info23 = models.IntegerField(
        verbose_name = "算定日情報_23日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info24 = models.IntegerField(
        verbose_name = "算定日情報_24日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info25 = models.IntegerField(
        verbose_name = "算定日情報_25日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info26 = models.IntegerField(
        verbose_name = "算定日情報_26日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info27 = models.IntegerField(
        verbose_name = "算定日情報_27日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info28 = models.IntegerField(
        verbose_name = "算定日情報_28日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info29 = models.IntegerField(
        verbose_name = "算定日情報_29日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info30 = models.IntegerField(
        verbose_name = "算定日情報_30日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info31 = models.IntegerField(
        verbose_name = "算定日情報_31日の情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_dental_practice"
        verbose_name_plural = "R:歯科診療行為レコード"

class RecordPractice(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_identification = models.IntegerField(
        verbose_name = "診療識別",
        blank = True,
        null = True,
        default = None
    )
    payer_type = models.CharField(
        verbose_name = "負担区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_code = models.IntegerField(
        verbose_name = "診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    volume_data = models.IntegerField(
        verbose_name = "数量データ",
        blank = True,
        null = True,
        default = None
    )
    score = models.IntegerField(
        verbose_name = "点数",
        blank = True,
        null = True,
        default = None
    )
    count = models.IntegerField(
        verbose_name = "回数",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info1 = models.IntegerField(
        verbose_name = "算定日情報_1日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info2 = models.IntegerField(
        verbose_name = "算定日情報_2日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info3 = models.IntegerField(
        verbose_name = "算定日情報_3日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info4 = models.IntegerField(
        verbose_name = "算定日情報_4日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info5 = models.IntegerField(
        verbose_name = "算定日情報_5日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info6 = models.IntegerField(
        verbose_name = "算定日情報_6日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info7 = models.IntegerField(
        verbose_name = "算定日情報_7日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info8 = models.IntegerField(
        verbose_name = "算定日情報_8日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info9 = models.IntegerField(
        verbose_name = "算定日情報_9日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info10 = models.IntegerField(
        verbose_name = "算定日情報_10日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info11 = models.IntegerField(
        verbose_name = "算定日情報_11日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info12 = models.IntegerField(
        verbose_name = "算定日情報_12日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info13 = models.IntegerField(
        verbose_name = "算定日情報_13日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info14 = models.IntegerField(
        verbose_name = "算定日情報_14日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info15 = models.IntegerField(
        verbose_name = "算定日情報_15日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info16 = models.IntegerField(
        verbose_name = "算定日情報_16日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info17 = models.IntegerField(
        verbose_name = "算定日情報_17日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info18 = models.IntegerField(
        verbose_name = "算定日情報_18日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info19 = models.IntegerField(
        verbose_name = "算定日情報_19日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info20 = models.IntegerField(
        verbose_name = "算定日情報_20日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info21 = models.IntegerField(
        verbose_name = "算定日情報_21日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info22 = models.IntegerField(
        verbose_name = "算定日情報_22日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info23 = models.IntegerField(
        verbose_name = "算定日情報_23日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info24 = models.IntegerField(
        verbose_name = "算定日情報_24日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info25 = models.IntegerField(
        verbose_name = "算定日情報_25日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info26 = models.IntegerField(
        verbose_name = "算定日情報_26日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info27 = models.IntegerField(
        verbose_name = "算定日情報_27日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info28 = models.IntegerField(
        verbose_name = "算定日情報_28日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info29 = models.IntegerField(
        verbose_name = "算定日情報_29日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info30 = models.IntegerField(
        verbose_name = "算定日情報_30日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info31 = models.IntegerField(
        verbose_name = "算定日情報_31日の情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_practice"
        verbose_name_plural = "R:医科診療行為レコード"

class RecordDrug(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_identification = models.IntegerField(
        verbose_name = "診療識別",
        blank = True,
        null = True,
        default = None
    )
    payer_type = models.CharField(
        verbose_name = "負担区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    drug_code = models.IntegerField(
        verbose_name = "医薬品コード",
        blank = True,
        null = True,
        default = None
    )
    usage = models.CharField(
        verbose_name = "使用量",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    score = models.IntegerField(
        verbose_name = "点数",
        blank = True,
        null = True,
        default = None
    )
    count = models.IntegerField(
        verbose_name = "回数",
        blank = True,
        null = True,
        default = None
    )
    drug_type = models.CharField(
        verbose_name = "医薬品区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    calculation_day_info1 = models.IntegerField(
        verbose_name = "算定日情報_1日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info2 = models.IntegerField(
        verbose_name = "算定日情報_2日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info3 = models.IntegerField(
        verbose_name = "算定日情報_3日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info4 = models.IntegerField(
        verbose_name = "算定日情報_4日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info5 = models.IntegerField(
        verbose_name = "算定日情報_5日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info6 = models.IntegerField(
        verbose_name = "算定日情報_6日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info7 = models.IntegerField(
        verbose_name = "算定日情報_7日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info8 = models.IntegerField(
        verbose_name = "算定日情報_8日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info9 = models.IntegerField(
        verbose_name = "算定日情報_9日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info10 = models.IntegerField(
        verbose_name = "算定日情報_10日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info11 = models.IntegerField(
        verbose_name = "算定日情報_11日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info12 = models.IntegerField(
        verbose_name = "算定日情報_12日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info13 = models.IntegerField(
        verbose_name = "算定日情報_13日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info14 = models.IntegerField(
        verbose_name = "算定日情報_14日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info15 = models.IntegerField(
        verbose_name = "算定日情報_15日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info16 = models.IntegerField(
        verbose_name = "算定日情報_16日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info17 = models.IntegerField(
        verbose_name = "算定日情報_17日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info18 = models.IntegerField(
        verbose_name = "算定日情報_18日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info19 = models.IntegerField(
        verbose_name = "算定日情報_19日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info20 = models.IntegerField(
        verbose_name = "算定日情報_20日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info21 = models.IntegerField(
        verbose_name = "算定日情報_21日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info22 = models.IntegerField(
        verbose_name = "算定日情報_22日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info23 = models.IntegerField(
        verbose_name = "算定日情報_23日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info24 = models.IntegerField(
        verbose_name = "算定日情報_24日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info25 = models.IntegerField(
        verbose_name = "算定日情報_25日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info26 = models.IntegerField(
        verbose_name = "算定日情報_26日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info27 = models.IntegerField(
        verbose_name = "算定日情報_27日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info28 = models.IntegerField(
        verbose_name = "算定日情報_28日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info29 = models.IntegerField(
        verbose_name = "算定日情報_29日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info30 = models.IntegerField(
        verbose_name = "算定日情報_30日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info31 = models.IntegerField(
        verbose_name = "算定日情報_31日の情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_drug"
        verbose_name_plural = "R:医薬品レコード"

class RecordSpecialEquipment(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_identification = models.IntegerField(
        verbose_name = "診療識別",
        blank = True,
        null = True,
        default = None
    )
    payer_type = models.CharField(
        verbose_name = "負担区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    special_equipment_code = models.IntegerField(
        verbose_name = "特定器材コード",
        blank = True,
        null = True,
        default = None
    )
    usage = models.CharField(
        verbose_name = "使用量",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    unit_code = models.IntegerField(
        verbose_name = "単位コード",
        blank = True,
        null = True,
        default = None
    )
    unit_cost = models.IntegerField(
        verbose_name = "単価",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_add_code1 = models.CharField(
        verbose_name = "特定器材加算等コード1",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    special_equipment_add_volume_data1 = models.IntegerField(
        verbose_name = "特定器材加算等数量データ1",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_add_code2 = models.IntegerField(
        verbose_name = "特定器材加算等コード2",
        blank = True,
        null = True,
        default = None
    )
    special_equipment_add_volume_data2 = models.CharField(
        verbose_name = "特定器材加算等数量データ2",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    standard_or_size = models.CharField(
        verbose_name = "商品名及び規格又はサイズ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    score = models.IntegerField(
        verbose_name = "点数",
        blank = True,
        null = True,
        default = None
    )
    count = models.IntegerField(
        verbose_name = "回数",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info1 = models.IntegerField(
        verbose_name = "算定日情報_1日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info2 = models.IntegerField(
        verbose_name = "算定日情報_2日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info3 = models.IntegerField(
        verbose_name = "算定日情報_3日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info4 = models.IntegerField(
        verbose_name = "算定日情報_4日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info5 = models.IntegerField(
        verbose_name = "算定日情報_5日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info6 = models.IntegerField(
        verbose_name = "算定日情報_6日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info7 = models.IntegerField(
        verbose_name = "算定日情報_7日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info8 = models.IntegerField(
        verbose_name = "算定日情報_8日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info9 = models.IntegerField(
        verbose_name = "算定日情報_9日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info10 = models.IntegerField(
        verbose_name = "算定日情報_10日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info11 = models.IntegerField(
        verbose_name = "算定日情報_11日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info12 = models.IntegerField(
        verbose_name = "算定日情報_12日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info13 = models.IntegerField(
        verbose_name = "算定日情報_13日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info14 = models.IntegerField(
        verbose_name = "算定日情報_14日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info15 = models.IntegerField(
        verbose_name = "算定日情報_15日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info16 = models.IntegerField(
        verbose_name = "算定日情報_16日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info17 = models.IntegerField(
        verbose_name = "算定日情報_17日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info18 = models.IntegerField(
        verbose_name = "算定日情報_18日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info19 = models.IntegerField(
        verbose_name = "算定日情報_19日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info20 = models.IntegerField(
        verbose_name = "算定日情報_20日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info21 = models.IntegerField(
        verbose_name = "算定日情報_21日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info22 = models.IntegerField(
        verbose_name = "算定日情報_22日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info23 = models.IntegerField(
        verbose_name = "算定日情報_23日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info24 = models.IntegerField(
        verbose_name = "算定日情報_24日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info25 = models.IntegerField(
        verbose_name = "算定日情報_25日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info26 = models.IntegerField(
        verbose_name = "算定日情報_26日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info27 = models.IntegerField(
        verbose_name = "算定日情報_27日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info28 = models.IntegerField(
        verbose_name = "算定日情報_28日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info29 = models.IntegerField(
        verbose_name = "算定日情報_29日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info30 = models.IntegerField(
        verbose_name = "算定日情報_30日の情報",
        blank = True,
        null = True,
        default = None
    )
    calculation_day_info31 = models.IntegerField(
        verbose_name = "算定日情報_31日の情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_special_equipment"
        verbose_name_plural = "R:特定器材レコード"

class RecordComment(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_identification = models.IntegerField(
        verbose_name = "診療識別",
        blank = True,
        null = True,
        default = None
    )
    payer_type = models.CharField(
        verbose_name = "負担区分",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    comment_code = models.IntegerField(
        verbose_name = "コメントコード",
        blank = True,
        null = True,
        default = None
    )
    character_data = models.CharField(
        verbose_name = "文字データ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    dentation_comment = models.CharField(
        verbose_name = "歯式(コメント)",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve1 = models.CharField(
        verbose_name = "予備_1",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve2 = models.CharField(
        verbose_name = "予備_2",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve3 = models.CharField(
        verbose_name = "予備_3",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    reserve4 = models.IntegerField(
        verbose_name = "予備_4",
        blank = True,
        null = True,
        default = None
    )
    reserve5 = models.IntegerField(
        verbose_name = "予備_5",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_comment"
        verbose_name_plural = "R:コメントレコード"

class RecordDetailSymptoms(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    detail_symptoms_type = models.IntegerField(
        verbose_name = "症状詳記区分",
        blank = True,
        null = True,
        default = None
    )
    detail_symptoms_data = models.CharField(
        verbose_name = "症状詳記データ",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    name = models.CharField(
        verbose_name = "氏名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_detail_symptoms"
        verbose_name_plural = "R:症状詳記レコード"

class RecordMedicalFeeClaim(models.Model):
    record_identification_info = models.CharField(
        verbose_name = "レコード識別情報",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    total_cases = models.IntegerField(
        verbose_name = "総件数",
        blank = True,
        null = True,
        default = None
    )
    total_score = models.IntegerField(
        verbose_name = "総合計点数",
        blank = True,
        null = True,
        default = None
    )
    multivolume_identification_info = models.IntegerField(
        verbose_name = "マルチボリューム識別情報",
        blank = True,
        null = True,
        default = None
    )
    practice_day = models.IntegerField(
        verbose_name = "診療年月",
        blank = True,
        null = True,
        default = None
    )
    row_number = models.IntegerField(
        verbose_name = "列番号",
        blank = True,
        null = True,
        default = None
    )
    examination_pay_institution = models.IntegerField(
        verbose_name = "審査支払機関",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "record_medical_fee_claim"
        verbose_name_plural = "R:診療報酬請求レコード"

class PracticeRecord(models.Model):
    name = models.CharField(
        verbose_name = "名前",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    date = models.DateField(
        verbose_name = "診療年月日",
        blank = True,
        null = True,
        default = None
    )
    practice_type = models.IntegerField(
        verbose_name = "治療／予防",
        blank = True,
        null = True,
        default = None
    )
    score = models.IntegerField(
        verbose_name = "点数",
        blank = True,
        null = True,
        default = None
    )
    responsible_dr = models.CharField(
        verbose_name = "歯科医師",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    responsible_dhda = models.CharField(
        verbose_name = "衛生士・助手",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_initial_medical_examination = models.CharField(
        verbose_name = "歯科診療行為_初診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_second_medical_examination = models.CharField(
        verbose_name = "歯科診療行為_再診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_management_rehab = models.CharField(
        verbose_name = "歯科診療行為_管理・リハ",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_medication_injection = models.CharField(
        verbose_name = "歯科診療行為_投薬・注射",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_xray_examination = models.CharField(
        verbose_name = "歯科診療行為_X線検査",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries1 = models.CharField(
        verbose_name = "歯科診療行為_処置・手術1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries2 = models.CharField(
        verbose_name = "歯科診療行為_処置・手術2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries3 = models.CharField(
        verbose_name = "歯科診療行為_処置・手術3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries_other = models.CharField(
        verbose_name = "歯科診療行為_処置・手術（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_anesthesia = models.CharField(
        verbose_name = "歯科診療行為_麻酔",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics1 = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics2 = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics3 = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics_other = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_other = models.CharField(
        verbose_name = "歯科診療行為_全体のその他",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_summary = models.CharField(
        verbose_name = "歯科診療行為_摘要",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_initial_medical_examination = models.CharField(
        verbose_name = "医薬品_初診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_second_medical_examination = models.CharField(
        verbose_name = "医薬品_再診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_management_rehab = models.CharField(
        verbose_name = "医薬品_管理・リハ",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_medication_injection = models.CharField(
        verbose_name = "医薬品_投薬・注射",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_xray_examination = models.CharField(
        verbose_name = "医薬品_X線検査",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_procedures_surgeries1 = models.CharField(
        verbose_name = "医薬品_処置・手術1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_procedures_surgeries2 = models.CharField(
        verbose_name = "医薬品_処置・手術2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_procedures_surgeries3 = models.CharField(
        verbose_name = "医薬品_処置・手術3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_procedures_surgeries_other = models.CharField(
        verbose_name = "医薬品_処置・手術（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_anesthesia = models.CharField(
        verbose_name = "医薬品_麻酔",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_restoration_prosthetics1 = models.CharField(
        verbose_name = "医薬品_修復・補綴1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_restoration_prosthetics2 = models.CharField(
        verbose_name = "医薬品_修復・補綴2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_restoration_prosthetics3 = models.CharField(
        verbose_name = "医薬品_修復・補綴3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_restoration_prosthetics_other = models.CharField(
        verbose_name = "医薬品_修復・補綴（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_other = models.CharField(
        verbose_name = "医薬品_全体のその他",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    drug_summary = models.CharField(
        verbose_name = "医薬品_摘要",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_initial_medical_examination = models.CharField(
        verbose_name = "特定機材_初診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_second_medical_examination = models.CharField(
        verbose_name = "特定機材_再診",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_management_rehab = models.CharField(
        verbose_name = "特定機材_管理・リハ",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_medication_injection = models.CharField(
        verbose_name = "特定機材_投薬・注射",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_xray_examination = models.CharField(
        verbose_name = "特定機材_X線検査",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_procedures_surgeries1 = models.CharField(
        verbose_name = "特定機材_処置・手術1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_procedures_surgeries2 = models.CharField(
        verbose_name = "特定機材_処置・手術2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_procedures_surgeries3 = models.CharField(
        verbose_name = "特定機材_処置・手術3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_procedures_surgeries_other = models.CharField(
        verbose_name = "特定機材_処置・手術（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_anesthesia = models.CharField(
        verbose_name = "特定機材_麻酔",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_restoration_prosthetics1 = models.CharField(
        verbose_name = "特定機材_修復・補綴1",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_restoration_prosthetics2 = models.CharField(
        verbose_name = "特定機材_修復・補綴2",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_restoration_prosthetics3 = models.CharField(
        verbose_name = "特定機材_修復・補綴3",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_restoration_prosthetics_other = models.CharField(
        verbose_name = "特定機材_修復・補綴（その他）",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_other = models.CharField(
        verbose_name = "特定機材_全体のその他",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    specific_equipment_summary = models.CharField(
        verbose_name = "特定機材_摘要",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_initial_medical_examination_add = models.CharField(
        verbose_name = "歯科診療行為_初診_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_second_medical_examination_add = models.CharField(
        verbose_name = "歯科診療行為_再診_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_management_rehab_add = models.CharField(
        verbose_name = "歯科診療行為_管理・リハ_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_medication_injection_add = models.CharField(
        verbose_name = "歯科診療行為_投薬・注射_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_xray_examination_add = models.CharField(
        verbose_name = "歯科診療行為_X線検査_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries1_add = models.CharField(
        verbose_name = "歯科診療行為_処置・手術1_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries2_add = models.CharField(
        verbose_name = "歯科診療行為_処置・手術2_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries3_add = models.CharField(
        verbose_name = "歯科診療行為_処置・手術3_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_procedures_surgeries_other_add = models.CharField(
        verbose_name = "歯科診療行為_処置・手術（その他）_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_anesthesia_add = models.CharField(
        verbose_name = "歯科診療行為_麻酔_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics1_add = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴1_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics2_add = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴2_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics3_add = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴3_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_restoration_prosthetics_other_add = models.CharField(
        verbose_name = "歯科診療行為_修復・補綴（その他）_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_other_add = models.CharField(
        verbose_name = "歯科診療行為_全体のその他_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    dental_practice_summary_add = models.CharField(
        verbose_name = "歯科診療行為_摘要_加算",
        blank = True,
        max_length = 255,
        null = True,
        default = None
    )
    class Meta:
        db_table = "practice_record"
        verbose_name_plural = "診療情報"

class PreventDentalPractice(models.Model):
    dental_practice_code = models.IntegerField(
        verbose_name = "歯科診療行為コード",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "prevent_dental_practice"
        verbose_name_plural = "予防診療行為コード"

class CancelList(models.Model):
    calte_num = models.CharField(
        verbose_name = "カルテ番号",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    name = models.CharField(
        verbose_name = "患者名",
        blank = True,
        max_length = 255,
        null = True,
        default = ""
    )
    booking_num = models.IntegerField(
        verbose_name = "予約件数",
        blank = True,
        null = True,
        default = None
    )
    cancel_num = models.IntegerField(
        verbose_name = "キャンセル件数",
        blank = True,
        null = True,
        default = None
    )
    without_permission = models.IntegerField(
        verbose_name = "無断",
        blank = True,
        null = True,
        default = None
    )
    appointed_day = models.IntegerField(
        verbose_name = "当日",
        blank = True,
        null = True,
        default = None
    )
    common = models.IntegerField(
        verbose_name = "通常",
        blank = True,
        null = True,
        default = None
    )    
    cancel_per = models.IntegerField(
        verbose_name = "キャンセル率",
        blank = True,
        null = True,
        default = None
    )
    class Meta:
        db_table = "cancel_per"
        verbose_name_plural = "予約表"