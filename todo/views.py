from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
from io import TextIOWrapper
import datetime
from django.db.models import Sum, Avg
import pandas as pd
from django_pandas.io import read_frame
import copy
import collections

# Create your views here.
def index(request):
    return render(request, 'index.html')

def csvexport_summary(request):
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;  filename="summmary.csv"'
        writer = csv.writer(response)

        start = int(request.POST["start"])
        end = int(request.POST["end"])
        month_list = [
            202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
            202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
            202205,202206,202207,202208,202209,202210,202211,202212
        ]
        for month in month_list[month_list.index(start):month_list.index(end)+1]:
            # 診療識別単位の合計
            list_20 = [
                    [11,12,13,21,31,41,42,43,44,54,61,62,63,64,80,99],
                    ["初診","再診","管理・リハ","投薬・注射","X線検査","処置・手術1","処置・手術2","処置・手術3","処置・手術（その他）","麻酔","修復・補綴1","修復・補綴2","修復・補綴3","修復・補綴（その他）","全体のその他","摘要"]
                ]
            writer.writerow([month,None,"合計",None,None,"社保",None,None,"国保"])
            writer.writerow(["診療識別","種別","回数","点数","平均点数","回数","点数","平均点数","回数","点数","平均点数"])
            # 歯科診療行為
            for ii in range(len(list_20[0])):
                summary = RecordDentalPractice.objects.filter(practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_shaho = RecordDentalPractice.objects.filter(examination_pay_institution=1,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_kokuho = RecordDentalPractice.objects.filter(examination_pay_institution=2,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                writer.writerow(
                    [
                        list_20[1][ii],
                        "歯科診療行為",
                        summary["total_count"],
                        summary["total_price"],
                        summary["average_price"],
                        summary_shaho["total_count"],
                        summary_shaho["total_price"],
                        summary_shaho["average_price"],
                        summary_kokuho["total_count"],
                        summary_kokuho["total_price"],
                        summary_kokuho["average_price"],
                    ]
                    )
            # 医薬品
            for ii in range(len(list_20[0])):
                summary = RecordDrug.objects.filter(practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_shaho = RecordDrug.objects.filter(examination_pay_institution=1,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_kokuho = RecordDrug.objects.filter(examination_pay_institution=2,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                writer.writerow(
                    [
                        list_20[1][ii],
                        "医薬品",
                        summary["total_count"],
                        summary["total_price"],
                        summary["average_price"],
                        summary_shaho["total_count"],
                        summary_shaho["total_price"],
                        summary_shaho["average_price"],
                        summary_kokuho["total_count"],
                        summary_kokuho["total_price"],
                        summary_kokuho["average_price"],
                    ]
                    )
            # 特定機材
            for ii in range(len(list_20[0])):
                summary = RecordSpecialEquipment.objects.filter(practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_shaho = RecordSpecialEquipment.objects.filter(examination_pay_institution=1,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                summary_kokuho = RecordSpecialEquipment.objects.filter(examination_pay_institution=2,practice_identification=list_20[0][ii],practice_day=month).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
                writer.writerow(
                    [
                        list_20[1][ii],
                        "特定機材",
                        summary["total_count"],
                        summary["total_price"],
                        summary["average_price"],
                        summary_shaho["total_count"],
                        summary_shaho["total_price"],
                        summary_shaho["average_price"],
                        summary_kokuho["total_count"],
                        summary_kokuho["total_price"],
                        summary_kokuho["average_price"],
                    ]
                    )
            writer.writerow([''])
        return response
    else:
        return render(request,"index.html")

def csvexport_practice(request):
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;  filename="summmary.csv"'
        writer = csv.writer(response)

        start = int(request.POST["start"])
        end = int(request.POST["end"])
        writer.writerow([None,"合計",None,None,"社保",None,None,"国保"])
        writer.writerow(["歯科診療行為","回数","点数","平均点数","回数","点数","平均点数","回数","点数","平均点数"])
        
        # 歯科診療行為単位の合計
        master_data = TableBasic.objects.all()
        for data in master_data:
            summary = RecordDentalPractice.objects.filter(practice_code=data.dental_practice_code,practice_day__range=(start,end)).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
            summary_shaho = RecordDentalPractice.objects.filter(examination_pay_institution=1,practice_code=data.dental_practice_code,practice_day__range=(start,end)).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
            summary_kokuho = RecordDentalPractice.objects.filter(examination_pay_institution=2,practice_code=data.dental_practice_code,practice_day__range=(start,end)).aggregate(total_count=Sum("count"),total_price=Sum("score"),average_price=Avg("score"))
            writer.writerow(
                [
                    data.practice_bassic_name,
                    summary["total_count"],
                    summary["total_price"],
                    summary["average_price"],
                    summary_shaho["total_count"],
                    summary_shaho["total_price"],
                    summary_shaho["average_price"],
                    summary_kokuho["total_count"],
                    summary_kokuho["total_price"],
                    summary_kokuho["average_price"],
                ]
                )
        writer.writerow([None])
        return response
    else:
        return render(request,"index.html")

def csvexport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="somefilename.csv"'

    writer = csv.writer(response)
    colomn_name = ["氏名","診療識別コード","診療識別","負担区分","診療行為コード","診療行為","回数","診療年月"]
    writer.writerow(colomn_name)

    for data in RecordDentalPractice.objects.all():
        day_check = []
        day_check.append(data.calculation_day_info1)
        day_check.append(data.calculation_day_info2)
        day_check.append(data.calculation_day_info3)
        day_check.append(data.calculation_day_info4)
        day_check.append(data.calculation_day_info5)
        day_check.append(data.calculation_day_info6)
        day_check.append(data.calculation_day_info7)
        day_check.append(data.calculation_day_info8)
        day_check.append(data.calculation_day_info9)
        day_check.append(data.calculation_day_info10)
        day_check.append(data.calculation_day_info11)
        day_check.append(data.calculation_day_info12)
        day_check.append(data.calculation_day_info13)
        day_check.append(data.calculation_day_info14)
        day_check.append(data.calculation_day_info15)
        day_check.append(data.calculation_day_info16)
        day_check.append(data.calculation_day_info17)
        day_check.append(data.calculation_day_info18)
        day_check.append(data.calculation_day_info19)
        day_check.append(data.calculation_day_info20)
        day_check.append(data.calculation_day_info21)
        day_check.append(data.calculation_day_info22)
        day_check.append(data.calculation_day_info23)
        day_check.append(data.calculation_day_info24)
        day_check.append(data.calculation_day_info25)
        day_check.append(data.calculation_day_info26)
        day_check.append(data.calculation_day_info27)
        day_check.append(data.calculation_day_info28)
        day_check.append(data.calculation_day_info29)
        day_check.append(data.calculation_day_info30)
        day_check.append(data.calculation_day_info31)

        
        list_20 = [
            [11,12,13,21,31,41,42,43,44,54,61,62,63,64,80,99],
            ["初診","再診","管理・リハ","投薬・注射","X線検査","処置・手術1","処置・手術2","処置・手術3","処置・手術（その他）","麻酔","修復・補綴1","修復・補綴2","修復・補綴3","修復・補綴（その他）","全体のその他","摘要"]
        ]
        practice_identification_trans = list_20[1][list_20[0].index(data.practice_identification)]
        practice_code = TableBasic.objects.get(dental_practice_code=data.practice_code).practice_bassic_name
        for i,count in enumerate(day_check):
            row = [
                data.name,
                data.practice_identification,
                practice_identification_trans,
                data.payer_type,
                data.practice_code,
                practice_code
            ]
            if count != None:
                date = str(data.practice_day)
                row.append(count)
                row.append(datetime.date(int(date[:4]),int(date[4:6]),i+1))
                writer.writerow(row)
    return response

def upload(request):
    if 'csv' in request.FILES:
        # RecordReceiptInfo.objects.all().delete()
        # RecordMedicalInstitutionInfo.objects.all().delete()
        # RecordReceiptCommon.objects.all().delete()
        # RecordInsurer.objects.all().delete()
        # RecordPublicExpense.objects.all().delete()
        # RecordStatusCheck.objects.all().delete()
        # RecordReceiptDay.objects.all().delete()
        # RecordCounterAmount.objects.all().delete()
        # RecordDiseasePosition.objects.all().delete()
        # RecordDentalPractice.objects.all().delete()
        # RecordPractice.objects.all().delete()
        # RecordDrug.objects.all().delete()
        # RecordSpecialEquipment.objects.all().delete()
        # RecordComment.objects.all().delete()
        # RecordDetailSymptoms.objects.all().delete()
        # RecordMedicalFeeClaim.objects.all().delete()

        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        data_row = csv.reader(form_data)

        practice_identification_before = None

        count = 0

        for row, data_unit in enumerate(data_row):
            for ii in range(len(data_unit)):
                if data_unit[ii] == "":
                    data_unit[ii] = None
                
            if data_unit[0] == 'UK':
                saved_uk = data_unit

            if data_unit[0] == 'IR':
                # レコードのカラム数とリストの要素数を一致させる,足りない要素数分nullを追加
                saved_ir = data_unit

            if data_unit[0] == 'RE':
                count += 1
                # REレコードに記載された氏名と請求年月を取得
                date = data_unit[3]                
                name = data_unit[4]

                if count == 1:
                    # 医療機関名称、請求年月が同じな場合レコードを追加しない
                    uk, created = RecordReceiptInfo.objects.get_or_create(row_number=0,billing_day=date,examination_pay_institution=saved_uk[1])
                    examination_pay_institution=saved_uk[1]
                    # データベースに追加(pythonコードで自動出力化)
                    try:
                        uk.record_identification_info = saved_uk[0]
                        uk.examination_pay_institution = saved_uk[1]
                        uk.prefectures = saved_uk[2]
                        uk.score_sheet = saved_uk[3]
                        uk.medical_institution_code = saved_uk[4]
                        uk.reserve = saved_uk[5]
                        uk.medical_institution_name = saved_uk[6]
                        uk.billing_day = date
                        uk.notification = saved_uk[8]
                        uk.multivolume_identifier_info = saved_uk[9]
                        uk.row_name = 0
                        uk.save()
                    except:
                        pass
                    uk.save()

                # IRレコードの追加
                # 医療機関コードと請求年月と氏名が一致するレコードがない場合追加
                ir, created = RecordMedicalInstitutionInfo.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    ir.record_identification_info = saved_ir[0]
                    ir.examination_pay_institution = saved_ir[1]
                    ir.prefectures = saved_ir[2]
                    ir.score_sheet = saved_ir[3]
                    ir.medical_institution_code = saved_ir[4]
                    ir.reserve = saved_ir[5]
                    ir.billing_day = saved_ir[6]
                    ir.phone_number = saved_ir[7]
                    ir.notification = saved_ir[8]
                    ir.name = name
                    ir.practice_day= date
                    ir.row_name = row
                    ir.examination_pay_institution = examination_pay_institution
                except:
                    pass
                ir.save()
    
                # REレコードの追加
                # 氏名と診療年月が一致するレコードがない場合追加
                re, created = RecordReceiptCommon.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    re.record_identification_info = data_unit[0]
                    re.receipt_number = data_unit[1]
                    re.receipt_identification = data_unit[2]
                    re.practice_day = data_unit[3]
                    re.name = data_unit[4]
                    re.sex_type = data_unit[5]
                    re.birth_day = data_unit[6]
                    re.benefit_ratio = data_unit[7]
                    re.admission_day = data_unit[8]
                    re.practice_start_day = data_unit[9]
                    re.return_origin_yupe = data_unit[10]
                    re.hospital_ward_type = data_unit[11]
                    re.copayment = data_unit[12]
                    re.receipt_special_remarks = data_unit[13]
                    re.reserve1 = data_unit[14]
                    re.chart_number = data_unit[15]
                    re.billing_info1 = data_unit[16]
                    re.reserve2 = data_unit[17]
                    re.future_hospital_billing = data_unit[18]
                    re.search_number = data_unit[19]
                    re.reserve3 = data_unit[20]
                    re.billing_info2 = data_unit[21]
                    re.reserve4 = data_unit[22]
                    re.reserve5 = data_unit[23]
                    re.reserve6 = data_unit[24]
                    re.cana_name = data_unit[25]
                    re.patient_condition = data_unit[26]
                    re.name = name
                    re.practice_day= date
                    re.row_name = row
                    re.examination_pay_institution = examination_pay_institution
                except:
                    pass
                re.save()

            if data_unit[0] == 'HO':
                # HOレコードの追加
                # 保険者番号と診療年月が一致するレコードがない場合追加
                ho, created = RecordInsurer.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    ho.record_identification_info = data_unit[0]
                    ho.insurer_number = data_unit[1]
                    ho.insurer_card_code = data_unit[2]
                    ho.insurer_card_number = data_unit[3]
                    ho.practice_acrual_days = data_unit[4]
                    ho.total_score = data_unit[5]
                    ho.dietary_lifestyle_care_times = data_unit[6]
                    ho.dietary_lifestyle_care_total_amount = data_unit[7]
                    ho.professional_reasons = data_unit[8]
                    ho.certificate_number = data_unit[9]
                    ho.insurance_copayments = data_unit[10]
                    ho.exempt_type = data_unit[11]
                    ho.reduction_ratio = data_unit[12]
                    ho.reduction_amount = data_unit[13]
                    ho.name = name
                    ho.practice_day= date
                    ho.row_name = row
                    ho.examination_pay_institution = examination_pay_institution
                except:
                    pass
                ho.save()
            
            if data_unit[0] == 'KO':
                # KOレコードの追加
                # 氏名と診療年月が一致するレコードがない場合追加
                ko, created = RecordPublicExpense.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    ko.record_identification_info = data_unit[0]
                    ko.payer_number = data_unit[1]
                    ko.recipient_number = data_unit[2]
                    ko.optional_benefit_type = data_unit[3]
                    ko.practice_acrual_days = data_unit[4]
                    ko.total_score = data_unit[5]
                    ko.copayment = data_unit[6]
                    ko.public_expense_benefit_copayment = data_unit[7]
                    ko.dietary_lifestyle_care_times = data_unit[8]
                    ko.dietary_lifestyle_care_total_amount = data_unit[9]
                    ko.name = name
                    ko.practice_day= date
                    ko.row_name = row
                    ko.examination_pay_institution = examination_pay_institution
                except:
                    pass
                ko.save()

            if data_unit[0] == 'SN':
                # SNレコードの追加
                # 氏名と診療年月が一致するレコードがない場合追加
                sn, created = RecordStatusCheck.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    sn.record_identification_info = data_unit[0]
                    sn.payer_class = data_unit[1]
                    sn.confirmation_type = data_unit[2]
                    sn.insurer_number_etc = data_unit[3]
                    sn.insurer_card_code_status_check = data_unit[4]
                    sn.insurer_card_number_status_check = data_unit[5]
                    sn.branch_number = data_unit[6]
                    sn.recipient_id = data_unit[7]
                    sn.reserve = data_unit[8]
                    sn.name = name
                    sn.practice_day= date
                    sn.row_name = row
                    sn.examination_pay_institution = examination_pay_institution
                except:
                    pass
                sn.save()

            if data_unit[0] == 'JD':
                # JDレコードの追加
                # 氏名と診療年月と負担者種別が一致するレコードがない場合追加
                jd, created = RecordReceiptDay.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    jd.record_identification_info = data_unit[0]
                    jd.payer_type = data_unit[1]
                    jd.info1 = data_unit[2]
                    jd.info2 = data_unit[3]
                    jd.info3 = data_unit[4]
                    jd.info4 = data_unit[5]
                    jd.info5 = data_unit[6]
                    jd.info6 = data_unit[7]
                    jd.info7 = data_unit[8]
                    jd.info8 = data_unit[9]
                    jd.info9 = data_unit[10]
                    jd.info10 = data_unit[11]
                    jd.info11 = data_unit[12]
                    jd.info12 = data_unit[13]
                    jd.info13 = data_unit[14]
                    jd.info14 = data_unit[15]
                    jd.info15 = data_unit[16]
                    jd.info16 = data_unit[17]
                    jd.info17 = data_unit[18]
                    jd.info18 = data_unit[19]
                    jd.info19 = data_unit[20]
                    jd.info20 = data_unit[21]
                    jd.info21 = data_unit[22]
                    jd.info22 = data_unit[23]
                    jd.info23 = data_unit[24]
                    jd.info24 = data_unit[25]
                    jd.info25 = data_unit[26]
                    jd.info26 = data_unit[27]
                    jd.info27 = data_unit[28]
                    jd.info28 = data_unit[29]
                    jd.info29 = data_unit[30]
                    jd.info30 = data_unit[31]
                    jd.info31 = data_unit[32]
                    jd.name = name
                    jd.practice_day= date
                    jd.row_name = row
                    jd.examination_pay_institution = examination_pay_institution
                except:
                    pass
                jd.save()

            if data_unit[0] == 'MF':
                # MFレコードの追加
                # 氏名と診療年月と窓口負担額区分が一致するレコードがない場合追加
                mf, created = RecordCounterAmount.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    mf.record_identification_info = data_unit[0]
                    mf.counter_amount_type = data_unit[1]
                    mf.reserve1 = data_unit[2]
                    mf.reserve2 = data_unit[3]
                    mf.reserve3 = data_unit[4]
                    mf.reserve4 = data_unit[5]
                    mf.reserve5 = data_unit[6]
                    mf.reserve6 = data_unit[7]
                    mf.reserve7 = data_unit[8]
                    mf.reserve8 = data_unit[9]
                    mf.reserve9 = data_unit[10]
                    mf.reserve10 = data_unit[11]
                    mf.reserve11 = data_unit[12]
                    mf.reserve12 = data_unit[13]
                    mf.reserve13 = data_unit[14]
                    mf.reserve14 = data_unit[15]
                    mf.reserve15 = data_unit[16]
                    mf.reserve16 = data_unit[17]
                    mf.reserve17 = data_unit[18]
                    mf.reserve18 = data_unit[19]
                    mf.reserve19 = data_unit[20]
                    mf.reserve20 = data_unit[21]
                    mf.reserve21 = data_unit[22]
                    mf.reserve22 = data_unit[23]
                    mf.reserve23 = data_unit[24]
                    mf.reserve24 = data_unit[25]
                    mf.reserve25 = data_unit[26]
                    mf.reserve26 = data_unit[27]
                    mf.reserve27 = data_unit[28]
                    mf.reserve28 = data_unit[29]
                    mf.reserve29 = data_unit[30]
                    mf.reserve30 = data_unit[31]
                    mf.reserve31 = data_unit[32]
                    mf.name = name
                    mf.practice_day= date
                    mf.row_name = row
                    mf.examination_pay_institution = examination_pay_institution
                except:
                    pass
                mf.save()
            
            if data_unit[0] == 'HS':
                # HSレコードの追加
                # 氏名と診療年月と歯式コードと傷病名コードと修飾語コードが一致するレコードがない場合追加
                hs, created = RecordDiseasePosition.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    hs.record_identification_info = data_unit[0]
                    hs.start_practice = data_unit[1]
                    hs.transcription_type = data_unit[2]
                    hs.dentation_code_diseaase = data_unit[3]
                    hs.disease_name_code = data_unit[4]
                    hs.modifier_code = data_unit[5]
                    hs.disease_name = data_unit[6]
                    hs.comorbidities_number = data_unit[7]
                    hs.disease_condition_transition = data_unit[8]
                    hs.major_disease = data_unit[9]
                    hs.comment_code = data_unit[10]
                    hs.supplementary_comment = data_unit[11]
                    hs.dentation_code_comment = data_unit[12]
                    hs.name = name
                    hs.practice_day= date
                    hs.row_name = row
                    hs.examination_pay_institution = examination_pay_institution
                except:
                    pass
                hs.save()
            
            if data_unit[0] == 'SS':
                # SSレコードの追加
                # 氏名と診療年月とと診療識別と負担区分と診療行為コードが一致するレコードがない場合追加
                ss, created = RecordDentalPractice.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # 診療識別が空欄の場合、直前のレコードの診療識別を追加
                if data_unit[1] == None:
                    data_unit[1] = practice_identification_before
                # データベースに追加                
                try:
                    ss.record_identification_info = data_unit[0]
                    ss.practice_identification = data_unit[1]
                    ss.payer_type = data_unit[2]
                    ss.practice_code = data_unit[3]
                    ss.practice_volume_data1 = data_unit[4]
                    ss.practice_volume_data2 = data_unit[5]
                    ss.add_code1 = data_unit[6]
                    ss.add_volume_data1 = data_unit[7]
                    ss.add_code2 = data_unit[8]
                    ss.add_volume_data2 = data_unit[9]
                    ss.add_code3 = data_unit[10]
                    ss.add_volume_data3 = data_unit[11]
                    ss.add_code4 = data_unit[12]
                    ss.add_volume_data4 = data_unit[13]
                    ss.add_code5 = data_unit[14]
                    ss.add_volume_data5 = data_unit[15]
                    ss.add_code6 = data_unit[16]
                    ss.add_volume_data6 = data_unit[17]
                    ss.add_code7 = data_unit[18]
                    ss.add_volume_data7 = data_unit[19]
                    ss.add_code8 = data_unit[20]
                    ss.add_volume_data8 = data_unit[21]
                    ss.add_code9 = data_unit[22]
                    ss.add_volume_data9 = data_unit[23]
                    ss.add_code10 = data_unit[24]
                    ss.add_volume_data10 = data_unit[25]
                    ss.add_code11 = data_unit[26]
                    ss.add_volume_data11 = data_unit[27]
                    ss.add_code12 = data_unit[28]
                    ss.add_volume_data12 = data_unit[29]
                    ss.add_code13 = data_unit[30]
                    ss.add_volume_data13 = data_unit[31]
                    ss.add_code14 = data_unit[32]
                    ss.add_volume_data14 = data_unit[33]
                    ss.add_code15 = data_unit[34]
                    ss.add_volume_data15 = data_unit[35]
                    ss.add_code16 = data_unit[36]
                    ss.add_volume_data16 = data_unit[37]
                    ss.add_code17 = data_unit[38]
                    ss.add_volume_data17 = data_unit[39]
                    ss.add_code18 = data_unit[40]
                    ss.add_volume_data18 = data_unit[41]
                    ss.add_code19 = data_unit[42]
                    ss.add_volume_data19 = data_unit[43]
                    ss.add_code20 = data_unit[44]
                    ss.add_volume_data20 = data_unit[45]
                    ss.add_code21 = data_unit[46]
                    ss.add_volume_data21 = data_unit[47]
                    ss.add_code22 = data_unit[48]
                    ss.add_volume_data22 = data_unit[49]
                    ss.add_code23 = data_unit[50]
                    ss.add_volume_data23 = data_unit[51]
                    ss.add_code24 = data_unit[52]
                    ss.add_volume_data24 = data_unit[53]
                    ss.add_code25 = data_unit[54]
                    ss.add_volume_data25 = data_unit[55]
                    ss.add_code26 = data_unit[56]
                    ss.add_volume_data26 = data_unit[57]
                    ss.add_code27 = data_unit[58]
                    ss.add_volume_data27 = data_unit[59]
                    ss.add_code28 = data_unit[60]
                    ss.add_volume_data28 = data_unit[61]
                    ss.add_code29 = data_unit[62]
                    ss.add_volume_data29 = data_unit[63]
                    ss.add_code30 = data_unit[64]
                    ss.add_volume_data30 = data_unit[65]
                    ss.add_code31 = data_unit[66]
                    ss.add_volume_data31 = data_unit[67]
                    ss.add_code32 = data_unit[68]
                    ss.add_volume_data32 = data_unit[69]
                    ss.add_code33 = data_unit[70]
                    ss.add_volume_data33 = data_unit[71]
                    ss.add_code34 = data_unit[72]
                    ss.add_volume_data34 = data_unit[73]
                    ss.add_code35 = data_unit[74]
                    ss.add_volume_data35 = data_unit[75]
                    ss.score = data_unit[76]
                    ss.count = data_unit[77]
                    ss.calculation_day_info1 = data_unit[78]
                    ss.calculation_day_info2 = data_unit[79]
                    ss.calculation_day_info3 = data_unit[80]
                    ss.calculation_day_info4 = data_unit[81]
                    ss.calculation_day_info5 = data_unit[82]
                    ss.calculation_day_info6 = data_unit[83]
                    ss.calculation_day_info7 = data_unit[84]
                    ss.calculation_day_info8 = data_unit[85]
                    ss.calculation_day_info9 = data_unit[86]
                    ss.calculation_day_info10 = data_unit[87]
                    ss.calculation_day_info11 = data_unit[88]
                    ss.calculation_day_info12 = data_unit[89]
                    ss.calculation_day_info13 = data_unit[90]
                    ss.calculation_day_info14 = data_unit[91]
                    ss.calculation_day_info15 = data_unit[92]
                    ss.calculation_day_info16 = data_unit[93]
                    ss.calculation_day_info17 = data_unit[94]
                    ss.calculation_day_info18 = data_unit[95]
                    ss.calculation_day_info19 = data_unit[96]
                    ss.calculation_day_info20 = data_unit[97]
                    ss.calculation_day_info21 = data_unit[98]
                    ss.calculation_day_info22 = data_unit[99]
                    ss.calculation_day_info23 = data_unit[100]
                    ss.calculation_day_info24 = data_unit[101]
                    ss.calculation_day_info25 = data_unit[102]
                    ss.calculation_day_info26 = data_unit[103]
                    ss.calculation_day_info27 = data_unit[104]
                    ss.calculation_day_info28 = data_unit[105]
                    ss.calculation_day_info29 = data_unit[106]
                    ss.calculation_day_info30 = data_unit[107]
                    ss.calculation_day_info31 = data_unit[108]
                    ss.name = name
                    ss.practice_day= date
                    ss.row_name = row
                    ss.examination_pay_institution = examination_pay_institution
                except:
                    pass
                ss.save()
                practice_identification_before = data_unit[1]

            if data_unit[0] == 'SI':
                # SIレコードの追加
                # 氏名と診療年月と診療行為コードが一致するレコードがない場合追加
                si, created = RecordPractice.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # 診療識別が空欄の場合、直前のレコードの診療識別を追加
                if data_unit[1] == None:
                    data_unit[1] = practice_identification_before
                # データベースに追加
                try:
                    si.record_identification_info = data_unit[0]
                    si.practice_identification = data_unit[1]
                    si.payer_type = data_unit[2]
                    si.practice_code = data_unit[3]
                    si.volume_data = data_unit[4]
                    si.score = data_unit[5]
                    si.count = data_unit[6]
                    si.calculation_day_info1 = data_unit[7]
                    si.calculation_day_info2 = data_unit[8]
                    si.calculation_day_info3 = data_unit[9]
                    si.calculation_day_info4 = data_unit[10]
                    si.calculation_day_info5 = data_unit[11]
                    si.calculation_day_info6 = data_unit[12]
                    si.calculation_day_info7 = data_unit[13]
                    si.calculation_day_info8 = data_unit[14]
                    si.calculation_day_info9 = data_unit[15]
                    si.calculation_day_info10 = data_unit[16]
                    si.calculation_day_info11 = data_unit[17]
                    si.calculation_day_info12 = data_unit[18]
                    si.calculation_day_info13 = data_unit[19]
                    si.calculation_day_info14 = data_unit[20]
                    si.calculation_day_info15 = data_unit[21]
                    si.calculation_day_info16 = data_unit[22]
                    si.calculation_day_info17 = data_unit[23]
                    si.calculation_day_info18 = data_unit[24]
                    si.calculation_day_info19 = data_unit[25]
                    si.calculation_day_info20 = data_unit[26]
                    si.calculation_day_info21 = data_unit[27]
                    si.calculation_day_info22 = data_unit[28]
                    si.calculation_day_info23 = data_unit[29]
                    si.calculation_day_info24 = data_unit[30]
                    si.calculation_day_info25 = data_unit[31]
                    si.calculation_day_info26 = data_unit[32]
                    si.calculation_day_info27 = data_unit[33]
                    si.calculation_day_info28 = data_unit[34]
                    si.calculation_day_info29 = data_unit[35]
                    si.calculation_day_info30 = data_unit[36]
                    si.calculation_day_info31 = data_unit[37]
                    si.name = name
                    si.practice_day= date
                    si.row_name = row
                    si.examination_pay_institution = examination_pay_institution
                except:
                    pass
                practice_identification_before = data_unit[1]
                si.save()

            if data_unit[0] == 'IY':
                # IYレコードの追加
                # 氏名と診療年月と医薬品コードが一致するレコードがない場合追加
                iy, created = RecordDrug.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # 診療識別が空欄の場合、直前のレコードの診療識別を追加
                if data_unit[1] == None:
                    data_unit[1] = practice_identification_before
                # データベースに追加
                try:
                    iy.record_identification_info = data_unit[0]
                    iy.practice_identification = data_unit[1]
                    iy.payer_type = data_unit[2]
                    iy.drug_code = data_unit[3]
                    iy.usage = data_unit[4]
                    iy.score = data_unit[5]
                    iy.count = data_unit[6]
                    iy.drug_type = data_unit[7]
                    iy.calculation_day_info1 = data_unit[8]
                    iy.calculation_day_info2 = data_unit[9]
                    iy.calculation_day_info3 = data_unit[10]
                    iy.calculation_day_info4 = data_unit[11]
                    iy.calculation_day_info5 = data_unit[12]
                    iy.calculation_day_info6 = data_unit[13]
                    iy.calculation_day_info7 = data_unit[14]
                    iy.calculation_day_info8 = data_unit[15]
                    iy.calculation_day_info9 = data_unit[16]
                    iy.calculation_day_info10 = data_unit[17]
                    iy.calculation_day_info11 = data_unit[18]
                    iy.calculation_day_info12 = data_unit[19]
                    iy.calculation_day_info13 = data_unit[20]
                    iy.calculation_day_info14 = data_unit[21]
                    iy.calculation_day_info15 = data_unit[22]
                    iy.calculation_day_info16 = data_unit[23]
                    iy.calculation_day_info17 = data_unit[24]
                    iy.calculation_day_info18 = data_unit[25]
                    iy.calculation_day_info19 = data_unit[26]
                    iy.calculation_day_info20 = data_unit[27]
                    iy.calculation_day_info21 = data_unit[28]
                    iy.calculation_day_info22 = data_unit[29]
                    iy.calculation_day_info23 = data_unit[30]
                    iy.calculation_day_info24 = data_unit[31]
                    iy.calculation_day_info25 = data_unit[32]
                    iy.calculation_day_info26 = data_unit[33]
                    iy.calculation_day_info27 = data_unit[34]
                    iy.calculation_day_info28 = data_unit[35]
                    iy.calculation_day_info29 = data_unit[36]
                    iy.calculation_day_info30 = data_unit[37]
                    iy.calculation_day_info31 = data_unit[38]
                    iy.name = name
                    iy.practice_day= date
                    iy.row_name = row
                    iy.examination_pay_institution = examination_pay_institution
                except:
                    pass
                practice_identification_before = data_unit[1]
                iy.save()

            if data_unit[0] == 'TO':
                # TOレコードの追加
                # 氏名と診療年月と特定機材コードが一致するレコードがない場合追加
                to, created = RecordSpecialEquipment.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # 診療識別が空欄の場合、直前のレコードの診療識別を追加
                if data_unit[1] == None:
                    data_unit[1] = practice_identification_before
                # データベースに追加
                try:
                    to.record_identification_info = data_unit[0]
                    to.practice_identification = data_unit[1]
                    to.payer_type = data_unit[2]
                    to.special_equipment_code = data_unit[3]
                    to.usage = data_unit[4]
                    to.unit_code = data_unit[5]
                    to.unit_cost = data_unit[6]
                    to.special_equipment_add_code1 = data_unit[7]
                    to.special_equipment_add_volume_data1 = data_unit[8]
                    to.special_equipment_add_code2 = data_unit[9]
                    to.special_equipment_add_volume_data2 = data_unit[10]
                    to.standard_or_size = data_unit[11]
                    to.score = data_unit[12]
                    to.count = data_unit[13]
                    to.calculation_day_info1 = data_unit[14]
                    to.calculation_day_info2 = data_unit[15]
                    to.calculation_day_info3 = data_unit[16]
                    to.calculation_day_info4 = data_unit[17]
                    to.calculation_day_info5 = data_unit[18]
                    to.calculation_day_info6 = data_unit[19]
                    to.calculation_day_info7 = data_unit[20]
                    to.calculation_day_info8 = data_unit[21]
                    to.calculation_day_info9 = data_unit[22]
                    to.calculation_day_info10 = data_unit[23]
                    to.calculation_day_info11 = data_unit[24]
                    to.calculation_day_info12 = data_unit[25]
                    to.calculation_day_info13 = data_unit[26]
                    to.calculation_day_info14 = data_unit[27]
                    to.calculation_day_info15 = data_unit[28]
                    to.calculation_day_info16 = data_unit[29]
                    to.calculation_day_info17 = data_unit[30]
                    to.calculation_day_info18 = data_unit[31]
                    to.calculation_day_info19 = data_unit[32]
                    to.calculation_day_info20 = data_unit[33]
                    to.calculation_day_info21 = data_unit[34]
                    to.calculation_day_info22 = data_unit[35]
                    to.calculation_day_info23 = data_unit[36]
                    to.calculation_day_info24 = data_unit[37]
                    to.calculation_day_info25 = data_unit[38]
                    to.calculation_day_info26 = data_unit[39]
                    to.calculation_day_info27 = data_unit[40]
                    to.calculation_day_info28 = data_unit[41]
                    to.calculation_day_info29 = data_unit[42]
                    to.calculation_day_info30 = data_unit[43]
                    to.calculation_day_info31 = data_unit[44]
                    to.name = name
                    to.practice_day= date
                    to.row_name = row
                    to.examination_pay_institution = examination_pay_institution
                except:
                    pass
                to.save()
                practice_identification_before = data_unit[1]

            if data_unit[0] == 'CO':
                # COレコードの追加
                # 氏名と診療年月とコメントコードが一致するレコードがない場合追加
                co, created = RecordComment.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # 診療識別が空欄の場合、直前のレコードの診療識別を追加
                if data_unit[1] == None:
                    data_unit[1] = practice_identification_before
                # データベースに追加
                try:
                    co.record_identification_info = data_unit[0]
                    co.practice_identification = data_unit[1]
                    co.payer_type = data_unit[2]
                    co.comment_code = data_unit[3]
                    co.character_data = data_unit[4]
                    co.dentation_comment = data_unit[5]
                    co.reserve1 = data_unit[6]
                    co.reserve2 = data_unit[7]
                    co.reserve3 = data_unit[8]
                    co.reserve4 = data_unit[9]
                    co.reserve5 = data_unit[10]
                    co.name = name
                    co.practice_day= date
                    co.row_name = row
                    co.examination_pay_institution = examination_pay_institution
                except:
                    pass
                co.save()
                practice_identification_before = data_unit[1]

            if data_unit[0] == 'SJ':
                # SJレコードの追加
                # 氏名と診療年月と症状詳記区分と症状詳記データが一致するレコードがない場合追加
                sj, created = RecordDetailSymptoms.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    sj.record_identification_info = data_unit[0]
                    sj.detail_symptoms_type = data_unit[1]
                    sj.detail_symptoms_data = data_unit[2]
                    sj.name = name
                    sj.practice_day= date
                    sj.row_name = row
                    sj.examination_pay_institution = examination_pay_institution
                except:
                    pass
                sj.save()
                
            if data_unit[0] == 'GO':
                # GOレコードの追加
                # 診療年月が一致するレコードがない場合追加
                go, created = RecordMedicalFeeClaim.objects.get_or_create(row_number=row,practice_day=date,examination_pay_institution=data_unit[1])
                # データベースに追加
                try:
                    go.record_identification_info = data_unit[0]
                    go.total_cases = data_unit[1]
                    go.total_score = data_unit[2]
                    go.multivolume_identification_info = data_unit[3]
                    go.practice_day= date
                    go.row_name = row
                    go.examination_pay_institution = examination_pay_institution
                except:
                    pass
                go.save()

        return render(request, 'index.html')

    else:
        return render(request, 'index.html')

def yobou(request):
    PreventDentalPractice.objects.all().delete()
    input_list = [
        309004810,
        304000910,
        309005710,
        305004310,
        304000410,
        309005210,
        309014810,
        309004710,
        308002610,
        303007410,
        309005110,
        309001410,
        302003010,
        304000710,
        304001610,
        308002510,
        309011410,
        309005010,
        302010710,
        309001310,
        304000610,
        302000610,
        305004010,
        302000110,
        304000510,
    ]

    records = []
    for data in input_list:
        records.append(PreventDentalPractice(dental_practice_code=data))
    PreventDentalPractice.objects.bulk_create(records)
    return render(request, 'index.html')

def transform_practice_data(request):
    PracticeRecord.objects.all().delete()

    practice_identification_code = [11,12,13,21,31,41,42,43,44,54,61,62,63,64,80,99]
    dental_practice = RecordDentalPractice.objects.all().values(
        "name",
        "practice_day",
        "practice_identification",
        "practice_code",
        "score",
        'add_code1',
        'add_code2',
        'add_code3',
        'add_code4',
        'add_code5',
        'add_code6',
        'add_code7',
        'add_code8',
        'add_code9',
        'add_code10',
        'add_code11',
        'add_code12',
        'add_code13',
        'add_code14',
        'add_code15',
        'add_code16',
        'add_code17',
        'add_code18',
        'add_code19',
        'add_code20',
        'add_code21',
        'add_code22',
        'add_code23',
        'add_code24',
        'add_code25',
        'add_code26',
        'add_code27',
        'add_code28',
        'add_code29',
        'add_code30',
        'add_code31',
        'add_code32',
        'add_code33',
        'add_code34',
        'add_code35',
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
        )
    drug = RecordDrug.objects.all().values(
        "name",
        "practice_day",
        "practice_identification",
        "drug_code",
        "score",
        "usage",
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
        )
    special_equipment = RecordSpecialEquipment.objects.all().values(
        "name",
        "practice_day",
        "practice_identification",
        "special_equipment_code",
        "score",
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
        )
    record_num = []

    for data in dental_practice:
        day_list = [
            data["calculation_day_info1"],
            data["calculation_day_info2"],
            data["calculation_day_info3"],
            data["calculation_day_info4"],
            data["calculation_day_info5"],
            data["calculation_day_info6"],
            data["calculation_day_info7"],
            data["calculation_day_info8"],
            data["calculation_day_info9"],
            data["calculation_day_info10"],
            data["calculation_day_info11"],
            data["calculation_day_info12"],
            data["calculation_day_info13"],
            data["calculation_day_info14"],
            data["calculation_day_info15"],
            data["calculation_day_info16"],
            data["calculation_day_info17"],
            data["calculation_day_info18"],
            data["calculation_day_info19"],
            data["calculation_day_info20"],
            data["calculation_day_info21"],
            data["calculation_day_info22"],
            data["calculation_day_info23"],
            data["calculation_day_info24"],
            data["calculation_day_info25"],
            data["calculation_day_info26"],
            data["calculation_day_info27"],
            data["calculation_day_info28"],
            data["calculation_day_info29"],
            data["calculation_day_info30"],
            data["calculation_day_info31"]
            ]
        for ii,day in enumerate(day_list):
            if day != None:
                content = f'{data["name"]},{str(data["practice_day"])[:4]}-{str(data["practice_day"])[4:6]}-{ii+1}'
                if content not in record_num:
                    record_num.append(content)
    
    print(len(record_num))
    create_list=[]

    prevent_dental_practice = PreventDentalPractice.objects.all().values("dental_practice_code")
    prevent_dental_practice_set = set([jj["dental_practice_code"] for jj in prevent_dental_practice])

    for data in record_num:
        name = data.split(",")[0]
        date = datetime.date(int(data.split(",")[1].split("-")[0]),int(data.split(",")[1].split("-")[1]),int(data.split(",")[1].split("-")[2]))
        practice_day = int(data.split(",")[1].split("-")[0])*100+int(data.split(",")[1].split("-")[1])
        day = int(data.split(",")[1].split("-")[2])
        
        record_dental_practice = eval(f'dental_practice.filter(name=name,practice_day=practice_day,calculation_day_info{day}__gt = 0)')
        record_drug = eval(f'drug.filter(name=name,practice_day=practice_day,calculation_day_info{day}__gt = 0)')
        record_special_equipment = eval(f'special_equipment.filter(name=name,practice_day=practice_day,calculation_day_info{day}__gt = 0)')

        dental_practice_initial_medical_examination = ""
        dental_practice_second_medical_examination = ""
        dental_practice_management_rehab = ""
        dental_practice_medication_injection = ""
        dental_practice_xray_examination = ""
        dental_practice_procedures_surgeries1 = ""
        dental_practice_procedures_surgeries2 = ""
        dental_practice_procedures_surgeries3 = ""
        dental_practice_procedures_surgeries_other = ""
        dental_practice_anesthesia = ""
        dental_practice_restoration_prosthetics1 = ""
        dental_practice_restoration_prosthetics2 = ""
        dental_practice_restoration_prosthetics3 = ""
        dental_practice_restoration_prosthetics_other = ""
        dental_practice_other = ""
        dental_practice_summary = ""
        drug_initial_medical_examination = ""
        drug_second_medical_examination = ""
        drug_management_rehab = ""
        drug_medication_injection = ""
        drug_xray_examination = ""
        drug_procedures_surgeries1 = ""
        drug_procedures_surgeries2 = ""
        drug_procedures_surgeries3 = ""
        drug_procedures_surgeries_other = ""
        drug_anesthesia = ""
        drug_restoration_prosthetics1 = ""
        drug_restoration_prosthetics2 = ""
        drug_restoration_prosthetics3 = ""
        drug_restoration_prosthetics_other = ""
        drug_other = ""
        drug_summary = ""
        specific_equipment_initial_medical_examination = ""
        specific_equipment_second_medical_examination = ""
        specific_equipment_management_rehab = ""
        specific_equipment_medication_injection = ""
        specific_equipment_xray_examination = ""
        specific_equipment_procedures_surgeries1 = ""
        specific_equipment_procedures_surgeries2 = ""
        specific_equipment_procedures_surgeries3 = ""
        specific_equipment_procedures_surgeries_other = ""
        specific_equipment_anesthesia = ""
        specific_equipment_restoration_prosthetics1 = ""
        specific_equipment_restoration_prosthetics2 = ""
        specific_equipment_restoration_prosthetics3 = ""
        specific_equipment_restoration_prosthetics_other = ""
        specific_equipment_other = ""
        specific_equipment_summary = ""
        dental_practice_initial_medical_examination_add = ""
        dental_practice_second_medical_examination_add = ""
        dental_practice_management_rehab_add = ""
        dental_practice_medication_injection_add = ""
        dental_practice_xray_examination_add = ""
        dental_practice_procedures_surgeries1_add = ""
        dental_practice_procedures_surgeries2_add = ""
        dental_practice_procedures_surgeries3_add = ""
        dental_practice_procedures_surgeries_other_add = ""
        dental_practice_anesthesia_add = ""
        dental_practice_restoration_prosthetics1_add = ""
        dental_practice_restoration_prosthetics2_add = ""
        dental_practice_restoration_prosthetics3_add = ""
        dental_practice_restoration_prosthetics_other_add = ""
        dental_practice_other_add = ""
        dental_practice_summary_add = ""

        score = 0

        this_data = []
        for var in record_dental_practice:
            idx = practice_identification_code.index(var["practice_identification"])
            if var["score"] != None:
                score += eval(f'var["calculation_day_info{day}"]*var["score"]')
            else:
                continue

            if idx == 0:
                dental_practice_initial_medical_examination += str(var["practice_code"])+","
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_initial_medical_examination_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 1:
                dental_practice_second_medical_examination += str(var["practice_code"])+","
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_second_medical_examination_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 2:
                dental_practice_management_rehab += str(var["practice_code"])+","
                this_data.append(var["practice_code"])
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_management_rehab_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 3:
                dental_practice_medication_injection += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_medication_injection_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 4:
                dental_practice_xray_examination += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_xray_examination_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 5:
                dental_practice_procedures_surgeries1 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_procedures_surgeries1_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 6:
                dental_practice_procedures_surgeries2 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_procedures_surgeries2_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 7:
                dental_practice_procedures_surgeries3 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_procedures_surgeries3_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 8:
                dental_practice_procedures_surgeries_other += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_procedures_surgeries_other_add += eval(f'str(var["add_code{ii}"])+","')
            elif idx == 9:
                dental_practice_anesthesia += str(var["practice_code"])+","
                this_data.append(var["practice_code"])            
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_anesthesia_add += eval(f'str(var["add_code{ii}"])+","')    
            elif idx == 10:
                dental_practice_restoration_prosthetics1 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_restoration_prosthetics1_add += eval(f'str(var["add_code{ii}"])+","')    
            elif idx == 11:
                dental_practice_restoration_prosthetics2 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_restoration_prosthetics2_add += eval(f'str(var["add_code{ii}"])+","')    
            elif idx == 12:
                dental_practice_restoration_prosthetics3 += str(var["practice_code"])+","
                this_data.append(var["practice_code"])          
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_restoration_prosthetics3_add += eval(f'str(var["add_code{ii}"])+","')          
            elif idx == 13:
                dental_practice_restoration_prosthetics_other += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_restoration_prosthetics_other_add += eval(f'str(var["add_code{ii}"])+","')    
            elif idx == 14:
                dental_practice_other += str(var["practice_code"])+","
                this_data.append(var["practice_code"])                
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_other_add += eval(f'str(var["add_code{ii}"])+","')    
            elif idx == 15:
                dental_practice_summary += str(var["practice_code"])+","
                this_data.append(var["practice_code"])
                for ii in range(1,36):
                    add_code = eval(f'var["add_code{ii}"]')
                    if add_code != None:
                        dental_practice_summary_add += eval(f'str(var["add_code{ii}"])+","')    
            
            else:
                print(idx)
                
                
        for var in record_drug:
            idx = practice_identification_code.index(var["practice_identification"])
            if var["score"] != None:
                score += eval(f'var["calculation_day_info{day}"]*var["score"]')
            else:
                continue

            if idx == 0:
                drug_initial_medical_examination += str(var["drug_code"])+","
            elif idx == 1:
                drug_second_medical_examination += str(var["drug_code"])+","
            elif idx == 2:
                drug_management_rehab += str(var["drug_code"])+","
            elif idx == 3:
                drug_medication_injection += str(var["drug_code"])+","
            elif idx == 4:
                drug_xray_examination += str(var["drug_code"])+","
            elif idx == 5:
                drug_procedures_surgeries1 += str(var["drug_code"])+","
            elif idx == 6:
                drug_procedures_surgeries2 += str(var["drug_code"])+","
            elif idx == 7:
                drug_procedures_surgeries3 += str(var["drug_code"])+","
            elif idx == 8:
                drug_procedures_surgeries_other += str(var["drug_code"])+","
            elif idx == 9:
                drug_anesthesia += str(var["drug_code"])+","
            elif idx == 10:
                drug_restoration_prosthetics1 += str(var["drug_code"])+","
            elif idx == 11:
                drug_restoration_prosthetics2 += str(var["drug_code"])+","
            elif idx == 12:
                drug_restoration_prosthetics3 += str(var["drug_code"])+","
            elif idx == 13:
                drug_restoration_prosthetics_other += str(var["drug_code"])+","
            elif idx == 14:
                drug_other += str(var["drug_code"])+","
            elif idx == 15:
                drug_summary += str(var["drug_code"])+","
            
            else:
                print(idx)
                

        for var in record_special_equipment:
            idx = practice_identification_code.index(var["practice_identification"])
            if var["score"] != None:
                score += eval(f'var["calculation_day_info{day}"]*var["score"]')
            else:
                continue

            if idx == 0:
                specific_equipment_initial_medical_examination += str(var["special_equipment_code"])+","
            elif idx == 1:
                specific_equipment_second_medical_examination += str(var["special_equipment_code"])+","
            elif idx == 2:
                specific_equipment_management_rehab += str(var["special_equipment_code"])+","
            elif idx == 3:
                specific_equipment_medication_injection += str(var["special_equipment_code"])+","
            elif idx == 4:
                specific_equipment_xray_examination += str(var["special_equipment_code"])+","
            elif idx == 5:
                specific_equipment_procedures_surgeries1 += str(var["special_equipment_code"])+","
            elif idx == 6:
                specific_equipment_procedures_surgeries2 += str(var["special_equipment_code"])+","
            elif idx == 7:
                specific_equipment_procedures_surgeries3 += str(var["special_equipment_code"])+","
            elif idx == 8:
                specific_equipment_procedures_surgeries_other += str(var["special_equipment_code"])+","
            elif idx == 9:
                specific_equipment_anesthesia += str(var["special_equipment_code"])+","
            elif idx == 10:
                specific_equipment_restoration_prosthetics1 += str(var["special_equipment_code"])+","
            elif idx == 11:
                specific_equipment_restoration_prosthetics2 += str(var["special_equipment_code"])+","
            elif idx == 12:
                specific_equipment_restoration_prosthetics3 += str(var["special_equipment_code"])+","
            elif idx == 13:
                specific_equipment_restoration_prosthetics_other += str(var["special_equipment_code"])+","
            elif idx == 14:
                specific_equipment_other += str(var["special_equipment_code"])+","
            elif idx == 15:
                specific_equipment_summary += str(var["special_equipment_code"])+","
            else:
                print(idx)
        
        this_data = set(this_data)
        prevent_dental_practice_set.add(309010510) # P基処追加
        prevent_dental_practice_set.add(309016210) # SPT2
        prevent_dental_practice_set.add(309016310) # SPT2
        prevent_dental_practice_set.add(309016410) # SPT2
        if this_data <= prevent_dental_practice_set:
            practice_type = 1
        else:
            practice_type = 0

        create_list.append(PracticeRecord(
            name=name,
            date=date,
            score=score,
            practice_type=practice_type,
            dental_practice_initial_medical_examination=dental_practice_initial_medical_examination,
            dental_practice_second_medical_examination=dental_practice_second_medical_examination,
            dental_practice_management_rehab=dental_practice_management_rehab,
            dental_practice_medication_injection=dental_practice_medication_injection,
            dental_practice_xray_examination=dental_practice_xray_examination,
            dental_practice_procedures_surgeries1=dental_practice_procedures_surgeries1,
            dental_practice_procedures_surgeries2=dental_practice_procedures_surgeries2,
            dental_practice_procedures_surgeries3=dental_practice_procedures_surgeries3,
            dental_practice_procedures_surgeries_other=dental_practice_procedures_surgeries_other,
            dental_practice_anesthesia=dental_practice_anesthesia,
            dental_practice_restoration_prosthetics1=dental_practice_restoration_prosthetics1,
            dental_practice_restoration_prosthetics2=dental_practice_restoration_prosthetics2,
            dental_practice_restoration_prosthetics3=dental_practice_restoration_prosthetics3,
            dental_practice_restoration_prosthetics_other=dental_practice_restoration_prosthetics_other,
            dental_practice_other=dental_practice_other,
            dental_practice_summary=dental_practice_summary,
            drug_initial_medical_examination=drug_initial_medical_examination,
            drug_second_medical_examination=drug_second_medical_examination,
            drug_management_rehab=drug_management_rehab,
            drug_medication_injection=drug_medication_injection,
            drug_xray_examination=drug_xray_examination,
            drug_procedures_surgeries1=drug_procedures_surgeries1,
            drug_procedures_surgeries2=drug_procedures_surgeries2,
            drug_procedures_surgeries3=drug_procedures_surgeries3,
            drug_procedures_surgeries_other=drug_procedures_surgeries_other,
            drug_anesthesia=drug_anesthesia,
            drug_restoration_prosthetics1=drug_restoration_prosthetics1,
            drug_restoration_prosthetics2=drug_restoration_prosthetics2,
            drug_restoration_prosthetics3=drug_restoration_prosthetics3,
            drug_restoration_prosthetics_other=drug_restoration_prosthetics_other,
            drug_other=drug_other,
            drug_summary=drug_summary,
            specific_equipment_initial_medical_examination=specific_equipment_initial_medical_examination,
            specific_equipment_second_medical_examination=specific_equipment_second_medical_examination,
            specific_equipment_management_rehab=specific_equipment_management_rehab,
            specific_equipment_medication_injection=specific_equipment_medication_injection,
            specific_equipment_xray_examination=specific_equipment_xray_examination,
            specific_equipment_procedures_surgeries1=specific_equipment_procedures_surgeries1,
            specific_equipment_procedures_surgeries2=specific_equipment_procedures_surgeries2,
            specific_equipment_procedures_surgeries3=specific_equipment_procedures_surgeries3,
            specific_equipment_procedures_surgeries_other=specific_equipment_procedures_surgeries_other,
            specific_equipment_anesthesia=specific_equipment_anesthesia,
            specific_equipment_restoration_prosthetics1=specific_equipment_restoration_prosthetics1,
            specific_equipment_restoration_prosthetics2=specific_equipment_restoration_prosthetics2,
            specific_equipment_restoration_prosthetics3=specific_equipment_restoration_prosthetics3,
            specific_equipment_restoration_prosthetics_other=specific_equipment_restoration_prosthetics_other,
            specific_equipment_other=specific_equipment_other,
            specific_equipment_summary=specific_equipment_summary,
            dental_practice_initial_medical_examination_add=dental_practice_initial_medical_examination_add,
            dental_practice_second_medical_examination_add=dental_practice_second_medical_examination_add,
            dental_practice_management_rehab_add=dental_practice_management_rehab_add,
            dental_practice_medication_injection_add=dental_practice_medication_injection_add,
            dental_practice_xray_examination_add=dental_practice_xray_examination_add,
            dental_practice_procedures_surgeries1_add=dental_practice_procedures_surgeries1_add,
            dental_practice_procedures_surgeries2_add=dental_practice_procedures_surgeries2_add,
            dental_practice_procedures_surgeries3_add=dental_practice_procedures_surgeries3_add,
            dental_practice_procedures_surgeries_other_add=dental_practice_procedures_surgeries_other_add,
            dental_practice_anesthesia_add=dental_practice_anesthesia_add,
            dental_practice_restoration_prosthetics1_add=dental_practice_restoration_prosthetics1_add,
            dental_practice_restoration_prosthetics2_add=dental_practice_restoration_prosthetics2_add,
            dental_practice_restoration_prosthetics3_add=dental_practice_restoration_prosthetics3_add,
            dental_practice_restoration_prosthetics_other_add=dental_practice_restoration_prosthetics_other_add,
            dental_practice_other_add=dental_practice_other_add,
            dental_practice_summary_add=dental_practice_summary_add,            
        ))
    PracticeRecord.objects.bulk_create(create_list)
        
    return render(request, 'index.html')

def analysis_monthly_data(request):
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)
    idx = ['合計','治療','予防','治療割合','予防割合']
    df = pd.DataFrame(index=idx, columns=[])
    idx_stage = ["治療1回目","治療2回目","治療3回目","治療4回目","治療4回目以降","予防1回目","予防2回目","予防3回目","予防4回目","予防4回目以降",]
    df_stage = pd.DataFrame(index=idx_stage, columns=[])
    
    for ii in range(start_idx,end_idx+1):
        # 予防と治療の割合
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)
        medical_treatment = PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1).count()
        prevent_treatment = PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).count()
        sum_treatment = medical_treatment+prevent_treatment
        try:
            medical_treatment_rate = f'{round(medical_treatment/sum_treatment*100,1)} %'
        except:
            medical_treatment_rate = '- %'
        try:
            prevent_treatment_rate = f'{round(prevent_treatment/sum_treatment*100,1)} %'
        except:
            prevent_treatment_rate = '- %'
        df[f'{start_date.year}/{start_date.month}'] = [
            sum_treatment,
            medical_treatment,
            prevent_treatment,
            medical_treatment_rate,
            prevent_treatment_rate
            ]
        
        # ステージ管理        
        medical_0 = 0
        medical_1 = 0
        medical_2 = 0
        medical_3 = 0
        medical_over = 0
        prevent_0 = 0
        prevent_1 = 0
        prevent_2 = 0
        prevent_3 = 0
        prevent_over = 0

        names = PracticeRecord.objects.filter(date__range=(start_date,end_date)).values("name")
        name_list = set([name["name"] for name in names])

        for name in name_list:
            treatments = PracticeRecord.objects.filter(name=name).values("practice_type","date")
            date_list = [treatment["date"] for treatment in treatments]
            practice_type_list = [treatment["practice_type"] for treatment in treatments]
            df_treat = pd.DataFrame({
                "date_list":date_list,
                "practice_type_list":practice_type_list
            })
            df_treat = df_treat.sort_values("date_list")
            stage_list = []
            for ii, data in enumerate(list(df_treat["practice_type_list"])):
                if ii==0:
                    if data == 0:
                        count_0 = 1
                        count_1 = 0
                        stage_list.append(f'0-{count_0}')
                    else:
                        count_0 = 0
                        count_1 = 1
                        stage_list.append(f'1-{count_1}')
                else:
                    if data == 0:
                        if int(stage_list[-1].split("-")[0]) == 0:
                            count_0 += 1
                            stage_list.append(f'0-{count_0}')
                        else:
                            count_0 = 1
                            stage_list.append(f'0-{count_0}')
                    else:
                        if int(stage_list[-1].split("-")[0]) == 0:
                            count_1 = 1
                            stage_list.append(f'1-{count_1}')
                        else:
                            count_1 += 1
                            stage_list.append(f'1-{count_1}')
            df_treat["stage_list"] = stage_list
            treatments = PracticeRecord.objects.filter(name=name,date__range=(start_date,end_date)).values("date")
            for treatment in treatments:
                stage = df_treat[df_treat["date_list"] == treatment["date"]]["stage_list"].item()
                practice_type = df_treat[df_treat["date_list"] == treatment["date"]]["practice_type_list"].item()
                if practice_type == 0:
                    if stage == "0-1":
                        medical_0 += 1
                    elif stage == "0-2":
                        medical_1 += 1
                    elif stage == "0-3":
                        medical_2 += 1
                    elif stage == "0-4":
                        medical_3 += 1
                    else:
                        medical_over += 1
                else:
                    if stage == "1-1":
                        prevent_0 += 1
                    elif stage == "1-2":
                        prevent_1 += 1
                    elif stage == "1-3":
                        prevent_2 += 1
                    elif stage == "1-4":
                        prevent_3 += 1
                    else:
                        prevent_over += 1
        df_stage[f'{start_date.year}/{start_date.month}'] = [
            medical_0,
            medical_1,
            medical_2,
            medical_3,
            medical_over,
            prevent_0,
            prevent_1,
            prevent_2,
            prevent_3,
            prevent_over
            ]
                
    
    context = {
    'monthly_data' : df.to_html(), 
    'monthly_stage_data' : df_stage.to_html(), 
    }

    return render(request, 'analysis_monthly_data.html', context)

def export_patient_data(request):
    start = request.POST["start"].split("-")
    end = request.POST["end"].split("-")
    print(start)
    start_date = datetime.date(int(start[0]),int(start[1]),int(start[2]))
    end_date = datetime.date(int(end[0]),int(end[1]),int(end[2]))
    records = PracticeRecord.objects.filter(date__range=(start_date,end_date))
    df = read_frame(records)
    dental_practice_set = []
    master_basic = TableBasic.objects.all().values("dental_practice_code","practice_bassic_name","new_score_etc","add_code")
    score_list = []
    no_code_set = set([])

    for ii in range(len(df["id"])):
        score_list.append(df["score"][ii])

        dental_practice_initial_medical_examination = df["dental_practice_initial_medical_examination"][ii].split(",")
        dl = []
        for data in dental_practice_initial_medical_examination[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_initial_medical_examination"][ii] = set(dl)

        dental_practice_second_medical_examination = df["dental_practice_second_medical_examination"][ii].split(",")
        dl = []
        for data in dental_practice_second_medical_examination[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_second_medical_examination"][ii] = set(dl)
        

        dental_practice_management_rehab = df["dental_practice_management_rehab"][ii].split(",")
        dl = []
        for data in dental_practice_management_rehab[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_management_rehab"][ii] = set(dl)

        dental_practice_medication_injection = df["dental_practice_medication_injection"][ii].split(",")
        dl = []
        for data in dental_practice_medication_injection[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_medication_injection"][ii] = set(dl)

        dental_practice_xray_examination = df["dental_practice_xray_examination"][ii].split(",")
        dl = []
        for data in dental_practice_xray_examination[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_xray_examination"][ii] = set(dl)

        dental_practice_procedures_surgeries1 = df["dental_practice_procedures_surgeries1"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries1[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_procedures_surgeries1"][ii] = set(dl)

        dental_practice_procedures_surgeries2 = df["dental_practice_procedures_surgeries2"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries2[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_procedures_surgeries2"][ii] = set(dl)

        dental_practice_procedures_surgeries3 = df["dental_practice_procedures_surgeries3"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries3[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_procedures_surgeries3"][ii] = set(dl)

        dental_practice_procedures_surgeries_other = df["dental_practice_procedures_surgeries_other"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries_other[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_procedures_surgeries_other"][ii] = set(dl)

        dental_practice_anesthesia = df["dental_practice_anesthesia"][ii].split(",")
        dl = []
        for data in dental_practice_anesthesia[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_anesthesia"][ii] = set(dl)

        dental_practice_restoration_prosthetics1 = df["dental_practice_restoration_prosthetics1"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics1[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_restoration_prosthetics1"][ii] = set(dl)

        dental_practice_restoration_prosthetics2 = df["dental_practice_restoration_prosthetics2"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics2[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_restoration_prosthetics2"][ii] = set(dl)

        dental_practice_restoration_prosthetics3 = df["dental_practice_restoration_prosthetics3"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics3[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_restoration_prosthetics3"][ii] = set(dl)

        dental_practice_restoration_prosthetics_other = df["dental_practice_restoration_prosthetics_other"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics_other[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_restoration_prosthetics_other"][ii] = set(dl)

        dental_practice_other = df["dental_practice_other"][ii].split(",")
        dl = []
        for data in dental_practice_other[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_other"][ii] = set(dl)

        dental_practice_summary = df["dental_practice_summary"][ii].split(",")
        dl = []
        for data in dental_practice_summary[:-1]:
            try:
                dl.append(master_basic.get(dental_practice_code=int(data))["practice_bassic_name"])
            except:
                dl.append(int(data))
                no_code_set.add(int(data))
        df["dental_practice_summary"][ii] = set(dl)
        
        dental_practice_initial_medical_examination_add = df["dental_practice_initial_medical_examination_add"][ii].split(",")
        dl = []
        for data in dental_practice_initial_medical_examination_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_initial_medical_examination_add"][ii] = set(dl)

        dental_practice_second_medical_examination_add = df["dental_practice_second_medical_examination_add"][ii].split(",")
        dl = []
        for data in dental_practice_second_medical_examination_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_second_medical_examination_add"][ii] = set(dl)
        

        dental_practice_management_rehab_add = df["dental_practice_management_rehab_add"][ii].split(",")
        dl = []
        for data in dental_practice_management_rehab_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_management_rehab_add"][ii] = set(dl)

        dental_practice_medication_injection_add = df["dental_practice_medication_injection_add"][ii].split(",")
        dl = []
        for data in dental_practice_medication_injection_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_medication_injection_add"][ii] = set(dl)

        dental_practice_xray_examination_add = df["dental_practice_xray_examination_add"][ii].split(",")
        dl = []
        for data in dental_practice_xray_examination_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_xray_examination_add"][ii] = set(dl)

        dental_practice_procedures_surgeries1_add = df["dental_practice_procedures_surgeries1_add"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries1_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_procedures_surgeries1_add"][ii] = set(dl)

        dental_practice_procedures_surgeries2_add = df["dental_practice_procedures_surgeries2_add"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries2_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_procedures_surgeries2_add"][ii] = set(dl)

        dental_practice_procedures_surgeries3_add = df["dental_practice_procedures_surgeries3_add"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries3_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_procedures_surgeries3_add"][ii] = set(dl)

        dental_practice_procedures_surgeries_other_add = df["dental_practice_procedures_surgeries_other_add"][ii].split(",")
        dl = []
        for data in dental_practice_procedures_surgeries_other_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_procedures_surgeries_other_add"][ii] = set(dl)

        dental_practice_anesthesia_add = df["dental_practice_anesthesia_add"][ii].split(",")
        dl = []
        for data in dental_practice_anesthesia_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_anesthesia_add"][ii] = set(dl)

        dental_practice_restoration_prosthetics1_add = df["dental_practice_restoration_prosthetics1_add"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics1_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_restoration_prosthetics1_add"][ii] = set(dl)

        dental_practice_restoration_prosthetics2_add = df["dental_practice_restoration_prosthetics2_add"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics2_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_restoration_prosthetics2_add"][ii] = set(dl)

        dental_practice_restoration_prosthetics3_add = df["dental_practice_restoration_prosthetics3_add"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics3_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_restoration_prosthetics3_add"][ii] = set(dl)

        dental_practice_restoration_prosthetics_other_add = df["dental_practice_restoration_prosthetics_other_add"][ii].split(",")
        dl = []
        for data in dental_practice_restoration_prosthetics_other_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_restoration_prosthetics_other_add"][ii] = set(dl)

        dental_practice_other_add = df["dental_practice_other_add"][ii].split(",")
        dl = []
        for data in dental_practice_other_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_other_add"][ii] = set(dl)

        dental_practice_summary_add = df["dental_practice_summary_add"][ii].split(",")
        dl = []
        for data in dental_practice_summary_add[:-1]:
            try:
                dl.append(master_basic.get(add_code=data)["practice_bassic_name"])
            except:
                dl.append(data)
                no_code_set.add(data)
        df["dental_practice_summary_add"][ii] = set(dl)

        dental_practice_set.append(
                df["dental_practice_initial_medical_examination"][ii] | \
                df["dental_practice_second_medical_examination"][ii] | \
                df["dental_practice_management_rehab"][ii] | \
                df["dental_practice_medication_injection"][ii] | \
                df["dental_practice_xray_examination"][ii] | \
                df["dental_practice_procedures_surgeries1"][ii] | \
                df["dental_practice_procedures_surgeries2"][ii] | \
                df["dental_practice_procedures_surgeries3"][ii] | \
                df["dental_practice_restoration_prosthetics_other"][ii] | \
                df["dental_practice_anesthesia"][ii] | \
                df["dental_practice_restoration_prosthetics1"][ii] | \
                df["dental_practice_restoration_prosthetics2"][ii] | \
                df["dental_practice_restoration_prosthetics3"][ii] | \
                df["dental_practice_restoration_prosthetics_other"][ii] | \
                df["dental_practice_other"][ii] | \
                df["dental_practice_summary"][ii] | \
                df["dental_practice_initial_medical_examination_add"][ii] | \
                df["dental_practice_second_medical_examination_add"][ii] | \
                df["dental_practice_management_rehab_add"][ii] | \
                df["dental_practice_medication_injection_add"][ii] | \
                df["dental_practice_xray_examination_add"][ii] | \
                df["dental_practice_procedures_surgeries1_add"][ii] | \
                df["dental_practice_procedures_surgeries2_add"][ii] | \
                df["dental_practice_procedures_surgeries3_add"][ii] | \
                df["dental_practice_restoration_prosthetics_other_add"][ii] | \
                df["dental_practice_anesthesia_add"][ii] | \
                df["dental_practice_restoration_prosthetics1_add"][ii] | \
                df["dental_practice_restoration_prosthetics2_add"][ii] | \
                df["dental_practice_restoration_prosthetics3_add"][ii] | \
                df["dental_practice_restoration_prosthetics_other_add"][ii] | \
                df["dental_practice_other_add"][ii] | \
                df["dental_practice_summary_add"][ii]
        )
    df['dental_practice_set'] = dental_practice_set

    df["score"] = score_list

    print("=========================")
    print(no_code_set)
    print("=========================")
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="patient_practice_data.csv"'
    df.to_csv(response)
    return response

def export_patient_data_set(request):
    start = request.POST["start"].split("-")
    end = request.POST["end"].split("-")
    print(start)
    start_date = datetime.date(int(start[0]),int(start[1]),int(start[2]))
    end_date = datetime.date(int(end[0]),int(end[1]),int(end[2]))
    records = PracticeRecord.objects.filter(date__range=(start_date,end_date))
    df = read_frame(records)
    master_basic = TableBasic.objects.all().values("dental_practice_code","practice_bassic_name")
    dental_practice_set = []
    for ii in range(len(df["id"])):
        dental_practice_initial_medical_examination = df["dental_practice_initial_medical_examination"][ii].split(",")
        try:
            df["dental_practice_initial_medical_examination"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_initial_medical_examination[:-1]])
        except:
            pass
        dental_practice_second_medical_examination = df["dental_practice_second_medical_examination"][ii].split(",")
        try:
            df["dental_practice_second_medical_examination"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_second_medical_examination[:-1]])
        except:
            pass
        dental_practice_management_rehab = df["dental_practice_management_rehab"][ii].split(",")
        try:
            df["dental_practice_management_rehab"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_management_rehab[:-1]])
        except:
            pass
        dental_practice_medication_injection = df["dental_practice_medication_injection"][ii].split(",")
        try:
            df["dental_practice_medication_injection"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_medication_injection[:-1]])
        except:
            pass
        dental_practice_xray_examination = df["dental_practice_xray_examination"][ii].split(",")
        try:
            df["dental_practice_xray_examination"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_xray_examination[:-1]])
        except:
            pass
        dental_practice_procedures_surgeries1 = df["dental_practice_procedures_surgeries1"][ii].split(",")
        try:
            df["dental_practice_procedures_surgeries1"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_procedures_surgeries1[:-1]])
        except:
            pass
        dental_practice_procedures_surgeries2 = df["dental_practice_procedures_surgeries2"][ii].split(",")
        try:
            df["dental_practice_procedures_surgeries2"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_procedures_surgeries2[:-1]])
        except:
            pass
        dental_practice_procedures_surgeries3 = df["dental_practice_procedures_surgeries3"][ii].split(",")
        try:
            df["dental_practice_procedures_surgeries3"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_procedures_surgeries3[:-1]])
        except:
            pass
        dental_practice_procedures_surgeries_other = df["dental_practice_procedures_surgeries_other"][ii].split(",")
        try:
            df["dental_practice_procedures_surgeries_other"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_procedures_surgeries_other[:-1]])
        except:
            pass
        dental_practice_anesthesia = df["dental_practice_anesthesia"][ii].split(",")
        try:
            df["dental_practice_anesthesia"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_anesthesia[:-1]])
        except:
            pass
        dental_practice_restoration_prosthetics1 = df["dental_practice_restoration_prosthetics1"][ii].split(",")
        try:
            df["dental_practice_restoration_prosthetics1"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_restoration_prosthetics1[:-1]])
        except:
            pass
        dental_practice_restoration_prosthetics2 = df["dental_practice_restoration_prosthetics2"][ii].split(",")
        try:
            df["dental_practice_restoration_prosthetics2"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_restoration_prosthetics2[:-1]])
        except:
            pass
        dental_practice_restoration_prosthetics3 = df["dental_practice_restoration_prosthetics3"][ii].split(",")
        try:
            df["dental_practice_restoration_prosthetics3"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_restoration_prosthetics3[:-1]])
        except:
            pass
        dental_practice_restoration_prosthetics_other = df["dental_practice_restoration_prosthetics_other"][ii].split(",")
        try:
            df["dental_practice_restoration_prosthetics_other"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_restoration_prosthetics_other[:-1]])
        except:
            pass
        dental_practice_other = df["dental_practice_other"][ii].split(",")
        try:
            df["dental_practice_other"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_other[:-1]])
        except:
            pass
        dental_practice_summary = df["dental_practice_summary"][ii].split(",")
        try:
            df["dental_practice_summary"][ii] = set([master_basic.get(dental_practice_code=int(data))["practice_bassic_name"] for data in dental_practice_summary[:-1]])
        except:
            pass
        dental_practice_set.append(str(
                df["dental_practice_initial_medical_examination"][ii] | \
                df["dental_practice_second_medical_examination"][ii] | \
                df["dental_practice_management_rehab"][ii] | \
                df["dental_practice_medication_injection"][ii] | \
                df["dental_practice_xray_examination"][ii] | \
                df["dental_practice_procedures_surgeries1"][ii] | \
                df["dental_practice_procedures_surgeries2"][ii] | \
                df["dental_practice_procedures_surgeries3"][ii] | \
                df["dental_practice_restoration_prosthetics_other"][ii] | \
                df["dental_practice_anesthesia"][ii] | \
                df["dental_practice_restoration_prosthetics1"][ii] | \
                df["dental_practice_restoration_prosthetics2"][ii] | \
                df["dental_practice_restoration_prosthetics3"][ii] | \
                df["dental_practice_restoration_prosthetics_other"][ii] | \
                df["dental_practice_other"][ii] | \
                df["dental_practice_summary"][ii]
        ))
        
    dental_practice_set = set(dental_practice_set)
    print(dental_practice_set)
    df = pd.DataFrame(dental_practice_set)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="patient_practice_data.csv"'
    df.to_csv(response)
    return response

def export_prevent_set(request):
    records = PreventDentalPractice.objects.all()
    df = read_frame(records)
    master_basic = TableBasic.objects.all().values("dental_practice_code","practice_bassic_name")
    
    for ii in range(len(df['id'])):
        df['dental_practice_code'][ii] = master_basic.get(dental_practice_code = df['dental_practice_code'][ii])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="patient_practice_data.csv"'
    df.to_csv(response)
    return response

def transform_yobou(request):
    prevent_set = set([prevent_code.dental_practice_code for prevent_code in PreventDentalPractice.objects.all()])
    prevent_set.add(309010510) # P基処追加
    prevent_set.add(309016210) # SPT2
    prevent_set.add(309016310) # SPT2
    prevent_set.add(309016410) # SPT2

    name_list_query = PracticeRecord.objects.distinct().values_list("name")
    name_list = [name[0] for name in name_list_query]

    for name in name_list:
        practice_type_list = [obj.practice_type for obj in PracticeRecord.objects.filter(name=name)]
        date_list = [obj.date for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_management_rehab = [obj.dental_practice_management_rehab for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_medication_injection = [obj.dental_practice_medication_injection for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_xray_examination = [obj.dental_practice_xray_examination for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_procedures_surgeries1 = [obj.dental_practice_procedures_surgeries1 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_procedures_surgeries2 = [obj.dental_practice_procedures_surgeries2 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_procedures_surgeries3 = [obj.dental_practice_procedures_surgeries3 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_procedures_surgeries_other = [obj.dental_practice_procedures_surgeries_other for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_anesthesia = [obj.dental_practice_anesthesia for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_restoration_prosthetics1 = [obj.dental_practice_restoration_prosthetics1 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_restoration_prosthetics2 = [obj.dental_practice_restoration_prosthetics2 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_restoration_prosthetics3 = [obj.dental_practice_restoration_prosthetics3 for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_restoration_prosthetics_other = [obj.dental_practice_restoration_prosthetics_other for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_other = [obj.dental_practice_other for obj in PracticeRecord.objects.filter(name=name)]
        dental_practice_summary = [obj.dental_practice_summary for obj in PracticeRecord.objects.filter(name=name)]
        code_list = []

        for ii in range(len(date_list)):
            treat_code = dental_practice_management_rehab[ii]
            treat_code += dental_practice_medication_injection[ii]
            treat_code += dental_practice_xray_examination[ii]
            treat_code += dental_practice_procedures_surgeries1[ii]
            treat_code += dental_practice_procedures_surgeries2[ii]
            treat_code += dental_practice_procedures_surgeries3[ii]
            treat_code += dental_practice_procedures_surgeries_other[ii]
            treat_code += dental_practice_anesthesia[ii]
            treat_code += dental_practice_restoration_prosthetics1[ii]
            treat_code += dental_practice_restoration_prosthetics2[ii]
            treat_code += dental_practice_restoration_prosthetics3[ii]
            treat_code += dental_practice_restoration_prosthetics_other[ii]
            treat_code += dental_practice_other[ii]
            treat_code += dental_practice_summary[ii]
            code_list.append(set(map(int,treat_code.split(",")[:-1])))

        df = pd.DataFrame({
            "date":date_list,
            "code_list":code_list,
            "practice_type":practice_type_list
                           })
        
        df = df.sort_values("date")
        df = df.reset_index(drop=True) # ソートしたdfでindexを付け直す

        before_date = "-"
        before_type = "-"
        date_interval = []
        for index, row in df.iterrows():
            date = row["date"]
            code_set = row["code_list"]
            try:
                after_date_interval = (df["date"][index+1]-date).days
                after_type = df["practice_type"][index+1]
            except:
                after_date_interval = "-"
                after_type = "-"

            if before_date == "-":
                date_interval = ("-")
            else:
                date_interval = (date-before_date).days
        
            
            if (date_interval == "-") and (after_date_interval == "-"):
                if code_set <= prevent_set:
                    type = 2
                else:
                    type = 0
            elif (date_interval == "-"):
                if code_set <= prevent_set:
                    if (after_type == 0) and (after_date_interval <= 30):
                        type = 1
                    else:
                        type = 2
                else:
                    type = 0
            elif (after_date_interval == "-"):
                if code_set <= prevent_set:
                    if (before_type == 0) and (date_interval <= 30):
                        type = 1
                    else:
                        type = 2
                else:
                    type = 0
            else:
                if code_set <= prevent_set:
                    if ((before_type == 0) and (date_interval <= 30)) or ((after_type == 0) and (after_date_interval <= 30)):
                        type = 1
                    else:
                        type = 2
                else:
                    type = 0

            update_record = PracticeRecord.objects.get(name=name, date=date)
            update_record.practice_type = type
            update_record.save()

            before_date = row["date"]  
            before_type = type
        del df

    return render(request, 'index.html')

def analysis_monthly_data_score(request):
    counts = 0
    sc_srp = [
    309004810,
    309004970,
    309005010,
    309005110,
    309005210
    ]
    spt = [
        309014710,
        309014810,
        309005710,
        309020370
    ]

    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)

    medical_score_list = []
    prevent_score_list = []
    sc_srp_score_list = []
    sc_srp_count_list = []
    spt_score_list = []
    spt_count_list = []
    
    columns = []
    for ii in range(start_idx,end_idx+1):
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)
        columns.append(f'{start_date.year}/{start_date.month}')

        sc_srp_score = 0
        sc_srp_count = 0
        spt_score = 0
        spt_count = 0

        medical_treatment = PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1)
        prevent_treatment = PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2)

        month_medical_score = 0
        for treat in medical_treatment:
            treat_list =[]
            treat_list += list(map(int,treat.dental_practice_initial_medical_examination.split(",")[:-1]))            
            treat_list += list(map(int,treat.dental_practice_second_medical_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_management_rehab.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_medication_injection.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_xray_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_anesthesia.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_summary.split(",")[:-1]))

            month_medical_score += treat.score
        medical_score_list.append(month_medical_score)

        month_prevent_score = 0
        for treat in prevent_treatment:
            flag_sc_srp = 0
            flag_spt = 0
            treat_list =[] 
            treat_list += list(map(int,treat.dental_practice_initial_medical_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_second_medical_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_management_rehab.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_medication_injection.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_xray_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_anesthesia.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_summary.split(",")[:-1]))
            
            month_prevent_score += treat.score

            for ii in treat_list:
                if ii in sc_srp:
                    flag_sc_srp = 1
                if ii in spt:
                    flag_spt = 1

            if flag_sc_srp == 1:
                sc_srp_count += 1
                sc_srp_score += treat.score
            if flag_spt == 1:
                spt_count += 1
                spt_score += treat.score
        sc_srp_count_list.append(sc_srp_count)
        sc_srp_score_list.append(sc_srp_score)
        spt_count_list.append(spt_count)
        spt_score_list.append(spt_score)
        
        prevent_score_list.append(month_prevent_score)

    sum_score = [x + y for (x, y) in zip(medical_score_list, prevent_score_list)]

    idx = ['合計','治療','予防','SC/SRP回数','SC/SRP点数','SPT回数','SPT点数']
    df = pd.DataFrame([sum_score,medical_score_list,prevent_score_list,sc_srp_count_list,sc_srp_score_list,spt_count_list,spt_score_list],index=idx, columns=columns)
    print(df)
    print(counts)

    context = {
    'monthly_data' : df.to_html(), 
    }

    return render(request, 'analysis_monthly_data_score.html', context)

def analysis_monthly_patient_stage(request):
    ## 治療または予防の何回めかを各診療にラベル付する
    # DataFrameに診療情報を入れる
    records = PracticeRecord.objects.all()
    df = read_frame(records)
    
    # 名前順、日付順の優先順位で並び替える
    df = df.sort_values(["name","date"])
    df = df.reset_index(drop=True) # ソートしたdfでindexを付け直す
    df.loc[df["practice_type"] == 1,"practice_type"] = 0 # practice_typeが"1"のものを"0"に変換する

    # 治療・予防何回目かを判定
    max_date = df["date"].max() #データの最終日を取得
    stage_num_list = []
    active_list = []    
    before_name = "reset name"
    for ii in range(len(df)):
        name = df["name"][ii]
        if ii != len(df)-1:
            if df["name"][ii+1] == name:
                active_list.append(1)
            else:
                if (max_date - df["date"][ii]).days <= 180:
                    active_list.append(1)
                else:
                    active_list.append(0)
        else:
            if (max_date - df["date"][ii]).days <= 180:
                active_list.append(1)
            else:
                active_list.append(0)

        if name != before_name:
            before_name = copy.copy(name)
            stage_num_list.append(1)
            before_type = df["practice_type"][ii]
        else:
            if before_type == df["practice_type"][ii]:
                stage_num_list.append(stage_num_list[ii-1]+1)
            else:
                stage_num_list.append(1)
                before_type = df["practice_type"][ii]
            
    df["stage_continue_num"] = stage_num_list
    df["active"] = active_list

    # 治療終了フラグをつける
    finish_flag = []

    ## 月次のステージ集計する
    # 入力を受け取り何年何月から何月までを表示するかを取得
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)

    df_result_all = pd.DataFrame(index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_result_break = pd.DataFrame(index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_result_break_per = pd.DataFrame(index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])

    for ii in range(start_idx,end_idx+1):
        # 該当月のみを抽出
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)        
        monthly_df = df[(df["date"]>=start_date) & (df["date"]<=end_date)]

        # 治療の離脱人数のカウント
        medic_1_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==1)).sum()
        medic_2_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==2)).sum()
        medic_3_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==3)).sum()
        medic_4_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==4)).sum()
        medic_over_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]>4)).sum()
        medic_break_sum = medic_1_break + medic_2_break + medic_3_break + medic_4_break + medic_over_break 

        # 予防の離脱人数のカウント
        prevent_1_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==1)).sum()
        prevent_2_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==2)).sum()
        prevent_3_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==3)).sum()
        prevent_4_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==4)).sum()
        prevent_over_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]>4)).sum() 
        prevent_break_sum = prevent_1_break + prevent_2_break + prevent_3_break + prevent_4_break + prevent_over_break        

        # 治療の全体人数のカウント
        medic_1_all = ((monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==1)).sum()
        medic_2_all = ((monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==2)).sum()
        medic_3_all = ((monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==3)).sum()
        medic_4_all = ((monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]==4)).sum()
        medic_over_all = ((monthly_df["practice_type"]==0) & (monthly_df["stage_continue_num"]>4)).sum()
        medic_all_sum = medic_1_all + medic_2_all + medic_3_all + medic_4_all + medic_over_all 

        # 予防の全体人数のカウント
        prevent_1_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==1)).sum()
        prevent_2_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==2)).sum()
        prevent_3_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==3)).sum()
        prevent_4_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==4)).sum()
        prevent_over_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]>4)).sum()
        prevent_all_sum = prevent_1_all + prevent_2_all + prevent_3_all + prevent_4_all + prevent_over_all        

        # 治療の離脱率
        medic_1_break_per = str(round(medic_1_break*100/medic_1_all,2))+" %"        
        medic_2_break_per = str(round(medic_2_break*100/medic_2_all,2))+" %"                
        medic_3_break_per = str(round(medic_3_break*100/medic_3_all,2))+" %"                
        medic_4_break_per = str(round(medic_4_break*100/medic_4_all,2))+" %"                
        medic_over_break_per = str(round(medic_over_break*100/medic_over_all,2))+" %"
        medic_break_per_sum = str(round(medic_break_sum/medic_all_sum,2))+" %"

        # 予防の離脱率        
        prevent_1_break_per = str(round(prevent_1_break*100/prevent_1_all,2))+" %"                
        prevent_2_break_per = str(round(prevent_2_break*100/prevent_2_all,2))+" %"                
        prevent_3_break_per = str(round(prevent_3_break*100/prevent_3_all,2))+" %"                
        prevent_4_break_per = str(round(prevent_4_break*100/prevent_4_all,2))+" %"                
        prevent_over_break_per = str(round(prevent_over_break*100/prevent_over_all,2))+" %"   
        prevent_break_per_sum = str(round(prevent_break_sum/prevent_all_sum,2))+" %"     

        break_per_sum = str(round((medic_break_sum+prevent_break_sum)/(medic_all_sum+prevent_all_sum),2))+" %"

        append_list_all = [medic_all_sum+prevent_all_sum,medic_all_sum,medic_1_all,medic_2_all,medic_3_all,medic_4_all,medic_over_all,prevent_all_sum,prevent_1_all,prevent_2_all,prevent_3_all,prevent_4_all,prevent_over_all]
        append_list_break = [medic_break_sum+prevent_break_sum,medic_break_sum,medic_1_break,medic_2_break,medic_3_break,medic_4_break,medic_over_break,prevent_break_sum,prevent_1_break,prevent_2_break,prevent_3_break,prevent_4_break,prevent_over_break]
        append_list_break_per = [break_per_sum,medic_break_per_sum,medic_1_break_per,medic_2_break_per,medic_3_break_per,medic_4_break_per,medic_over_break_per,prevent_break_per_sum,prevent_1_break_per,prevent_2_break_per,prevent_3_break_per,prevent_4_break_per,prevent_over_break_per]
        
        df_result_all[month_list[ii]] = append_list_all
        df_result_break[month_list[ii]] = append_list_break
        df_result_break_per[month_list[ii]] = append_list_break_per
    
    context = {
    'all' : df_result_all.to_html(), 
    'break' : df_result_break.to_html(), 
    'break_per' : df_result_break_per.to_html()
    }

    return render(request, 'analysis_monthly_patient_stage.html', context)

