#Imports
import time
#

#Problem Functions

class node:
    def __init__(self, fun):
        self.fun = fun
        self.point = None
        self.back = []
        self.chainscore = []
        
        
class tree:
    def __init__(self, mods):
        self.mods = []
        self.trigger = []
        
    def add_node(self, node) -> None:
        self.mods.append(node)
        self.trigger.append(node)
    
    def update_point(self, i, Pi) -> None:
        self.mods[i].point = Pi
        self.mods[Pi].back.append(i)
        self.trigger[Pi] = None
    
    def get_node(self, index) -> 'Node':
        return self.mods[index]
        

def solve(mods, funs, points):
    machine = tree(mods)    
    for Fi in funs:
        new_node = node(Fi)
        machine.add_node(new_node)
    
    for i, Pi in enumerate(points):
        machine.update_point(i, Pi)
    
    '''
    for trig in machine.trigger:
        if trig == None:
            next
        
        i = trig.point
        node = machine.get_node(trig.point)
        add_up = trig.fun
        
        if i == 0:
            trig.chainscore.append((i, add_up))
        
        while node != None:
            if len(node.back) > 1:
                trig.chainscore.append((i, add_up))
            
            add_up += node.fun
            node = machine.get_node(node.point)
            
        print(trig.chainscore)
    '''
    return "1"
#

#Helper Input Functions
def q_in():
    return(int(input()))

def q_inlt():
    return(list(map(int,input().split())))
#

#Inputting
if __name__ == '__main__':
    start_time = time.time()
    T = q_in() #Usually Number of testscases
    for t in range(1, T+1): 
        n_modules = q_in() #Number of moduless   
        f_fun = q_inlt() #Fun factor of each module
        p_point = q_inlt() #The module which i points to, P=0 is abyss
        output_statement = 'Case #' + str(t) + ': ' + solve(n_modules, f_fun, p_point) #Solve
        print(output_statement)
    print(time.time() - start_time)

#