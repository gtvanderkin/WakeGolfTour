
class JSONGolferRoundScores (object):
    def __init__ (self, tournGolferId, roundId):     
        self.model = "golfer.golferroundscores"
        self.fields = {"grs_tourn_golfer": tournGolferId,
                       "grs_round": roundId,
                       "grs_total_score": 0,
                       "grs_hole2_score": 0,
                       "grs_hole3_score": 0,
                       "grs_hole4_score": 0,
                       "grs_hole5_score": 0,
                       "grs_hole6_score": 0,
                       "grs_hole7_score": 0,
                       "grs_hole8_score": 0,
                       "grs_hole9_score": 0,
                       "grs_hole10_score": 0,
                       "grs_hole11_score": 0,
                       "grs_hole12_score": 0,
                       "grs_hole13_score": 0,
                       "grs_hole14_score": 0,
                       "grs_hole15_score": 0,
                       "grs_hole16_score": 0,
                       "grs_hole17_score": 0,
                       "grs_hole18_score": 0}

def main():

    standaloneDjango()
    jsonStr = getJSONstr()
    writeJSONstr(jsonStr)
    
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
    
def getGolferID(name_to_get):

    from django.db import models
    from golfer.models import Golfer

    newGolfer = Golfer.objects.get(golfer_name = name_to_get)

    return newGolfer.golfer_id
    
def getTournGolferID (golfer_id, tourn_id):

    from django.db import models
    from golfer.models import TournGolfer

    tourn_golfers = TournGolfer.objects.filter(tg_tourn = tourn_id)

    tourn_golfer_id = 0

    for tourn_golfer in tourn_golfers:
        if tourn_golfer.tg_golfer.golfer_id == golfer_id:
            tourn_golfer_id = tourn_golfer.tg_id
            break

    return tourn_golfer_id
    
def getRoundIDs (tourn_id):            

    from django.db import models
    from tournament.models import Round

    rounds = Round.objects.filter(round_tourn_id = tourn_id)

    round1_id = 0
    round2_id = 0

    for round in rounds:
        if round.round_day == 'Sat':
            round1_id = round.round_id
        else:
            round2_id = round.round_id
    
    return round1_id, round2_id 
    
def readScores():
    
    # Add needed code
    # This is the same code as in your 
    # create_golfer_scores function from Project 1

    import csv

    filename = "golferScores.csv"

    round_scores_list = []

    # 3. Initialize the golfer_scores_id to 1
    golfer_scores_id = 1

    # 4. Use a try/except block to capture a File Not Found Error
    try:
        #    a. Open the input file object for reading the input file
        input_file = open(filename, 'r')

        #    b. Call the csv.reader function, passing in the input file
        #       and capturing the CSV file contents.
        input_lines = csv.reader(input_file)

        #    c. Create a list from the file contents: 'golfer_scores_list'
        golfer_scores_list = list(input_lines)

        #    d. Close input_file object
        input_file.close()

        # 5. Create an outer loop to read each set of scores in
        #    'golfer_scores_list'

        for scores in golfer_scores_list:
            #    Loop:
            #      a. Get the golfer_name, tourn_name, and day from the
            #         the first three elements, stripping whitespace.
            golfer_name = scores[0].strip()
            tourn_name = scores[1].strip()
            day = scores[2].strip()

            #      b. The rest of the elements (using slice scores[3:])
            #         are converted to a list of ints - scores_list.
            #         Use Python's 'map' function to convert the strings to
            #         ints and then use the 'list' function to convert the
            #         object returned from the map to a list.
            def convertInt(n):
                return int(n)

            scores_list = list(map(convertInt, scores[3:]))

            slaponlist = [golfer_name, tourn_name, day] + scores_list

            round_scores_list.append(slaponlist)

            #      i. Increment the golfer_scores_id
            golfer_scores_id += 1

    except IOError:
        print("File Not Found Error.")

    # 6. Print the round_scores_list objects to the console
    print("Round Scores List from readscores")
    for x in round_scores_list:
        print(x)
    # 7. Return the round_scores_list

    return round_scores_list

    
def getJSONstr():

    # Add needed code

    import json

    scores = readScores()
    tourn_id = getTournID()
    round1_id, round2_id = getRoundIDs(tourn_id)

    round_scores = []

    for score in scores:
        golfer_id = getGolferID(score[0])
        tourn_golfer_id = getTournGolferID (golfer_id, tourn_id)
        
        if score[2] == 'Sat':
            grs = JSONGolferRoundScores (tourn_golfer_id, round1_id)
        else:
            grs = JSONGolferRoundScores (tourn_golfer_id, round2_id)
        
        scores_list = list(map(int, score[3:]))
        
        round_score = 0;          
        j = 1
        for sc in scores_list:
            grs.fields["grs_hole{}_score".format(j)] = sc
            round_score = round_score + sc
            j = j + 1
                                 
        grs.fields["grs_total_score"] = round_score
            
        json_grs = json.dumps (grs.__dict__)   
        round_scores.append (json_grs)
         
    jsonStr = str (round_scores).replace ("'",'')
    
    return jsonStr
            
def writeJSONstr (jsonStr):
    
    outFile = open ('golfer_round_scores_data.json', 'w')
    outFile.write (jsonStr)
    outFile.close()
    
main()   
   

