#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import random


# In[2]:


# Command-Line Visual Functions Starts Here.


# In[3]:


def EndGameBoard():
    print("-----------------")
    print("END GAME BOARD")
    print(Board)
    print("PRIOR TARGET")
    print(Target)
    print("-----------------")
    print("")


# In[4]:


def GameRules():
    print("-----------------")
    print("GAME RULES")
    print("You need to choose two adjacent elements and the operation on each step.")
    print("Division will be rounded to floor. Division by zero will be zero.")
    print("")
    print("Operations:")
    print("1-Add 2-Substract 3-Multiply 4-Divide")
    print("")
    print("EXAMPLE")
    print("State: [30, 50, 10, 40]")
    print("Operation: 1 Index1: 0 Index2: 1")
    print("Result: [(30+50), 10, 40]")
    print("Result: [  80   , 10, 40]")
    print("-----------------")
    print("")


# In[5]:


def CurrentState():
    n = len(Board)-1
    print("-----------------")
    print("CURRENT INDEXES: ")
    print(", ".join(str(n) for n in range(n+1)))
    print("CURRENT GAME BOARD")
    print(Board)
    print("CURRENT TARGET")
    print(Target)
    print("-----------------")
    print("")


# In[6]:


def isBigger(str1, str2):
    try:
        int1 = int(str1)
        int2 = int(str2)
        
        if (int1 > int2):
            return True
        else:
            return False
    except:
        return False


# In[7]:


def isNext(str1, str2):
    try:
        int1 = int(str1)
        int2 = int(str2)
        
        if ( ((int1+1 == int2) | (int2+1 == int1)) & (int1>=0) & (int2>=0) ) :
            return True
        else:
            return False
    except:
            return False


# In[8]:


def delTwoNextElements(l, i, j):

    if (i<j):
        del l[i:j+1]
        return l
    elif (j<i):
        del l[j:i+1]
        return l
    else:
        print("Unexpected error occured!")
        return None


# In[9]:


def Addition(l, i, j):
    #print(l,i,j)
    OperationResult = l[i] + l[j] 
    l = delTwoNextElements(l, i, j)
    l.insert( min(i, j), OperationResult)
    return l


# In[10]:


def Substraction(l, x, y):
    i = min(x,y)
    j = max(x,y)
    #print(l,i,j)
    OperationResult = l[i] - l[j]
    l = delTwoNextElements(l, i, j)
    l.insert( min(i, j), OperationResult)
    return l


# In[11]:


def Multiplication(l, i, j):
    #print(l,i,j)
    OperationResult = l[i] * l[j]
    l = delTwoNextElements(l, i, j)
    l.insert( min(i, j), OperationResult)
    return l


# In[12]:


def Division(l, x, y):
    i = min(x,y)
    j = max(x,y)
    #print(l,i,j)
    if l[j] == 0:
        OperationResult = 0
    else:
        OperationResult = int(l[i] / l[j])
    l = delTwoNextElements(l, i, j)
    l.insert( min(i, j), OperationResult)
    return l


# In[ ]:





# In[13]:


def InputNextMove():
    
    n = len(Board)-1
    
    print("Enter the operation.")
    operation = input()

    while(not( (operation.isdigit()) & (isBigger(operation,"0")) & (isBigger("5", operation)) )):
        print("Wrong type of input entered. Enter in index range [1-4]")
        operation = input()

    print("Enter the index of the first element.")
    index1 = input()

    while(not((index1.isdigit()) & (isBigger(index1,"-1")) & (isBigger(n+1,index1)))):
        print("Wrong type of input entered. Enter in index range [0-"+str(n)+"]")
        index1 = input()

    print("Enter the index of the next element.")
    index2 = input()

    while(not( (index2.isdigit()) & (isNext(index1,index2)) & (isBigger(index2,"-1")) & (isBigger(n+1,index2)))):
        print("Wrong type of input entered. Enter an index next to", index1)
        index2 = input()

    print("Your move is: {} {} {}".format (operation, index1, index2))
    
    print("Confirm [y|n]: ")
    confirm = input()
    
    while(not( (confirm =="y") | (confirm =="Y") | (confirm =="n") | (confirm =="N"))):
        print("Wrong type of input entered. Enter [y|n]: ")
        confirm = input()
    
    if ((confirm =="y") | (confirm =="Y")):
        print("-----------------")
        print("")
        return int(operation), int(index1), int(index2)
    else:
        print("-----------------")
        print("")
        operation, index1, index2 = InputNextMove()
        return int(operation), int(index1), int(index2)
    


# In[14]:


def Operate(Board, operation, index1, index2):
    
    if operation == 1:
        Board = Addition(Board, index1, index2)
        
    elif operation == 2:
        Board = Substraction(Board, index1, index2)
        
    elif operation == 3:
        Board = Multiplication(Board, index1, index2)
        
    elif operation == 4:
        Board = Division(Board, index1, index2)
        
    else:
        print("Unexpected error occured!")
    
    return Board


# In[15]:


# Command-Line Visual Functions Finishes Here.


# In[ ]:





# In[16]:


# MinMaxFunctions Starts Here.


# In[17]:


