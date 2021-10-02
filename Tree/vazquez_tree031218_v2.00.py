
# coding: utf-8

# In[1]:

#T = DiGraph({0:[1,2,3], 1:[4,5], 2:[6,7], 3:[8,9]})
#T.graphplot(layout='tree',tree_root=0,tree_orientation='down').show()

BT = BinaryTree('[[[[.,.],[.,.]],[.,.]],[[.,.],[[.,.],[.,.]]]]')
ascii_art(BT)


# Sources:
# 1)http://doc.sagemath.org/html/en/reference/plotting/sage/graphs/graph_plot.html
# 
# 2)http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/binary_tree.html
# 
# 3)Dustin Powell helped me figure out why SageMath would not start on OVM.
# 
# 4)Maxwell Rahmani explained me how to work Sage.
