from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    with open('pyramid_learning_journal/templates/index.html') as file:
        return Response(file.read())


def detail_view(request):
    with open('pyramid_learning_journal/templates/detail-entry.html') as file:
        return Response(file.read())


def create_view(request):
    with open('pyramid_learning_journal/templates/new-entry.html') as file:
        return Response(file.read())


def update_view(request):
    with open('pyramid_learning_journal/templates/edit-entry.html') as file:
        return Response(file.read())
