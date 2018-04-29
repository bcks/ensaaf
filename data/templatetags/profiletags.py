import re
from django import template

register = template.Library()


monthNames = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]


@register.simple_tag()
def sex(var):
    if var == 1:
      return 'Male'
    if var == 2:
      return 'Female'
    return



@register.simple_tag()
def hyes_no(var):
    opt = ["No", "Yes", "", "", "", "", "", "", "", "Don’t know"]
    return opt[var]



@register.simple_tag()
def hyes_no_unknown(var):
    opt = ["No", "Yes", "", "", "", "", "", "", "", "Unknown"]
    return opt[var]



@register.simple_tag()
def hyes_no_na(var):
    opt = ["", "Yes", "No", "Don’t know", "", "", "", "", "", "N/A"]
    return opt[var]




@register.simple_tag()
def hdate_link(var):
  if (var == 'Don\'t know'):
    return ', date unknown'
  if (var == ''):
    return ', date unknown'
  var = var.replace('/','-')
  parts = var.split('-')
  if (len(parts) > 3):
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if int(parts[5]) < 1900:
      parts[5] = int(parts[5]) + 1900

    if (int(parts[1]) > 12):
      return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'
    else:
      return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'
  else:
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if (int(parts[1]) > 12):
      return ' on ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';
    else:
      return ' on ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';



@register.simple_tag()
def hdate(var):
  if (var == 'Don\'t know'):
    return ', date unknown'
  if (var == ''):
    return ', date unknown'
  var = var.replace('/','-')
  parts = var.split('-')
  if (len(parts) > 3):
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if int(parts[5]) < 1900:
      parts[5] = int(parts[5]) + 1900

    if (int(parts[1]) > 12):
      return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ', ' +  str(parts[5])
    else:
      return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ', ' +  str(parts[5])
  else:
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if (int(parts[1]) > 12):
      return ' on ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2]);
    else:
      return ' on ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2]);




@register.simple_tag()
def hvictim_address_other(value):
  str = value.split('_')
  str = str[0]
  # TODO get VILLAGE FROM CENSUS CODE
  return str



@register.simple_tag()
def heducation(value):
  education  = ['No education','Primary school/5th standard','Middle school/8th standard','High school/matriculated','10 plus 1','10 plus 2/senior secondary','Some college','Bachelor’s degree','Master’s/graduate diploma','Vocational diploma','Giyani','Don’t know']
  return education[value]



@register.simple_tag()
def hphoto(value):
  value = value.replace('\n', '').replace('\r', '')
  names = value.split(',')
  s = "";
  photos = []
  path = 'http://graphonomy.com/ensaaf/photos'
  if value:
    for n in names:
      thisName = n.strip()
      first_dir = re.findall('([A-Z]+)', thisName)
      second_dir = re.findall("([^-]+)", thisName)
      if not second_dir:
        second_dir = first_dir
      photopath = path + '/' + first_dir[0] + '/' + second_dir[0] + '/' + thisName + '.jpg'
      photos.append(photopath)
    return s.join(photos)
  else:
    return ''



@register.simple_tag()
def hvictim_militant_reason(v1, v2, v3, v4, v5, v6, v7, v8, other):
  groups = []
  groups.append('1984 Indian Army attack on the Harmandir Sahib') if v1 == 1 else 0
  groups.append('Persecution (i.e. arbitrary arrest, torture, self-defense)') if v2 == 1 else 0
  groups.append('Persecution of a family member or a friend') if v3 == 1 else 0
  groups.append('General persecution of Sikhs') if v4 == 1 else 0
  groups.append('Supported the goals of the militancy movement') if v5 == 1 else 0
  groups.append('Was forced to join') if v6 == 1 else 0
  groups.append('Don’t know') if v7 == 1 else 0
  if v8 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''


