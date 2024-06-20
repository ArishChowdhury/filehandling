import csv

with open('IPL_2018.csv') as f:
  data=csv.reader(f)

  data_list=list(data)

print(data_list)

import csv

with open('IPL_2018.csv') as f:
  data=csv.reader(f)
  data_list=list(data)

match_runs=[]
for row in data_list[1:]:
  print("Total runs scored by",row[0],"in IPL2018 are",row[4])
  match_runs.append(int(row[4]))

print("Total run scored by all the players in matches are",sum(match_runs))