def import_apodent_responsible_data(request):
    if 'csv' in request.FILES:
        record_receipt_common = RecordReceiptCommon.objects.all()
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        data_row = csv.reader(form_data)
        df = pd.read_csv(form_data)
        df = df.loc[:,["カルテ番号","患者名","予約日","歯科医師","衛生士・助手"]]
        df = df.dropna(subset=['カルテ番号'])
        df = df.reset_index(drop=True)
        count = 0

        for ii in range(len(df)):
            name = ""
            date = datetime.date(int(df["予約日"][ii].split("/")[0]),int(df["予約日"][ii].split("/")[1]),int(df["予約日"][ii].split("/")[2]))
            dr = df["歯科医師"][ii]
            dh_da = df["衛生士・助手"][ii]
            chart_num = "0"*(8-len(str(int(df["カルテ番号"][ii])))) + str(int(df["カルテ番号"][ii]))
            names = RecordReceiptCommon.objects.filter(chart_number=chart_num)
            for ii in names:
                name = ii.name            
            try:                
                record = PracticeRecord.objects.get(name=name,date=date)
                record.responsible_dr = dr
                record.responsible_dhda = dh_da
                record.save()
            except:
                count += 1
        print(count)

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def analysis_assess_responsible(request):
    ## 治療または予防の何回めかを各診療にラベル付する
    # DataFrameに診療情報を入れる
    records = PracticeRecord.objects.all()
    df = read_frame(records)
    
    # 名前順、日付順の優先順位で並び替える
    df = df.sort_values(["name","date"])
    df = df.reset_index(drop=True) # ソートしたdfでindexを付け直す
    df.loc[df["practice_type"] == 1,"practice_type"] = 0 # practice_typeが"1"のものを"0"に変換する

    # 治療・予防何回目かを判定
    max_date = df["date"].max() #データの最終日を取得
    stage_num_list = []
    active_list = []    
    before_name = "reset name"
    for ii in range(len(df)):
        name = df["name"][ii]
        if ii != len(df)-1:
            if df["name"][ii+1] == name:
                active_list.append(1)
            else:
                if (max_date - df["date"][ii]).days <= 180:
                    active_list.append(1)
                else:
                    active_list.append(0)
        else:
            if (max_date - df["date"][ii]).days <= 180:
                active_list.append(1)
            else:
                active_list.append(0)

        if name != before_name:
            before_name = copy.copy(name)
            stage_num_list.append(1)
            before_type = df["practice_type"][ii]
        else:
            if before_type == df["practice_type"][ii]:
                stage_num_list.append(stage_num_list[ii-1]+1)
            else:
                stage_num_list.append(1)
                before_type = df["practice_type"][ii]
            
    df["stage_continue_num"] = stage_num_list
    df["active"] = active_list

    # 該当月のデータを集計
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    month = request.GET["month"]
    idx = month_list.index(int(month))
    start_date = datetime.date(int(month[:4]),int(month[4:]),1)
    end_date = datetime.date(int(str(month_list[idx+1])[:4]),int(str(month_list[idx+1])[4:]),1)-datetime.timedelta(days=1)
    print(start_date,end_date)

    # 該当月内のデータのみを抽出
    df = df[(df["date"]>=start_date) & (df["date"]<=end_date)]
    dhda = list(df["responsible_dhda"].unique()) #dhdaリスト作成
    dr = list(df["responsible_dr"].unique()) #drリスト作成
    print(len(df))

    print(dhda)
    print(dr)

    ## ステージごとに集計
    df_dhda_count = pd.DataFrame(columns=dhda,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_dhda_breakaway = pd.DataFrame(columns=dhda,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_dhda_breakaway_per = pd.DataFrame(columns=dhda,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_dr_count = pd.DataFrame(columns=dr,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_dr_breakaway = pd.DataFrame(columns=dr,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_dr_breakaway_per = pd.DataFrame(columns=dr,index=["合計","治療","治療１回目","治療２回目","治療３回目","治療４回目","治療４回目以降","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])

    # dhdaについて集計
    for var in dhda:
        df_dhda_count.at["合計",var] = (df["responsible_dhda"]==var).sum()
        df_dhda_count.at["治療",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0)).sum()
        df_dhda_count.at["治療１回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==1)).sum()
        df_dhda_count.at["治療２回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==2)).sum()
        df_dhda_count.at["治療３回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==3)).sum()
        df_dhda_count.at["治療４回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==4)).sum()
        df_dhda_count.at["治療４回目以降",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]>4)).sum()
        df_dhda_count.at["予防",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2)).sum()
        df_dhda_count.at["予防１回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==1)).sum()
        df_dhda_count.at["予防２回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==2)).sum()
        df_dhda_count.at["予防３回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==3)).sum()
        df_dhda_count.at["予防４回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==4)).sum()
        df_dhda_count.at["予防４回目以降",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]>4)).sum()

        df_dhda_breakaway.at["合計",var] = ((df["responsible_dhda"]==var) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療１回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0 ) & (df["stage_continue_num"]==1) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療２回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==2) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療３回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==3) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療４回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==4) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["治療４回目以降",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]>4) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防１回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==1) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防２回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==2) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防３回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==3) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防４回目",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==4) & (df["active"]==0)).sum()
        df_dhda_breakaway.at["予防４回目以降",var] = ((df["responsible_dhda"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]>4) & (df["active"]==0)).sum()
        
        try:
            df_dhda_breakaway_per.at["合計",var] = df_dhda_breakaway.at["合計",var] / df_dhda_count.at["合計",var]
        except:
            df_dhda_breakaway_per.at["合計",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療",var] = df_dhda_breakaway.at["治療",var] / df_dhda_count.at["治療",var]
        except:
            df_dhda_breakaway_per.at["治療",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療１回目",var] = df_dhda_breakaway.at["治療１回目",var] / df_dhda_count.at["治療１回目",var]
        except:
            df_dhda_breakaway_per.at["治療１回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療２回目",var] = df_dhda_breakaway.at["治療２回目",var] / df_dhda_count.at["治療２回目",var]
        except:
            df_dhda_breakaway_per.at["治療２回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療３回目",var] = df_dhda_breakaway.at["治療３回目",var] / df_dhda_count.at["治療３回目",var]
        except:
            df_dhda_breakaway_per.at["治療３回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療４回目",var] = df_dhda_breakaway.at["治療４回目",var] / df_dhda_count.at["治療４回目",var]
        except:
            df_dhda_breakaway_per.at["治療４回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["治療４回目以降",var] = df_dhda_breakaway.at["治療４回目以降",var] / df_dhda_count.at["治療４回目以降",var]
        except:
            df_dhda_breakaway_per.at["治療４回目以降",var] = "-"
        try:
            df_dhda_breakaway_per.at["予防",var] = df_dhda_breakaway.at["予防",var] / df_dhda_count.at["予防",var]
        except:
            df_dhda_breakaway_per.at["予防",var] = "-"
        try:    
            df_dhda_breakaway_per.at["予防１回目",var] = df_dhda_breakaway.at["予防１回目",var] / df_dhda_count.at["予防１回目",var]
        except:
            df_dhda_breakaway_per.at["予防１回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["予防２回目",var] = df_dhda_breakaway.at["予防２回目",var] / df_dhda_count.at["予防２回目",var]
        except:
            df_dhda_breakaway_per.at["予防２回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["予防３回目",var] = df_dhda_breakaway.at["予防３回目",var] / df_dhda_count.at["予防３回目",var]
        except:
            df_dhda_breakaway_per.at["予防３回目",var]
        try:
            df_dhda_breakaway_per.at["予防４回目",var] = df_dhda_breakaway.at["予防４回目",var] / df_dhda_count.at["予防４回目",var]
        except:
            df_dhda_breakaway_per.at["予防４回目",var] = "-"
        try:
            df_dhda_breakaway_per.at["予防４回目以降",var] = df_dhda_breakaway.at["予防４回目以降",var] / df_dhda_count.at["予防４回目以降",var]
        except:
            df_dhda_breakaway_per.at["予防４回目以降",var] = "-"

    for var in dr:
        df_dr_count.at["合計",var] = (df["responsible_dr"]==var).sum()
        df_dr_count.at["治療",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0)).sum()
        df_dr_count.at["治療１回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==1)).sum()
        df_dr_count.at["治療２回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==2)).sum()
        df_dr_count.at["治療３回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==3)).sum()
        df_dr_count.at["治療４回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==4)).sum()
        df_dr_count.at["治療４回目以降",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]>4)).sum()
        df_dr_count.at["予防",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2)).sum()
        df_dr_count.at["予防１回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==1)).sum()
        df_dr_count.at["予防２回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==2)).sum()
        df_dr_count.at["予防３回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==3)).sum()
        df_dr_count.at["予防４回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==4)).sum()
        df_dr_count.at["予防４回目以降",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]>4)).sum()

        df_dr_breakaway.at["合計",var] = ((df["responsible_dr"]==var) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療１回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0 ) & (df["stage_continue_num"]==1) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療２回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==2) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療３回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==3) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療４回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]==4) & (df["active"]==0)).sum()
        df_dr_breakaway.at["治療４回目以降",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==0) & (df["stage_continue_num"]>4) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防１回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==1) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防２回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==2) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防３回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==3) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防４回目",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]==4) & (df["active"]==0)).sum()
        df_dr_breakaway.at["予防４回目以降",var] = ((df["responsible_dr"]==var) & (df["practice_type"]==2) & (df["stage_continue_num"]>4) & (df["active"]==0)).sum()
        
        try:
            df_dr_breakaway_per.at["合計",var] = df_dr_breakaway.at["合計",var] / df_dr_count.at["合計",var]
        except:
            df_dr_breakaway_per.at["合計",var] = "-"
        try:
            df_dr_breakaway_per.at["治療",var] = df_dr_breakaway.at["治療",var] / df_dr_count.at["治療",var]
        except:
            df_dr_breakaway_per.at["治療",var]
        try:
            df_dr_breakaway_per.at["治療１回目",var] = df_dr_breakaway.at["治療１回目",var] / df_dr_count.at["治療１回目",var]
        except:
            df_dr_breakaway_per.at["治療１回目",var] = "-"
        try:
            df_dr_breakaway_per.at["治療２回目",var] = df_dr_breakaway.at["治療２回目",var] / df_dr_count.at["治療２回目",var]
        except:
            df_dr_breakaway_per.at["治療２回目",var] = "-"
        try:
            df_dr_breakaway_per.at["治療３回目",var] = df_dr_breakaway.at["治療３回目",var] / df_dr_count.at["治療３回目",var]
        except:
            df_dr_breakaway_per.at["治療３回目",var] = "-"
        try:
            df_dr_breakaway_per.at["治療４回目",var] = df_dr_breakaway.at["治療４回目",var] / df_dr_count.at["治療４回目",var]
        except:
            df_dr_breakaway_per.at["治療４回目",var]
        try:
            df_dr_breakaway_per.at["治療４回目以降",var] = df_dr_breakaway.at["治療４回目以降",var] / df_dr_count.at["治療４回目以降",var]
        except:
            df_dr_breakaway_per.at["治療４回目以降",var] = "-"
        try:
            df_dr_breakaway_per.at["予防",var] = df_dr_breakaway.at["予防",var] / df_dr_count.at["予防",var]
        except:
            df_dr_breakaway_per.at["予防",var] = "-"
        try:
            df_dr_breakaway_per.at["予防１回目",var] = df_dr_breakaway.at["予防１回目",var] / df_dr_count.at["予防１回目",var]
        except:
            df_dr_breakaway_per.at["予防１回目",var] = "-"
        try:
            df_dr_breakaway_per.at["予防２回目",var] = df_dr_breakaway.at["予防２回目",var] / df_dr_count.at["予防２回目",var]
        except:
            df_dr_breakaway_per.at["予防２回目",var] = "-"
        try:
            df_dr_breakaway_per.at["予防３回目",var] = df_dr_breakaway.at["予防３回目",var] / df_dr_count.at["予防３回目",var]
        except:
            df_dr_breakaway_per.at["予防３回目",var] = "-"
        try:
            df_dr_breakaway_per.at["予防４回目",var] = df_dr_breakaway.at["予防４回目",var] / df_dr_count.at["予防４回目",var]
        except:
            df_dr_breakaway_per.at["予防４回目",var] = "-"
        try:
            df_dr_breakaway_per.at["予防４回目以降",var] = df_dr_breakaway.at["予防４回目以降",var] / df_dr_count.at["予防４回目以降",var]
        except:
            df_dr_breakaway_per.at["予防４回目以降",var] = "-"

    context = {
    'df_dhda_count' : df_dhda_count.to_html(), 
    'df_dhda_breakaway' : df_dhda_breakaway.to_html(), 
    'df_dhda_breakaway_per' : df_dhda_breakaway_per.to_html(),
    'df_dr_count' : df_dr_count.to_html(), 
    'df_dr_breakaway' : df_dr_breakaway.to_html(), 
    'df_dr_breakaway_per' : df_dr_breakaway_per.to_html()
    }

    return render(request, 'analysis_assess_responsible.html', context)

def assess_dh(request):
    month = request.POST["month"]
    form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
    df_booking = pd.read_csv(form_data)
    for ii in range(len(df_booking)):
        df_booking["予約日"][ii] = datetime.date(
            int(df_booking["予約日"][ii].split("/")[0]),
            int(df_booking["予約日"][ii].split("/")[1]),
            int(df_booking["予約日"][ii].split("/")[2])
        )

    ## 治療または予防の何回めかを各診療にラベル付する
    # DataFrameに診療情報を入れる
    records = PracticeRecord.objects.all()
    df = read_frame(records)
    
    # 名前順、日付順の優先順位で並び替える
    df = df.sort_values(["name","date"])
    df = df.reset_index(drop=True) # ソートしたdfでindexを付け直す
    df.loc[df["practice_type"] == 1,"practice_type"] = 0 # practice_typeが"1"のものを"0"に変換する

    # 治療・予防何回目かを判定    
    max_date = datetime.date(int(str(month)[:4]),int(str(month)[4:]),1)-datetime.timedelta(days=1)
    stage_num_list = []
    active_list = []    
    before_name = "reset name"
    for ii in range(len(df)):
        name = df["name"][ii]
        if ii != len(df)-1:
            if df["name"][ii+1] == name:
                active_list.append(1)
            else:
                if (max_date - df["date"][ii]).days <= 90:
                    active_list.append(1) # アクティブ
                elif 90 < (max_date - df["date"][ii]).days <= 180:
                    active_list.append(2) # 中断
                else:
                    active_list.append(0) # 離脱
        else:
            if (max_date - df["date"][ii]).days <= 90:
                active_list.append(1) # アクティブ
            elif 90 < (max_date - df["date"][ii]).days <= 180:
                active_list.append(2) # 中断
            else:
                active_list.append(0) # 離脱

        if name != before_name:
            before_name = copy.copy(name)
            stage_num_list.append(1)
            before_type = df["practice_type"][ii]
        else:
            if before_type == df["practice_type"][ii]:
                stage_num_list.append(stage_num_list[ii-1]+1)
            else:
                stage_num_list.append(1)
                before_type = df["practice_type"][ii]
            
    df["stage_continue_num"] = stage_num_list
    df["active"] = active_list

    # 該当月のデータを集計
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    idx = month_list.index(int(month))
    index = ["予約済み(予防・治療)","対応患者数","対応患者数(治療)","対応患者数(予防)","キャンセル数(予防・治療)","キャンセル率(予防・治療)","無断","当日","通常","中断患者数（予防）","中断患者率（予防）","離脱患者数(予防)","離脱患者率(予防)","点数","点数(治療)","点数(予防)"]
    df_result = pd.DataFrame(index=index)

    name = request.POST["name"]

    for ii in range(idx-12,idx+5):
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)
        df_month = df[(df["date"]>=start_date) & (df["date"]<=end_date)]

        records = []
        
        #予約済
        records.append(((df_booking["予約日"]>=start_date) & (df_booking["予約日"]<=end_date) & (df_booking["衛生士・助手"]==name)).sum())
        #対応患者数
        records.append(((df_month["responsible_dhda"]==name)).sum())
        #対応患者数(治療)
        records.append(((df_month["responsible_dhda"]==name) & (df_month["practice_type"]==0)).sum())
        #対応患者数(予防)
        records.append(((df_month["responsible_dhda"]==name) & (df_month["practice_type"]==2)).sum())
        #キャンセル数
        records.append("-")
        #キャンセル率
        records.append("-")
        #無断
        records.append("-")
        #当日
        records.append("-")
        #通常
        records.append("-")
        #中断患者数
        records.append(((df_month["responsible_dhda"]==name) & (df_month["practice_type"]==2) & (df_month["active"]==2)).sum())
        #中断患者率
        records.append(records[-1]/records[3])
        #離脱患者数
        records.append(((df_month["responsible_dhda"]==name) & (df_month["practice_type"]==2) & (df_month["active"]==0)).sum())
        #離脱患者率
        records.append(records[-1]/records[3])
        #点数
        records.append(df_month[df_month["responsible_dhda"]==name].score.sum())
        #点数(治療)
        records.append(df_month[(df_month["responsible_dhda"]==name) & (df_month["practice_type"]==0)].score.sum())
        #点数(予防)
        records.append(df_month[(df_month["responsible_dhda"]==name) & (df_month["practice_type"]==2)].score.sum())

        df_result[month_list[ii]] = records
    print(df_result)

    context = {
    'df_result' : df_result.to_html(), 
    'name' : name
    }

    return render(request, 'assess_dh.html', context)

