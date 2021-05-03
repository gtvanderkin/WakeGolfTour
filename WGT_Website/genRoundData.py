

class JSONRound (object):
    def __init__ (self, tournId, day):     
        self.model = "tournament.round"
        self.fields = {"round_tourn": tournId,
                       "round_day": day}

def main():
    standaloneDjango()
    jsonStr = getJSONstr ()
    writeJSONstr (jsonStr)
    
def standaloneDjango():
    import os
    import django
    import json

    os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "wgt_site.settings")
    django.setup()

def getTournID():
    from django.db import models
    from tournament.models import Tournament

    newTournObj = Tournament.objects.get (
                         tourn_name="Oak City Championship")
    return newTournObj.tourn_id

def getJSONstr ():
    import json
    
    tourn_id = getTournID()
    rounds = []

    sat_round = JSONRound (tourn_id, "Sat")
    sun_round = JSONRound (tourn_id, "Sun")

    json_sat_round = json.dumps (sat_round.__dict__)
    json_sun_round = json.dumps (sun_round.__dict__)

    rounds.append (json_sat_round)
    rounds.append (json_sun_round)

    jsonStr = str (rounds).replace ("'",'')
    return jsonStr

def writeJSONstr (jsonStr):
    outFile = open ('rounds_data.json', 'w')    
    outFile.write (jsonStr)    
    outFile.close()

main()
