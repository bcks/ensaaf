from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from .models import *
from simple_search import search_filter
from .filters import InterviewFilter



districts = [{"district":"Amritsar","district_pb":"ਅੰਮ੍ਰਿਤਸਰ","district_id":302,"subdistricts":[{"tehsil":"Ajnala","tehsil_pb":"ਅਜਨਾਲਾ","tehsil_id":3020001},{"tehsil":"Amritsar I","tehsil_pb":"ਅੰਮ੍ਰਿਤਸਰ - I","tehsil_id":3020002},{"tehsil":"Amritsar II","tehsil_pb":"ਅੰਮ੍ਰਿਤਸਰ - II","tehsil_id":3020003},{"tehsil":"Baba Bakala","tehsil_pb":"ਬਾਬਾ ਬਕਾਲਾ","tehsil_id":3020007},{"tehsil":"Khadoor Sahib","tehsil_pb":"ਖਡੂਰ ਸਾਹਿਬ","tehsil_id":3020006},{"tehsil":"Patti","tehsil_pb":"ਪੱਟੀ","tehsil_id":3020005},{"tehsil":"Tarn Taran","tehsil_pb":"ਤਰਨ ਤਾਰਨ","tehsil_id":3020004}]},{"district":"Bathinda","district_pb":"ਬਠਿੰਡਾ","district_id":314,"subdistricts":[{"tehsil":"Bathinda","tehsil_pb":"ਬਠਿੰਡਾ","tehsil_id":3140002},{"tehsil":"Rampura Phul","tehsil_pb":"ਰਾਮਪੁਰਾ ਫੂਲ","tehsil_id":3140001},{"tehsil":"Talwandi Sabo","tehsil_pb":"ਤਲਵੰਡੀ ਸਾਬੋ","tehsil_id":3140003}]},{"district":"Faridkot","district_pb":"ਫਰੀਦਕੋਟ","district_id":313,"subdistricts":[{"tehsil":"Faridkot","tehsil_pb":"ਫਰੀਦਕੋਟ","tehsil_id":3130001},{"tehsil":"Jaitu","tehsil_pb":"ਜੈਤੋ","tehsil_id":3130002}]},{"district":"Fatehgarh Sahib","district_pb":"ਫਤਿਹਗੜ੍ਹ ਸਾਹਿਬ","district_id":308,"subdistricts":[{"tehsil":"Amloh","tehsil_pb":"ਅਮਲੋਹ","tehsil_id":3080003},{"tehsil":"Bassi Pathana","tehsil_pb":"ਬੱਸੀ ਪਠਾਣਾਂ","tehsil_id":3080001},{"tehsil":"Fatehgarh Sahib","tehsil_pb":"ਫਤਿਹਗੜ੍ਹ ਸਾਹਿਬ","tehsil_id":3080002},{"tehsil":"Khamanon","tehsil_pb":"ਖਮਾਣੋ","tehsil_id":3080004}]},{"district":"Firozpur","district_pb":"ਫਿਰੋਜਪੁਰ","district_id":311,"subdistricts":[{"tehsil":"Abohar","tehsil_pb":"ਅਬੋਹਰ","tehsil_id":3110005},{"tehsil":"Fazilka","tehsil_pb":"ਫਾਜ਼ਿਲਕਾ","tehsil_id":3110004},{"tehsil":"Firozpur","tehsil_pb":"ਫਿਰੋਜਪੁਰ","tehsil_id":3110002},{"tehsil":"Jalalabad","tehsil_pb":"ਜਲਾਲਾਬਾਦ","tehsil_id":3110003},{"tehsil":"Zira","tehsil_pb":"ਜ਼ੀਰਾ","tehsil_id":3110001}]},{"district":"Gurdaspur","district_pb":"ਗੁਰਦਾਸਪੁਰ","district_id":301,"subdistricts":[{"tehsil":"Batala","tehsil_pb":"ਬਟਾਲਾ","tehsil_id":3010004},{"tehsil":"Dera Baba Nanak","tehsil_pb":"ਡੇਰਾ ਬਾਬਾ ਨਾਨਕ","tehsil_id":3010005},{"tehsil":"Dhar Kalan","tehsil_pb":"ਧਾਰ ਕਲਾਂ","tehsil_id":3010001},{"tehsil":"Gurdaspur","tehsil_pb":"ਗੁਰਦਾਸਪੁਰ","tehsil_id":3010003},{"tehsil":"Pathankot","tehsil_pb":"ਪਠਾਨਕੋਟ","tehsil_id":3010002}]},{"district":"Hoshiarpur","district_pb":"ਹੁਸ਼ਿਆਰਪੁਰ","district_id":305,"subdistricts":[{"tehsil":"Dasuya","tehsil_pb":"ਦਸੂਹਾ","tehsil_id":3050001},{"tehsil":"Garhshankar","tehsil_pb":"ਗੜਸ਼ੰਕਰ","tehsil_id":3050004},{"tehsil":"Hoshiarpur","tehsil_pb":"ਹੁਸ਼ਿਆਰਪੁਰ","tehsil_id":3050003},{"tehsil":"Mukerian","tehsil_pb":"ਮੁਕੇਰੀਆਂ","tehsil_id":3050002}]},{"district":"Jalandhar","district_pb":"ਜਲੰਧਰ","district_id":304,"subdistricts":[{"tehsil":"Jalandhar I","tehsil_pb":"ਜਲੰਧਰ - I","tehsil_id":3040004},{"tehsil":"Jalandhar II","tehsil_pb":"ਜਲੰਧਰ - II","tehsil_id":3040005},{"tehsil":"Nakodar","tehsil_pb":"ਨਕੋਦਰ","tehsil_id":3040002},{"tehsil":"Phillaur","tehsil_pb":"ਫਿਲੌਰ","tehsil_id":3040003},{"tehsil":"Shahkot","tehsil_pb":"ਸ਼ਾਹਕੋਟ","tehsil_id":3040001}]},{"district":"Kapurthala","district_pb":"ਕਪੂਰਥਲਾ","district_id":303,"subdistricts":[{"tehsil":"Bhulath","tehsil_pb":"ਭੁਲੱਥ","tehsil_id":3030001},{"tehsil":"Kapurthala","tehsil_pb":"ਕਪੂਰਥਲਾ","tehsil_id":3030002},{"tehsil":"Phagwara","tehsil_pb":"ਫੱਗਵਾੜਾ","tehsil_id":3030004},{"tehsil":"Sultanpur Lodhi","tehsil_pb":"ਸੁਲਤਾਨਪੁਰ ਲੋਧੀ","tehsil_id":3030003}]},{"district":"Ludhiana","district_pb":"ਲੁਧਿਆਣਾ","district_id":309,"subdistricts":[{"tehsil":"Jagraon","tehsil_pb":"ਜਗਰਾਓ","tehsil_id":3090007},{"tehsil":"Khanna","tehsil_pb":"ਖੰਨਾ","tehsil_id":3090002},{"tehsil":"Ludhiana East","tehsil_pb":"ਲੁਧਿਆਣਾ ਈਸਟ","tehsil_id":3090004},{"tehsil":"Ludhiana West","tehsil_pb":"ਲੁਧਿਆਣਾ ਵੈਸਟ","tehsil_id":3090005},{"tehsil":"Payal","tehsil_pb":"ਪਾਇਲ","tehsil_id":3090003},{"tehsil":"Raikot","tehsil_pb":"ਰਾਏਕੋਟ","tehsil_id":3090006},{"tehsil":"Samrala","tehsil_pb":"ਸਮਰਾਲਾ","tehsil_id":3090001}]},{"district":"Mansa","district_pb":"ਮਾਨਸਾ","district_id":315,"subdistricts":[{"tehsil":"Budhlada","tehsil_pb":"ਬੁੱਡਲਾਡਾ","tehsil_id":3150002},{"tehsil":"Mansa","tehsil_pb":"ਮਾਨਸਾ","tehsil_id":3150003},{"tehsil":"Sardulgarh","tehsil_pb":"ਸਰਦੂਲਗੱੜ","tehsil_id":3150001}]},{"district":"Moga","district_pb":"ਮੋਗਾ","district_id":310,"subdistricts":[{"tehsil":"Bhagha Purana","tehsil_pb":"ਬਾਘਾ ਪੁਰਾਣਾ","tehsil_id":3100002},{"tehsil":"Moga","tehsil_pb":"ਮੋਗਾ","tehsil_id":3100003},{"tehsil":"Nihal Singhwala","tehsil_pb":"ਨਿਹਾਲ ਸਿੰਘਵਾਲਾ","tehsil_id":3100001}]},{"district":"Muktsar","district_pb":"ਮੁਕਤਸਰ","district_id":312,"subdistricts":[{"tehsil":"Giddarbaha","tehsil_pb":"ਗਿੱਦੜਬਾਹਾ","tehsil_id":3120002},{"tehsil":"Malout","tehsil_pb":"ਮਲੋਟ","tehsil_id":3120001},{"tehsil":"Muktsar","tehsil_pb":"ਮੁਕਤਸਰ","tehsil_id":3120003}]},{"district":"Nawanshahr","district_pb":"ਨਵਾਂਸ਼ਹਿਰ","district_id":306,"subdistricts":[{"tehsil":"Balachaur","tehsil_pb":"ਬਲਾਚੌਰ","tehsil_id":3060002},{"tehsil":"Nawanshahr","tehsil_pb":"ਨਵਾਂਸ਼ਹਿਰ","tehsil_id":3060001}]},{"district":"Patiala","district_pb":"ਪਟਿਆਲਾ","district_id":317,"subdistricts":[{"tehsil":"Dera Bassi","tehsil_pb":"ਡੇਰਾ ਬੱਸੀ","tehsil_id":3170005},{"tehsil":"Nabha","tehsil_pb":"ਨਾਭਾ","tehsil_id":3170002},{"tehsil":"Patiala","tehsil_pb":"ਪਟਿਆਲਾ","tehsil_id":3170003},{"tehsil":"Rajpura","tehsil_pb":"ਰਾਜਪੁਰਾ","tehsil_id":3170004},{"tehsil":"Samana","tehsil_pb":"ਸਮਾਣਾ","tehsil_id":3170001}]},{"district":"Rupnagar","district_pb":"ਰੂਪਨਗਰ","district_id":307,"subdistricts":[{"tehsil":"Anandpur Sahib","tehsil_pb":"ਅਨੰਦਪੁਰ ਸਾਹਿਬ","tehsil_id":3070001},{"tehsil":"Kharar","tehsil_pb":"ਖਰੜ","tehsil_id":3070003},{"tehsil":"Rupnagar","tehsil_pb":"ਰੂਪਨਗਰ","tehsil_id":3070002},{"tehsil":"S.A.S.Nagar (Mohali)","tehsil_pb":"ਸਾਹਿਬਜ਼ਾਦਾ ਅਜੀਤ ਸਿੰਘ ਨਗਰ (ਮੋਹਾਲੀ)","tehsil_id":3070004}]},{"district":"Sangrur","district_pb":"ਸੰਗਰੂਰ","district_id":316,"subdistricts":[{"tehsil":"Barnala","tehsil_pb":"ਬਰਨਾਲਾ","tehsil_id":3160001},{"tehsil":"Dhuri","tehsil_pb":"ਧੂਰੀ","tehsil_id":3160003},{"tehsil":"Malerkotla","tehsil_pb":"ਮਲੇਰਕੋਟਲਾ","tehsil_id":3160002},{"tehsil":"Moonak","tehsil_pb":"ਮੂਨਕ","tehsil_id":3160006},{"tehsil":"Sangrur","tehsil_pb":"ਸੰਗਰੂਰ","tehsil_id":3160004},{"tehsil":"Sunam","tehsil_pb":"ਸੁਨਾਮ","tehsil_id":3160005}]}]


