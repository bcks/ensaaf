from django.db.models import Count
import operator


def calculate_stats(all):
    total_disappeared = all.filter(victim_disappeared_killed='1').count()
    total_killed = all.filter(victim_disappeared_killed='2').count()
    male = all.filter(victim_sex='1').count()
    female = all.filter(victim_sex='2').count()
    married = all.filter(victim_marital_status='1').count()
    not_married = all.filter(victim_marital_status='0').count()
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
    securityoff_id_known = all.filter(victim_arrest_status='1').count()
    no_securityoff_id_known = all.filter(victim_arrest_status='0').count()

    so_body_disposal_1 = all.filter(so_body_disposal='1').count()
    so_body_disposal_2 = all.filter(so_body_disposal='2').count()
    so_body_disposal_3 = all.filter(so_body_disposal='3').count()
    so_body_disposal_4 = all.filter(so_body_disposal='4').count()
    so_body_disposal_6 = all.filter(so_body_disposal='6').count()

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
      "Relative": witness_detention_4,
      "Other Detainee": witness_detention_5,
      "Sarpanch/politician": witness_detention_6,
      "Newspaper": witness_detention_7,
      "Security official": witness_detention_8,
      "Friend": witness_detention_9,
      "Other witness": witness_detention_10,
      "Interview Belief (No Source)": witness_detention_11,
      "Doctor": witness_detention_12,
      "Other Victim Family": witness_detention_13,
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
      "so_body_disposal_1": so_body_disposal_1,
      "so_body_disposal_2": so_body_disposal_2,
      "so_body_disposal_3": so_body_disposal_3,
      "so_body_disposal_4": so_body_disposal_4,
      "so_body_disposal_6": so_body_disposal_6,
      
      "witness_arrest": witness_arrest,
      "witness_detention": witness_detention,

      "number_of_victims": number_of_victims,
      }

