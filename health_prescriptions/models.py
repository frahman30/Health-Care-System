from django.db import models

# Create your models here.
class gnuhealth_prescription_order(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    healthprof = models.IntegerField()
    notes = models.CharField(max_length=100)
    patient = models.IntegerField()
    pharmacy = models.IntegerField()
    pregnancy_warning = models.BooleanField()
    prescription_date = models.DateTimeField()
    prescription_id = models.CharField(max_length=100)
    prescription_warning_ack = models.BooleanField()
    state = models.CharField(max_length=100)
    user_id = models.IntegerField()
    digital_signature = models.CharField(max_length=100)
    document_digest = models.CharField(max_length=100)
    serializer = models.CharField(max_length=100)
    service = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_prescription_order'

class gnuhealth_prescription_line(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    add_to_history = models.BooleanField()
    admin_times = models.CharField(max_length=100)
    allow_substitution = models.BooleanField()
    common_dosage = models.IntegerField()
    dose = models.IntegerField()
    dose_unit = models.IntegerField()
    duration = models.IntegerField()
    duartion_period = models.DateTimeField()
    end_treatment = models.CharField(max_length=100)
    form = models.IntegerField()
    frequency = models.IntegerField()
    frequency_unit = models.CharField(max_length=100)
    frequency_prn = models.BooleanField()
    indication = models.CharField(max_length=100)
    infusion = models.CharField(max_length=100)
    infusion_rate = models.IntegerField()
    infusion_rate_units = models.CharField(max_length=100)
    medicament = models.IntegerField()
    name = models.IntegerField()
    prnt = models.BooleanField()
    qty = models.IntegerField()
    quantity = models.IntegerField()
    refills = models.IntegerField()
    review = models.DateTimeField()
    route = models.IntegerField()
    short_comment = models.CharField(max_length=100)
    start_treatment = models.DateTimeField()
    class Meta:
        db_table = 'gnuhealth_prescription_line'