def search(request):

    p = Page.objects.filter(slug='search')[0]
    
    q = request.POST.get('q', None)
    if q:
      
      video_filter = search_filter([ 'title', 'transcription' ], q)
      video_results = Video.objects.filter(video_filter)
      
      clip_filter = search_filter([ 'video__title', 'transcription' ], q)
      clip_results = Clip.objects.filter(clip_filter)

    else:
      clip_results = None
      video_results = None

    return render( request, "search.html", {
      "p": p,
      "q": q,
      "video_results": video_results,
      "clip_results": clip_results
      }, )


def theme(request, slug=None):
    theme = get_object_or_404(Theme, slug=slug)
    return render( request, "theme.html", { "t": theme, }, )


def themes(request):
    p = Page.objects.filter(slug='themes')[0]
    themes = Theme.objects.all()
    return render( request, "themes.html", { "themes": themes, "p": p}, )


def video(request, id=None):
    video = get_object_or_404(Video, id=id)

    if video:
      other_videos = Video.objects.filter(profile_id=video.profile_id).exclude(id= video.id)
    else:
      other_videos = None

    return render( request, "video.html", {
        "video": video,
        "other_videos": other_videos
      }, )


def clip(request, id=None):
    clip = get_object_or_404(Clip, id=id)
    return render( request, "clip.html", { "clip": clip, "video": clip.video, }, )



