from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.text import slugify
from image_cropping import ImageRatioField
import requests


def get_unique_slug(id, title, obj):
    title = title.replace(".", "")
    title = title.replace("ı", "i")
    title = title[:255]
    slug = slugify(title)
    unique_slug = slug
    counter = 1
    while obj.filter(slug=unique_slug).exists():
        if obj.filter(slug=unique_slug).values("id")[0]["id"] == id:
            break
        unique_slug = "{}-{}".format(slug, counter)
        counter += 1
    return unique_slug


class Theme(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to = 'themes/', max_length=200, blank=True)
    image_cropping = ImageRatioField('image', '830x500', size_warning=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(self.id, self.name, Theme.objects)
        super().save(*args, **kwargs)

    def __unicode__(self):
        return self.__str__()


GENDER_CHOICES = (("Male", "Male"), ("Female", "Female"))

COMBATANT_CHOICES = (
    ("Combatant", "Combatant"),
    ("Non-Combatant", "Non-Combatant"),
    ("Unknown", "Unknown"),
)

DISTRICT_CHOICES = (
    ("302", "Amritsar"),
    ("314", "Bathinda"),
    ("313", "Faridkot"),
    ("308", "Fatehgarh Sahib"),
    ("311", "Firozpur"),
    ("301", "Gurdaspur"),
    ("305", "Hoshiarpur"),
    ("304", "Jalandhar"),
    ("303", "Kapurthala"),
    ("309", "Ludhiana"),
    ("315", "Mansa"),
    ("310", "Moga"),
    ("312", "Muktsar"),
    ("306", "Nawanshahr"),
    ("317", "Patiala"),
    ("307", "Rupnagar"),
    ("316", "Sangrur"),
)



def get_vimeo_thumbnail(vimeo_id):
    vimeo_json = requests.get( 'http://vimeo.com/api/v2/video/{}.json'.format(vimeo_id) ).json()
    image_url = vimeo_json[0]['thumbnail_large']
    r = requests.get(image_url, stream = True)
    file_name = '{}images/{}.jpg'.format(settings.MEDIA_ROOT, vimeo_id) 

    if r.status_code == 200:
        r.raw.decode_content = True        
        fs = FileSystemStorage()
        file_name_saved = fs.save(file_name, r.raw)
        file_name_field = file_name_saved.replace(settings.MEDIA_ROOT,'')
        return(file_name_field)
    else:
        return None



class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    profile_id = models.CharField(max_length=10, blank=True, verbose_name="data.ensaaf.org Profile ID")
    vimeo_id = models.CharField(max_length=64, blank=True, verbose_name="vimeo ID")
    image = models.ImageField(upload_to = 'themes/', max_length=200, blank=True)
    image_cropping = ImageRatioField('image', '830x500', size_warning=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, blank=True)
    age = models.CharField(max_length=3, blank=True)
    combatant_status = models.CharField(
        choices=COMBATANT_CHOICES, max_length=14, blank=True
    )
    year = models.CharField(max_length=4, blank=True)
    district = models.CharField(choices=DISTRICT_CHOICES, max_length=14, blank=True)
    theme = models.ManyToManyField(Theme, default=None, blank=True)
    transcription = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image == '':          
          self.image = get_vimeo_thumbnail(self.vimeo_id)
        super().save(*args, **kwargs)


class Clip(models.Model):
    video = models.ForeignKey(Video, default=None, on_delete=models.CASCADE, blank=True)
    start_time_minutes = models.CharField(blank=True, max_length=10)
    start_time_seconds = models.CharField(blank=True, max_length=10)
    end_time_minutes =   models.CharField(blank=True, max_length=10)
    end_time_seconds =   models.CharField(blank=True, max_length=10)
    theme = models.ManyToManyField(Theme, default=None, blank=True)
    transcription = models.TextField(blank=True)

    def __str__(self):
        return self.video.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    background_video = models.FileField(
        upload_to="video/", blank=True, verbose_name="Background Video"
    )
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(self.id, self.title, Page.objects)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
