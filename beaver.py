import sys
import os
import datetime
from rapidfuzz import fuzz



filename = sys.argv[1]
dbname = sys.argv[2]
print(filename)
print(dbname)
date = datetime.date.today()
date = str(date)
cur_year = datetime.date.today().year
cur_year = str(cur_year)
print("Filtering ", filename, "for the database ", dbname)
path = "~/Beaver-Tools/" + dbname + date + ".txt"
path = os.path.expanduser(path)
newfile = open(path, "w")
flag = False
with open(filename) as old:
    for line in old:
        if(len(line) == 0):
           break
        else:
           cur_line = line
           logyear = cur_line[:4]
           yearscore = fuzz.partial_token_set_ratio(logyear, cur_year, score_cutoff=51)
           linescore = fuzz.partial_token_set_ratio(dbname, cur_line, score_cutoff=90)
           #if(yearscore != 0.0 or yearscore != 100.0):
           #    print(cur_line, yearscore)
           cur_line = cur_line.replace('"', '\'')
           if yearscore > 51:
               flag = False
           if "ERROR" in cur_line and linescore >= 90:
               flag = True
           if linescore>=90 or flag is True:
               newfile.write(line)
