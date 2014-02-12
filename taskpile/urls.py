from django.conf.urls.defaults import *

urlpatterns = patterns(
    'taskpile.views',
    (r'^$', 'homepage'),
    (r'^ajax/ajax_create_task$', 'ajax_create_task'),
    (r'^ajax/ajax_complete_task$', 'ajax_complete_task'),
    (r'^ajax/ajax_mark_task_incomplete$', 'ajax_mark_task_incomplete'),
    )
