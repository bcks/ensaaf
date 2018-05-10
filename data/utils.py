from django.db.models import Count
import operator


def calculate_stats(all):
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()

    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()

    religion = {
      "Sikhism": all.filter(victim_religion='1').count(),
      "Hinduism": all.filter(victim_religion='2').count(),
      "Islam": all.filter(victim_religion='3').count(),
      "Christianity": all.filter(victim_religion='4').count(),
      "No religion": all.filter(victim_religion='5').count(),
      "Other": all.filter(victim_religion='7').count(),
    }
    religion = sorted(religion.items(), key=operator.itemgetter(1), reverse=True)

    caste = {
      "Jat": all.filter(victim_religion='1').count(),
      "Ramgarhia": all.filter(victim_religion='2').count(),
      "Dalit/SC/BC": all.filter(victim_religion='3').count(),
      "Mazbi": all.filter(victim_religion='4').count(),
      "Chamar": all.filter(victim_religion='5').count(),
      "Khatri": all.filter(victim_religion='6').count(),
      "Naee": all.filter(victim_religion='7').count(),
      "Other": all.filter(victim_religion='9').count(),
    }
    caste = sorted(caste.items(), key=operator.itemgetter(1), reverse=True)

    education = {
      "No education": all.filter(victim_education='0').count(),
      "Primary school/5th standard": all.filter(victim_education='1').count(),
      "Middle school/8th standard": all.filter(victim_education='2').count(),
      "High school/matriculated": all.filter(victim_education='3').count(),
      "10 plus 1": all.filter(victim_education='4').count(),
      "10 plus 2/senior secondary": all.filter(victim_education='5').count(),
      "Some college, bachelors degree": all.filter(victim_education='6').count(),
      "Masters/graduate diploma": all.filter(victim_education='7').count(),
      "Vocational diploma": all.filter(victim_education='8').count(),
      "Giyani": all.filter(victim_education='9').count(),
    }
    education = sorted(education.items(), key=operator.itemgetter(1), reverse=True)

    age_range = { # Dataset.objects.filter(i_end_int__gte=x,i_begin_int__lte=x)
      "0-17": all.filter(victim_age_averaged__gte=0,victim_age_averaged__lte=17).count(),
      "18-34": all.filter(victim_age_averaged__gte=18,victim_age_averaged__lte=24).count(),
      "35-51": all.filter(victim_age_averaged__gte=35,victim_age_averaged__lte=51).count(),
      "52-68": all.filter(victim_age_averaged__gte=52,victim_age_averaged__lte=68).count(),
      "69-90": all.filter(victim_age_averaged__gte=69,victim_age_averaged__lte=100).count(),
    }
    age_range = sorted(age_range.items(), key=operator.itemgetter(0))


    victim_militant_reason = {
      "Because of Bluestar": all.filter(victim_militant_reason_1='1').count(),
      "Persecution (i.e. arbitrary arrest, torture, self-defense)": all.filter(victim_militant_reason_2='1').count(),
      "Persecution of a family member or a friend": all.filter(victim_militant_reason_3='1').count(),
      "General persecution of Sikhs": all.filter(victim_militant_reason_4='1').count(),
      "Supported the goals of the militancy movement": all.filter(victim_militant_reason_5='1').count(),
      "Was forced to join": all.filter(victim_militant_reason_6='1').count(),
      "Other": all.filter(victim_militant_reason_8='1').count(),
    }
    victim_militant_reason = sorted(victim_militant_reason.items(), key=operator.itemgetter(1), reverse=True)

    target_reason = {
      "Victim was a militant": all.filter(victim_militant_reason_1='1').count(),
      "Victim was related to a militant": all.filter(victim_militant_reason_2='1').count(),
      "Victim gave support to a militant": all.filter(victim_militant_reason_3='1').count(),
      "Victim was involved in criminal activities": all.filter(victim_militant_reason_4='1').count(),
      "Victim was identifiably Sikh": all.filter(victim_militant_reason_5='1').count(),
      "Security forces thought victim was a militant": all.filter(victim_militant_reason_6='1').count(),
      "Mistaken for a wanted individual": all.filter(victim_militant_reason_7='1').count(),
      "Don't Know": all.filter(victim_militant_reason_8='1').count(),
      "Other": all.filter(victim_militant_reason_9='1').count(),
    }
    target_reason = sorted(target_reason.items(), key=operator.itemgetter(1), reverse=True)


    employment = {
      "Farmer/agriculture": all.filter(victim_employment_1='1').count(),
      "Shopkeeper": all.filter(victim_employment_2='1').count(),
      "Day labourer": all.filter(victim_employment_3='1').count(),
      "Driver (bus/truck/car)": all.filter(victim_employment_4='1').count(),
      "Mechanic": all.filter(victim_employment_5='1').count(),
      "Student": all.filter(victim_employment_6='1').count(),
      "Housewife": all.filter(victim_employment_7='1').count(),
      "Carpenter": all.filter(victim_employment_8='1').count(),
      "Unemployed": all.filter(victim_employment_9='1').count(),
      "Other": all.filter(victim_employment_11='1').count(),
    }
    employment = sorted(employment.items(), key=operator.itemgetter(1), reverse=True)


    no_action_pursued_reason = {
      "Not Applicable": all.filter(no_action_pursued_reason_0='1').count(),
      "Afraid of retaliation": all.filter(no_action_pursued_reason_1='1').count(),
      "Believed it would have been ineffective": all.filter(no_action_pursued_reason_2='1').count(),
      "Didn’t know what to do": all.filter(no_action_pursued_reason_3='1').count(),
      "Couldn’t Afford": all.filter(no_action_pursued_reason_4='1').count(),
      "Other": all.filter(no_action_pursued_reason_6='1').count(),
    }
    no_action_pursued_reason = sorted(no_action_pursued_reason.items(), key=operator.itemgetter(1), reverse=True)


    so_approached_type = {
      "Same as officials involved in abduction/killing": all.filter(so_approached_type_1='1').count(),
      "Punjab Police": all.filter(so_approached_type_2='1').count(),
      "BSF": all.filter(so_approached_type_3='1').count(),
      "CRPF": all.filter(so_approached_type_4='1').count(),
      "Army": all.filter(so_approached_type_5='1').count(),
      "CIA": all.filter(so_approached_type_6='1').count(),
      "Black Cat": all.filter(so_approached_type_7='1').count(),
      "Other": all.filter(so_approached_type_9='1').count(),
    }
    so_approached_type = sorted(so_approached_type.items(), key=operator.itemgetter(1), reverse=True)

    family_effects = {
      "No drastic action": all.filter(family_effects_1='1').count(),
      "Someone ran away": all.filter(family_effects_2='1').count(),
      "Militant activity": all.filter(family_effects_3='1').count(),
      "Dropped out of school": all.filter(family_effects_4='1').count(),
      "Alcohol/Drug Abuse": all.filter(family_effects_5='1').count(),
      "Suicide": all.filter(family_effects_6='1').count(),
      "Family Abandoned Home": all.filter(family_effects_7='1').count(),
      "Someone died due to depression/shock": all.filter(family_effects_8='1').count(),
      "Mentally disturbed": all.filter(family_effects_9='1').count(),
      "Significant loss of income / became impoverished": all.filter(family_effects_12='1').count(),
      "Other": all.filter(family_effects_11='1').count(),
    }
    family_effects = sorted(family_effects.items(), key=operator.itemgetter(1), reverse=True)

    govnt_response_desired = {
      "Monetary compensation to family": all.filter(govnt_response_desired_1='1').count(),
      "Rehabilitation services to family members": all.filter(govnt_response_desired_2='1').count(),
      "Public acknowledgement of wrongful deaths": all.filter(govnt_response_desired_3='1').count(),
      "Criminal Sanctions against those responsible": all.filter(govnt_response_desired_4='1').count(),
      "Employment": all.filter(govnt_response_desired_5='1').count(),
      "Truth commission": all.filter(govnt_response_desired_6='1').count(),
      "Investigations into abuses": all.filter(govnt_response_desired_7='1').count(),
      "Memorial for victims": all.filter(govnt_response_desired_8='1').count(),
      "Desire nothing from government": all.filter(govnt_response_desired_9='1').count(),
      "Other": all.filter(govnt_response_desired_10='1').count(),
    }
    govnt_response_desired = sorted(govnt_response_desired.items(), key=operator.itemgetter(1), reverse=True)


    children = all.values('victim_children').extra({'victim_children': "CAST(victim_children as UNSIGNED)"}).annotate(Count('victim_children')).order_by('victim_children')

    genuine_encounter = all.filter(genuine_encounters='1').count()
    not_genuine_encounter = all.filter(genuine_encounters='0').count()
    kesdhari = all.filter(victim_kesdhari='1').count()
    amritdhari = all.filter(victim_amritdhari='1').count()
    militant = all.filter(victim_militant_status='1').count()
    not_militant = all.filter(victim_militant_status='0').count()
    militant_support = all.filter(victim_militant_support='1').count()
    no_militant_support = all.filter(victim_militant_support='0').count()
    prior_detentions = all.filter(victim_prior_detention_st='1').count()
    no_prior_detentions = all.filter(victim_prior_detention_st='0').count()
    security_officials_apprchd = all.filter(security_officials_apprchd='1').count()
    no_security_officials_apprchd = all.filter(security_officials_apprchd='0').count()
    court_or_commission = all.filter(court_or_commission='1').count()
    no_court_or_commission = all.filter(court_or_commission='0').count()
    victim_militant_support = all.filter(victim_militant_support='1').count()
    no_victim_militant_support = all.filter(victim_militant_support='0').count()
    victim_militant_support_voluntary = all.filter(victim_militant_sprt_vol='1').count()
    victim_militant_support_forced = all.filter(victim_militant_sprt_vol='2').count()
    victim_arrest_status = all.filter(victim_arrest_status__in=['0','1']).count()
    no_victim_arrest_status = all.filter(victim_arrest_status='2').count()
    so_inform_witnesses = all.filter(so_inform_witnesses='1').count()
    no_so_inform_witnesses = all.filter(so_inform_witnesses='2').count()
    security_forces_uniformed = all.filter(security_forces_uniformed='1').count()
    no_security_forces_uniformed = all.filter(security_forces_uniformed='0').count()
    judge_or_magistrate_status = all.filter(judge_or_magistrate_status='1').count()
    no_judge_or_magistrate_status = all.filter(judge_or_magistrate_status='0').count()
    victim_detention_loc_known = all.filter(victim_detention_loc_known='1').count()
    no_victim_detention_loc_known = all.filter(victim_detention_loc_known='0').count()    
    so_return_body = all.filter(victim_arrest_status__in=['1','2']).count()
    no_so_return_body = all.filter(victim_arrest_status='3').count()
    securityoff_id_known = all.filter(securityoff_id_known='1').count() + all.filter(securityforces_idknown__in=['1','2']).count()
    no_securityoff_id_known = all.filter(securityoff_id_known='0').count() + all.filter(securityforces_idknown='3').count()


    so_body_disposal = {
      "Cremated the body": all.filter(so_body_disposal='1').count(),
      "Dumped body in canal or river": all.filter(so_body_disposal='2').count(),
      "Dumped body in well or drain": all.filter(so_body_disposal='3').count(),
      "Buried the body": all.filter(so_body_disposal='4').count(),
      "Other": all.filter(so_body_disposal='6').count(),
    }
    so_body_disposal = sorted(so_body_disposal.items(), key=operator.itemgetter(1), reverse=True)

    witness_arrest_0 = all.filter(witness_arrest_0 ='1').count()
    witness_arrest_1 = all.filter(witness_arrest_1 ='1').count()
    witness_arrest_2 = all.filter(witness_arrest_2 ='1').count()
    witness_arrest_3 = all.filter(witness_arrest_3 ='1').count()
    witness_arrest_4 = all.filter(witness_arrest_4 ='1').count()
    witness_arrest_5 = all.filter(witness_arrest_5 ='1').count()
    witness_arrest_6 = all.filter(witness_arrest_6 ='1').count()
    witness_arrest_7 = all.filter(witness_arrest_7 ='1').count()
    witness_arrest_8 = all.filter(witness_arrest_8 ='1').count()
    witness_arrest_9 = all.filter(witness_arrest_9 ='1').count()
    witness_arrest_10 = all.filter(witness_arrest_10 ='1').count()
    witness_arrest_11 = all.filter(witness_arrest_11 ='1').count()
    witness_arrest_12 = all.filter(witness_arrest_12 ='1').count()

    witness_total = witness_arrest_1 + witness_arrest_2 + witness_arrest_3 + \
                    witness_arrest_4 + witness_arrest_5 + witness_arrest_6 + \
                    witness_arrest_7 + witness_arrest_8 + witness_arrest_9 + \
                    witness_arrest_10 + witness_arrest_11

    witness_arrest = {
      "No witness": witness_arrest_0,
      "Spouse": witness_arrest_1,
      "Parents": witness_arrest_2,
      "Children": witness_arrest_3,
      "Sibling": witness_arrest_4,
      "Grandparent": witness_arrest_5,
      "Cousin": witness_arrest_6,
      "Aunt/Uncle": witness_arrest_7,
      "Friend": witness_arrest_8,
      "Co-villager": witness_arrest_9,
      "Interviewee": witness_arrest_10,
      "Other": witness_arrest_11,
    }
    witness_arrest = sorted(witness_arrest.items(), key=operator.itemgetter(1), reverse=True)

    number_of_victims = all.values('number_of_victims').annotate(Count('number_of_victims')).order_by('number_of_victims')


    witness_detention = {
      "Interviewee": all.filter(where_victim_detained__witness_detention_3='1').count(),
      "Other relative": all.filter(where_victim_detained__witness_detention_4='1').count(),
      "Other detainee": all.filter(where_victim_detained__witness_detention_5='1').count(),
      "Sarpanch/politician": all.filter(where_victim_detained__witness_detention_6='1').count(),
      "Newspaper": all.filter(where_victim_detained__witness_detention_7='1').count(),
      "Security official": all.filter(where_victim_detained__witness_detention_8='1').count(),
      "Friend": all.filter(where_victim_detained__witness_detention_9='1').count(),
      "Other witness": all.filter(where_victim_detained__witness_detention_10='1').count(),
      "Interview belief (no source)": all.filter(where_victim_detained__witness_detention_11='1').count(),
      "Doctor": all.filter(where_victim_detained__witness_detention_12='1').count(),
      "Other victim family": all.filter(where_victim_detained__witness_detention_13='1').count(),
      "Other": all.filter(where_victim_detained__witness_detention_14='1').count(),
    }
    witness_detention = sorted(witness_detention.items(), key=operator.itemgetter(1), reverse=True)


    victim_arrest_location = {
      "Victim’s Residence": all.filter(victim_arrest_location='2').count(),
      "Friend/Relative's residence": all.filter(victim_arrest_location='3').count(),
      "Checkpoint (Naka)": all.filter(victim_arrest_location='4').count(),
      "Roadside": all.filter(victim_arrest_location='5').count(),
      "Village Fields": all.filter(victim_arrest_location='6').count(),
      "Market/Bazaar": all.filter(victim_arrest_location='7').count(),
      "Bus Station/Stand": all.filter(victim_arrest_location='8').count(),
      "Police Station": all.filter(victim_arrest_location='9').count(),
      "Village Drain": all.filter(victim_arrest_location='10').count(),
      "Other": all.filter(victim_arrest_location='11').count(),
    }
    victim_arrest_location = sorted(victim_arrest_location.items(), key=operator.itemgetter(1), reverse=True)


    detention_facility_type = {
      "Police Station/Post": all.filter(victim_arrest_location='1').count(),
      "CIA Staff": all.filter(victim_arrest_location='2').count(),
      "BSF": all.filter(victim_arrest_location='3').count(),
      "CRPF Camp": all.filter(victim_arrest_location='4').count(),
      "Army Camp": all.filter(victim_arrest_location='5').count(),
      "Interrogation Center": all.filter(victim_arrest_location='6').count(),
      "Other": all.filter(victim_arrest_location='8').count(),
    }
    detention_facility_type = sorted(detention_facility_type.items(), key=operator.itemgetter(1), reverse=True)


    arrest_security_type = {
      "Punjab Police": all.filter(arrest_security_type_1='1').count(),
      "BSF": all.filter(arrest_security_type_2='1').count(),
      "CRPF": all.filter(arrest_security_type_3='1').count(),
      "Army": all.filter(arrest_security_type_4='1').count(),
      "CIA": all.filter(arrest_security_type_5='1').count(),
      "Black cat": all.filter(arrest_security_type_6='1').count(),
      "Other": all.filter(arrest_security_type_8='1').count(),
    }
    arrest_security_type = sorted(arrest_security_type.items(), key=operator.itemgetter(1), reverse=True)



    condition_of_remains = {
      "Bruises": all.filter(condition_of_remains_1='1').count(),
      "Bullet wounds": all.filter(condition_of_remains_2='1').count(),
      "Cuts/wounds": all.filter(condition_of_remains_3='1').count(),
      "Broken bones": all.filter(condition_of_remains_4='1').count(),
      "Missing hair from head or face": all.filter(condition_of_remains_5='1').count(),
      "Missing fingernails": all.filter(condition_of_remains_6='1').count(),
      "Burn marks": all.filter(condition_of_remains_7='1').count(),
      "Other": all.filter(condition_of_remains_9='1').count(),
    }
    condition_of_remains = sorted(condition_of_remains.items(), key=operator.itemgetter(1), reverse=True)



    killing_securityforcestype = {
      "Punjab police": all.filter(killing_securityforcestype_1='1').count(),
      "BSF": all.filter(killing_securityforcestype_2='1').count(),
      "CRPF": all.filter(killing_securityforcestype_3='1').count(),
      "Army": all.filter(killing_securityforcestype_4='1').count(),
      "CIA": all.filter(killing_securityforcestype_5='1').count(),
      "Black cat": all.filter(killing_securityforcestype_6='1').count(),
      "Other": all.filter(killing_securityforcestype_8='1').count(),
    }
    killing_securityforcestype = sorted(killing_securityforcestype.items(), key=operator.itemgetter(1), reverse=True)


    security_official_response = {
      "No Response": all.filter(security_official_response_0='1').count(),
      "Killed victim in an “encounter”": all.filter(security_official_response_1='1').count(),
      "Denied involvement": all.filter(security_official_response_2='1').count(),
      "Admitted killing with no explanation": all.filter(security_official_response_3='1').count(),
      "Admitted custody only": all.filter(security_official_response_4='1').count(),
      "Victim had escaped": all.filter(security_official_response_5='1').count(),
      "Victim killed will trying to escape": all.filter(security_official_response_6='1').count(),
      "Victim killed by militants": all.filter(security_official_response_7='1').count(),
      "Told family to go to another police station": all.filter(security_official_response_8='1').count(),
      "Victim killed in crossfire with militants": all.filter(security_official_response_9='1').count(),
      "Victim accidentally killed in custody": all.filter(security_official_response_10='1').count(),
      "Victim killed while resisting arrest/search": all.filter(security_official_response_11='1').count(),
      "Victim killed by Black Cats": all.filter(security_official_response_12='1').count(),
      "Other": all.filter(security_official_response_13='1').count(),
    }
    security_official_response = sorted(security_official_response.items(), key=operator.itemgetter(1), reverse=True)

    
    
    total = all.values('record_id').count()

    return {
      "age_range": age_range,
      "amritdhari": amritdhari,
      "arrest_security_type": arrest_security_type,
      "caste": caste,
      "children": children,
      "condition_of_remains": condition_of_remains,
      "court_or_commission": court_or_commission,
      "detention_facility_type": detention_facility_type,
      "education": education,
      "employment": employment,
      "family_effects": family_effects,
      "female": female,
      "genuine_encounter": genuine_encounter,
      "govnt_response_desired": govnt_response_desired,
      "judge_or_magistrate_status": judge_or_magistrate_status,
      "kesdhari": kesdhari,
      "killing_securityforcestype": killing_securityforcestype,
      "male": male,
      "married": married,
      "militant_support": militant_support,
      "militant": militant,
      "no_action_pursued_reason": no_action_pursued_reason,
      "no_court_or_commission": no_court_or_commission,
      "no_judge_or_magistrate_status": no_judge_or_magistrate_status,
      "no_militant_support": no_militant_support,
      "no_prior_detentions": no_prior_detentions,
      "no_security_forces_uniformed": no_security_forces_uniformed,
      "no_security_officials_apprchd": no_security_officials_apprchd,
      "no_securityoff_id_known": no_securityoff_id_known,
      "no_so_inform_witnesses": no_so_inform_witnesses,
      "no_so_return_body": no_so_return_body,
      "no_victim_arrest_status": no_victim_arrest_status,
      "no_victim_detention_loc_known": no_victim_detention_loc_known,
      "no_victim_militant_support": no_victim_militant_support,
      "not_genuine_encounter": not_genuine_encounter,
      "not_married": not_married,
      "not_militant": not_militant,
      "number_of_victims": number_of_victims,
      "prior_detentions": prior_detentions,
      "religion": religion,
      "security_forces_uniformed": security_forces_uniformed,
      "security_official_response": security_official_response,
      "security_officials_apprchd": security_officials_apprchd,
      "securityoff_id_known": securityoff_id_known,
      "so_approached_type": so_approached_type,
      "so_body_disposal": so_body_disposal,
      "so_inform_witnesses": so_inform_witnesses,
      "so_return_body": so_return_body,
      "target_reason": target_reason,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "total": total,
      "victim_arrest_location": victim_arrest_location,
      "victim_arrest_status": victim_arrest_status,
      "victim_detention_loc_known": victim_detention_loc_known,
      "victim_militant_reason": victim_militant_reason,
      "victim_militant_support_forced": victim_militant_support_forced,
      "victim_militant_support_voluntary": victim_militant_support_voluntary,
      "victim_militant_support": victim_militant_support,
      "witness_arrest": witness_arrest,
      "witness_detention": witness_detention,
      "witness_total": witness_total,
      }

