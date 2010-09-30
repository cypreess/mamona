from django.conf.urls.defaults import *
from utils import import_backend_modules

includes_list = []
for bknd_name, urls in import_backend_modules('urls').items():
	includes_list.append(url(r'^%s/' % bknd_name, include(urls)))

urlpatterns = patterns('mamona',
		url('^process/(?P<payment_id>[0-9]+)/$', 'views.process_payment', name='mamona-process-payment'),
		*includes_list
		)