from django.conf.urls import url
from . import views

app_name="question"

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^register_acc/$', views.UserFormView.as_view(), name='reg'),
    url(r'^question/new/$', views.question_new, name='question_new'),
    url(r'^(?P<ques_id>[0-9]+)/$', views.details, name="details"),
    url(r'^add_ans/$', views.add_ans, name="add_ans")
]