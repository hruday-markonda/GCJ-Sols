#Imports
import time
#

#Problem Functions
def card_print(card):
    
    for row in card:
        output = ""
        for column in row:
            output += column
        print(output)

def solve(L):
    rows = L[0]
    columns = L[1]
    
    card = []
    border = True
    
    for i in range(2*rows + 1):
        line = []
        border_char = "+"
        cell_char = "|"
        for j in range(2*columns + 1):
            if border == True:
                line.append(border_char)
                if border_char == "+":
                   border_char = "-"
                   
                else:
                    border_char = "+"
            
            else:
                line.append(cell_char)
                if cell_char == "|":
                   cell_char = "."
                   
                else:
                    cell_char = "|"
        card.append(line)    
        border = not border     
    
    card[0][0] = card[0][1] = card[1][0] = card[1][1] = "."
    card_print(card)
#

#Helper Input Functions
def q_in():
    return int(input())

def q_inlt():
    return list(map(int,input().split()))
#

#Inputting
if __name__ == '__main__':
    #start_time = time.time()
    T = q_in() #Usually Number of testcases
    for t in range(1, T+1): 
        L = q_inlt() #Usually the input lines 
        output_statement = 'Case #' + str(t) + ': '
        print(output_statement)
        solve(L) #Solve
    #print(time.time() - start_time)