def import_cancel_csv(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        data_row = csv.reader(form_data)
        df = pd.read_csv(form_data)

        create_list = []
        for ii in range(len(df)):            
            create_list.append(CancelList(
                calte_num = df["カルテ番号"][ii],
                name = df["患者名"][ii],
                booking_num = df["予約件数"][ii],
                cancel_num = df["キャンセル件数"][ii],
                without_permission = df["無断"][ii],
                appointed_day = df["当日"][ii],
                common = df["通常"][ii],
                cancel_per = df["キャンセル率"][ii],
            ))
        
        CancelList.objects.bulk_create(create_list)
        return render(request, 'index.html')

def analysis_monthly_patient_v2(request):
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)

    master = TableBasic.objects.all()
    master_df = read_frame(master)
    records = PracticeRecord.objects.all()
    df = read_frame(records)

    master_df["word_check"] = master_df.practice_bassic_name.map(lambda word: "訪問" in word)

    visit_codes_df = master_df.loc[master_df["word_check"] == True]
    visit_codes = set(visit_codes_df.dental_practice_code)
    visit_add = set(visit_codes_df.add_code)

    df["all_code"] = (df.dental_practice_initial_medical_examination + \
                    df.dental_practice_second_medical_examination + \
                    df.dental_practice_management_rehab + \
                    df.dental_practice_medication_injection + \
                    df.dental_practice_xray_examination + \
                    df.dental_practice_procedures_surgeries1 + \
                    df.dental_practice_procedures_surgeries2 + \
                    df.dental_practice_procedures_surgeries3 + \
                    df.dental_practice_procedures_surgeries_other + \
                    df.dental_practice_anesthesia + \
                    df.dental_practice_restoration_prosthetics1 + \
                    df.dental_practice_restoration_prosthetics2 + \
                    df.dental_practice_restoration_prosthetics3 + \
                    df.dental_practice_restoration_prosthetics_other + \
                    df.dental_practice_other + \
                    df.dental_practice_summary).map(lambda code:set(code.split(",")))
    
    df["all_add"] = (df.dental_practice_initial_medical_examination_add + \
                    df.dental_practice_second_medical_examination_add + \
                    df.dental_practice_management_rehab_add + \
                    df.dental_practice_medication_injection_add + \
                    df.dental_practice_xray_examination_add + \
                    df.dental_practice_procedures_surgeries1_add + \
                    df.dental_practice_procedures_surgeries2_add + \
                    df.dental_practice_procedures_surgeries3_add + \
                    df.dental_practice_procedures_surgeries_other_add + \
                    df.dental_practice_anesthesia_add + \
                    df.dental_practice_restoration_prosthetics1_add + \
                    df.dental_practice_restoration_prosthetics2_add + \
                    df.dental_practice_restoration_prosthetics3_add + \
                    df.dental_practice_restoration_prosthetics_other_add + \
                    df.dental_practice_other_add + \
                    df.dental_practice_summary_add).map(lambda code:set(code.split(",")))
    df["visit_check_code"] = df.all_code.map(lambda code: code.isdisjoint(visit_codes))
    df["visit_check_add"] = df.all_add.map(lambda code: code.isdisjoint(visit_add))

    df_visit = df.loc[(df.visit_check_code == False) | (df.visit_check_add == False)].loc[:,["all_code","all_add","practice_type","score","date"]].reset_index(drop=True)

    df = pd.DataFrame(index=["回数","点数","平均点数"])
    for ii in range(start_idx,end_idx+1):
        month_start = str(month_list[ii])
        month_end = str(month_list[ii+1])
        start_date = datetime.date(int(month_start[:4]),int(month_start[4:]),1)
        end_date = datetime.date(int(month_end[:4]),int(month_end[4:]),1)-datetime.timedelta(days=1)

        month_df = df_visit.loc[(df_visit.date >= start_date) & (df_visit.date <= end_date)]
        counts = len(month_df)
        score = month_df.score.sum()
        score_avg = score/counts
        df[month_list[ii]] = [counts,score,score_avg]
    
    context = {
    'df' : df.to_html()
    }

    return render(request, 'analysis_monthly_patient_v2.html', context)

