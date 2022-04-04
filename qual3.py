#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(n, L):
    sorted_list = L
    sorted_list.sort()
    max_straight = 1
    start = 1
    
    straight_length = 0
    current_number = start
    for dice in sorted_list:
        if current_number <= dice:
            current_number += 1
            straight_length += 1
    
    if straight_length > max_straight:
        max_straight = straight_length
    start += 1
    
    return str(max_straight)
    
#

#Helper Input Functions
def q_in():
    return(int(input()))

def q_inlt():
    return(list(map(int,input().split())))
#

#Inputting
if __name__ == '__main__':
    #start_time = time.time()
    T = q_in() #Usually Number of testscases
    for t in range(1, T+1): 
        n = q_in() #Number of Dice   
        L = q_inlt() #Dice with different sides 
        output_statement = 'Case #' + str(t) + ': ' + solve(n, L) #Solve
        print(output_statement)
    #print(time.time() - start_time)

#