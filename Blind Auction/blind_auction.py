from IPython import get_ipython
import time


get_ipython().magic('clear')
def AskName():
    Name = input("What is your name? ")
    return Name

def Bid():
    bid = int(input("what is your bid? "))
    return bid

def dict_name(dic,name,bid):
    dic[name] = bid
    return dic

more_bidders = "yes"
dic = dict()
while more_bidders != "No" or more_bidders != "no":
    name = AskName()
    bid = Bid()
    dic = dict_name(dic,name,bid)
    more_bidders = input("are there any more bidders? ")
    if more_bidders == "yes" or more_bidders == "YES":
        get_ipython().magic('clear')
    if more_bidders == "no" or more_bidders == "No":
    
        break
        
Max = 0    
for name,bid in dic.items():
    if bid>Max:
        Max = bid
        Max_Name =name
        
get_ipython().magic('clear')
time.sleep(1)
print("{} has placed the highest bid of {}".format(Max_Name,Max))