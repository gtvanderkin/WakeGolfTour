

class JSONTournGolfer(object):
    def __init__(self, tg_tourn, tg_golfer):
        self.model = "golfer.tourngolfer"
        self.fields = {"tg_tourn": tg_tourn,
                       "tg_golfer": tg_golfer[1]}

def main():
    
    standaloneDjango()
    jsonStr = getJSONstr()
    writeJSONstr(jsonStr)
        
def standaloneDjango():
    
    import os
    import django
    import json
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wgt_site.settings")
    django.setup()

def getTournID():

    from django.db import models
    from tournament.models import Tournament

    newTournObj = Tournament.objects.get(tourn_name = "Oak City Championship")
    return newTournObj.tourn_id

def getTopTenGolfers():
    from django.db import models
    from golfer.models import Golfer, GolferRoundScores

    golfers = Golfer.objects.all()
    scores = GolferRoundScores.objects.all()
    
    golfer_lists = []
    
    for golfer in golfers:
        total_score = 0        
        num_rounds = 0
        golfer_list = []
        for score in scores:
            if score.grs_tourn_golfer.tg_golfer.golfer_id == golfer.golfer_id:
                num_rounds = num_rounds + 1
                total_score = total_score + score.grs_total_score
                
        avg_round_score = float (total_score / num_rounds)        
        golfer_list.append (avg_round_score)
        golfer_list.append (golfer.golfer_id)     
        golfer_lists.append (golfer_list)

    sorted_list = sorted (golfer_lists)
    return sorted_list[:10]
    
def getJSONstr():

    import json

    tourn_id = getTournID()

    tourn_golfers = []

    top_ten_list = getTopTenGolfers()

    for golfer in top_ten_list:
        golfer_id = golfer[1]
        tourn_golfer = JSONTournGolfer(tourn_id, golfer)
        tourn_golfers.append(json.dumps(tourn_golfer.__dict__))

    jsonStr = str(tourn_golfers).replace("'",'')
    return jsonStr
    
def writeJSONstr (jsonStr):
    
    outFile = open ('tourn_golfer_data.json', 'w')
    outFile.write (jsonStr)
    outFile.close()


main()
