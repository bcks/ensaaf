from django.db import models
from django.db.models.functions import Cast
from django.contrib import admin
from django import forms





class Data(models.Model):
    victim_name = models.CharField(max_length=256)
    victim_name_pb = models.CharField(max_length=256, blank=True, null=True)
    village_name = models.CharField(max_length=256, blank=True, null=True)
    village_name_pb = models.CharField(max_length=256, blank=True, null=True)
    victim_alias = models.IntegerField(blank=True, null=True)
    victim_alias_name = models.CharField(max_length=256, blank=True, null=True)
    village_id = models.CharField(max_length=64, blank=True, null=True, unique=True)
    district_id =models.CharField(max_length=8, blank=True, null=True)
    record_id = models.CharField(max_length=8, db_column='record_id', primary_key=True)
    urban_rural = models.IntegerField(db_column='urban_rural', blank=True, null=True)
    timeline = models.DateField(db_column='timeline', blank=True, null=True)
    timeline_start = models.DateField(db_column='timeline_start', blank=True, null=True)
    timeline_end = models.DateField(db_column='timeline_end', blank=True, null=True)
    arrest_start = models.DateField(db_column='arrest_start', blank=True, null=True)
    arrest_end = models.DateField(db_column='arrest_end', blank=True, null=True)
    othervill_interview = models.CharField(max_length=256, blank=True, null=True)
    publish_information = models.IntegerField(blank=True, null=True)
    publish_restriction = models.IntegerField(blank=True, null=True)
    publish_restriction_other = models.CharField(max_length=64, blank=True, null=True)
    number_of_victims = models.IntegerField(blank=True, null=True)
    genuine_encounters = models.IntegerField(blank=True, null=True)
    respondent_information_complete = models.IntegerField()
    victim_first_name = models.CharField(max_length=256, blank=True, null=True)
    victim_first_name_pb = models.CharField(max_length=256, blank=True, null=True)
    victim_sex = models.IntegerField(blank=True, null=True)
    victim_age = models.CharField(max_length=64)
    victim_age_averaged = models.IntegerField(db_column='victim_age_averaged', blank=True, null=True)
    victim_address_int_loc = models.IntegerField(blank=True, null=True)
    victim_address_other = models.CharField(max_length=256, blank=True, null=True)
    victim_education = models.IntegerField()
    victim_employment_1 = models.IntegerField(db_column='victim_employment___1')
    victim_employment_2 = models.IntegerField(db_column='victim_employment___2')
    victim_employment_3 = models.IntegerField(db_column='victim_employment___3')
    victim_employment_4 = models.IntegerField(db_column='victim_employment___4')
    victim_employment_5 = models.IntegerField(db_column='victim_employment___5')
    victim_employment_6 = models.IntegerField(db_column='victim_employment___6')
    victim_employment_7 = models.IntegerField(db_column='victim_employment___7')
    victim_employment_8 = models.IntegerField(db_column='victim_employment___8')
    victim_employment_9 = models.IntegerField(db_column='victim_employment___9')
    victim_employment_10 = models.IntegerField(db_column='victim_employment___10')
    victim_employment_11 = models.IntegerField(db_column='victim_employment___11')
    victim_employment_other = models.CharField(max_length=256, blank=True, null=True)
    victim_marital_status = models.IntegerField(blank=True, null=True)
    victim_children = models.CharField(db_column='victim_children', max_length=64, blank=True, null=True)
    victim_religion = models.IntegerField(db_column='victim_religion', blank=True, null=True)
    victim_amritdhari = models.IntegerField(blank=True, null=True)
    victim_kesdhari = models.IntegerField(blank=True, null=True)
    victim_caste = models.IntegerField()
    other_victim_caste = models.CharField(max_length=256, blank=True, null=True)
    victim_militant_status = models.IntegerField()
    victim_militant_group_1 = models.IntegerField(db_column='victim_militant_group___1')
    victim_militant_group_2 = models.IntegerField(db_column='victim_militant_group___2')
    victim_militant_group_3 = models.IntegerField(db_column='victim_militant_group___3')
    victim_militant_group_4 = models.IntegerField(db_column='victim_militant_group___4')
    victim_militant_group_5 = models.IntegerField(db_column='victim_militant_group___5')
    victim_militant_group_6 = models.IntegerField(db_column='victim_militant_group___6')
    victim_militant_group_7 = models.IntegerField(db_column='victim_militant_group___7')
    victim_militant_group_8 = models.IntegerField(db_column='victim_militant_group___8')
    victim_militant_group_9 = models.IntegerField(db_column='victim_militant_group___9')
    victim_militant_group_10 = models.IntegerField(db_column='victim_militant_group___10')
    victim_militant_reason_1 = models.IntegerField(db_column='victim_militant_reason___1')
    victim_militant_reason_2 = models.IntegerField(db_column='victim_militant_reason___2')
    victim_militant_reason_3 = models.IntegerField(db_column='victim_militant_reason___3')
    victim_militant_reason_4 = models.IntegerField(db_column='victim_militant_reason___4')
    victim_militant_reason_5 = models.IntegerField(db_column='victim_militant_reason___5')
    victim_militant_reason_6 = models.IntegerField(db_column='victim_militant_reason___6')
    victim_militant_reason_7 = models.IntegerField(db_column='victim_militant_reason___7')
    victim_militant_reason_8 = models.IntegerField(db_column='victim_militant_reason___8')
    victim_militant_reason_9 = models.IntegerField(db_column='victim_militant_reason___9')
    victim_militant_support = models.IntegerField(blank=True, null=True)
    victim_militant_sprt_vol = models.IntegerField(blank=True, null=True)
    victim_prior_detention_st = models.IntegerField()
    victim_prior_detentions = models.CharField(max_length=64, blank=True, null=True)
    victim_prior_detention_trt = models.IntegerField(blank=True, null=True)
    target_reason_1 = models.IntegerField(db_column='target_reason___1')
    target_reason_2 = models.IntegerField(db_column='target_reason___2')
    target_reason_3 = models.IntegerField(db_column='target_reason___3')
    target_reason_4 = models.IntegerField(db_column='target_reason___4')
    target_reason_5 = models.IntegerField(db_column='target_reason___5')
    target_reason_6 = models.IntegerField(db_column='target_reason___6')
    target_reason_7 = models.IntegerField(db_column='target_reason___7')
    target_reason_8 = models.IntegerField(db_column='target_reason___8')
    target_reason_9 = models.IntegerField(db_column='target_reason___9')
    target_reason_other = models.CharField(max_length=256, blank=True, null=True)
    victim_disappeared_killed = models.IntegerField(blank=True, null=True)
    victim_death_date = models.CharField(max_length=64, blank=True, null=True)
    victim_arrest_status = models.IntegerField(blank=True, null=True)
    victim_arrest_date = models.CharField(max_length=64, blank=True, null=True)
    #victim_arrest_exact_date = models.IntegerField(blank=True, null=True)
    victim_arrest_location = models.IntegerField(blank=True, null=True)
    victim_arrest_loc_oth = models.CharField(max_length=256, blank=True, null=True)
    victim_arrest_loc_vill = models.CharField(max_length=256, blank=True, null=True)
    arrest_security_type_1 = models.IntegerField(db_column='arrest_security_type___1')
    arrest_security_type_2 = models.IntegerField(db_column='arrest_security_type___2')
    arrest_security_type_3 = models.IntegerField(db_column='arrest_security_type___3')
    arrest_security_type_4 = models.IntegerField(db_column='arrest_security_type___4')
    arrest_security_type_5 = models.IntegerField(db_column='arrest_security_type___5')
    arrest_security_type_6 = models.IntegerField(db_column='arrest_security_type___6')
    arrest_security_type_7 = models.IntegerField(db_column='arrest_security_type___7')
    arrest_security_type_8 = models.IntegerField(db_column='arrest_security_type___8')
    arrest_security_locality = models.IntegerField(db_column='arrest_security_locality', blank=True, null=True)
    securityoff_id_known = models.IntegerField(blank=True, null=True)
    security_forces_uniformed = models.IntegerField(blank=True, null=True)
    security_forces_civilcloth = models.IntegerField(blank=True, null=True)
    witness_arrest_0 = models.IntegerField(db_column='witness_arrest___0')
    witness_arrest_1 = models.IntegerField(db_column='witness_arrest___1')
    witness_arrest_2 = models.IntegerField(db_column='witness_arrest___2')
    witness_arrest_3 = models.IntegerField(db_column='witness_arrest___3')
    witness_arrest_4 = models.IntegerField(db_column='witness_arrest___4')
    witness_arrest_5 = models.IntegerField(db_column='witness_arrest___5')
    witness_arrest_6 = models.IntegerField(db_column='witness_arrest___6')
    witness_arrest_7 = models.IntegerField(db_column='witness_arrest___7')
    witness_arrest_8 = models.IntegerField(db_column='witness_arrest___8')
    witness_arrest_9 = models.IntegerField(db_column='witness_arrest___9')
    witness_arrest_10 = models.IntegerField(db_column='witness_arrest___10')
    witness_arrest_11 = models.IntegerField(db_column='witness_arrest___11')
    witness_arrest_12 = models.IntegerField(db_column='witness_arrest___12')
    so_inform_witnesses = models.IntegerField(blank=True, null=True)
    others_arrested = models.IntegerField(blank=True, null=True)
    victim_detention_loc_known = models.IntegerField(blank=True, null=True)
    demands_1 = models.IntegerField(db_column='demands___1')
    demands_2 = models.IntegerField(db_column='demands___2')
    demands_3 = models.IntegerField(db_column='demands___3')
    demands_4 = models.IntegerField(db_column='demands___4')
    demands_5 = models.IntegerField(db_column='demands___5')
    demands_6 = models.IntegerField(db_column='demands___6')
    demands_7 = models.IntegerField(db_column='demands___7')
    demands_8 = models.IntegerField(db_column='demands___8')
    demands_9 = models.IntegerField(db_column='demands___9')
    demands_10 = models.IntegerField(db_column='demands___10')
    judge_or_magistrate_status = models.IntegerField(blank=True, null=True)
    judge_or_magistrate_result_1 = models.IntegerField(db_column='judge_or_magistrate_result___1')
    judge_or_magistrate_result_2 = models.IntegerField(db_column='judge_or_magistrate_result___2')
    judge_or_magistrate_result_3 = models.IntegerField(db_column='judge_or_magistrate_result___3')
    judge_or_magistrate_result_4 = models.IntegerField(db_column='judge_or_magistrate_result___4')
    #victim_last_heard_alive = models.IntegerField(blank=True, null=True)
    #dt_last_heard_victim_alive = models.CharField(max_length=64, blank=True, null=True)
    victim_killed_location = models.IntegerField(blank=True, null=True)
    killing_securityforcestype_1 = models.IntegerField(db_column='killing_securityforcestype___1')
    killing_securityforcestype_2 = models.IntegerField(db_column='killing_securityforcestype___2')
    killing_securityforcestype_3 = models.IntegerField(db_column='killing_securityforcestype___3')
    killing_securityforcestype_4 = models.IntegerField(db_column='killing_securityforcestype___4')
    killing_securityforcestype_5 = models.IntegerField(db_column='killing_securityforcestype___5')
    killing_securityforcestype_6 = models.IntegerField(db_column='killing_securityforcestype___6')
    killing_securityforcestype_7 = models.IntegerField(db_column='killing_securityforcestype___7')
    killing_securityforcestype_8 = models.IntegerField(db_column='killing_securityforcestype___8')
    killing_securityforces_lcl = models.CharField(max_length=256, blank=True, null=True)
    securityforces_idknown_1 = models.IntegerField(db_column='securityforces_idknown___1', blank=True, null=True, default='NULL')
    securityforces_idknown_2 = models.IntegerField(db_column='securityforces_idknown___2', blank=True, null=True, default='NULL')
    securityforces_idknown_3 = models.IntegerField(db_column='securityforces_idknown___3', blank=True, null=True, default='NULL')
    others_killed_1 = models.IntegerField(db_column='others_killed___1')
    others_killed_2 = models.IntegerField(db_column='others_killed___2')
    others_killed_0 = models.IntegerField(db_column='others_killed___0')
    others_killed_9 = models.IntegerField(db_column='others_killed___9')
    others_killed_3 = models.IntegerField(db_column='others_killed___3')
    security_officials_apprchd = models.IntegerField(blank=True, null=True)
    so_approached_type_1 = models.IntegerField(db_column='so_approached_type___1')
    so_approached_type_2 = models.IntegerField(db_column='so_approached_type___2')
    so_approached_type_3 = models.IntegerField(db_column='so_approached_type___3')
    so_approached_type_4 = models.IntegerField(db_column='so_approached_type___4')
    so_approached_type_5 = models.IntegerField(db_column='so_approached_type___5')
    so_approached_type_6 = models.IntegerField(db_column='so_approached_type___6')
    so_approached_type_7 = models.IntegerField(db_column='so_approached_type___7')
    so_approached_type_8 = models.IntegerField(db_column='so_approached_type___8')
    so_approached_type_9 = models.IntegerField(db_column='so_approached_type___9')
    so_approached_loc = models.CharField(max_length=237, blank=True, null=True)
    security_official_response_0 = models.IntegerField(db_column='security_official_response___0')
    security_official_response_1 = models.IntegerField(db_column='security_official_response___1')
    security_official_response_2 = models.IntegerField(db_column='security_official_response___2')
    security_official_response_3 = models.IntegerField(db_column='security_official_response___3')
    security_official_response_4 = models.IntegerField(db_column='security_official_response___4')
    security_official_response_5 = models.IntegerField(db_column='security_official_response___5')
    security_official_response_6 = models.IntegerField(db_column='security_official_response___6')
    security_official_response_7 = models.IntegerField(db_column='security_official_response___7')
    security_official_response_8 = models.IntegerField(db_column='security_official_response___8')
    security_official_response_9 = models.IntegerField(db_column='security_official_response___9')
    security_official_response_10 = models.IntegerField(db_column='security_official_response___10')
    security_official_response_11 = models.IntegerField(db_column='security_official_response___11')
    security_official_response_12 = models.IntegerField(db_column='security_official_response___12')
    security_official_response_13 = models.IntegerField(db_column='security_official_response___13')
    security_official_response_14 = models.IntegerField(db_column='security_official_response___14')
    other_so_response = models.CharField(max_length=256, blank=True, null=True)
    court_or_commission = models.IntegerField(blank=True, null=True)
    no_action_pursued_reason_0 = models.IntegerField(db_column='no_action_pursued_reason___0')
    no_action_pursued_reason_1 = models.IntegerField(db_column='no_action_pursued_reason___1')
    no_action_pursued_reason_2 = models.IntegerField(db_column='no_action_pursued_reason___2')
    no_action_pursued_reason_3 = models.IntegerField(db_column='no_action_pursued_reason___3')
    no_action_pursued_reason_4 = models.IntegerField(db_column='no_action_pursued_reason___4')
    no_action_pursued_reason_5 = models.IntegerField(db_column='no_action_pursued_reason___5')
    no_action_pursued_reason_6 = models.IntegerField(db_column='no_action_pursued_reason___6')
    other_no_action_reason = models.CharField(max_length=256, blank=True, null=True)
    so_return_body = models.IntegerField(blank=True, null=True)
    so_body_disposal = models.IntegerField(blank=True, null=True)
    cremation_location_type = models.IntegerField(blank=True, null=True)
    #cremation_location_name = models.CharField(max_length=256, blank=True, null=True)
    condition_of_remains_0 = models.IntegerField(db_column='condition_of_remains___0')
    condition_of_remains_1 = models.IntegerField(db_column='condition_of_remains___1')
    condition_of_remains_2 = models.IntegerField(db_column='condition_of_remains___2')
    condition_of_remains_3 = models.IntegerField(db_column='condition_of_remains___3')
    condition_of_remains_4 = models.IntegerField(db_column='condition_of_remains___4')
    condition_of_remains_5 = models.IntegerField(db_column='condition_of_remains___5')
    condition_of_remains_6 = models.IntegerField(db_column='condition_of_remains___6')
    condition_of_remains_7 = models.IntegerField(db_column='condition_of_remains___7')
    condition_of_remains_8 = models.IntegerField(db_column='condition_of_remains___8')
    condition_of_remains_9 = models.IntegerField(db_column='condition_of_remains___9')
    killing_so_affiliation = models.IntegerField(blank=True, null=True)
    killing_so_affiliation_oth = models.IntegerField(blank=True, null=True)
    family_effects_1 = models.IntegerField(db_column='family_effects___1')
    family_effects_2 = models.IntegerField(db_column='family_effects___2')
    family_effects_3 = models.IntegerField(db_column='family_effects___3')
    family_effects_4 = models.IntegerField(db_column='family_effects___4')
    family_effects_5 = models.IntegerField(db_column='family_effects___5')
    family_effects_6 = models.IntegerField(db_column='family_effects___6')
    family_effects_7 = models.IntegerField(db_column='family_effects___7')
    family_effects_8 = models.IntegerField(db_column='family_effects___8')
    family_effects_9 = models.IntegerField(db_column='family_effects___9')
    family_effects_12 = models.IntegerField(db_column='family_effects___12')
    family_effects_10 = models.IntegerField(db_column='family_effects___10')
    family_effects_11 = models.IntegerField(db_column='family_effects___11')
    govnt_response_desired_1 = models.IntegerField(db_column='govnt_response_desired___1')
    govnt_response_desired_2 = models.IntegerField(db_column='govnt_response_desired___2')
    govnt_response_desired_3 = models.IntegerField(db_column='govnt_response_desired___3')
    govnt_response_desired_4 = models.IntegerField(db_column='govnt_response_desired___4')
    govnt_response_desired_5 = models.IntegerField(db_column='govnt_response_desired___5')
    govnt_response_desired_6 = models.IntegerField(db_column='govnt_response_desired___6')
    govnt_response_desired_7 = models.IntegerField(db_column='govnt_response_desired___7')
    govnt_response_desired_8 = models.IntegerField(db_column='govnt_response_desired___8')
    govnt_response_desired_9 = models.IntegerField(db_column='govnt_response_desired___9')
    govnt_response_desired_10 = models.IntegerField(db_column='govnt_response_desired___10')
    govnt_response_desired_11 = models.IntegerField(db_column='govnt_response_desired___11')
    oth_govnt_response_desired = models.CharField(max_length=256, blank=True, null=True)
    photo_vic_fn = models.CharField(max_length=256, blank=True, null=True)
    photo_doc_fn = models.CharField(max_length=256, blank=True, null=True)
    photo_news_fn = models.CharField(max_length=256, blank=True, null=True)
    photo_advocacy_fn = models.CharField(max_length=256, blank=True, null=True)
    photo_personalpapers_fn = models.CharField(max_length=256, blank=True, null=True)
    photo_family_fn = models.CharField(max_length=256, blank=True, null=True)
    victim_summary = models.TextField(blank=True, null=True)
    photo_family_fn = models.CharField(max_length=256, blank=True, null=True)
    video_url = models.CharField(max_length=256, blank=True, null=True)
    video_url2 = models.CharField(max_length=256, blank=True, null=True)
    related_materials = models.TextField(blank=True, null=True)
    related_materials_pb = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'data'
        indexes = [
          models.Index(fields=['village_id']),
          models.Index(fields=['village_name']),
        ]
        #ordering = [
        #    Cast("record_id", output_field=models.IntegerField()),
        #]




