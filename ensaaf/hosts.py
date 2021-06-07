from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'(interviews)', 'interviews.urls', name='interviews'),
    host('', 'ensaaf.urls', name='data'),
)
