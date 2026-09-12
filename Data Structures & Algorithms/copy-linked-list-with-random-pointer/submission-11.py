"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

#Create a deep copy of the list.

#The deep copy should consist of exactly n new nodes, each including:

#The original value val of the copied node

#A next pointer to the new node corresponding to the next pointer of the original node

#A random pointer to the new node corresponding to the random pointer of the original node

#Note: None of the pointers in the new list should point to nodes in the original list.

#Return the head of the copied linked list.


#In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

#0 <= n <= 100
# -100 <= Node.val <= 100
# Node values are not guaranteed to be unique.
# random is null or is pointing to some node in the linked list.

#if the node values are not unique, we must identify them in some way (their counter)
#how do we know which the random points to, it must be by address
#how can we figure out the address?

#or is there another way
#if we go one by one as we create the new linked list 
#we need to figure out where the random is pointing to
#how do we do that in python?
#hash()?
#if we hash the address then we can see which ones are different to each other
#we could do one pass and add the addresses to the list
#then do another pass where we identify the randoms

#hash map? item address : index
#
# minimum we must
# identify all the nodes and their indexes
# go through each node again and map their randoms to indexes
# create new nodes as per the values in og nodes
# arrange them as per stored data
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
        addr_indx = {} # address : indx
        val_random_indx = [] # index of node, index of random
        new_nodes = []

        sentinal = Node(0)
        sentinal.next = head
        current = sentinal

        current = sentinal.next
        counter = 0
        while current:
            addr_indx[current] = counter
            counter += 1
            new_nodes.append(Node(current.val))
            current = current.next

        addr_indx[None] = counter
        new_nodes.append(None)


        current = sentinal.next
        while current:
            val_random_indx.append((current.val, addr_indx[current.random])) #val, random indx
            current=current.next
            
        del addr_indx            
        

        for i in range(len(val_random_indx)):
            new_nodes[i].next = new_nodes[i+1]
            new_nodes[i].random = new_nodes[val_random_indx[i][1]]


        return new_nodes[0]
