import csv

row1 = [x for x in range(0,10)]
row2 = [str(x*x)+"\n"+"5" for x in range(0,10)]

RESULTS = [
    row1,
    row2,
]

RESULTS = [
    ("x,", "z"),
    ("howdo", "iknow"),
]

with open('output.csv','w', newline="") as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(RESULTS)

run_log = []

with open("bad_log.txt", "r") as f:
    data = f.readlines()
    
    for line in data:
        if line.startswith("Step"):
            run_log.append(line)
            
with open('output.txt','w') as result_file:
    for line in run_log:
        result_file.write(line)