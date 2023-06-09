# Generated by Django 4.1.5 on 2023-03-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_preventdentalpractice"),
    ]

    operations = [
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_anesthesia_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_麻酔",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_initial_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_初診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_management_rehab_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_管理・リハ",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_medication_injection_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_投薬・注射",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_全体のその他",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_procedures_surgeries1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_処置・手術1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_procedures_surgeries2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_処置・手術2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_procedures_surgeries3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_処置・手術3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_procedures_surgeries_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_処置・手術（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_restoration_prosthetics1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_修復・補綴1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_restoration_prosthetics2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_修復・補綴2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_restoration_prosthetics3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_修復・補綴3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_restoration_prosthetics_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_修復・補綴（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_second_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_再診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_summary_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_摘要",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="dental_practice_xray_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="歯科診療行為_X線検査",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_anesthesia_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_麻酔",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_initial_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_初診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_management_rehab_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_管理・リハ",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_medication_injection_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_投薬・注射",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_全体のその他",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_procedures_surgeries1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_処置・手術1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_procedures_surgeries2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_処置・手術2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_procedures_surgeries3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_処置・手術3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_procedures_surgeries_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_処置・手術（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_restoration_prosthetics1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_修復・補綴1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_restoration_prosthetics2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_修復・補綴2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_restoration_prosthetics3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_修復・補綴3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_restoration_prosthetics_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_修復・補綴（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_second_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_再診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_summary_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_摘要",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="drug_xray_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="医薬品_X線検査",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="score",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="点数"
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_anesthesia_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_麻酔",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_initial_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_初診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_management_rehab_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_管理・リハ",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_medication_injection_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_投薬・注射",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_全体のその他",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_procedures_surgeries1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_処置・手術1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_procedures_surgeries2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_処置・手術2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_procedures_surgeries3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_処置・手術3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_procedures_surgeries_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_処置・手術（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_restoration_prosthetics1_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_修復・補綴1",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_restoration_prosthetics2_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_修復・補綴2",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_restoration_prosthetics3_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_修復・補綴3",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_restoration_prosthetics_other_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_修復・補綴（その他）",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_second_medical_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_再診",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_summary_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_摘要",
            ),
        ),
        migrations.AddField(
            model_name="practicerecord",
            name="specific_equipment_xray_examination_score",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="特定機材_X線検査",
            ),
        ),
    ]
