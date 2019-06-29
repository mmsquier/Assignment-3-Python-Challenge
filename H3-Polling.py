import os
import csv

csvpath=os.path.join('election_data.csv')

Total_votes=0
Votes=0
LVotes=0
CVotes=0
TVotes=0
KP=0
LP=0
CP=0
TP=0
Winner=0

with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    csv_header= next(csvreader) # To ignore headers 


    for r in csvreader: 
    
        Total_votes=Total_votes+1
        names= str(r[2])
        if names== "Khan":
            Votes=Votes + 1
        if names=="Li":
            LVotes= LVotes +1
        if names=="Correy": 
            CVotes= CVotes +1
        if names=="O'Tooley":
            TVotes=TVotes+1
    KP=(Votes/Total_votes)*100
    LP=(LVotes/Total_votes)*100
    CP=(CVotes/Total_votes)*100
    TP=(TVotes/Total_votes)*100

    if Votes> LVotes and CVotes and TVotes:
        print("Khan wins")
    Final=(f"Election Results  \n\
        ............................\n\
        Total Votes: {Total_votes}\n\
        ..............................\n\
        Khan: ({KP}%) ({Votes})\n\
        Correy: ({CP}%) ({CVotes})\n\
        Li: ({LP}%) ({LVotes}%)\n\
        O'Tooley: ({TP}%) ({TVotes}%)\n\
        ................................\n\
        Winner: Khan \n\"))

print(Final, file=open('pypoll.txt','a'))
