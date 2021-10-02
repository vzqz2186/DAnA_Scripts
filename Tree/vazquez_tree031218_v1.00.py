"""
          Program: Tree
           Author: Daniel Vazquez
             Date: 02/12/2018 (v1.00)

       Assignment: Create a tree by using any method necessary.

         Due Date: 2/13/2018

        Objective: Initialize a fully functional binary tree by using any 
                   method.
                   (WORKS??: v1.00)

      Execute via: >>python vazquez_tree031218_v1.00.py

    Sample output: 


**               Source: https://pythonspot.com/python-tree/                 **
**				Template based on Dr. Nichols program example.				 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.

def main():
	
    class Tree(object):          # Defines what a tree is since Python does
        def _init_(self):        # not know what a tree is from the get go.
            self.left = None  # There can be something at the right of the tree
            self.right = None # There can be something at the left of the tree.
            self.data = None     # It is "that" something at the right or left.
	
    root = Tree()                # Initializes the root (Level 0).
    root.data = "I AM ROOT"      # Declares what is at the root node.

    root.left = Tree()           # Initializes left node of Level 1.
    root.left.data = "LEFT"      # Declares what is at this node.

    """ The following two nodes are descendants of LEFT """
    root.left.left = Tree()      # Initializes 1st node of Level 2.
    root.left.left.data = "LL"   # Declares what is at the node.
    root.left.right = Tree()     # Initializes 2nd node of Level 2.
    root.left.right.data = "LR"	 # Declares what is at the node.

    root.right = Tree()          # Initializes right node of Level 1.
    root.right.data = "RIGHT"    # Declares what is at the node.

    """ THe following two nodes are descendants of RIGHT """
    root.right.left = Tree()     # Initializes node.
    root.right.left.data = "RL"  # Declares what is at the node.
    root.right.right = Tree()    # Initializes node.
    root.right.right.data = "RR" # Declares what is at the node.

    print(root.left)

    disDate() # Prints date

# Date/Time Function---------------------------------------------------------80
#  Source:
#   https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
    print(time.strftime('%m/%d/%Y %H:%M'))
	
# Call Main------------------------------------------------------------------80
main()