def monthly_score(request):
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)
    
    columns = []

    score = []
    score_medical = []
    score_prevent = []
    count = []
    count_medical = []
    count_prevent = []
    price = []
    price_medical = []
    price_prevent = []

    for ii in range(start_idx,end_idx+1):
        # 開始年月日と終了年月日を取得
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)
        # 年月をカラムとして追加
        columns.append(f'{start_date.year}/{start_date.month}')
        # 点数
        score.append(PracticeRecord.objects.filter(date__range=(start_date,end_date)).aggregate(score=Sum('score'))['score'])
        score_medical.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1).aggregate(score=Sum('score'))['score'])
        score_prevent.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).aggregate(score=Sum('score'))['score'])
        # 回数
        count.append(PracticeRecord.objects.filter(date__range=(start_date,end_date)).count())
        count_medical.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1).count())
        count_prevent.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).count())
        # 単価
        price.append(
            PracticeRecord.objects.filter(date__range=(start_date,end_date)).aggregate(score=Sum('score'))['score']/PracticeRecord.objects.filter(date__range=(start_date,end_date)).count()
            )
        price_medical.append(
            PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1).aggregate(score=Sum('score'))['score']/PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type__lte=1).count()
            )
        price_prevent.append(
            PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).aggregate(score=Sum('score'))['score']/PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).count()
            )

    # DataFrame化する
    idx = ['点数','治療','予防','来院回数','治療','予防','単価','治療','予防']
    df = pd.DataFrame([score,score_medical,score_prevent,count,count_medical,count_prevent,price,price_medical,price_prevent],index=idx, columns=columns)

    # 平均と比率を追加
    df.insert(0, '平均', list(df.mean(axis=1)))
    df.insert(
        1,
        '比率'
        ,[
        '-',
        df.iat[1,0]/df.iat[0,0],
        df.iat[2,0]/df.iat[0,0],
        '-',
        df.iat[4,0]/df.iat[3,0],
        df.iat[5,0]/df.iat[3,0],
        '-',
        '-',
        '-'
        ]
        )
    print(df)
    context = {
    'monthly_score' : df.to_html(), 
    }

    return render(request, 'monthly_score.html', context)

