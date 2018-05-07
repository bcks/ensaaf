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
      "0-10": all.filter(victim_age_averaged__gte=0,victim_age_averaged__lte=10).count(),
      "11-20": all.filter(victim_age_averaged__gte=11,victim_age_averaged__lte=20).count(),
      "21-30": all.filter(victim_age_averaged__gte=21,victim_age_averaged__lte=30).count(),
      "31-40": all.filter(victim_age_averaged__gte=31,victim_age_averaged__lte=40).count(),
      "41-50": all.filter(victim_age_averaged__gte=41,victim_age_averaged__lte=50).count(),
      "51-60": all.filter(victim_age_averaged__gte=51,victim_age_averaged__lte=60).count(),
      "61-70": all.filter(victim_age_averaged__gte=61,victim_age_averaged__lte=70).count(),
      "71-80": all.filter(victim_age_averaged__gte=71,victim_age_averaged__lte=80).count(),
      "81-90": all.filter(victim_age_averaged__gte=81,victim_age_averaged__lte=90).count(),
      "91-100": all.filter(victim_age_averaged__gte=91,victim_age_averaged__lte=100).count(),
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

    witness_detention_3 = all.filter(where_victim_detained__witness_detention_3='1').count()
    witness_detention_4 = all.filter(where_victim_detained__witness_detention_4='1').count()
    witness_detention_5 = all.filter(where_victim_detained__witness_detention_5='1').count()
    witness_detention_6 = all.filter(where_victim_detained__witness_detention_6='1').count()
    witness_detention_7 = all.filter(where_victim_detained__witness_detention_7='1').count()
    witness_detention_8 = all.filter(where_victim_detained__witness_detention_8='1').count()
    witness_detention_9 = all.filter(where_victim_detained__witness_detention_9='1').count()
    witness_detention_10 = all.filter(where_victim_detained__witness_detention_10='1').count()
    witness_detention_11 = all.filter(where_victim_detained__witness_detention_11='1').count()
    witness_detention_12 = all.filter(where_victim_detained__witness_detention_12='1').count()
    witness_detention_13 = all.filter(where_victim_detained__witness_detention_13='1').count()
    witness_detention_14 = all.filter(where_victim_detained__witness_detention_14='1').count()

    witness_detention = {
      "Interviewee": witness_detention_3,
      "Other relative": witness_detention_4,
      "Other detainee": witness_detention_5,
      "Sarpanch/politician": witness_detention_6,
      "Newspaper": witness_detention_7,
      "Security official": witness_detention_8,
      "Friend": witness_detention_9,
      "Other witness": witness_detention_10,
      "Interview belief (no source)": witness_detention_11,
      "Doctor": witness_detention_12,
      "Other victim family": witness_detention_13,
      "Other": witness_detention_14,
    }
    witness_detention = sorted(witness_detention.items(), key=operator.itemgetter(1), reverse=True)
    
    total = all.values('record_id').count()

    return {
      "total": total,
      "total_disappeared": total_disappeared,
      "total_killed": total_killed,
      "male": male,
      "female": female,
      "married": married,
      "not_married": not_married,
      "religion": religion,
      "caste": caste,
      "education": education,
      "employment": employment,
      "age_range": age_range,
      "children": children,
      "genuine_encounter": genuine_encounter,
      "not_genuine_encounter": not_genuine_encounter,
      "kesdhari": kesdhari,
      "amritdhari": amritdhari,
      "militant": militant,
      "not_militant": not_militant,
      "militant_support": militant_support,
      "no_militant_support": no_militant_support,
      "prior_detentions": prior_detentions,
      "no_prior_detentions": no_prior_detentions,
      "security_officials_apprchd": security_officials_apprchd,
      "no_security_officials_apprchd": no_security_officials_apprchd,
      "court_or_commission": court_or_commission,
      "no_court_or_commission": no_court_or_commission,
      "victim_militant_support": victim_militant_support,
      "no_victim_militant_support": no_victim_militant_support,
      "victim_militant_support_voluntary": victim_militant_support_voluntary,
      "victim_militant_support_forced": victim_militant_support_forced,
      "victim_militant_reason": victim_militant_reason,
      "victim_arrest_status": victim_arrest_status,
      "no_victim_arrest_status": no_victim_arrest_status,
      "so_inform_witnesses": so_inform_witnesses,
      "no_so_inform_witnesses": no_so_inform_witnesses,
      "security_forces_uniformed": security_forces_uniformed,
      "no_security_forces_uniformed": no_security_forces_uniformed,
      "judge_or_magistrate_status": judge_or_magistrate_status,
      "no_judge_or_magistrate_status": no_judge_or_magistrate_status,
      "victim_detention_loc_known": victim_detention_loc_known,
      "no_victim_detention_loc_known": no_victim_detention_loc_known,
      "so_return_body": so_return_body,
      "no_so_return_body": no_so_return_body,
      "securityoff_id_known": securityoff_id_known,
      "no_securityoff_id_known": no_securityoff_id_known,

      "so_body_disposal": so_body_disposal,
      
      "witness_arrest": witness_arrest,
      "witness_total": witness_total,
      "witness_detention": witness_detention,

      "number_of_victims": number_of_victims,
      }

