# CSV
import csv

with open("data_csv.csv",'w') as csvfile:
    wirter = csv.writer(csvfile)
    wirter.writerow(['id','name','age'])
    wirter.writerow(['10001','Mike',20])
    wirter.writerow(['10002','Bob',22])
    wirter.writerow(['10003','Jordan',21])
    print("Successful\n")