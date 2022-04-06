# from django.shortcuts import get_object_or_404, render
from django.views import generic
from rest_framework import viewsets
from .models import Card, CardSet
from .serializers import CardSerializer


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'aceproc/index.html'
    context_object_name = 'set_list'

    def get_queryset(self):
        '''Return the last five published questions'''
        return CardSet.objects.order_by('-pub_date')[:5]


class CardView(viewsets.ModelViewSet):
    # Two variables are made for REST:
    # Serializer_class = serializer from serializer.py
    # Queryset = the model to take the data from
    serializer_class = CardSerializer
    queryset = Card.objects.all()
# class CardDetailView(generic.DetailView):
#     # Takes in the model, and passes it into the view
#     model = Card
#     template_name = "aceproc/detail.html"

#     def get_queryset(self):
#         '''Returns all the cards from the cardset'''
#         return Card.objects.filter(rel_cardset=)


# def CardView(request, cardset_id):
#     # Queries for a cardset with the id of cardset_id;
#     # passed in from detail.html
#     cardset = get_object_or_404(CardSet, pk=cardset_id)
#     # print(cardset.card_set.all())
#     # RESULT: <QuerySet <Card: """">>
#     context = {
#         'Cardset': cardset,
#     }
#     return render(request, 'aceproc/detail.html', context)

# TODO: include a card view to edit and delete cards
