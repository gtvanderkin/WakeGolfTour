from django.shortcuts import redirect
from golfer.models import GolferRoundScores

def homepage (request):
    return redirect ('golf_course_list')
