from django.shortcuts import render


def content_detail(self, id):
    return "The detail page with id {}".format(id)