import os
import csv

# inform path to collect data from 

budget_data = os.path.join ('..', 'Resources', 'budget_data.csv')

# define lists to store data

months = []
results = []
result_change = []

# read csv file

with open (budget_data, "r", encoding="utf-8") as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")

    # print(csvreader)

    csv_header = next (csvreader)


    for row in csvreader:
        # print(row)


        months.append(row[0])
        results.append(int(row[1]))
       
 


        
        # result_change = ((results[1]) - (results[0]))

        #        result_change.append((results[1]) - (results[0]))
    
    # print(results)


    for x in range(len(results) - 1):
        result_change.append(results[x+1] - results[x])

    #print(result_change)


# Total of months 

    print(len(months))

# net total amount over period 
   
    print(sum(results))

# Changes in "profit / losses" over the period 

    print(sum(result_change))

# Average of changes in "profit / losses" over the period     

    print((sum(result_change)) / (len(months)-1))

#     


    print(min(result_change))
    # print(result_change.index(min(result_change)))
    print(months[(result_change.index(min(result_change)))+1])



    print(max(result_change))
    # print(result_change.index(max(result_change)))
    print(months[(result_change.index(max(result_change)))+1])




   
   
#     max_value = max(result_change)
#     index_max = list.index(max_value)
# print(index_max)


    # max_value = max(result_change)
    # index_max = list.index(max_value)

    # print(index_max)



#  max_val = max(list)
# index_max = list.index(max_val)



        # print(value)


    # result_change = (sum(results[x:len(results)])) / (len(results))
    # print(result_change)




# x = results.co

#     print(x)







    # print(len(months))
    # print(sum(results))

    









    









    # csv_header = next(csvreader)

    # for months in csvreader:

    #     months.append(months[0])
    #     print(months)

#         results.append(row[1])


# print(months)






    


# define lists