class Villages(models.Model):
    village_name = models.CharField(max_length=256)
    village_name_pb = models.CharField(max_length=256, blank=True, null=True)
    tehsil = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    district_id = models.IntegerField()
    tehsil_id = models.IntegerField()
    vid = models.CharField(max_length=16, primary_key=True)
    lon = models.CharField(max_length=16, blank=True, null=True)
    lat = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'villages'
        indexes = [
            models.Index(fields=['tehsil_id']),
            models.Index(fields=['district_id']),
            models.Index(fields=['vid']),
        ]



# COUNT_CHOICES = (
#     ('tehsil', 'Subdistrict'),
#     ('district', 'District'),
#     )
# 
# class CountCache(models.Model):
#     object_type = models.CharField(max_length=20, choices=COUNT_CHOICES)
#     object_id = models.IntegerField()
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add = True)
#     value = models.IntegerField(default = 0)
#     name = models.CharField(max_length=64)
    


class OtherArrest(models.Model):
    id  = models.IntegerField(primary_key=True)
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='other_arrested', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    other_arrested_first_name = models.CharField(max_length=256, blank=True, null=True)
    other_arrested_last_name = models.CharField(max_length=256, blank=True, null=True)
    other_arrested_village = models.CharField(max_length=256, blank=True, null=True)
    covictm_record = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'other_arrested'



