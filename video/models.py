from django.db import models
from django.utils.text import slugify



def get_unique_slug(id,title,obj):
    title = title.replace('.', '')
    title = title.replace('ı', 'i')
    title = title[:255]
    slug = slugify(title)
    unique_slug = slug
    counter = 1
    while obj.filter(slug=unique_slug).exists():
       if(obj.filter(slug=unique_slug).values('id')[0]['id']==id):
           break
       unique_slug = '{}-{}'.format(slug, counter)
       counter += 1
    return unique_slug



class Theme(models.Model):
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = get_unique_slug(self.id,self.name,Theme.objects)
       super().save(*args, **kwargs)


    def __unicode__(self):
        return self.__str__()


GENDER_CHOICES = (
    ('Male','Male'),
    ('Female', 'Female')
)

COMBATANT_CHOICES = (
    ('Combatant','Combatant'),
    ('Non-Combatant', 'Non-Combatant'),
    ('Unknown', 'Unknown')
)

DISTRICT_CHOICES = (
  ('302','Amritsar'),
  ('314','Bathinda'),
  ('313','Faridkot'),
  ('308','Fatehgarh Sahib'),
  ('311','Firozpur'),
  ('301','Gurdaspur'),
  ('305','Hoshiarpur'),
  ('304','Jalandhar'),
  ('303','Kapurthala'),
  ('309','Ludhiana'),
  ('315','Mansa'),
  ('310','Moga'),
  ('312','Muktsar'),
  ('306','Nawanshahr'),
  ('317','Patiala'),
  ('307','Rupnagar'),
  ('316','Sangrur')
)


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    youtube_id = models.CharField(max_length=200, blank=True, verbose_name="YouTube ID")
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6, blank=True)
    age = models.CharField(max_length=3, blank=True)
    combatant_status = models.CharField(choices=COMBATANT_CHOICES,max_length=14, blank=True)
    year = models.CharField(max_length=4, blank=True)
    district = models.CharField(choices=DISTRICT_CHOICES,max_length=14, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
       self.slug = get_unique_slug(self.id,self.title,Video.objects)
       super().save(*args, **kwargs)



class Clip(models.Model):
    video = models.ForeignKey(Video, default=None, on_delete=models.CASCADE)
    start_time = models.CharField(blank=True, max_length=8, help_text="Use format MM:SS")
    end_time = models.CharField(blank=True, max_length=8, help_text="Use format MM:SS")
    clip_youtube_id = models.CharField(max_length=200, blank=True, verbose_name="YouTube ID", help_text="YouTube ID, if uploaded as a separate clip")
    theme = models.ManyToManyField(Theme, default=None, blank=True)
    def __str__(self): return self.video.title



class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
       self.slug = get_unique_slug(self.id,self.title,Page.objects)
       super().save(*args, **kwargs)


