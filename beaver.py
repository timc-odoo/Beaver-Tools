import sys
import os
import datetime



#filename = input("Enter log file name: ")
filename = sys.argv[1]
dbname = sys.argv[2]
print(filename)
print(dbname)
date = datetime.date.today()
date = str(date)
#dbname = input("Enter database name: ")
print("Filtering ", filename, "for the database ", dbname)
path = "~/Beaver-Tools/" + dbname + date + ".txt"
path = os.path.expanduser(path)
newfile = open(path, "w")
flag = False
with open(filename) as old:
    for line in old:
        cur_line = line
        if dbname in cur_line or flag is True:
            if "2026" in cur_line:
                #print(cur_line)
                flag = False
            if "ERROR" in cur_line:
                flag = True
                #print(flag)
            newfile.write(cur_line)
