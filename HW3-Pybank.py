#uploaded sheet to visual studio/python
import os
import csv
#from statistics import mean
csvpath = os.path.join('budget_data.csv')

#define function & accept the data as main parameter 

Total_Months=0
Profit_sum=0
Change=0
GIncrease=0
GDecrease=0

Revenue_change=0
Total_Revenuechange=0
prevenue=0
GMonth=0
DMonth=0

#used csv module to read 
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    csv_header= next(csvreader) # To ignore headers 
    
# To read each row after the header (loops)

    for  r in (csvreader): 
        revenue=int(r[1])

        Total_Months= Total_Months+1

        Profit_sum= Profit_sum + revenue
        
        if Total_Months> 1:
            Revenue_change= (revenue-prevenue)
            
            Total_Revenuechange= Total_Revenuechange+ Revenue_change 
        prevenue=revenue

        if Revenue_change> GIncrease:
            GMonth=r[0]
            GIncrease= Revenue_change

        if Revenue_change< GDecrease:
            DMonth=r[0]
            GDecrease= Revenue_change  

    Change= Total_Revenuechange/(Total_Months-1)


    Printout=(f"Total Months:{Total_Months}\n\
    Total Revenue: ${Profit_sum}\n\
    Average Revenue Change: $ {Change}\n\
    Greatest Increase in Revenue:{GMonth}, (${GIncrease})\n\
    Greatest Decrease in Revenue:{DMonth}, (${GDecrease})")

    print(Printout, file=open('pybank.txt','a'))


