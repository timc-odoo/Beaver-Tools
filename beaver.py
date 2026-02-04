import sys

#filename = input("Enter log file name: ")
filename = sys.argv[1]
dbname = sys.argv[2]
print(filename)
#dbname = input("Enter database name: ")
print("Filtering ", filename, "for the database ", dbname)
newfile = open("/home/odoo/Downloads/filtered.txt", "a")
flag = False
with open(filename) as old:
    for line in old:
        cur_line = line
        if dbname in cur_line or flag is True:
            newfile.write(cur_line)
            if "2026" in cur_line:
                #print(cur_line)
                flag = False
            if "ERROR" in cur_line:
                flag = True
                #print(flag)
