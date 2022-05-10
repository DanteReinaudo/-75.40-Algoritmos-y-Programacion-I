# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:49:55 2020

@author: User
"""

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): #Muesta el ultimo elemento de la fila
        if self.items==[]:
            return None
        else:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
     
    def __repr__(self): #Lo que aparece cuando printea
        return repr(self.items)
    
    
# pila=Stack()
# pila.push(4)
# pila.push(20) 
# pila.peek()
# print(pila.isEmpty()) 
# print(pila.size())
# print(pila) 