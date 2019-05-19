from django.urls import path
from documentation_app.views import index,detail,vote,results,latest_question, latest_questionhtml,latest_questionhtml1,detail404
#this app name is for differentiate b/w url among multiple different app in {%url } check in index.html
app_name = 'documentation_app'
urlpatterns = [
    path('index/',index,name="index"),
    # ex: /polls/5/
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/detail/', detail404, name='detail404concept'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
    path('latest/',latest_question, name="latestquestion"),
    path('latesthtml/',latest_questionhtml, name="questionhtml"),
    path('latesthtml1/',latest_questionhtml1, name="questionhtmlrender"),
]