def insurance_addition_simulation(request):
    # SC/SRPとSPTに該当する診療コードをリスト化
    sc_srp = [309004810,309004970,309005010,309005110,309005210]
    spt = [309014710,309014810,309005710,309020370]
    sets = set()

    # 入力を取得し、開始年月と終了年月を取得
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)

    # 必要なインデックスを設定
    prevent_score_list = []
    sc_srp_score_list = []
    spt_score_list = []
    other_score_list = []
    prevent_count_list = []
    sc_srp_count_list = []
    spt_count_list = []
    other_count_list = []
    prevent_price_list = []
    sc_srp_price_list = []
    spt_price_list = []
    other_price_list = []
    
    # カラムに入れるリスト
    columns = []

    # 算定内容Top 5をSC/SRPとSPTで集計する
    practice_codes_spt = []
    practice_codes_sc_srp = []

    for ii in range(start_idx,end_idx+1):
        # 開始年月日と終了年月日を取得
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)
        columns.append(f'{start_date.year}/{start_date.month}')

        # 予防点数
        prevent_score_list.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).aggregate(score = Sum('score'))['score'])
        # 予防回数
        prevent_count_list.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).count())
        # 予防単価
        prevent_price_list.append(PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).aggregate(score = Sum('score'))['score']/PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2).count())

        # 予防レコードを取得
        prevent_treatment = PracticeRecord.objects.filter(date__range=(start_date,end_date),practice_type=2)

        # 初期値を設定
        sc_srp_score = 0
        spt_score = 0
        sc_srp_count = 0
        spt_count = 0
        
        # 診療ごとにSC/SRPかSPTかその他かを判定し、集計する
        for treat in prevent_treatment:
            flag_sc_srp = 0
            flag_spt = 0

            # 診療コードをリスト化
            treat_list = []
            treat_list += list(map(int,treat.dental_practice_initial_medical_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_second_medical_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_management_rehab.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_medication_injection.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_xray_examination.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_procedures_surgeries_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_anesthesia.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics1.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics2.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics3.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_restoration_prosthetics_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_other.split(",")[:-1]))
            treat_list += list(map(int,treat.dental_practice_summary.split(",")[:-1]))

            # 診療加算コードをリスト化
            treat_add_list =[]
            treat_add_list += list(map(str,treat.dental_practice_initial_medical_examination_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_second_medical_examination_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_management_rehab_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_medication_injection_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_xray_examination_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_procedures_surgeries1_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_procedures_surgeries2_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_procedures_surgeries3_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_procedures_surgeries_other_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_anesthesia_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_restoration_prosthetics1_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_restoration_prosthetics2_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_restoration_prosthetics3_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_restoration_prosthetics_other_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_other_add.split(",")[:-1]))
            treat_add_list += list(map(str,treat.dental_practice_summary_add.split(",")[:-1]))
            
            # 診療コードから名称に変換
            treat_name_list = []
            for var in treat_list:
                try:
                    if var == 309016410:
                        treat_name_list.append('SPT2(20歯以上)')
                    elif var == 309016310:
                        treat_name_list.append('SPT2(10歯以上20歯未満)')
                    elif var == 309016210:
                        treat_name_list.append('SPT2(1歯以上10歯未満)')
                    elif var == 309010510:
                        treat_name_list.append('P基処')
                    else:
                        treat_name_list.append(TableBasic.objects.get(dental_practice_code=var).practice_bassic_name)
                except:
                    sets.add(var)
            for var in treat_add_list:
                try:
                    if var == 'CA154':
                        treat_name_list.append('乳幼児感染予防策加算（新型コロナウイルス感染症に係る診療報酬上の臨時的な取扱い）')
                    else:
                        treat_name_list.append(TableBasic.objects.get(add_code=var).practice_bassic_name)
                except:
                    sets.add(var)
            
            treat_name_list.sort()

            # SC/SRPかSPTであればフラグ
            for ii in treat_list:
                if ii in sc_srp:
                    flag_sc_srp = 1
                elif ii in spt:
                    flag_spt = 1

            # SC/SRPかSPTであれば加算
            if flag_sc_srp == 1:
                sc_srp_count += 1
                sc_srp_score += treat.score
                practice_codes_sc_srp.append(str(treat_name_list))

            if flag_spt == 1:
                spt_count += 1
                spt_score += treat.score
                practice_codes_spt.append(str(treat_name_list))        
        
        # SC/SRP点数
        sc_srp_score_list.append(sc_srp_score)
        # SC/SRP回数
        sc_srp_count_list.append(sc_srp_count)
        # SC/SRP単価
        try:
            sc_srp_price_list.append(sc_srp_score/sc_srp_count)
        except:
            sc_srp_price_list.append(0)
        # SPT点数
        spt_score_list.append(spt_score)
        # SPT回数
        spt_count_list.append(spt_count)
        # SPT単価
        try:
            spt_price_list.append(spt_score/spt_count)
        except:
            spt_price_list.append(0)
        # その他点数
        other_score_list.append(prevent_score_list[-1]-(sc_srp_score+spt_score))
        # その他回数
        other_count_list.append(prevent_count_list[-1]-(sc_srp_count+spt_count))
        # その他単価
        try:
            other_price_list.append(other_score_list[-1]/other_count_list[-1])
        except:
            other_price_list.append(0)
    print('========================')
    print('this code is not exisited in master database.')
    print(sets)
    print('========================')

    # SC/SRPとSPTの算定内容における出現頻度Top5を取得
    c_sc_srp = collections.Counter(practice_codes_sc_srp)
    c_spt = collections.Counter(practice_codes_spt)
    try:
        content_sc_srp = [c_sc_srp.most_common()[0][0],c_sc_srp.most_common()[1][0],c_sc_srp.most_common()[2][0],c_sc_srp.most_common()[3][0],c_sc_srp.most_common()[4][0]]
        counts_sc_srp = [c_sc_srp.most_common()[0][1],c_sc_srp.most_common()[1][1],c_sc_srp.most_common()[2][1],c_sc_srp.most_common()[3][1],c_sc_srp.most_common()[4][1]]
    except:
        content_sc_srp = [None,None,None,None,None]
        counts_sc_srp = [None,None,None,None,None]
    try:
        content_spt = [c_spt.most_common()[0][0],c_spt.most_common()[1][0],c_spt.most_common()[2][0],c_spt.most_common()[3][0],c_spt.most_common()[4][0]]
        counts_spt = [c_spt.most_common()[0][1],c_spt.most_common()[1][1],c_spt.most_common()[2][1],c_spt.most_common()[3][1],c_spt.most_common()[4][1]]
    except:
        content_spt = [None,None,None,None,None]
        counts_spt = [None,None,None,None,None]

    df_sc_srp = pd.DataFrame(index=['No.1','No.2','No.3','No.4','No.5'])
    df_sc_srp['算定内容'] = content_sc_srp
    df_sc_srp['回数'] = counts_sc_srp
    df_spt = pd.DataFrame(index=['No.1','No.2','No.3','No.4','No.5'])
    df_spt['算定内容'] = content_spt
    df_spt['回数'] = counts_spt

    idx = ['予防点数','SC/SRP','SPT','その他','予防回数','SC/SRP','SPT','その他','予防単価','SC/SRP','SPT','その他']
    df = pd.DataFrame([
        prevent_score_list,
        sc_srp_score_list,
        spt_score_list,
        other_score_list,
        prevent_count_list,
        sc_srp_count_list,
        spt_count_list,
        other_count_list,
        prevent_price_list,
        sc_srp_price_list,
        spt_price_list,
        other_price_list
        ],
        index=idx, columns=columns)
    
    # 平均と比率を追加
    df.insert(0, '平均', list(df.mean(axis=1)))
    df.insert(
        1,
        '比率'
        ,[
        '-',
        df.iat[1,0]/df.iat[0,0],
        df.iat[2,0]/df.iat[0,0],
        df.iat[3,0]/df.iat[0,0],
        '-',
        df.iat[5,0]/df.iat[4,0],
        df.iat[6,0]/df.iat[4,0],
        df.iat[7,0]/df.iat[4,0],
        '-',
        '-',
        '-',
        '-'
        ]
        )

    context = {
    'df' : df.to_html(), 
    'df_sc_srp' : df_sc_srp.to_html(), 
    'df_spt' : df_spt.to_html()
    }

    return render(request, 'insurance_addition_simulation.html', context)

