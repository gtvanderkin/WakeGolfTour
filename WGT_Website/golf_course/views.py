from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import GolfCourse
from tournament.models import Tournament
from . models import GolfCourse, Hole

# first view:
# List golf courses from home page hyperlinks navigation panel

class GolfCourseListView(generic.ListView):
    model = GolfCourse
    template_name = 'golf_course/golf_course_list.html'
    context_object_name = 'golf_courses'

class GolfCourseDetailView(generic.DetailView):
    model = GolfCourse
    template_name = 'golf_course/golf_course_detail.html'

    def get_context_data(self, **kwargs):
        # This is how to get the context dictionary
        context = super(GolfCourseDetailView, self).get_context_data(**kwargs)

        # We are using the golf course object which was clicked by the user
        golf_course = self.get_object()

        # Use the golf course object to get the rest of the context
        context['golf_course'] = golf_course
        context['holes'] = Hole.objects.filter(hole_course_id = golf_course.course_id)
        context['tournaments'] = Tournament.objects.filter(tourn_course_id = golf_course.course_id)

        return context