# Checks if the board is in terminal state
def Terminal_Test(Board):
    if len(Board) == 1:
        return True
    else:
        return False


# In[18]:


# Gives a numeric value to terminal states.
def Utility(Board):
    Value = Board[0]
    x = int(Target)
    
    Utility = abs(Value - x)
    
    return Utility


# In[19]:


# Returns list of legal moves for the given state.
def Actions_Result(Board):
    #print('Actions_Result')
    actions = []
    
    n = len(Board)
    indexes = [n for n in range(n)]
    index_pairs = [(x,y) for x,y in zip(indexes, indexes[1:])]
    
    ByValueCopy = Board[:]
    
    for pair in index_pairs:
        i, j = pair[0], pair[1]
        #print(i,j)
        
        ByValueCopy = Board[:]
        current_action = Addition(ByValueCopy, i, j)
        actions.append(current_action)
        #print(current_action)
        
        ByValueCopy = Board[:]
        current_action = Substraction(ByValueCopy, i, j)
        actions.append(current_action)
        #print(current_action)
        
        ByValueCopy = Board[:]
        current_action = Multiplication(ByValueCopy, i, j)
        actions.append(current_action)
        #print(current_action)
        
        ByValueCopy = Board[:]
        current_action = Division(ByValueCopy, i, j)
        actions.append(current_action)
        #print(current_action)
        
        
    return actions


# In[ ]:





# In[20]:


def Max_Value(Board, alpha, beta):
    
    if Terminal_Test(Board):
        return Utility(Board), Board
    
    v = -np.inf
    actions = Actions_Result(Board)
    #print('actions')
    #print(actions)
    #print('thats all for actions')
    for action in Actions_Result(Board):
        
        #print("Max_Fun: ", Board, action, alpha, beta)
        v_compare, result = Min_Value(action, alpha, beta)
        #print("v / v_comp ",v,v_compare)
        v = max(v, v_compare)
        
        if v >= beta:
            return v, result
        alpha = max(alpha, v)
    
    return v, result


# In[21]:


def Min_Value(Board, alpha, beta):
    
    if Terminal_Test(Board):
        return Utility(Board), Board
    
    v = np.inf
    
    for action in Actions_Result(Board):
        
        #print("Min_Func: ", Board, action, alpha, beta)
        v_compare, result = Max_Value(action, alpha, beta)
        #print("v / v_comp ",v,v_compare)
        v = min(v, v_compare)
        
        if v <= alpha:
            return v, result
        beta = min(beta, v)
    
    return v, result


# In[22]:


def Alpha_Beta_Search(Board):
    
    if(len(Board)==1):
        return None,None,None,Board
    
    v = -np.inf
    action_list = Actions_Result(Board)
    
    for index, action in enumerate(action_list):
        
        v_new, result_new = Max_Value(Board, -np.inf, np.inf)
        
        if(v_new > v):
            operation = (index%4) + 1
            i = int(index/4)
            j = i + 1
            result = result_new
            v = v_new
            
    
    return operation, i, j, result


# In[23]:


def AI_Move(Board):
    
    # Random Move
    #n = len(Board)
    #indexes = [n for n in range(n)]
    #index_pairs = [(x,y) for x,y in zip(indexes, indexes[1:])]
    #tuple_choice = random.choice(index_pairs)
    
    #operation = random.randint(1,5)
    #i = tuple_choice[0]
    #j = tuple_choice[1]
    #result = "random"
    
    # Alpha_Beta_Search() Move by 80% chance
    #if random.randint(0,101) < 80:
        #operation, i, j, result = Alpha_Beta_Search(Board)
        
    operation, i, j, result = Alpha_Beta_Search(Board)
    
    print("AI's Move is: ",operation, i, j, result)
    
    Board = Operate(Board, operation, i, j)
    
    return Board


# In[24]:


# MinMaxFunctions Ends Here.


# In[25]:


#deneme = list(random.randint(101, size = 7, dtype=np.int64))
#Target = random.randint(101, dtype=np.int64)

#print(deneme, Target)
#operation,i,j,result = Alpha_Beta_Search(deneme)
#print(operation,i,j,result)


# In[ ]:





# In[ ]:





# In[26]:


# The Main Function Starts Here.


# In[ ]:


# Initialize the game.
Board = list(random.randint(101, size = 7, dtype=np.int64))
Target = random.randint(101, dtype=np.int64)


IfContinue = True
while(IfContinue):
    
    GameRules()
    CurrentState()
    operation, index1, index2 = InputNextMove()
    
    Operate(Board, operation, index1, index2)
    print("Your Move")
    CurrentState()
    
    Board = AI_Move(Board)
    print("AI's Move")
    CurrentState()
    
    if(len(Board) == 1):
        print("GAME OVER!")
        EndGameBoard()
        IfContinue = False
        x = input("Enter something to exit.")


# In[ ]:





# In[ ]:


dtype("=np.int64")


# In[ ]:


deneme = list(random.randint(101, size = 4))
Target = random.randint(101)

print(deneme, Target)
operation,i,j,result = Alpha_Beta_Search(deneme)
print(operation,i,j,result)


# In[ ]:





# In[ ]:




