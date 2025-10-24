# main.py
from bst import BST
tree = BST([10, 5, 15, 2, 7, 18])
print("Search 7:", tree.search(7)) # True
print("Search 99:", tree.search(99)) # False
print("Comparisons so far:", tree.comparisons)