def import_apotool_responsible_data(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        df = pd.read_csv(form_data)
        date_list = list(df.date)
        date_list_new = []
        for ii in date_list:
            string = ii.split('-')
            date_list_new.append(datetime.date(int(string[0]),int(string[1]),int(string[2])))
        df['date'] = date_list_new

        # DHの名前とDrの名前をリスト化
        dh_list = ['DH岡本','DH稲川','DH小沢','DH古川','DH西山','DH村野','DH山原','DH畑田']
        dr_list = ['院長','Dr藤原','Dr竹原','Dr南原']

        # 名前がDBとアポツールで違うので、一旦DataFrameにして最後名前だけDBを更新する
        df_record = read_frame(PracticeRecord.objects.all())
        # 名前と年月日を取得する
        names = list(df_record['name'])
        dates = list(df_record['date'])
        # 名字と名前の間の空欄を消す
        names_new = [x.replace('　','') for x in names]

        # 担当者リストを作る
        res_1_list = []
        res_2_list = []

        for ii in range(len(names)):
            # DB側の名前と年月日取得
            name = names_new[ii]
            date = dates[ii]

            # Apotoolから名前と年月日でインデックスを検索する
            try:
                res_1 = df.loc[(df['Name'] == name) & (df['date'] == date),'res_1'].item()
                res_2 = df.loc[(df['Name'] == name) & (df['date'] == date),'res_2'].item()
            except:
                res_1 = '-'
                res_2 = '-'
            
            if res_1 in dh_list:
                dh = res_1
                print(1)
            elif res_1 in dr_list:
                dr = res_1
                print(2)
            elif res_2 in dh_list:
                dh = res_2
                print(3)
            elif res_2 in dr_list:
                dr = res_2
                print(4)
            else:
                dh = None
                dr = None
                   
            try:
                record = PracticeRecord.objects.get(name=names[ii],date=date)
                record.responsible_dr = dr
                record.responsible_dhda = dh
                record.save()
            except:
                pass
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def assess_responsible(request):
    start = int(request.GET["start"])
    dh_name = request.GET["name"]

    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)

    # 結果を入れるDataFrame
    index = ['次回予約済み(治療・予防)','対応患者数','治療 患者数','予防 患者数','キャンセル数(治療・予防)','キャンセル率(治療・予防) %','中断患者数(予防)','中断患者率(予防) %','離脱患者数(予防)','離脱患者率(予防) %','点数','点数(治療)','点数(予防)']
    df_result = pd.DataFrame(index=index)

    # 中断と離脱をフラグ付けする
    # 患者の最終来院が最新日から180日以上経過＝離脱,90日以上180日未満経過＝中断
    df_all = read_frame(PracticeRecord.objects.all())
    df_all = df_all.sort_values(["name","date"])
    df_all = df_all.reset_index(drop=True) # ソートしたdfでindexを付け直す

    break_flag = [] # 継続：0, 不明：1, 中断：2, 離脱:3
    max_date = datetime.date(int(str(month_list[start_idx])[:4]),int(str(month_list[start_idx])[4:]),1)
    for ii in range(len(df_all)):
        if ii != len(df_all)-1:
            if (df_all.name[ii] != df_all.name[ii+1]):
                if (max_date-df_all.date[ii]).days >= 180:
                    break_flag.append(3)
                elif (max_date-df_all.date[ii]).days >= 90:
                    break_flag.append(2)
                else:
                    break_flag.append(1)
            else:
                break_flag.append(0)
        else:
            if (max_date-df_all.date[ii]).days >= 180:
                break_flag.append(3)
            elif (max_date-df_all.date[ii]).days >= 90:
                break_flag.append(2)
            else:
                break_flag.append(1)
    df_all['break_flag'] = break_flag

    # 出力する衛生士のDataFrame
    df_res = df_all.loc[df_all['responsible_dhda'] == dh_name]

    for ii in range(start_idx-12,start_idx):
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)

        colomn = str(start_date.year)+'/'+str(start_date.month)

        data = []
        # 次回予約済み(治療・予防)
        data.append(0)
        # 対応患者数
        data.append(((df_res['date'] >= start_date) & (df_res['date'] <= end_date)).sum())
        # 治療患者数
        data.append(((df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] <= 1)).sum())
        # 予防患者数
        data.append(((df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] == 2)).sum())
        # キャンセル数
        data.append(0)
        # キャンセル率
        data.append(0)
        # 中断患者数
        data.append(((df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] == 2) & (df_res['break_flag'] == 2)).sum())
        # 中断患者率
        try:
            data.append(data[-1]/data[-4])
        except:
            data.append(0)
        # 離脱患者数
        data.append(((df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] == 2) & (df_res['break_flag'] == 3)).sum())
        # 離脱患者率
        try:
            data.append(data[-1]/data[-6])
        except:
            data.append(0)
        # 点数
        data.append(df_res[(df_res['date'] >= start_date) & (df_res['date'] <= end_date)]['score'].sum())
        # 点数(治療)
        data.append(df_res[(df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] <= 1)]['score'].sum())
        # 点数(予防)
        data.append(df_res[(df_res['date'] >= start_date) & (df_res['date'] <= end_date) & (df_res['practice_type'] == 2)]['score'].sum())
        df_result[colomn] = data
    
    context = {
    'df' : df_result.to_html(), 
    }
    print(max_date)

    return render(request, 'assess_responsible.html', context)

