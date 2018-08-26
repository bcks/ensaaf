import re
from django import template

register = template.Library()


monthNames = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",\
  "November", "December","13####","14####","15####","16####","17####","18####","19####",\
  "20####","21####","22####","23####","24####","25####","26####","27####","28####","29####",
  "30####","31####","32####","33####","34####","35####","36####","37####","38####","39####",
  "40####","41####","42####","43####","44####","45####","46####","47####","48####","49####",]


@register.simple_tag()
def sex(var):
    if var == 1:
      return 'Male'
    if var == 2:
      return 'Female'
    return



@register.filter(name='uncensus')
def uncensus(value):
    return re.sub(r'([0123456789.]+)-','', value)


# moved to views
#@register.simple_tag()
#def hvictim_address_other(value):
#  str = value.split('_')
#  str = str[0]
#  str = re.sub(r'([0123456789.]+)-','', str)
#  # TODO get VILLAGE FROM CENSUS CODE
#  village = Villages.objects.filter(id=village_id).get()
#  print (village)  
#  return str



@register.filter(name='censuslink')
def censuslink(value):
    
    # split on comma
    parts = value.split(',')
    
    # make href from each census-ed name
    regexp = re.compile(r'([0123456789]+)-')
    newparts = []
    for part in parts:
      if regexp.search(part):
        newparts.append(
          '<a href="/locality/' + regexp.search(part).group(1)  + '">' + \
           re.sub(r'([0123456789.]+)-','', part) + \
           '</a>')

    s = ", ";
    return s.join(newparts)



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

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ' on ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ' on ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';


@register.simple_tag()
def hdate(var):
  if (var == 'Don\'t know'):
    return ', date unknown'
  if (var == ''):
    return ', date unknown'

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ',  ' +  str(parts[5])

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2]) + ' and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ',  ' +  str(parts[5])

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ' on ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', ' +  str(parts[2])

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ' on ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', ' +  str(parts[2])




@register.simple_tag()
def hdateslash(start, end):
  if (start == None):
    return 'date unknown'
  start = str(start).split('-')[0]
  end = str(end).split('-')[0]
  if start == end:
    return start
  else:
    return start + '-' + end



@register.simple_tag()
def hyear(var):
  if (var == 'Don\'t know'):
    return ', date unknown'
  if (var == ''):
    return ', date unknown'

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return ', ' + str(parts[5])

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return ', ' + str(parts[5])

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ', ' + str(parts[2])

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ', ' + str(parts[2])




@register.simple_tag()
def heducation(value):
  education  = ['No education','Primary school','Middle school','High school','High school','High school','Some college','College degree','Graduate diploma','Vocational degree','Vocational degree','Don’t know']
  return education[value]



@register.simple_tag()
def hphoto(value):
  value = value.replace('\n', '').replace('\r', '')
  names = value.split(',')
  s = "";
  photos = []
  path = 'https://data.ensaaf.org/static/photos'
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


@register.filter(name='smallparen')
def smallparen(value):
    value = re.sub('\(','<div class="smallparen">(', value)
    value = re.sub('\)',')</div>', value)
    return value

@register.filter(name='unparen')
def unparen(value):
    return re.sub(r' \(.+\)','', value)

@register.filter(name='lowercaselocationwithheld')
def lowercaselocationwithheld(value):
    if value == 'Location withheld':
      return 'location withheld'
    else:
      return value



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
  groups.append('Victim gave support to militants') if v3 == 1 else 0
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
  caste = ['', '<span define="A caste associated with agriculture">Jat</span>','Ramgarhia','Dalit/SC/BC','Mazbi','Chamar','Khatri','Naee','Don’t know','Other']
  return caste[value]



