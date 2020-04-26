import re
import numbers
from django import template
from django.utils.translation import ugettext as _
from django.utils.translation import get_language

register = template.Library()


monthNames = ["", 'January', 'February', 'March', 'April', 'May',\
  'June', 'July', 'August', 'September', 'October', 'November',\
  'December',"13####","14####","15####","16####","17####","18####","19####",\
  "20####","21####","22####","23####","24####","25####","26####","27####","28####",\
  "29####", "30####","31####","32####","33####","34####","35####","36####","37####",\
  "38####","39####", "40####","41####","42####","43####","44####","45####","46####",\
  "47####", "48####","49####",]

monthNamesForPO = [_("January"), _("February"), _("March"), _("April"), _("May"), _("June"), _("July"), _("August"), _("September"), _("October"), _("November"), _("December")]


@register.simple_tag()
def sex(var):
  if var == 1:
    return _('Male')
  if var == 2:
    return _('Female')
  return




@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    if lang == 'en':
      return context['request'].path.replace('/pa/','/')    
    else:
      return '/' + lang + context['request'].path

def not_int(s):
    try: 
        int(s)
        return False
    except ValueError:
        return True



@register.filter()
def numpa(number_string):
#    if (get_language() == 'pa') and ( isinstance(number_string, numbers.Number) ):
    if not_int(number_string):
      number_string = number_string.lstrip('0')
    if (get_language() == 'pa'):
      number_string = str(number_string)
      dic = {'0':'੦','1':'੧','2':'੨','3':'੩','4':'੪','5':'੫',\
      '6':'੬','7':'੭','8':'੮','9':'੯','.':'.',',':',','-':'-'}
      return "".join([dic[c] for c in number_string])
    else:
      try:
        number_string = format(number_string, ",")
        return number_string
      except ValueError:       
        return number_string
        

@register.filter()
def yearpa(number_string):
    number_string = str(number_string)
    if (get_language() == 'pa') and (number_string == 'Date Unknown'):
        return _('Date Unknown')    
    if (get_language() == 'pa') and number_string.isdigit():      
      dic = {'0':'੦','1':'੧','2':'੨','3':'੩','4':'੪','5':'੫',\
      '6':'੬','7':'੭','8':'੮','9':'੯','.':'.',',':','}
      return "".join([dic[c] for c in number_string])
    else:
      return number_string


@register.filter(name='uncensus')
def uncensus(value):
    return re.sub(r'([0123456789.]+)-','', value)



# moved to views
#@register.simple_tag()
#def hvictim_address_other(value):



@register.filter(name='censuslink')
def censuslink(value):
          
    if value == None:
      return None

    lang = '/' + str(get_language())
    lang = lang.replace('/en-us','')
    
    if "," in value:
      # split on comma
      parts = value.split(',')
    
      # make href from each census-ed name
      regexp = re.compile(r'([0123456789]+)-')
      newparts = []
      for part in parts:
        if regexp.search(part):
          newparts.append(
            '<a href="'+lang+'/locality/' + regexp.search(part).group(1)  + '">' + \
             re.sub(r'([0123456789.]+)-','', part) + \
             '</a>')
        else:
          newparts.append(part)

      s = ", ";
      return s.join(newparts)

    elif "-" in value:
      # split on dash
      parts = value.split('-')
    
      # make href from each census-ed name
      regexp = re.compile(r'([0123456789]+)')
      newparts = ''
      if regexp.search(parts[0]):
        newparts = '<a href="'+lang+'/locality/' + parts[0]  + '">' + \
           parts[1] + '</a>'
      return newparts

    return value



@register.filter(name='cremationlink')
def cremationlink(value):
    
    if value == None:
      return None

    lang = '/' + str(get_language())
    lang = lang.replace('/en-us','')
    
    # split on comma
    parts = value.split(',')
    
    # make href from each census-ed name
    regexp = re.compile(r'([0123456789]+)-')
    newparts = []
    for part in parts:
      if regexp.search(part):
        newparts.append(
          '<a href="'+lang+'/cremation/' + regexp.search(part).group(1)  + '">' + \
           re.sub(r'([0123456789.]+)-','', part) + \
           '</a>')

    s = ", ";
    return s.join(newparts)




@register.simple_tag()
def hyes_no(var):
    if var == None:
      return var
    opt = [_("No"), _("Yes"), "", "", "", "", "", "", "", _('Don’t know')]
    return opt[var]



