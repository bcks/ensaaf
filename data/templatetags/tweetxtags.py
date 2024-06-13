import re
import numbers
from django import template
from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.urls import reverse
from ..models import *

import requests
import json

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


@register.simple_tag(name='concatenate')
def concatenate(v1, v2):
  concatenated = ''
  if str(v1) == "Don't know": v1 = ''
  if str(v2) == "Don't know": v2 = ''  
  if v1:
    concatenated =  str(v1)
  if v2:
    concatenated = concatenated + ' ' + str(v2)
  return _( concatenated )


@register.filter(name='translate')
def translate(text):
  try:    
    return _(text)
  except ValueError:
    return text


@register.filter(name='vnametranslate')
def vnametranslate(village):
  try:    
    if (get_language() == 'pb'):
      return village.village_name_pb
    else:
      return village.village_name
  except ValueError:
    return text


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    path = context['request'].path.replace('_cache','')
    print(path)
    if lang == 'en':
      return path.replace('/pb/','/')
    else:
      return '/' + lang + path


def not_int(s):
    if "-" in str(s): 
      s = str(s).replace('-','')    
    try: 
        int(s)
        return False
    except:
        return True


@register.filter()
def numpa(number_string):
    
    if number_string == None:
      return number_string

    if not_int(number_string):
      try:
        number_string = number_string.lstrip('0')
      except:
        None

    if (get_language() == 'pb'):
      if not_int(number_string):
        return _(number_string)

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
    if (get_language() == 'pb') and (number_string == 'Date Unknown'):
        return _('Date Unknown')    
    if (get_language() == 'pb') and number_string.isdigit():      
      dic = {'0':'੦','1':'੧','2':'੨','3':'੩','4':'੪','5':'੫',\
      '6':'੬','7':'੭','8':'੮','9':'੯','.':'.',',':','}
      return "".join([dic[c] for c in number_string])
    else:
      return number_string


