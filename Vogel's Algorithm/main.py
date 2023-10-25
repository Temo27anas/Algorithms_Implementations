#Vogel's Approximation
#@Author: Anas Temouden

import numpy as np
import pandas as pd

def min_difference(arr):
    if(len(arr) == 1):
        return arr[0]
    min1 = np.min(arr)
    arr = np.delete(arr, np.argmin(arr))
    min2 = np.min(arr)
    return min2 - min1

def vogel_algorithm(cost_matrix, supply, demand):
    # demand & supply check
    if(sum(demand)>sum(supply)):
        print("Demand is greater than supply!")
        return 0
    elif(sum(demand)==sum(supply)):
        print("Possible solution!")

    cost = 0
    iterations = 1
    print("============Initialization:===============")
    print(cost_matrix)
    print("Supply: ", supply)
    print("Demand: ", demand)

    while (supply.size != 0 and demand.size != 0):
        print(f"==============={iterations}==================")

        dic_row = {}
        dic_col = {}

        #get min_difference for each row and col
        for row in range(len(cost_matrix)):
            dic_row[row] = min_difference(cost_matrix[row])
        print("Min_diff on Rows: ", dic_row)
        for col in range(len(cost_matrix[0])):
            dic_col[col] = min_difference(cost_matrix[:,col])
        print("Min_diff on Columns:", dic_col)

        #Select the row or col with the highest min_difference
        min_row = max(dic_row, key=dic_row.get)
        min_col = max(dic_col, key=dic_col.get)

        #if the biggest value is in dic_row:
        if(dic_row[min_row] > dic_col[min_col]):

            print(">>Working on row: ", min_row)
            min_index = np.argmin(cost_matrix[min_row])

            #allocate all the supply to the smallest value in the row
            allocation = min(supply[min_row], demand[min_index])
            supply[min_row] -= allocation
            demand[min_index] -= allocation
            print("Allocation: ", allocation)
            cost += allocation * cost_matrix[min_row][min_index]

            if(supply[min_row] == 0):
                print(">>Deleting row: ", min_row)
                cost_matrix = np.delete(cost_matrix, min_row, 0)
                supply = np.delete(supply, min_row)
            if(demand[min_index] == 0):
                print(">>Deleting col: ", min_index)
                cost_matrix = np.delete(cost_matrix, min_index, 1)
                demand = np.delete(demand, min_index)
           
        #if the biggest value is in dic_col:
        else:
            print(">>Working on col: ", min_col)
            min_index = np.argmin(cost_matrix[:,min_col])

            #allocate all the supply to the smallest value in the col
            allocation = min(supply[min_index], demand[min_col])
            supply[min_index] -= allocation
            demand[min_col] -= allocation
            print("Allocation: ", allocation)
            cost += allocation * cost_matrix[min_index][min_col]

            if(supply[min_index] == 0):
                print(">>Deleting row: ", min_index)
                cost_matrix = np.delete(cost_matrix, min_index, 0)
                supply = np.delete(supply, min_index)
            if(demand[min_col] == 0):
                print(">>Deleting col: ", min_col)
                cost_matrix = np.delete(cost_matrix, min_col, 1)
                demand = np.delete(demand, min_col)

        print(cost_matrix)
        print("Supply: ", supply)
        print("Demand: ", demand)

        iterations += 1
                     
    print("Total cost: ", cost)

#Test cases:
cost_matrix = np.array([[11,13,17,14],[16,18,14,10],[21,24,13,10]])
supply=np.array([250,300,400])
demand=np.array([200,225,275,250])
vogel_algorithm(cost_matrix, supply, demand)#12075

#print("\n#############################################\n")

#cost_matrix = np.array([[3,1,7,4],[2,6,5,9],[8,3,3,2]])
#supply=np.array([300,400,500])
#demand=np.array([250,350,400,200])
#vogel_algorithm(cost_matrix, supply, demand) #2850

#print("\n#############################################\n")

#cost_matrix = np.array([[8,6,12,9],[7,11,10,14],[13,8,8,7]])
#supply=np.array([400,500,600])
#demand=np.array([325,425,475,275])
#vogel_algorithm(cost_matrix, supply, demand) #10950



