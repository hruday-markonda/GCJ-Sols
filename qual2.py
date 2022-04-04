#Imports
import time

#

#Problem Functions

def solve(inks): #Order for inks is C,M,Y,K
    D = 10**6
    ideal = []
    
    for index in range(4):
        colour = [inks[0][index], inks[1][index], inks[2][index]]
        ideal.append(min(colour))
    
    cum_sum = sum(ideal)
    if cum_sum < D:
        return "IMPOSSIBLE"
        
    else:
        difference = cum_sum - D
        index_maxs = max_indexs(ideal)
        max_i = 0
        while sum(ideal) > D:
            
            if ideal[index_maxs[max_i]] == 0:
                max_i += 1
                
                if max_i == 4:
                    return "IMPOSSIBLE"
            else:    
                if ideal[index_maxs[max_i]] <= difference:
                    difference -= ideal[index_maxs[max_i]]
                    ideal[index_maxs[max_i]] = 0
            
                else:
                    ideal[index_maxs[max_i]] = ideal[index_maxs[max_i]] - difference
                    difference = 0
                    break
    
    return ' '.join(list(map(str,ideal)))

def max_indexs(array):
    new_arr = array.copy()
    maxs = []
    for i in range(len(new_arr)):
        max_index = new_arr.index(max(new_arr))
        new_arr[max_index] = -1
        maxs.append(max_index)
    return maxs
    
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
        inks = []
        for i in range(3):
            inks.append(q_inlt()) #Usually the input lines 
        output_statement = 'Case #' + str(t) + ': ' + solve(inks)
        print(output_statement)
    #print(time.time() - start_time)
        
        