from django.urls import path
from documentation_app.views import index,LatestQuestionhtmView,detail,DetailView,vote,results,ResultsView,latest_question, latest_questionhtml,latest_questionhtml1,detail404
#this app name is for differentiate b/w url among multiple different app in {%url } check in index.html
app_name = 'documentation_app'
urlpatterns = [
    path('index/', LatestQuestionhtmView.as_view(), name='index1'),
    #Generic detail view DetailView must be called with either an object pk or a slug in the URLconf.
    path('<int:pk>/', DetailView.as_view(), name='detail'), 
    path('<int:question_id>/detail/', detail404, name='detail404concept'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('latest/',latest_question, name="latestquestion"),
    path('latesthtml/',latest_questionhtml, name="questionhtml"),
    path('latesthtml1/',latest_questionhtml1, name="questionhtmlrender"),
]
