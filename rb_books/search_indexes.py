# coding=utf-8
from haystack import indexes
from models import booksInfo


class booksInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self):

        return booksInfo

    def index_queryset(self, using=None):

        return self.get_model().objects.all()

    # def newsbooks(request):
    #     newbook = booksInfo.objects.all().order_by('-id')[:2]
    #
    #     context = {
    #         'newbook': newbook,
    #     }
    #     return context