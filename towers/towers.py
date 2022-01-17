#!/bin/python3
import sys

src=[]
aux=[]
trg=[]

num_moves=0

def disc(stack,i):
    if len(stack) < i:
        return " " * max_width * 2
    else:
        return ("#"*stack[i-1]*2).center(max_width*2," ")
    
def printTowers():
    for i in range(max_width,0,-1):
        print(disc(src,i),disc(aux,i),disc(trg,i))
        
    print("*"*(max_width*2*3+2))

def move(n,s,t,a):   
    if n > 0:
        global num_moves
        num_moves+=1
        
        move(n-1,s,a,t)
        t.append(s.pop())
        printTowers()
        move(n-1,a,t,s)

if __name__ == "__main__":    
    if len(sys.argv) < 2:
        l=3
    else:
        l=int(sys.argv[1])
        
    src=[x for x in range(l,0,-1)]
    max_width=len(src+aux+trg)
    
    printTowers()       
    move(len(src),src,trg,aux)
    print("Total Number of Moves = ",num_moves)