@register.simple_tag()
def hdate_link_t(var):
  if var == 'Don\'t know' or var == '' or var == None:
    return ', ' + _('date unknown')

  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

  # 09/20/1988-10/05/1988
  #      pattern => '%m/%d/%Y',
  if '/' in var and '-' in var:
    var = var.replace('/','-')
    parts = var.split('-')
    return _(' Between ') + _(monthNames[int(parts[0])]) + ' ' + numpa(int(parts[1])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[3])]) + ' ' + numpa(int(parts[4])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return _(' Between ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>' + _(' and ') + _(monthNames[int(parts[4])]) + ' ' + numpa(int(parts[3])) + ',  <a href="'+lang+'/year/'+str(parts[5])+'">' +  yearpa(parts[5]) + '</a>'

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return _(' On ') + _(monthNames[int(parts[1])]) + ' ' + numpa( int(parts[0]) ) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    parts[0] = int(parts[0])
    return _(' On ') + _(monthNames[ parts[0] ]) + ' ' + numpa( int(parts[1]) ) + ', <a href="'+lang+'/year/'+str(parts[2])+'">' +  yearpa(parts[2]) + '</a>';


@register.simple_tag()
def hdate_t(var):
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
    return _(' Between ') + _(monthNames[int(parts[0])]) + ' ' + numpa(int(parts[1])) + ', ' +  yearpa(parts[2]) + _(' and ') + _(monthNames[int(parts[3])]) + ' ' + numpa(int(parts[4])) + ',  ' +  yearpa(parts[5])

  # 15-02-1992 - 15-03-1992    
  #        pattern => '%d-%m-%Y',
  if ' - ' in var:
    var = var.replace(' ','')
    parts = var.split('-')
    return _(' Between ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', ' +  yearpa(parts[2]) + _(' and ') + _(monthNames[int(parts[4])]) + ' ' + numpa(int(parts[3])) + ',  ' +  yearpa(parts[5])

  # 23-07-1991
  #    pattern => '%d-%m-%Y',
  if '-' in var:
    parts = var.split('-')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    return _(' On ') + _(monthNames[int(parts[1])]) + ' ' + numpa(int(parts[0])) + ', ' + yearpa(parts[2])

  # 10/15/1992
  #      pattern => '%m/%d/%Y',
  if '/' in var:
    parts = var.split('/')
    if int(parts[2]) < 20:
      parts[2] = int(parts[2]) + 2000    
    elif int(parts[2]) < 1900:
      parts[2] = int(parts[2]) + 1900
    parts[0] = int(parts[0])
    return _(' On ') + _(monthNames[ parts[0] ]) + ' ' + numpa(parts[1]) + ', ' +  yearpa(parts[2])


@register.simple_tag()
def hdateslash_t(start, end):
  if (start == None):
    return _('date unknown')
  start = str(start).split('-')[0]
  end = str(end).split('-')[0]
  if start == end:
    return yearpa(start)
  else:
    return yearpa(start) + '-' + yearpa(end)


@register.simple_tag()
def hyear_t(var):
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
def harrest_security_type_link_t(v1, v2, v3, v4, v5, v6, v7, other):
  lang = '/' + str(get_language())
  lang = lang.replace('/en-us','')

#remove all lings
  groups = []
  groups.append('#PunjabPolice') if v1 == 1 else 0
  groups.append('#BorderSecurityForce') if v2 == 1 else 0
  groups.append('#CentralReservePoliceForce') if v3 == 1 else 0
  groups.append('#Army') if v4 == 1 else 0
  groups.append('#CriminalInvestigationAgency') if v5 == 1 else 0
  groups.append('#Blackcat (Irregular undercover security force, often consisting of criminals)') if v6 == 1 else 0
  groups.append( 'Unknown type of security forces') if v7 == 1 else 0
  if (other):
    groups.append(other)
  if len(groups):
      s = '; '
      return s.join(groups)
  else:
      return ''



@register.simple_tag()
def harrest_security_type_t(v1, v2, v3, v4, v5, v6, v7, other):
  groups = []
  groups.append(_('#PunjabPolice')) if v1 == 1 else 0
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

  
@register.filter(name='censuslink_t')
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
          census_id = regexp.search(part).group(1)
          vname = re.sub(r'([0123456789.]+)-','', part)
          if lang == '/pb':
            vname = get_village_name_pb(census_id)
          newparts.append(
             vname )
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
        census_id = parts[0]
        vname = parts[1]
        if lang == '/pb':
          vname = get_village_name_pb(census_id)
        newparts =   vname 
      return newparts

    return value


@register.simple_tag()
def hvictim_address_other_t(value):
  if value == None:
    return value
  str = value.split('_')
  str = str[0]
  p = re.compile(r'([0123456789.]+)-')
  m = p.search(str)
  vname = re.sub(r'([0123456789.]+)-','', str)
  if m:
    census_id = m.group(1)
    if get_language() == 'pb':
      vname = get_village_name_pb(census_id)
    try:
      village = Villages.objects.filter(vid=census_id)[:1].get()
      
      if village.district == 'Chandigarh':
        return '<a href="' + \
          reverse('village', args=(census_id,)) + '">' + vname + '</a>'
      else:      
        return reverse('village') + vname + ', ' + ('Subdistrict') + \
          _(village.tehsil) + \
         + _(village.district)

    except Villages.DoesNotExist:
      str = re.sub(r'([0123456789.]+)-','', str)
      return str
  else:
    str = re.sub(r'([0123456789.]+)-','', str)
    return str


@register.simple_tag()
def hashtag_victim_address_other_t(value):
  if value == None:
    return value
  str = value.split('_')
  str = str[0]
  p = re.compile(r'([0123456789.]+)-')
  m = p.search(str)
  vname = re.sub(r'([0123456789.]+)-','', str)
  if m:
    census_id = m.group(1)
    if get_language() == 'pb':
      vname = get_village_name_pb(census_id)
    try:
      village = Villages.objects.filter(vid=census_id)[:1].get()
      
      if village.district == 'Chandigarh':
        return  vname 
      else:      
        return  vname + ', ' + _(village.tehsil) + ' #' + village.district.replace(' ','') + ' District'

    except Villages.DoesNotExist:
      str = re.sub(r'([0123456789.]+)-','', str)
      return str
  else:
    str = re.sub(r'([0123456789.]+)-','', str)
    return str

