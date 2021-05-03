from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Golfer, GolferRoundScores
from golfer.models import Golfer, TournGolfer, GolferRoundScores
from tournament.models import Tournament
from golf_course.models import GolfCourse, Hole

# first view:
# List golf courses from home page hyperlinks navigation panel

class GolferListView(generic.ListView):
    model = Golfer
    template_name = 'golf_course/golfer_list.html'
    context_object_name = 'golfers'


class GolferDetailView(generic.DetailView):
    model = Golfer
    template_name = 'golfer/golfer_detail.html'

    # override the get_context_data to return to context_object_name
    def get_context_data(self, **kwargs):
        # This is how to get the context dictionary
        context = super(GolferDetailView, self).get_context_data(**kwargs)

        # Use the golfer object that was clicked by the user
        golfer = self.get_object()

        # Use the golfer object to get the rest of the context
        context['golfer'] = golfer
        context['scores'] = GolferRoundScores.getTournScoresByGolfer(golfer.golfer_id)

        return context


class GolferRoundScoresView(generic.DetailView):
    model = TournGolfer
    template_name = 'golfer/golfer_round_scores.html'

    def get_context_data(self, **kwargs):
        context = super(GolferRoundScoresView, self).get_context_data(**kwargs)

        tourn_golfer = self.get_object()

        tg_id = self.kwargs.get('pk')

        scores = GolferRoundScores.objects.filter(grs_tourn_golfer_id=tg_id)

        tournament = Tournament.objects.filter(pk=tourn_golfer.tg_tourn.tourn_id).get()

        golf_course = GolfCourse.objects.filter(pk=tournament.tourn_course.course_id).get()

        holes = Hole.objects.filter(hole_course_id=golf_course.course_id)

        context['tourn_golfer'] = tourn_golfer
        context['tournament'] = tournament
        context['golf_course'] = golf_course
        context['scores'] = scores
        context['holes'] = holes

        return context
