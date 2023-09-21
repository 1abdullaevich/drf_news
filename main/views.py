from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class CategoryView(APIView):
    def post(self, request):

        data = request.data
        serializer = CategorySerializers(data=data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request):
        users = Users.objects.all()
        user_data = []
        for user in users:
            articles = ArticleModel.objects.filter(author=user.id)
            serializer = UserSerializers(user)
            article_serializer = ArticleSerializers(articles, many=True)
            user_data.append({
                "user": serializer.data,
                "posts": article_serializer.data
            })
        return Response(user_data)


class ArticleView(APIView):
    def post(self, request):
        data = request.data
        serializer = ArticleSerializers(data=data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request):
        article = ArticleModel.objects.all()
        serializer = ArticleSerializers(article, many=True)
        return Response(serializer.data)
