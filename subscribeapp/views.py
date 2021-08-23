from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])
        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독 했는데 누르면 구독 삭제, 구독 안했는데 누르면 구독하기
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':kwargs['project_pk']})

# 구독중인 게시판 리스트만 보여주기
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        # 요청한 유저가 구독한 게시판을 list 형태로 가져오기
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        # project_list에 article 리스트가 있다면 (게시글)
        article_list = Article.objects.filter(project__in=project_list)
        return article_list