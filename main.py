from GenNormallyDistributedArray import GenNormallyDistributedArray
from Subtask1 import subtask1
from Subtask2 import subtask2
from Subtask3 import GetParameters

if __name__=="__main__":
    numbers=GenNormallyDistributedArray()
    print(numbers)
    subtask1(numbers)
    print("\n")
    subtask2(numbers,1,0.95)
    x1=GenNormallyDistributedArray()
    x2=GenNormallyDistributedArray()
    x3=GenNormallyDistributedArray()
    y=GenNormallyDistributedArray()
    betas= GetParameters([x1,x2,x3],y)