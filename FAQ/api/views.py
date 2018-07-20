from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from FAQ.models import Question, Topic
from FAQ.api.serializers import (
    TopicListSerializer,
    QuestionSerializer,
)


class TopicListView(ListAPIView):
    serializer_class = TopicListSerializer
    queryset = Topic.objects.all()

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(TopicListView, self).dispatch(*args, **kwargs)


class TopicDetailView(ListAPIView):
    lookup_field = 'slug'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Question.objects.filter(active=True, topic__slug=slug)
        return queryset

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(TopicDetailView, self).dispatch(*args, **kwargs)


class QuestionDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        topic = self.kwargs['topic__slug']
        slug = self.kwargs['slug']
        queryset = Question.objects.filter(active=True, topic__slug=topic, slug=slug)
        return queryset

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(QuestionDetailView, self).dispatch(*args, **kwargs)


class QuestionListView(ListAPIView):
    lookup_field = 'slug'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Question.objects.filter(active=True, question_for=slug)
        return queryset

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(QuestionListView, self).dispatch(*args, **kwargs)
