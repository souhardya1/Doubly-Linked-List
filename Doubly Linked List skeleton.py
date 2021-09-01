# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 08:49:55 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head!=None:
            self.head.prev=new_node
        self.head=new_node
    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
ll=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
ll.printList()