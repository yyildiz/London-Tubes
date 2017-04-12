import csv 

N = 5
start_point = "East Ham"


visited = []
current_stops = [start_point]

for i in range(N):
    temp = []
    visited.extend(current_stops)
    for stop in current_stops:
        f = open("tubeLines.csv", "r")
        reader = csv.reader(f)
        for row in reader:
            if(row[1] == stop and row[2] not in visited and row[2] not in temp):
                temp.append(row[2])
            if(row[2] == stop and row[1] not in visited and row[1] not in temp):
                temp.append(row[1])
    current_stops = temp
    
print(sorted(current_stops))        

f.close()