def assess_responsible_cancel(request):
    if 'csv' in request.FILES:
        print(request.POST["start"])
        start = int(request.POST["start"])
        dh_name = request.POST["name"]
        # キャンセルデータの入ったcsv
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        data_row = csv.reader(form_data)
        df = pd.read_csv(form_data)

        responsible_list = ['DH岡本','DH稲川','DH小沢','DH古川','DH西山','DH村野','DH山原','DH畑田','院長','Dr藤原','Dr竹原','Dr南原']

        # 日付をdatetimeに変換
        date_list = list(df.date)
        for ii in range(len(date_list)):
            date_list[ii] = datetime.date(int(date_list[ii].split('-')[0]),int(date_list[ii].split('-')[1]),int(date_list[ii].split('-')[2]))
        df['date'] = date_list
        # 衛生士を分離 入力した衛生士の場合1, それ以外0
        responsible_dh = []
        for ii in range(len(df)):
            if df.res_1[ii] in responsible_list:
                if df.res_1[ii] == dh_name:
                    responsible_dh.append(1)
                else:
                    responsible_dh.append(0)
            elif df.res_2[ii] == dh_name:
                responsible_dh.append(1)
            else:
                responsible_dh.append(0)
        df['responsible_dh'] = responsible_dh

        month_list = [
            202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
            202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
            202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
            202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
        ]
        start_idx = month_list.index(start)

        df_result = pd.DataFrame(index=['キャンセル数'])

        for ii in range(start_idx-12,start_idx):
            start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
            end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)

            colomn = str(start_date.year)+'/'+str(start_date.month)

            df_result[colomn] = [((df['date'] >= start_date) & (df['date'] <= end_date) & (df['responsible_dh'] == 1)).sum()]

        context = {
        'df' : df_result.to_html(), 
        }
        return render(request, 'assess_responsible_cancel.html', context)
    else:
        return render(request, 'index.html')