class OthersKilled(models.Model):
    id  = models.IntegerField(primary_key=True)
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='others_killed', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    others_killed_first_name = models.CharField(max_length=256, blank=True, null=True)
    others_killed_last_name = models.CharField(max_length=256, blank=True, null=True)
    others_killed_villtown = models.CharField(max_length=256, blank=True, null=True)
    others_killed_record = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'others_killed'



class SecurityArrest(models.Model):
    id  = models.IntegerField(primary_key=True)
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='security_arrest', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    arrest_so_first_name = models.CharField(max_length=256, blank=True, null=True)
    arrest_so_last_name = models.CharField(max_length=256, blank=True, null=True)
    arrest_so_rank = models.IntegerField(blank=True, null=True)
    arrest_so_rank_other = models.CharField(max_length=256, blank=True, null=True)
    arrest_so_affiliation = models.IntegerField(blank=True, null=True)
    arrest_so_affiliation_oth = models.CharField(max_length=256, blank=True, null=True)
    arrest_so_affiliation_loc = models.CharField(max_length=256, blank=True, null=True)
    soa_code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'security_arrest'


class SecurityKilled(models.Model):
    id  = models.IntegerField(primary_key=True)
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='security_killed', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    killing_so_first_name = models.CharField(max_length=256, blank=True, null=True)
    killing_so_last_name = models.CharField(max_length=256, blank=True, null=True)
    killing_so_rank = models.IntegerField(blank=True, null=True)
    killing_so_rank_other = models.CharField(max_length=256, blank=True, null=True)
    killing_so_affiliation = models.IntegerField(blank=True, null=True)
    killing_so_affiliation_oth = models.CharField(max_length=256, blank=True, null=True)
    killing_so_affiliation_loc = models.CharField(max_length=256, blank=True, null=True)
    sok_code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'security_killed'


