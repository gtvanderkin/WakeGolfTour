from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Tournament
from golfer.models import GolferRoundScores

# first view:
# List golf courses from home page hyperlinks navigation panel

class TournamentListView(generic.ListView):
    model = Tournament
    template_name = 'tournament/tournament_list.html'
    context_object_name = 'tournaments'

class TournamentDetailView(generic.DetailView):
    model = Tournament
    template_name = 'tournament/tournament_detail.html'

    # We need to override get_context_data to return the context
    def get_context_data(self, **kwargs):
        # This is how to get the context dictionary
        context = super(TournamentDetailView, self).get_context_data(**kwargs)

        # We are using the tournament object which was clicked by the user
        tournament = self.get_object()

        # We are using the tournament object to get the rest of the context
        context['tournament'] = tournament
        # Call the GolferRoundScores method, getTournScores, to return scores
        context['scores'] = GolferRoundScores.getTournScores(tournament.tourn_id)

        return context