@register.simple_tag()
def hyes_no_unknown(var):
    if var == None:
      return var
    opt = [_("No"), _("Yes"), "", "", "", "", "", "", "", _('Unknown')]
    return opt[var]



@register.simple_tag()
def hyes_no_na(var):
    if var == None:
      return var
    opt = ["", _("Yes"), _("No"), _('Don’t know'), "", "", "", "", "", _('N/A')]
    return opt[var]




@register.simple_tag()
def hdate_link(var):
  if var == 'Don\'t know' or var == '' or var == None:
    return ', ' + _('date unknown')

  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return _(' between ') + _(monthNames[int(parts[0])]) + ' ' + numpa(int(parts[1])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[3])]) + ' ' + numpa(int(parts[4])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return _(' between ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[4])]) + ' ' + numpa(int(parts[3])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return _(' on ') + _(monthNames[int(parts[1])]) + ' ' + numpa( int(parts[0]) ) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    parts[0] = int(parts[0])
    return _(' on ') + _(monthNames[ parts[0] ]) + ' ' + numpa( parts[1] ) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';


@register.simple_tag()
def hdate(var):
  if (var == 'Don\'t know'):
    return ', ' + _('date unknown')
  if (var == ''):
    return ', ' + _('date unknown')
  if (var == None):
    return ', ' + _('date unknown')


  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return _(' between ') + _(monthNames[int(parts[0])]) + ' ' + numpa(int(parts[1])) + ', ' +  str(parts[2]) + _(' and ') + _(monthNames[int(parts[3])]) + ' ' + str(int(parts[4])) + ',  ' +  yearpa(parts[5])

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return _(' between ') + _(monthNames[int(parts[1])]) + ' ' + str(int(parts[0])) + ', ' +  str(parts[2]) + _(' and ') + _(monthNames[int(parts[4])]) + ' ' + str(int(parts[3])) + ',  ' +  yearpa(parts[5])

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return _(' on ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', ' + yearpa(parts[2])

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    parts[0] = int(parts[0])
    return _(' on ') + _(monthNames[ parts[0] ]) + ' ' + numpa(parts[1]) + ', ' +  yearpa(parts[2])




@register.simple_tag()
def hdateslash(start, end):
  if (start == None):
    return _('date unknown')
  start = str(start).split('-')[0]
  end = str(end).split('-')[0]
  if start == end:
    return yearpa(start)
  else:
    return yearpa(start) + '-' + yearpa(end)


@register.simple_tag()
def hyear(var):
  if (var == 'Don\'t know'):
    return ', ' + _('date unknown')
  if (var == ''):
    return ', ' + _('date unknown')

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return ', ' + yearpa(parts[5])

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return ', ' + yearpa(parts[5])

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ', ' + yearpa(parts[2])

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return ', ' + yearpa(parts[2])




@register.simple_tag()
def heducation(value):
  if value != None:
    education  = [_('No education'),_('Primary school'),_('Middle school'),_('High school'),_('High school'),_('High school'),_('Some college'),_('College degree'),_('Graduate diploma'),_('Vocational degree'),_('Vocational degree'),_('Don’t know')]
    return education[value]
  else:
    return value



@register.simple_tag()
def district_count(value):
  count = 0
  for n in value:
    if n['data_count']:
      count = count + n['data_count']
  return numpa(count)



@register.simple_tag()
def hphoto(value):
  if value:
    value = value.replace('\n', '').replace('\r', '')
    names = value.split(',')
    s = "";
    photos = []
    path = 'https://data.ensaaf.org/static/photos'
    if value != None:
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
      return _('location withheld')
    else:
      return value



@register.simple_tag()
def hvictim_militant_reason(v1, v2, v3, v4, v5, v6, v7, v8, other):
  groups = []
  groups.append(_('1984 Indian Army attack on the Harmandir Sahib')) if v1 == 1 else 0
  groups.append(_('Persecution (i.e. arbitrary arrest, torture, self-defense)')) if v2 == 1 else 0
  groups.append(_('Persecution of a family member or a friend')) if v3 == 1 else 0
  groups.append(_('General persecution of Sikhs')) if v4 == 1 else 0
  groups.append(_('Supported the goals of the militancy movement')) if v5 == 1 else 0
  groups.append(_('Was forced to join')) if v6 == 1 else 0
  groups.append(_('Don’t know')) if v7 == 1 else 0
  if v8 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append( _('Other') )
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''


@register.simple_tag()
def hvictim_employment(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, other):
  groups = []
  groups.append(_('Farmer/agriculture')) if v1 == 1 else 0
  groups.append(_('Shopkeeper')) if v2 == 1 else 0
  groups.append(_('Day laborer')) if v3 == 1 else 0
  groups.append(_('Driver (bus/truck/car)')) if v4 == 1 else 0
  groups.append(_('Mechanic')) if v5 == 1 else 0
  groups.append(_('Student')) if v6 == 1 else 0
  groups.append(_('Housewife')) if v7 == 1 else 0
  groups.append(_('Carpenter')) if v8 == 1 else 0
  groups.append(_('Unemployed')) if v9 == 1 else 0
  groups.append(_('Don’t know')) if v10 == 1 else 0
  if v11 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append( _('Other') )
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def htarget_reason(v1, v2, v3, v4, v5, v6, v7, v8, v9, other):
  groups = []
  groups.append(_('Victim was a militant')) if v1 == 1 else 0
  groups.append(_('Victim was related to a militant')) if v2 == 1 else 0
  groups.append(_('Victim gave support to militants')) if v3 == 1 else 0
  groups.append(_('Victim was involved in criminal activities')) if v4 == 1 else 0
  groups.append(_('Victim was identifiably Sikh')) if v5 == 1 else 0
  groups.append(_('Security forces thought victim was a militant')) if v6 == 1 else 0
  groups.append(_('Mistaken for a wanted individual')) if v7 == 1 else 0
  groups.append(_('Don’t know')) if v8 == 1 else 0
  if v9 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append(_('Other'))
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hcaste(value):
  caste = ['', '<span define="'+_('A caste associated with agriculture')+'">'+_('Jat')+'</span>',_('Ramgarhia'),_('Dalit/SC/BC'),_('Mazbi'),_('Chamar'),_('Khatri'),_('Naee'),_('Don’t know'),_('Other')]
  return caste[value]



@register.simple_tag()
def hreligion(value):
  religion = ['',_('Sikh'),_('Hinduism'),_('Islam'),_('Christianity'),_('No religion'),_('Don’t know'),'Other']
  return religion[value]



@register.simple_tag()
def hforced(value):
  forced = ['',_('Voluntary'),_('Forced'),_('Don’t know'),'','','','','',_('N/A')]
  return forced[value]



@register.simple_tag()
def hvictim_arrest_status(value):
  if value == None:
    return value
  status = ['',_('Yes'),_('Yes, the victim turned himself/herself in'),_('No'),_('Unknown'),]
  return status[value]



@register.simple_tag()
def hvictim_arrest_date(victim_arrest_date):

  if victim_arrest_date == None:
    return ', ' + _('date unknown')

  if (victim_arrest_date == 'Don\'t know'):
    return ', ' + _('date unknown')

  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in victim_arrest_date and '-' in victim_arrest_date:
    victim_arrest_date = victim_arrest_date.replace('//','/')
    victim_arrest_date = victim_arrest_date.replace('/','-')
    parts = victim_arrest_date.split('-')
    return _(' between ') + _(monthNames[int(parts[0])]) + ' ' + numpa(int(parts[1])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[3])]) + ' ' + numpa(int(parts[4])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in victim_arrest_date:
    victim_arrest_date = victim_arrest_date.replace(' ','')
    parts = victim_arrest_date.split('-')
    return _(' between ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[4])]) + ' ' + numpa(int(parts[3])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  around = ''

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in victim_arrest_date:
    parts = victim_arrest_date.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return around + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in victim_arrest_date:
    parts = victim_arrest_date.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    parts[0] = int(parts[0])
    return around + _(monthNames[ parts[0] ]) + ' ' + numpa( parts[1] ) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';

  return ''



@register.simple_tag()
def hwitness_arrest(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v12, other):
  groups = []
  
  if v0 == 1 or v12 == 1:
    groups.append(_('Unknown'),)
    
  groups.append(_('Spouse')) if v1 == 1 else 0
  groups.append(_('Parents')) if v2 == 1 else 0
  groups.append(_('Children')) if v3 == 1 else 0
  groups.append(_('Sibling')) if v4 == 1 else 0
  groups.append(_('Grandparent')) if v5 == 1 else 0
  groups.append(_('Cousin')) if v6 == 1 else 0
  groups.append(_('Aunt/uncle')) if v7 == 1 else 0
  groups.append(_('Friend')) if v8 == 1 else 0
  groups.append(_('Co-villager')) if v9 == 1 else 0
  groups.append(_('Respondent')) if v10 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def harrest_security_type_link(v1, v2, v3, v4, v5, v6, v7, other):
  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

  groups = []
  groups.append('<a href="'+lang+'/securityforce/police/">'+_('Punjab Police')+'</a>') if v1 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/bsf/"><span define="'+_('Border Security Force')+'">'+_('BSF')+'</span></a>') if v2 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/crpf/"><span define="'+_('Central Reserve Police Force')+'">'+_('CRPF')+'</span></a>') if v3 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/army/">'+_('Army')+'</a>') if v4 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/cia/">'+_('Criminal Investigation Agency')+'</a>') if v5 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/black-cat/"><span define="'+_('Irregular undercover security force, often consisting of criminals')+'">'+_('Black cat')+'</span></a>') if v6 == 1 else 0
  groups.append( _('Unknown type of security forces') ) if v7 == 1 else 0
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
  groups.append(_('Punjab Police')) if v1 == 1 else 0
  groups.append(_('Border Security Force')) if v2 == 1 else 0
  groups.append(_('Central Reserve Police Force')) if v3 == 1 else 0
  groups.append(_('Army')) if v4 == 1 else 0
  groups.append(_('Criminal Investigation Agency')) if v5 == 1 else 0
  groups.append(_('Black cat')) if v6 == 1 else 0
  groups.append(_('Unknown type of security forces')) if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hso_approached_type(v1, v2, v3, v4, v5, v6, v7, other):
  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

  groups = []
  groups.append( _('Same as officials involved in abduction/extrajudicial execution') ) if v1 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/police/">' + _('Punjab Police') + '</a>') if v2 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/bsf/"><span define="Border Security Force">BSF</span></a>') if v3 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/crpf/"><span define="Central Reserve Police Force">CRPF</span></a>') if v4 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/army/">Army</a>') if v5 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/cia/">Criminal Investigation Agency</a>') if v6 == 1 else 0
  groups.append('<a href="'+lang+'/securityforce/black-cat/"><span define="Irregular undercover security force, often consisting of criminals">Black cat</span></a>') if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hadd_spaces(value):
  if value == None:
    return value
  terms = value.split(',')
  s = ', '
  return s.join(terms)



@register.simple_tag()
def hvictim_arrest_location(value):
  if value == None:
    return value
  location = ['', '', _('Victim\'s residence'), _('Friend/relative\'s residence'), _('Checkpoint (naka)'), _('Roadside'), _('Village fields'), _('Shop/market'), _('Bus station/stand'), _('Police station'), _('Village drain')]
  return location[value]



@register.simple_tag()
def hso_return_body(value):
  if value == None:
    return value
  so_return_body = ['',_('Yes'),_('Yes, but forced immediate cremation'),_('No'),_('Don’t know')]
  return so_return_body[value]



@register.simple_tag()
def hso_body_disposal(value):
  if value == None:
    return value
  so_body_disposal = ['',_('Cremated the body'),_('Dumped body in canal/river'),_('Dumped body in well/drain'),_('Buried the body'),_('Don’t know'),_('Other')]
  return so_body_disposal[value]



@register.simple_tag()
def hcremation_location_type(value):
  if value == None:
    return value
  cremation_location_type = ['',_('Municipal cremation ground'),_('Village cremation ground'),_('Gurdwara cremation ground'),_('Don’t know'),_('Other')]
  return cremation_location_type[value]



@register.simple_tag()
def hcondition_of_remains(v1, v2, v3, v4, v5, v6, v7, other):
  groups = []
  groups.append(_('Bruises')) if v1 == 1 else 0
  groups.append(_('Bullet wounds')) if v2 == 1 else 0
  groups.append(_('Cuts/wounds')) if v3 == 1 else 0
  groups.append(_('Broken bones')) if v4 == 1 else 0
  groups.append(_('Missing hair from head or face')) if v5 == 1 else 0
  groups.append(_('Missing fingernails')) if v6 == 1 else 0
  groups.append(_('Burn marks')) if v7 == 1 else 0
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
  groups.append(_('Money')) if v2 == 1 else 0
  groups.append(_('Information about another person')) if v3 == 1 else 0
  groups.append(_('Forced identification of another person')) if v4 == 1 else 0
  groups.append(_('Another person must turn himself in')) if v5 == 1 else 0
  groups.append(_('Signature on blank papers')) if v6 == 1 else 0
  groups.append(_('Valuables (jewelry/electronics/land/etc.)')) if v7 == 1 else 0
  groups.append(_('Land')) if v8 == 1 else 0
  # groups.append('Don’t know')) if v9 == 1 else 0
  if v10 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append(_('Other'))
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hjudge_or_magistrate_result(v1, v2, v3, v4, other):
  groups = []
  groups.append(_('Jail')) if v1 == 1 else 0
  groups.append(_('Police custody/remand')) if v2 == 1 else 0
  groups.append(_('Don’t know')) if v3 == 1 else 0
  if v4 == 1:
    if (other):
      groups.append(other)
    else:
      groups.append( _('Other') )
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hsecurity_official_response(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, other):
  groups = []
  groups.append(_('No Response')) if v0 == 1 else 0
  groups.append(_('Extrajudicial execution [of victim] in an "encounter"')) if v1 == 1 else 0
  groups.append(_('Denied involvement')) if v2 == 1 else 0
  groups.append(_('Admitted extrajudicial execution with no explanation')) if v3 == 1 else 0
  groups.append(_('Admitted custody only')) if v4 == 1 else 0
  groups.append(_('Victim had escaped')) if v5 == 1 else 0
  groups.append(_('Victim extrajudicial execution while trying to escape')) if v6 == 1 else 0
  groups.append(_('Victim extrajudicial execution by militants')) if v7 == 1 else 0
  groups.append(_('Told family to go to another police station')) if v8 == 1 else 0
  groups.append(_('Victim extrajudicial execution in crossfire with militants')) if v9 == 1 else 0
  groups.append(_('Victim accidentally killed in custody')) if v10 == 1 else 0
  groups.append(_('Victim extrajudicial execution while resisting arrest/search')) if v11 == 1 else 0
  groups.append(_('Victim extrajudicial execution by <span define="Irregular undercover security force, often consisting of criminals">Black cat</span>s')) if v12 == 1 else 0
  groups.append(_('Don’t know')) if v14 == 1 else 0
  if v13 == 1:
    if (other):
      groups.append(other)
  if len(groups):
      s = ', '
      return s.join(groups)
  else:
      return "None"



@register.filter(is_safe=True)
def is_numeric(value):
    return "{}".format(value).isdigit()


@register.simple_tag()
def hno_action_pursued_reason(v1, v2, v3, v4, other):
  groups = []
  groups.append(_('Afraid of retaliation')) if v1 == 1 else 0
  groups.append(_('Believed it would have been ineffective')) if v2 == 1 else 0
  groups.append(_('Did not know what to do')) if v3 == 1 else 0
  groups.append(_('Insufficient funds')) if v4 == 1 else 0
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
  groups.append(_('No drastic action')) if v1 == 1 else 0
  groups.append(_('Family members ran away')) if v2 == 1 else 0
  groups.append(_('Family member(s) engaged in militant activity')) if v3 == 1 else 0
  groups.append(_('Family member(s) dropped out of school')) if v4 == 1 else 0
  groups.append(_('Family member(s) abused alcohol/drugs')) if v5 == 1 else 0
  groups.append(_('Family member(s) committed suicide')) if v6 == 1 else 0
  groups.append(_('Family abandoned home')) if v7 == 1 else 0
  groups.append(_('Family member(s) died due to depression/shock')) if v8 == 1 else 0
  groups.append(_('Family member(s) was mentally disturbed')) if v9 == 1 else 0
  groups.append(_('Family became impoverished')) if v12 == 1 else 0
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
  groups.append(_('Monetary compensation to family')) if v1 == 1 else 0
  groups.append(_('Rehabilitation services to family')) if v2 == 1 else 0
  groups.append(_('Public acknowledgement of wrongful deaths')) if v3 == 1 else 0
  groups.append(_('Criminal prosecution of those responsible')) if v4 == 1 else 0
  groups.append(_('Employment')) if v5 == 1 else 0
  groups.append(_('Truth commission')) if v6 == 1 else 0
  groups.append(_('Investigations into abuses')) if v7 == 1 else 0
  groups.append(_('Memorial for victims')) if v8 == 1 else 0
  groups.append(_('Desire nothing from government')) if v9 == 1 else 0
  groups.append(_('Don’t know')) if v11 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hothers_arrested(value):
  if value == None:
    return value
  others_arrested = [_('No'),_('Yes'),_('Yes'),'','','','','','',_('Unknown'),]
  return others_arrested[value]



@register.simple_tag()
def hothers_killed(v0, v1, v2, v3):
  if v0 == 1:
    return( _('No') )
  if v1 == 1:
    return(_('Yes'))
  if v2 == 1:
    return(_('Yes'))
  if v3 == 1:
    return(_('Yes'))
#  if v9 == 1:
#    return(_('Unknown'),)
  return ''



@register.simple_tag()
def hwitness_detention(v3, v4, v5, v6, v7, v8, v9, v10, v12, v13, v14, other, status):
  groups = []

  if (v3 == 1):
    if (status):
      groups.append(_('Seen by respondent'))
    else:
      groups.append(_('Relative'))

  if (v4 == 1):
    if (status):
      groups.append(_('Seen by relative'))
    else:
      groups.append(_('Relative'))

  if (v5 == 1):
    if (status):
      groups.append(_('Seen by other detainee'))
    else:
      groups.append(_('Other detainee'))

  if (v6 == 1):
    if (status):
      groups.append(_('Seen by sarpanch/politician'))
    else:
      groups.append(_('<span define="Head of the village council">Sarpanch</span>/politician'))

  if (v7 == 1):
    if (status):
      groups.append(_('Seen by newspaper'))
    else:
      groups.append(_('Newspaper'))

  if (v8 == 1):
    if (status):
      groups.append(_('Seen by security official'))
    else:
      groups.append(_('Security official'))

  if (v9 == 1):
    if (status):
      groups.append(_('Seen by friend'))
    else:
      groups.append(_('Friend'))

  if (v10 == 1):
    if (status):
      groups.append(_('Seen by other witness (non-relative)'))
    else:
      groups.append(_('Other witness (non-relative)'))

  # if (v11 == 1): groups.append(_('Respondent belief (no source)'))

  if (v12 == 1):
    if (status):
      groups.append(_('Seen by doctor'))
    else:
      groups.append(_('Doctor'))

  if (v13 == 1):
    if (status):
      groups.append(_('Seen by other victim family'))
    else:
      groups.append(_('Other victim family'))

  if (other):
    if (status):
      groups.append(_('Seen by')+' '+other)
    else:
      groups.append(other)

  if len(groups):
      s = ' '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def hdetention_facility_type(var, other):
  opt = ['',_('Police station/post'),_('Criminal Investigation Agency staff'),_('<span define="Border Security Force">BSF</span>'),_('<span define="Central Reserve Police Force">CRPF</span> camp'),_('Army camp'),_('<span define="Unofficial interrogation location">Interrogation center</span>'),_('Don’t know'),_('Other')]
  if var == 8:
    if (other):
      return other
  return opt[var]



@register.simple_tag()
def hduration_of_detention(v1):
  if v1 == None:
    return v1
  try:
     val = int(v1)
     if val > 1:
      return v1 + ' ' + _('days')
     else:
      return v1 + ' ' + _('day')
  except ValueError:
     return v1.lower()



@register.simple_tag()
def harrest_so_rank(var):
  if var == None:
    return var
  opt = ['',_('Inspector'),_('Sub Inspector'),_('Assistant Sub Inspector'),_('Senior Superintendent of Police'),_('Deputy Superintendent of Police'),_('Station House Officer'),_('Constable'),_('Head Constable'),_('Sepoy'),_('DIG (Deputy Inspector General)'),_('IG (Inspector General)'),_('DGP (Director General of Police)'),_('Other'),_('Don’t know'),_('Superintendent of Police')]
  return opt[var]



@register.simple_tag()
def haffiliation(var):
  if var == None:
    return var
  affilation = ['',_('Punjab Police'),_('<span define="Border Security Force">BSF</span>'),_('<span define="Central Reserve Police Force">CRPF</span>'),_('Army'),_('Criminal Investigation Agency'),_('<span define="Irregular undercover security force, often consisting of criminals">Black cat</span>'),_('Don’t know'),_('Other')]
  return affilation[var];



@register.simple_tag()
def percent(item1, total):
    if total == 0:
      return 0
    try:
        return "%.1f" % ((float(item1) / float(total)) * 100) 
    except ValueError as e:
      return ''

@register.simple_tag()
def percentpa(item1, total):
    if total == 0:
      return numpa( 0 )
    try:
      return numpa( float( "%.1f" % ( ( float(item1) / float(total) ) * 100 ) ) )
    except ValueError as e:
      return ''


@register.simple_tag()
def dump(var):
    return vars(var)