class WhereVictimDetained(models.Model):  
    id  = models.IntegerField(primary_key=True)
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='where_victim_detained', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    detention_facility_type = models.IntegerField(blank=True, null=True)
    detention_fac_type_oth = models.CharField(max_length=144, blank=True, null=True)
    facility_name = models.CharField(max_length=124, blank=True, null=True)
    facility_nearest_villtown = models.CharField(max_length=54, blank=True, null=True)
    facility_tehsil = models.CharField(max_length=17, blank=True, null=True)
    facility_district = models.CharField(max_length=37, blank=True, null=True)
    duration_of_detention = models.CharField(max_length=311, blank=True, null=True)
    witness_detention_status = models.IntegerField(blank=True, null=True)
    witness_detention_1 = models.IntegerField(db_column='witness_detention___1')
    witness_detention_2 = models.IntegerField(db_column='witness_detention___2')
    witness_detention_3 = models.IntegerField(db_column='witness_detention___3')
    witness_detention_4 = models.IntegerField(db_column='witness_detention___4')
    witness_detention_5 = models.IntegerField(db_column='witness_detention___5')
    witness_detention_6 = models.IntegerField(db_column='witness_detention___6')
    witness_detention_7 = models.IntegerField(db_column='witness_detention___7')
    witness_detention_8 = models.IntegerField(db_column='witness_detention___8')
    witness_detention_9 = models.IntegerField(db_column='witness_detention___9')
    witness_detention_10 = models.IntegerField(db_column='witness_detention___10')
    witness_detention_11 = models.IntegerField(db_column='witness_detention___11')
    witness_detention_12 = models.IntegerField(db_column='witness_detention___12')
    witness_detention_13 = models.IntegerField(db_column='witness_detention___13')
    witness_detention_14 = models.IntegerField(db_column='witness_detention___14')
    witness_detention_other = models.CharField(max_length=1024, blank=True, null=True)
    witness_report = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'where_victim_detained'






class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    title_pb = models.CharField(max_length=200, blank=True)
    body_pb = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        db_table = 'Page'

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body')
    search_fields = ['title', 'body']

admin.site.register(Page, PageAdmin)






class FullProfile(models.Model):
    record_id = models.ForeignKey(Data, db_column='record_id', to_field='record_id', related_name='fullprofile', on_delete=models.CASCADE, blank=True, null=True, default='NULL')
    family_reflections = models.TextField(db_column='family_reflections', blank=True, null=True)
    video_url = models.CharField(db_column='video_url', max_length=256, blank=True, null=True)
    summary = models.TextField(db_column='summary', blank=True, null=True)
    class Meta:
        db_table = 'fullprofile'

class RecordIdField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.record_id

class FullProfileAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'family_reflections', 'summary')
    search_fields = ['family_reflections', 'summary']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'record_id':
            kwargs['form_class'] = RecordIdField
        return super(FullProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(FullProfile, FullProfileAdmin)