@register.simple_tag()
def hvictim_employment(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, other):
  groups = []
  groups.append('Farmer/agriculture') if v1 == 1 else 0
  groups.append('Shopkeeper') if v2 == 1 else 0
  groups.append('Day laborer') if v3 == 1 else 0
  groups.append('Driver (bus/truck/car)') if v4 == 1 else 0
  groups.append('Mechanic') if v5 == 1 else 0
  groups.append('Student') if v6 == 1 else 0
  groups.append('Housewife') if v7 == 1 else 0
  groups.append('Carpenter') if v8 == 1 else 0
  groups.append('Unemployed') if v9 == 1 else 0
  groups.append('Don’t know') if v10 == 1 else 0
  if v11 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def htarget_reason(v1, v2, v3, v4, v5, v6, v7, v8, v9, other):
  groups = []
  groups.append('Victim was a militant') if v1 == 1 else 0
  groups.append('Victim was related to a militant') if v2 == 1 else 0
  groups.append('Victim gave support to a militant') if v3 == 1 else 0
  groups.append('Victim was involved in criminal activities') if v4 == 1 else 0
  groups.append('Victim was identifiably Sikh') if v5 == 1 else 0
  groups.append('Security forces thought victim was a militant') if v6 == 1 else 0
  groups.append('Mistaken for a wanted individual') if v7 == 1 else 0
  groups.append('Don’t know') if v8 == 1 else 0
  if v9 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hcaste(value):
  caste = ['', 'Jat','Ramgarhia','Dalit/SC/BC','Mazbi','Chamar','Khatri','Naee','Don’t know','Other']
  return caste[value]



@register.simple_tag()
def hreligion(value):
  religion = ['','Sikhism','Hinduism','Islam','Christianity','No religion','Don’t know','Other']
  return religion[value]



@register.simple_tag()
def hforced(value):
  forced = ['','Voluntary','Forced','Don’t know','','','','','','N/A']
  return forced[value]



@register.simple_tag()
def hvictim_arrest_status(value):
  status = ['','Yes','Yes, the victim turned himself/herself in','No','Unknown']
  return status[value]



@register.simple_tag()
def hvictim_arrest_date(victim_arrest_exact_date, victim_arrest_date):
  if (victim_arrest_date == "Don't know"):
    return ' '
  parts = victim_arrest_date.split('-');
  if (len(parts) > 3):
    return ' '
  if victim_arrest_exact_date != '' and victim_arrest_exact_date == 0 or victim_arrest_exact_date == 9:
    return ' around '
  return ' '



@register.simple_tag()
def hdate_no_on(var):
  if (var == 'Don\'t know'):
    return ', date unknown'
  if (var == ''):
    return ', date unknown'
  var = var.replace('/','-')
  parts = var.split('-')
  if (len(parts) > 3):
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if int(parts[5]) < 1900:
      parts[5] = int(parts[5]) + 1900
    if (int(parts[1]) > 12):
      return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ', ' +  str(parts[5])
    else:
      return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ', ' +  str(parts[5])
  else:
    if int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    if (int(parts[1]) > 12):
      return monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2])
    else:
      return monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2])
  return



@register.simple_tag()
def hwitness_arrest(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v12, other):
  groups = []
  groups.append('Spouse') if v1 == 1 else 0
  groups.append('Parents') if v2 == 1 else 0
  groups.append('Children') if v3 == 1 else 0
  groups.append('Sibling') if v4 == 1 else 0
  groups.append('Grandparent') if v5 == 1 else 0
  groups.append('Cousin') if v6 == 1 else 0
  groups.append('Aunt/uncle') if v7 == 1 else 0
  groups.append('Friend') if v8 == 1 else 0
  groups.append('Co-villager') if v9 == 1 else 0
  groups.append('Respondent') if v10 == 1 else 0
  groups.append('Unknown') if v12 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def harrest_security_type(v1, v2, v3, v4, v5, v6, v7, other):
  groups = []
  groups.append('Punjab Police') if v1 == 1 else 0
  groups.append('BSF') if v2 == 1 else 0
  groups.append('CRPF') if v3 == 1 else 0
  groups.append('Army') if v4 == 1 else 0
  groups.append('CIA') if v5 == 1 else 0
  groups.append('Black cat') if v6 == 1 else 0
  groups.append('Don’t know') if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hso_approached_type(v1, v2, v3, v4, v5, v6, v7, other):
  groups = []
  groups.append('Same as officials involved in abduction/killing') if v1 == 1 else 0
  groups.append('Punjab Police') if v2 == 1 else 0
  groups.append('BSF') if v3 == 1 else 0
  groups.append('CRPF') if v4 == 1 else 0
  groups.append('Army') if v5 == 1 else 0
  groups.append('CIA') if v6 == 1 else 0
  groups.append('Black cat') if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hadd_spaces(value):
    terms = value.split(',')
    s = ', '
    return s.join(terms)