def assess_responsible_reserve(request):
    if 'csv' in request.FILES:
        start = int(request.POST["start"])
        dh_name = request.POST["name"]
        # キャンセルデータの入ったcsv
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='shift_jis')
        data_row = csv.reader(form_data)
        df = pd.read_csv(form_data)

        responsible_list = ['DH岡本','DH稲川','DH小沢','DH古川','DH西山','DH村野','DH山原','DH畑田','院長','Dr藤原','Dr竹原','Dr南原']

        # 日付をdatetimeに変換
        date_list = list(df.date)
        for ii in range(len(date_list)):
            date_list[ii] = datetime.date(int(date_list[ii].split('-')[0]),int(date_list[ii].split('-')[1]),int(date_list[ii].split('-')[2]))
        df['date'] = date_list
        # 衛生士を分離 入力した衛生士の場合1, それ以外0
        responsible_dh = []
        for ii in range(len(df)):
            if df.res_1[ii] in responsible_list:
                if df.res_1[ii] == dh_name:
                    responsible_dh.append(1)
                else:
                    responsible_dh.append(0)
            elif df.res_2[ii] == dh_name:
                responsible_dh.append(1)
            else:
                responsible_dh.append(0)
        df['responsible_dh'] = responsible_dh

        month_list = [
            202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
            202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
            202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
            202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
        ]
        start_idx = month_list.index(start)

        df_result = pd.DataFrame(index=['予約数'])

        for ii in range(start_idx,start_idx+5):
            start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
            end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)

            colomn = str(start_date.year)+'/'+str(start_date.month)

            df_result[colomn] = [((df['date'] >= start_date) & (df['date'] <= end_date) & (df['responsible_dh'] == 1)).sum()]
        context = {
        'df' : df_result.to_html(), 
        }
        return render(request, 'assess_responsible_reserve.html', context)
    else:
        return render(request, 'index.html')

def analysis_monthly_patient_stage_v2(request):
    ## 治療または予防の何回めかを各診療にラベル付する
    # DataFrameに診療情報を入れる
    records = PracticeRecord.objects.all()
    df = read_frame(records)
    
    # 名前順、日付順の優先順位で並び替える
    df = df.sort_values(["name","date"])
    df = df.reset_index(drop=True) # ソートしたdfでindexを付け直す
    df.loc[df["practice_type"] == 1,"practice_type"] = 0 # practice_typeが"1"のものを"0"に変換する

    # 治療・予防何回目かを判定
    max_date = df["date"].max() #データの最終日を取得
    stage_num_list = []
    active_list = []    
    before_name = "reset name"
    for ii in range(len(df)):
        name = df["name"][ii]
        if ii != len(df)-1:
            if df["name"][ii+1] == name:
                active_list.append(1)
            else:
                if (max_date - df["date"][ii]).days <= 180:
                    active_list.append(1)
                else:
                    active_list.append(0)
        else:
            if (max_date - df["date"][ii]).days <= 180:
                active_list.append(1)
            else:
                active_list.append(0)

        if name != before_name:
            before_name = copy.copy(name)
            stage_num_list.append(1)
            before_type = df["practice_type"][ii]
        else:
            if before_type == df["practice_type"][ii]:
                stage_num_list.append(stage_num_list[ii-1]+1)
            else:
                stage_num_list.append(1)
                before_type = df["practice_type"][ii]
            
    df["stage_continue_num"] = stage_num_list
    df["active"] = active_list

    # 治療終了フラグをつける
    finish_flag = []
    for ii in range(len(df)):
        name = df["name"][ii]
        practice_type = df['practice_type'][ii]
        if ii == len(df)-1:
            finish_flag.append(0)
        else:
            if df['name'][ii+1] == name:
                if df['practice_type'][ii] <= 1:
                    if df['practice_type'][ii+1] == 2:
                        finish_flag.append(1)
                    else:
                        finish_flag.append(0)
                else:
                    finish_flag.append(0)
            else:
                if df['practice_type'][ii] <= 1:
                    finish_flag.append(1)
                else:
                    finish_flag.append(0)
    df["finish_flag"] = finish_flag

    ## 月次のステージ集計する
    # 入力を受け取り何年何月から何月までを表示するかを取得
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    month_list = [
        202005,202006,202007,202008,202009,202010,202011,202012,202101,202102,202103,202104,
        202105,202106,202107,202108,202109,202110,202111,202112,202201,202202,202203,202204,
        202205,202206,202207,202208,202209,202210,202211,202212,202301,202302,202303,202304,
        202305,202306,202307,202308,202309,202310,202311,202312,202401,202402,202403,202404,
    ]
    start_idx = month_list.index(start)
    end_idx = month_list.index(end)

    df_result_all = pd.DataFrame(index=["合計","治療","治療継続","治療終了","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_result_break = pd.DataFrame(index=["合計","治療","治療継続","治療終了","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])
    df_result_break_per = pd.DataFrame(index=["合計","治療","治療継続","治療終了","予防","予防１回目","予防２回目","予防３回目","予防４回目","予防４回目以降"])

    for ii in range(start_idx,end_idx+1):
        # 該当月のみを抽出
        start_date = datetime.date(int(str(month_list[ii])[:4]),int(str(month_list[ii])[4:]),1)
        end_date = datetime.date(int(str(month_list[ii+1])[:4]),int(str(month_list[ii+1])[4:]),1)-datetime.timedelta(days=1)        
        monthly_df = df[(df["date"]>=start_date) & (df["date"]<=end_date)]

        # 全体の人数と離脱
        all_patient = len(monthly_df)
        all_break = (monthly_df["active"]==0).sum()
        all_break_per = str(round(all_break*100/all_patient,2))+" %"

        # 治療の全体人数のカウント
        medic_all = ((monthly_df["practice_type"]==0)).sum()
        medic_continue = ((monthly_df["practice_type"]==0) & (monthly_df["finish_flag"]==0)).sum()
        medic_finish = ((monthly_df["practice_type"]==0) & (monthly_df["finish_flag"]==1)).sum()

        # 予防の全体人数のカウント
        prevent_1_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==1)).sum()
        prevent_2_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==2)).sum()
        prevent_3_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==3)).sum()
        prevent_4_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==4)).sum()
        prevent_over_all = ((monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]>4)).sum()
        prevent_all_sum = prevent_1_all + prevent_2_all + prevent_3_all + prevent_4_all + prevent_over_all    

        # 治療の離脱人数のカウント
        medic_break_all = ((monthly_df["practice_type"]==0) & (monthly_df["active"]==0)).sum()
        medic_break_continue = ((monthly_df["practice_type"]==0) & (monthly_df["active"]==0) & (monthly_df["finish_flag"]==0)).sum()
        medic_break_finish = ((monthly_df["practice_type"]==0) & (monthly_df["active"]==0) & (monthly_df["finish_flag"]==1)).sum()

        # 予防の離脱人数のカウント
        prevent_1_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==1)).sum()
        prevent_2_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==2)).sum()
        prevent_3_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==3)).sum()
        prevent_4_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]==4)).sum()
        prevent_over_break = ((monthly_df["active"]==0) & (monthly_df["practice_type"]==2) & (monthly_df["stage_continue_num"]>4)).sum() 
        prevent_break_sum = prevent_1_break + prevent_2_break + prevent_3_break + prevent_4_break + prevent_over_break       

        # 予防の離脱率        
        prevent_1_break_per = str(round(prevent_1_break*100/prevent_1_all,2))+" %"                
        prevent_2_break_per = str(round(prevent_2_break*100/prevent_2_all,2))+" %"                
        prevent_3_break_per = str(round(prevent_3_break*100/prevent_3_all,2))+" %"                
        prevent_4_break_per = str(round(prevent_4_break*100/prevent_4_all,2))+" %"                
        prevent_over_break_per = str(round(prevent_over_break*100/prevent_over_all,2))+" %"   
        prevent_break_per_sum = str(round(prevent_break_sum/prevent_all_sum,2))+" %"    

        # 治療の離脱率
        medic_break_per = str(round(medic_break_all*100/medic_all,2))+" %"
        medic_continue_break_per = str(round(medic_break_continue*100/medic_continue,2))+" %"
        medic_finish_break_per = str(round(medic_break_finish*100/medic_finish,2))+" %"

        append_list_all = [all_patient,medic_all,medic_continue,medic_finish,prevent_all_sum,prevent_1_all,prevent_2_all,prevent_3_all,prevent_4_all,prevent_over_all]
        append_list_break = [all_break,medic_break_all,medic_break_continue,medic_break_finish,prevent_break_sum,prevent_1_break,prevent_2_break,prevent_3_break,prevent_4_break,prevent_over_break]
        append_list_break_per = [all_break_per,medic_break_per,medic_continue_break_per,medic_finish_break_per,prevent_break_per_sum,prevent_1_break_per,prevent_2_break_per,prevent_3_break_per,prevent_4_break_per,prevent_over_break_per]
        
        df_result_all[month_list[ii]] = append_list_all
        df_result_break[month_list[ii]] = append_list_break
        df_result_break_per[month_list[ii]] = append_list_break_per
    
    context = {
    'all' : df_result_all.to_html(), 
    'break' : df_result_break.to_html(), 
    'break_per' : df_result_break_per.to_html()
    }

    return render(request, 'analysis_monthly_patient_stage_v2.html', context)

def test(request):
    df = read_frame(RecordDentalPractice.objects.all())
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="patient_practice_data.csv"'
    df.to_csv(response)
    return response