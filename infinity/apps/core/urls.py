from django.conf.urls import patterns, url

from core.views import *


urlpatterns = patterns(
    '',
    url(r'^ajax/custom-chained-view-url/$', AjaxChainedView.as_view(), name='ajax_chained_view'),
    url(
        r'^comment/list/1$',
        CommentListView1.as_view(),
        name="comment-list1"
    ),
    url(
        r'^comment/(?P<slug>.*)/update/$',
        CommentUpdateView.as_view(),
        name="comment-update"
    ),

    url(
        r'^comment/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        CommentDeleteView.as_view(),
        name="comment-delete"
    ),

    url(
        r'^comment/(?P<goal>.*)/list/$',
        CommentListView2.as_view(),
        name="comment-list2"
    ),
    url(
        r'^comment-create/$',
        CommentCreateView.as_view(),
        name="comment-create"
    ),
    url(
        r'^goal/(?P<need>.*)/list/1$',
        GoalListView1.as_view(),
        name="goal-list1"
    ),
    url(
        r'^goal/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        GoalDeleteView.as_view(),
        name="goal-delete"
    ),

    url(
        r'^goal/(?P<slug>.*)/update/$',
        GoalUpdateView.as_view(),
        name="goal-update"
    ),

    url(
        r'^goal/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        GoalDetailView.as_view(),
        name="goal-detail"
    ),
    url(
        r'^goal/(?P<need>.*)/list/2$',
        GoalListView2.as_view(),
        name="goal-list2"
    ),
    url(
        r'^goal/list/$',
        GoalListView2.as_view(),
        name="goal-list"
    ),
    url(
        r'^goal-create/$',
        GoalCreateView.as_view(),
        name="goal-create"
    ),
    url(
        r'^goal-create/(?P<need_id>\d+)/$',
        GoalCreateView.as_view(),
        name="goal-create"
    ),
    url(
        r'^work/(?P<task>.*)/list/1$',
        WorkListView1.as_view(),
        name="work-list1"
    ),
    url(
        r'^work/(?P<slug>.*)/update/$',
        WorkUpdateView.as_view(),
        name="work-update"
    ),

    url(
        r'^work-create/(?P<task>.*)/$',
        WorkCreateView.as_view(),
        name="work-create"
    ),
    url(
        r'^work/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        WorkDeleteView.as_view(),
        name="work-delete"
    ),

    url(
        r'^work/list/$',
        WorkListView2.as_view(),
        name="work-list"
    ),
    url(
        r'^work/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        WorkDetailView.as_view(),
        name="work-detail"
    ),
    url(
        r'^idea/(?P<goal>.*)/list/1$',
        IdeaListView1.as_view(),
        name="idea-list1"
    ),
    url(
        r'^idea/(?P<slug>.*)/update/$',
        IdeaUpdateView.as_view(),
        name="idea-update"
    ),

    url(
        r'^idea-create/$',
        IdeaCreateView.as_view(),
        name="idea-create"
    ),
    url(
        r'^idea-create/(?P<goal_id>\d+)/$',
        IdeaCreateView.as_view(),
        name="idea-create"
    ),
    url(
        r'^idea/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        IdeaDeleteView.as_view(),
        name="idea-delete"
    ),

    url(
        r'^idea/list/$',
        IdeaListView2.as_view(),
        name="idea-list"
    ),
    url(
        r'^idea/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        IdeaDetailView.as_view(),
        name="idea-detail"
    ),
    url(
        r'^step/(?P<plan>.*)/list/1$',
        StepListView1.as_view(),
        name="step-list1"
    ),
    url(
        r'^step/(?P<slug>.*)/update/$',
        StepUpdateView.as_view(),
        name="step-update"
    ),

    url(
        r'^step-create/(?P<plan>.*)/$',
        StepCreateView.as_view(),
        name="step-create"
    ),
    url(
        r'^step/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        StepDeleteView.as_view(),
        name="step-delete"
    ),

    url(
        r'^step/list/$',
        StepListView2.as_view(),
        name="step-list"
    ),
    url(
        r'^step/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        StepDetailView.as_view(),
        name="step-detail"
    ),
    url(
        r'^task/(?P<step>.*)/list/1$',
        TaskListView1.as_view(),
        name="task-list1"
    ),
    url(
        r'^task/(?P<slug>.*)/update/$',
        TaskUpdateView.as_view(),
        name="task-update"
    ),

    url(
        r'^task-create/(?P<step>.*)/$',
        TaskCreateView.as_view(),
        name="task-create"
    ),
    url(
        r'^task/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        TaskDeleteView.as_view(),
        name="task-delete"
    ),

    url(
        r'^task/list/$',
        TaskListView2.as_view(),
        name="task-list"
    ),
    url(
        r'^task/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    url(
        r'^need-create/$',
        NeedCreateView.as_view(),
        name="need-create"
    ),
    url(
        r'^need/(?P<slug>.*)/update$',
        NeedUpdateView.as_view(),
        name="need-update"
    ),
    url(
        r'^need/list/$',
        NeedListView.as_view(),
        name="need-list"
    ),
    url(
        r'^need/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        NeedDetailView.as_view(),
        name="need-detail"
    ),
    url(
        r'^plan/(?P<idea>.*)/list/1$',
        PlanListView1.as_view(),
        name="plan-list1"
    ),
    url(
        r'^plan/(?P<slug>.*)/update/$',
        PlanUpdateView.as_view(),
        name="plan-update"
    ),

    url(
        r'^plan-create/(?P<idea>.*)/$',
        PlanCreateView.as_view(),
        name="plan-create"
    ),
    url(
        r'^need-ajax-create/$',
        NeedAjaxCreateView.as_view(),
        name="need-ajax-create"
    ),
    url(
        r'^goal-ajax-create/$',
        GoalAjaxCreateView.as_view(),
        name="goal-ajax-create"
    ),
    url(
        r'^plan/(?P<slug>[a-zA-Z-_0-9]+)/delete/$',
        PlanDeleteView.as_view(),
        name="plan-delete"
    ),

    url(
        r'^plan/list/$',
        PlanListView2.as_view(),
        name="plan-list"
    ),
    url(
        r'^plan/(?P<slug>[a-zA-Z-_0-9]+)/detail/$',
        PlanDetailView.as_view(),
        name="plan-detail"
    ),
)