def get_years(videos):
    years1 = videos.values_list('date_range_start__year', flat=True)    
    years2 = videos.values_list('date_range_end__year', flat=True)    
    years1 = list(dict.fromkeys(years1))
    years2 = list(dict.fromkeys(years2))
    years = list(dict.fromkeys(years1 + years2))
    years = [i for i in years if i] # remove None
    years.sort(reverse=True)
    years.append('Date Unknown')
    return years


def interviews(request):
    p = Page.objects.filter(slug='interviews')[0]
    videos = Video.objects.all()
    years = get_years(videos)
    return render( request, "interviews_map.html", {
        "districts": districts,
        "videos": videos,
        "years": years,
        "p": p 
      }, )


def gallery(request):
    p = Page.objects.filter(slug='interviews')[0]
    videos = Video.objects.all()    
    years = get_years(videos)
    return render( request, "interviews_gallery.html", {
        "districts": districts,
        "videos": videos,
        "years": years,
        "p": p 
      }, )


def about(request):
    p = Page.objects.filter(slug='about')[0]
    return render( request, "about.html", { "p": p, }, )


def interviews_home(request):
    p = Page.objects.filter(slug='home')[0]
    return render( request, "home.html", { "p": p, }, )


#@cache_page(60 * 60)
def interviews_map_xhr(request):
    victim_list = Video.objects.all();
    victim_filter = InterviewFilter(request.GET, queryset=victim_list)
    return render(request, "interviews_map_xhr.html", { "all": victim_filter.qs, }, content_type='application/json')


#@cache_page(60 * 60)
def interviews_gallery_xhr(request):
    victim_list = Video.objects.all();
    victim_filter = InterviewFilter(request.GET, queryset=victim_list)
    return render( request, "interviews_gallery_xhr.html", { "all": victim_filter.qs, }, )