@register.simple_tag()
def hvictim_arrest_location(value):
  location = ['', '', 'Victim\'s residence', 'Friend/relative\'s residence', 'Checkpoint (naka)', 'Roadside', 'Village fields', 'Market/bazaar', 'Bus station/stand', 'Police station', 'Village drain']
  return location[value]



@register.simple_tag()
def hso_return_body(value):
  so_return_body = ['','Yes','Yes, but forced immediate cremation','No','Don’t know']
  return so_return_body[value]



@register.simple_tag()
def hso_body_disposal(value):
  so_body_disposal = ['','Cremated the body','Dumped body in canal/river','Dumped body in well/drain','Buried the body','Don’t know','Other']
  return so_body_disposal[value]



@register.simple_tag()
def hcremation_location_type(value):
  cremation_location_type = ['','Municipal cremation ground','Village cremation ground','Gurdwara cremation ground','Don’t know','Other']
  return cremation_location_type[value]



@register.simple_tag()
def hcondition_of_remains(v1, v2, v3, v4, v5, v6, v7, other):
  groups = []
  groups.append('Bruises') if v1 == 1 else 0
  groups.append('Bullet wounds') if v2 == 1 else 0
  groups.append('Cuts/wounds') if v3 == 1 else 0
  groups.append('Broken bones') if v4 == 1 else 0
  groups.append('Missing hair from head or face') if v5 == 1 else 0
  groups.append('Missing fingernails') if v6 == 1 else 0
  groups.append('Burn marks') if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hdemands(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, other):
  groups = []
  groups.append('None') if v1 == 1 else 0
  groups.append('Money') if v2 == 1 else 0
  groups.append('Information about another person') if v3 == 1 else 0
  groups.append('Forced identification of another person') if v4 == 1 else 0
  groups.append('Another person must turn himself in') if v5 == 1 else 0
  groups.append('Signature on blank papers') if v6 == 1 else 0
  groups.append('Valuables (jewelry/electronics/land/etc.)') if v7 == 1 else 0
  groups.append('Land') if v8 == 1 else 0
  groups.append('Don’t know') if v9 == 1 else 0
  if v10 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hjudge_or_magistrate_result(v1, v2, v3, v4, other):
  groups = []
  groups.append('Jail') if v1 == 1 else 0
  groups.append('Police custody/remand') if v2 == 1 else 0
  groups.append('Don’t know') if v3 == 1 else 0
  if v4 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hsecurity_official_response(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, other):
  groups = []
  groups.append('No Response') if v0 == 1 else 0
  groups.append('Killed [victim] in an "encounter"') if v1 == 1 else 0
  groups.append('Denied involvement') if v2 == 1 else 0
  groups.append('Admitted killing with no explanation') if v3 == 1 else 0
  groups.append('Admitted custody only') if v4 == 1 else 0
  groups.append('Victim had escaped') if v5 == 1 else 0
  groups.append('Victim killed will trying to escape') if v6 == 1 else 0
  groups.append('Victim killed by militants') if v7 == 1 else 0
  groups.append('Told family to go to another police station') if v8 == 1 else 0
  groups.append('Victim killed in crossfire with militants') if v9 == 1 else 0
  groups.append('Victim accidentally killed in custody') if v10 == 1 else 0
  groups.append('Victim killed while resisting arrest/search') if v11 == 1 else 0
  groups.append('Victim killed by black cats') if v12 == 1 else 0
  groups.append('Don’t know') if v14 == 1 else 0
  if v3 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append('Other')
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return 0



