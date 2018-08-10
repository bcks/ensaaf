from django.db.models import Q, Count, Sum
import operator


def calculate_stats(all):
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()

    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()

    religion = {
      "Sikh": all.filter(victim_religion='1').count(),
      "Non-Sikh": all.filter(victim_religion__in=['2','3','4','5','7']).count(),
    }
    religion = sorted(religion.items(), key=operator.itemgetter(1), reverse=True)

    caste = {
      "Jat": all.filter(victim_caste='1').count(),
      "Non-Jat": all.filter(victim_caste__in=['2','3','4','5','6','7','9']).count(),
      # "Dalit/SC/BC": all.filter(victim_caste='3').count(),
      # "Mazbi": all.filter(victim_caste='4').count(),
      # "Chamar": all.filter(victim_caste='5').count(),
      # "Khatri": all.filter(victim_caste='6').count(),
      # "Naee": all.filter(victim_caste='7').count(),
      # "Other": all.filter(victim_caste='9').count(),
    }
    caste = sorted(caste.items(), key=operator.itemgetter(1), reverse=True)

    education = {
      "No education": all.filter(victim_education='0').count(),
      " Primary school": all.filter(victim_education='1').count(),
      "  Middle school": all.filter(victim_education='2').count(),
      "   High school": all.filter(victim_education__in=['3','4','5']).count(),
      "    Some college": all.filter(victim_education='6').count(),
      "     College degree": all.filter(victim_education='7').count(),
      "      Graduate degree": all.filter(victim_education='8').count(),
      "       Vocational degree": all.filter(victim_education__in=['9','10']).count(),
    }
    # education = sorted(education.items(), key=operator.itemgetter(1), reverse=True)
    education = sorted(education.items(), key=operator.itemgetter(0), reverse=True)

    age_range = { # Dataset.objects.filter(i_end_int__gte=x,i_begin_int__lte=x)
      "0-17": all.filter(victim_age_averaged__gte=0,victim_age_averaged__lte=17).count(),
      "18-33": all.filter(victim_age_averaged__gte=18,victim_age_averaged__lte=33).count(),
      "34-49": all.filter(victim_age_averaged__gte=34,victim_age_averaged__lte=49).count(),
      "50-64": all.filter(victim_age_averaged__gte=50,victim_age_averaged__lte=64).count(),
      "65+": all.filter(victim_age_averaged__gte=65,victim_age_averaged__lte=99).count(),
      "Age unknown": all.filter(victim_age__in=["Don't know",""]).count(),
    }
    age_range = sorted(age_range.items(), key=operator.itemgetter(0))


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
    }
    employment = sorted(employment.items(), key=operator.itemgetter(1), reverse=True)
    employment.append(('Other', all.filter(victim_employment_11='1').count()))
    

    no_action_pursued_reason = {
      "Not Applicable": all.filter(no_action_pursued_reason_0='1').count(),
      "Afraid of retaliation": all.filter(no_action_pursued_reason_1='1').count(),
      "Believed it would have been ineffective": all.filter(no_action_pursued_reason_2='1').count(),
      "Didn’t know what to do": all.filter(no_action_pursued_reason_3='1').count(),
      "Couldn’t Afford": all.filter(no_action_pursued_reason_4='1').count(),
      "Other": all.filter(no_action_pursued_reason_6='1').count(),
    }
    no_action_pursued_reason = sorted(no_action_pursued_reason.items(), key=operator.itemgetter(1), reverse=True)


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

    children = {
      "No": all.filter(victim_children='0').count(),
      "Yes": all.filter(victim_children__gte='1').count(),
    }
    children = sorted(children.items(), key=operator.itemgetter(1), reverse=True)

    total_children = all.filter(victim_children__gte='1').aggregate(Sum('victim_children'))
    total_children = int( total_children['victim_children__sum'] )

    genuine_encounter = all.filter(genuine_encounters='1').count()
    not_genuine_encounter = all.filter(genuine_encounters='0').count()
    militant = all.filter(victim_militant_status='1').count()
    not_militant = all.filter(victim_militant_status='0').count()
    militant_support = all.filter(victim_militant_support='1',victim_militant_status='0').count()
    no_militant_support = all.filter(victim_militant_support='0',victim_militant_status='0').count()
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

    securityoff_id_known = all.filter( Q(securityoff_id_known='1') | Q(securityforces_idknown__in=['1','2']) ).count()
    no_securityoff_id_known = all.filter( Q(securityoff_id_known='0') | Q(securityforces_idknown='3') ).count()

    so_body_disposal = {
      "Cremated the body": all.filter(so_body_disposal='1').count(),
      "Dumped body in canal or river": all.filter(so_body_disposal='2').count(),
      "Dumped body in well or drain": all.filter(so_body_disposal='3').count(),
      "Buried the body": all.filter(so_body_disposal='4').count(),
      "Other": all.filter(so_body_disposal='6').count(),
    }
    so_body_disposal = sorted(so_body_disposal.items(), key=operator.itemgetter(1), reverse=True)


    witness_arrest_no = all.filter(witness_arrest_0 ='1').count()

    witness_arrest_yes = all.filter(Q(witness_arrest_1='1') | \
        Q(witness_arrest_2='1') | \
        Q(witness_arrest_3='1') | \
        Q(witness_arrest_4='1') | \
        Q(witness_arrest_5='1') | \
        Q(witness_arrest_6='1') | \
        Q(witness_arrest_7='1') | \
        Q(witness_arrest_8='1') | \
        Q(witness_arrest_9='1') | \
        Q(witness_arrest_10='1') | \
        Q(witness_arrest_12='1') ).count()

    witness_arrest = {
      "No": witness_arrest_no,
      "Yes": witness_arrest_yes,
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
      "Criminal Investigation Agency Staff": all.filter(victim_arrest_location='2').count(),
      "<span define=\"Border Security Force\">BSF</span>": all.filter(victim_arrest_location='3').count(),
      "<span define=\"Central Reserve Police Force\">CRPF</span> Camp": all.filter(victim_arrest_location='4').count(),
      "Army Camp": all.filter(victim_arrest_location='5').count(),
      "<span define=\"Unofficial interrogation location\">Interrogation Center</span>": all.filter(victim_arrest_location='6').count(),
      "Other": all.filter(victim_arrest_location='8').count(),
    }
    detention_facility_type = sorted(detention_facility_type.items(), key=operator.itemgetter(1), reverse=True)


    arrest_security_type = {
      "Punjab Police": all.filter(arrest_security_type_1='1').count(),
      "<span define=\"Border Security Force\">BSF</span>": all.filter(arrest_security_type_2='1').count(),
      "<span define=\"Central Reserve Police Force\">CRPF</span>": all.filter(arrest_security_type_3='1').count(),
      "Army": all.filter(arrest_security_type_4='1').count(),
      "Criminal Investigation Agency": all.filter(arrest_security_type_5='1').count(),
      "<span define=\"Irregular undercover security force, often consisting of criminals\">Black cat</span>": all.filter(arrest_security_type_6='1').count(),
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
      "<span define=\"Border Security Force\">BSF</span>": all.filter(killing_securityforcestype_2='1').count(),
      "<span define=\"Central Reserve Police Force\">CRPF</span>": all.filter(killing_securityforcestype_3='1').count(),
      "Army": all.filter(killing_securityforcestype_4='1').count(),
      "Criminal Investigation Agency": all.filter(killing_securityforcestype_5='1').count(),
      "<span define=\"Irregular undercover security force, often consisting of criminals\">Black cat</span>": all.filter(killing_securityforcestype_6='1').count(),
      "Other": all.filter(killing_securityforcestype_8='1').count(),
    }
    killing_securityforcestype = sorted(killing_securityforcestype.items(), key=operator.itemgetter(1), reverse=True)


    security_official_response = {
      "Gave no response": all.filter(security_official_response_0='1').count(),
      "Killed victim in an “encounter”": all.filter(security_official_response_1='1').count(),
      "Denied involvement": all.filter(security_official_response_2='1').count(),
      "Admitted extrajudicial execution with no explanation": all.filter(security_official_response_3='1').count(),
      "Admitted custody only": all.filter(security_official_response_4='1').count(),
      "Victim had escaped": all.filter(security_official_response_5='1').count(),
      "Victim killed will trying to escape": all.filter(security_official_response_6='1').count(),
      "Victim killed by militants": all.filter(security_official_response_7='1').count(),
      "Told family to go to another police station": all.filter(security_official_response_8='1').count(),
      "Victim killed in crossfire with militants": all.filter(security_official_response_9='1').count(),
      "Victim accidentally killed in custody": all.filter(security_official_response_10='1').count(),
      "Victim killed while resisting arrest/search": all.filter(security_official_response_11='1').count(),
      "Victim killed by <span define=\"Irregular undercover security force, often consisting of criminals\">Black cat</span>s": all.filter(security_official_response_12='1').count(),
      "Other": all.filter(security_official_response_13='1').count(),
    }
    security_official_response = sorted(security_official_response.items(), key=operator.itemgetter(1), reverse=True)

    
    
    total = all.values('record_id').count()

    return {
      "age_range": age_range,
      "arrest_security_type": arrest_security_type,
      "caste": caste,
      "children": children,
      "total_children": total_children,
      "condition_of_remains": condition_of_remains,
      "court_or_commission": court_or_commission,
      "detention_facility_type": detention_facility_type,
      "education": education,
      "employment": employment,
      "female": female,
      "genuine_encounter": genuine_encounter,
      "govnt_response_desired": govnt_response_desired,
      "judge_or_magistrate_status": judge_or_magistrate_status,
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
      "so_body_disposal": so_body_disposal,
      "so_inform_witnesses": so_inform_witnesses,
      "so_return_body": so_return_body,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "total": total,
      "victim_arrest_location": victim_arrest_location,
      "victim_arrest_status": victim_arrest_status,
      "victim_detention_loc_known": victim_detention_loc_known,
      "victim_militant_support_forced": victim_militant_support_forced,
      "victim_militant_support_voluntary": victim_militant_support_voluntary,
      "victim_militant_support": victim_militant_support,
      "witness_arrest": witness_arrest,
      "witness_detention": witness_detention,
      }