@register.simple_tag()
def hreligion(value):
  religion = ['','Sikh','Hinduism','Islam','Christianity','No religion','Don’t know','Other']
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

  if (victim_arrest_date == 'Don\'t know'):
    return ', date unknown'
  if (victim_arrest_date == ''):
    return ', date unknown'

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in victim_arrest_date and '-' in victim_arrest_date:
    victim_arrest_date = victim_arrest_date.replace('/','-')
    parts = victim_arrest_date.split('-')
    return ' between ' + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[3])] + ' ' + str(int(parts[4])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in victim_arrest_date:
    victim_arrest_date = victim_arrest_date.replace(' ','')
    parts = victim_arrest_date.split('-')
    return ' between ' + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a> and ' + monthNames[int(parts[4])] + ' ' + str(int(parts[3])) + ',  <a href="/year/'+str(parts[5])+'">' +  str(parts[5]) + '</a>'

  around = ''
  if victim_arrest_exact_date != '' and victim_arrest_exact_date == 0 or victim_arrest_exact_date == 9:
    around = ' around '

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in victim_arrest_date:
    parts = victim_arrest_date.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return around + monthNames[int(parts[1])] + ' ' + str(int(parts[0])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in victim_arrest_date:
    parts = victim_arrest_date.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return around + monthNames[int(parts[0])] + ' ' + str(int(parts[1])) + ', <a href="/year/'+str(parts[2])+'">' +  str(parts[2]) + '</a>';

  return ''



@register.simple_tag()
def hwitness_arrest(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v12, other):
  groups = []
  
  if v0 == 1 or v12 == 1:
    groups.append('Unknown')
    
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
  groups.append('<a href="/securityforce/police/">Punjab Police</a>') if v1 == 1 else 0
  groups.append('<a href="/securityforce/bsf/"><span define="Border Security Force">BSF</span></a>') if v2 == 1 else 0
  groups.append('<a href="/securityforce/crpf/"><span define="Central Reserve Police Force">CRPF</span></a>') if v3 == 1 else 0
  groups.append('<a href="/securityforce/army/">Army</a>') if v4 == 1 else 0
  groups.append('<a href="/securityforce/cia/">Criminal Investigation Agency</a>') if v5 == 1 else 0
  groups.append('<a href="/securityforce/black-cat/"><span define="Irregular undercover security force, often consisting of criminals">Black cat</span></a>') if v6 == 1 else 0
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
  groups.append('Same as officials involved in abduction/extrajudicial execution') if v1 == 1 else 0
  groups.append('<a href="/securityforce/police/">Punjab Police</a>') if v2 == 1 else 0
  groups.append('<a href="/securityforce/bsf/"><span define="Border Security Force">BSF</span></a>') if v3 == 1 else 0
  groups.append('<a href="/securityforce/crpf/"><span define="Central Reserve Police Force">CRPF</span></a>') if v4 == 1 else 0
  groups.append('<a href="/securityforce/army/">Army</a>') if v5 == 1 else 0
  groups.append('<a href="/securityforce/cia/">Criminal Investigation Agency</a>') if v6 == 1 else 0
  groups.append('<a href="/securityforce/black-cat/"><span define="Irregular undercover security force, often consisting of criminals">Black cat</span></a>') if v7 == 1 else 0
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
  location = ['', '', 'Victim\'s residence', 'Friend/relative\'s residence', 'Checkpoint (naka)', 'Roadside', 'Village fields', 'Shop/market', 'Bus station/stand', 'Police station', 'Village drain']
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
def hdemands(v2, v3, v4, v5, v6, v7, v8, v10, other):
  groups = []
  # groups.append('None') if v1 == 1 else 0
  groups.append('Money') if v2 == 1 else 0
  groups.append('Information about another person') if v3 == 1 else 0
  groups.append('Forced identification of another person') if v4 == 1 else 0
  groups.append('Another person must turn himself in') if v5 == 1 else 0
  groups.append('Signature on blank papers') if v6 == 1 else 0
  groups.append('Valuables (jewelry/electronics/land/etc.)') if v7 == 1 else 0
  groups.append('Land') if v8 == 1 else 0
  # groups.append('Don’t know') if v9 == 1 else 0
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
  groups.append('Extrajudicial execution [of victim] in an "encounter"') if v1 == 1 else 0
  groups.append('Denied involvement') if v2 == 1 else 0
  groups.append('Admitted extrajudicial execution with no explanation') if v3 == 1 else 0
  groups.append('Admitted custody only') if v4 == 1 else 0
  groups.append('Victim had escaped') if v5 == 1 else 0
  groups.append('Victim extrajudicial execution will trying to escape') if v6 == 1 else 0
  groups.append('Victim extrajudicial execution by militants') if v7 == 1 else 0
  groups.append('Told family to go to another police station') if v8 == 1 else 0
  groups.append('Victim extrajudicial execution in crossfire with militants') if v9 == 1 else 0
  groups.append('Victim accidentally killed in custody') if v10 == 1 else 0
  groups.append('Victim extrajudicial execution while resisting arrest/search') if v11 == 1 else 0
  groups.append('Victim extrajudicial execution by <span define="Irregular undercover security force, often consisting of criminals">black cat</span>s') if v12 == 1 else 0
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
      return "None"



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
  groups.append('Family members ran away') if v2 == 1 else 0
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
  groups.append('Rehabilitation services to family') if v2 == 1 else 0
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
def hothers_killed(v0, v1, v2, v3):
  if v0 == 1:
    return('No')
  if v1 == 1:
    return('Yes')
  if v2 == 1:
    return('Yes')
  if v3 == 1:
    return('Yes')
#  if v9 == 1:
#    return('Unknown')
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
      groups.append('<span define="Head of the village council">Sarpanch</span>/politician')

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
  opt = ['','Police station/post','Criminal Investigation Agency staff','<span define="Border Security Force">BSF</span>','<span define="Central Reserve Police Force">CRPF</span> camp','Army camp','<span define="Unofficial interrogation location">Interrogation center</span>','Don’t know','Other']
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
  affilation = ['','Punjab Police','<span define="Border Security Force">BSF</span>','<span define="Central Reserve Police Force">CRPF</span>','Army','Criminal Investigation Agency','<span define="Irregular undercover security force, often consisting of criminals">Black Cat</span>','Don’t Know','Other']
  return affilation[var];



@register.simple_tag()
def percent(item1, total):
    if total == 0:
      return 0
    try:
        return "%.1f" % ((float(item1) / float(total)) * 100)
    except ValueError:
        return ''



@register.simple_tag()
def dump(var):
    return vars(var)