@register.simple_tag()
def hno_action_pursued_reason(v1, v2, v3, v4, other):
  groups = []
  groups.append('Afraid of retaliation') if v1 == 1 else 0
  groups.append('Believed it would have been ineffective') if v2 == 1 else 0
  groups.append('Did not know what to do') if v3 == 1 else 0
  groups.append('Insufficient funds') if v4 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hfamily_effects(v1, v2, v3, v4, v5, v6, v7, v8, v9, v12, other):
  groups = []
  groups.append('No drastic action') if v1 == 1 else 0
  groups.append('Family member(s) ran away') if v2 == 1 else 0
  groups.append('Family member(s) engaged in militant activity') if v3 == 1 else 0
  groups.append('Family member(s) dropped out of school') if v4 == 1 else 0
  groups.append('Family member(s) abused alcohol/drugs') if v5 == 1 else 0
  groups.append('Family member(s) committed suicide') if v6 == 1 else 0
  groups.append('Family abandoned home') if v7 == 1 else 0
  groups.append('Family member(s) died due to depression/shock') if v8 == 1 else 0
  groups.append('Family member(s) was mentally disturbed') if v9 == 1 else 0
  groups.append('Family became impoverished') if v12 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hgovnt_response_desired(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, other):
  groups = []
  groups.append('Monetary compensation to family') if v1 == 1 else 0
  groups.append('Rehabilitation services to family members') if v2 == 1 else 0
  groups.append('Public acknowledgement of wrongful deaths') if v3 == 1 else 0
  groups.append('Criminal prosecution of those responsible') if v4 == 1 else 0
  groups.append('Employment') if v5 == 1 else 0
  groups.append('Truth commission') if v6 == 1 else 0
  groups.append('Investigations into abuses') if v7 == 1 else 0
  groups.append('Memorial for victims') if v8 == 1 else 0
  groups.append('Desire nothing from government') if v9 == 1 else 0
  groups.append('Don’t know') if v11 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hothers_arrested(value):
  others_arrested = ['No','Yes','Yes','','','','','','','Unknown']
  return others_arrested[value]



@register.simple_tag()
def hothers_killed(v0, v1, v2, v3, v9):
  if v0 == 1:
    return('No')
  if v1 == 1:
    return('Yes')
  if v2 == 1:
    return('Yes')
  if v3 == 1:
    return('Yes')
  if v9 == 1:
    return('Unknown')
  return ''



@register.simple_tag()
def hwitness_detention(v3, v4, v5, v6, v7, v8, v9, v10, v12, v13, v14, other, status):
  groups = []

  if (v3 == 1):
    if (status):
      groups.append('SeenSeen by respondent')
    else:
      groups.append('Relative')

  if (v4 == 1):
    if (status):
      groups.append('Seen by relative')
    else:
      groups.append('Relative')

  if (v5 == 1):
    if (status):
      groups.append('Seen by other detainee')
    else:
      groups.append('Other detainee')

  if (v6 == 1):
    if (status):
      groups.append('Seen by sarpanch/politician')
    else:
      groups.append('Sarpanch/politician')

  if (v7 == 1):
    if (status):
      groups.append('Seen by newspaper')
    else:
      groups.append('Newspaper')

  if (v8 == 1):
    if (status):
      groups.append('Seen by security official')
    else:
      groups.append('Security official')

  if (v9 == 1):
    if (status):
      groups.append('Seen by friend')
    else:
      groups.append('Friend')

  if (v10 == 1):
    if (status):
      groups.append('Seen by other witness (non-relative)')
    else:
      groups.append('Other witness (non-relative)')

  # if (v11 == 1): groups.append('Respondent belief (no source)')

  if (v12 == 1):
    if (status):
      groups.append('Seen by doctor')
    else:
      groups.append('Doctor')

  if (v13 == 1):
    if (status):
      groups.append('Seen by other victim family')
    else:
      groups.append('Other victim family')

  if (other):
    if (status):
      groups.append('Seen by '+other)
    else:
      groups.append(other)

  if len(groups):
      s = ' '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hdetention_facility_type(var, other):
  opt = ['','Police station/post','CIA staff','BSF','CRPF camp','Army camp','Interrogation center','Don’t know','Other']
  if var == 8:
    if (other):
      return other
  return opt[var]



@register.simple_tag()
def hduration_of_detention(v1):
  try:
     val = int(v1)
     if val > 1:
      return v1 + ' days'
     else:
      return v1 + ' day'
  except ValueError:
     return v1.lower()



@register.simple_tag()
def harrest_so_rank(var):
  opt = ['','Inspector','Sub Inspector','Assistant Sub Inspector','Senior Superintendent of Police','Deputy Superintendent of Police','Station House Officer','Constable','Head Constable','Sepoy','DIG (Deputy Inspector General)','IG (Inspector General)','DGP (Director General of Police)','Other','Don’t know','Superintendent of Police']
  return opt[var]



@register.simple_tag()
def haffiliation(var):
  affilation = ['','Punjab Police','BSF','CRPF','Army','CIA','Black Cat','Don’t Know','Other']
  return affilation[var];



@register.simple_tag()
def percent(item1, total):
    try:
        return "%.1f" % ((float(item1) / float(total)) * 100)
    except ValueError:
        return ''



@register.simple_tag()
def dump(var):
    return vars(var)


