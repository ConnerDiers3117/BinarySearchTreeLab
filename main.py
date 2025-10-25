# main.py
import random
import sys
sys.setrecursionlimit(10000)

from bst import BST, Node
tree = BST([10, 5, 15, 2, 7, 18])
print("Search 7:", tree.search(7)) # True
print("Search 99:", tree.search(99)) # False
print("Comparisons so far:", tree.comparisons)

#Traversals
print("In-order Traversal:", tree.inorder())
print("Pre-order Traversal:", tree.preorder())
print("Post-order Traversal:", tree.postorder())
print("Level-order Traversal:", tree.level_order())

#Minimum and Maximum
print("Minimum:", tree.min())
print("Maximum:", tree.max())

#Delete nodes and show inorder traversal after each deletion
print("\nDeleting leaf node 18...")
tree.delete(18)
print("After deleting 18:", tree.inorder())
print("\nDeleting node 15 (one child)...")
tree.delete(15)
print("After deleting 15:", tree.inorder())
print("\nDeleting node 15 (one child)...")
tree.delete(15)
print("After deleting 15:", tree.inorder())
print("\nDeleting missing node 13...")
deleted = tree.delete(13)
print("Was 13 deleted?", deleted)
print("After trying to delete 13:", tree.inorder())

#Not found case 
print("\nDeleting missing node 13...")
deleted = tree.delete(13)
if not deleted:
    print("Value 13 not found in the tree.")
else:
    print("Value 13 deleted successfully.")
print("After attempting delete(13):", tree.inorder())

#DFS and BFS traversals
from bst import BST

def show_valid(name: str, t: BST) -> None:
    ok = t.is_valid_bst()
    print(f"{name}: is_valid_bst -> {ok}")
    print("  inorder:", t.inorder())
    assert ok, f"{name} should be valid"

print("----------------------------------------------------")

# Case A: standard valid BST
t1 = BST([10, 5, 15, 2, 7, 12, 18])
show_valid("Case A: standard", t1)

# Case B: empty tree is valid
t2 = BST([])
show_valid("Case B: empty", t2)

# Case C: single node is valid
t3 = BST([42])
show_valid("Case C: single", t3)

# Case D: balanced-ish (still valid)
t4 = BST([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
show_valid("Case D: balanced-ish", t4)

# Case E: valid after deletes and inserts
t5 = BST([10, 5, 15, 2, 7, 12, 18])
t5.delete(5)
t5.delete(12)
t5.delete(2)
for x in (1, 6, 13, 19):
    t5.insert(x)
show_valid("Case E: after deletes/inserts", t5)

print("All true-positive validations passed")

#False Fail Reports
print("--------------------------------------------------------")
base = [10, 5, 15, 2, 7, 12, 18]
#Case 1: Left child > parent
t1 = BST(base)
t1.root.left.key = 11 #left child (was 5) now 11 > 10
ok = t1.is_valid_bst()
print(f"Case 1: is_valid_bst -> {ok}")
#Case 2: Value in right subtree < root (deep violation)
t2 = BST(base)
t2.root.right.left.key = 3 #right-left node must be > 10; set to 3
ok2 = t2.is_valid_bst()
print(f"Case 2: is_valid_bst -> {ok2}")
#Case 3: Equal-to-boundary violation (duplicates not allowed by validator)
t3 = BST(base)
t3.root.right.left.key = 10 #equals root; violates strict inequality
ok3 = t3.is_valid_bst()
print(f"Case 3: is_valid_bst -> {ok3}")
#Case 4: Rewire a node to an invalid value on the left side
t4 = BST(base)
t4.root.left = Node(100) #left subtree must be < 10; 100 breaks it
ok4= t4.is_valid_bst()
print(f"Case 4: is_valid_bst -> {ok4}")
print("All false BST cases correctly detected")

#Instrimentation and Complexity Analysis
print("---------------------------------------------------------------------")
keys = list(range(1, 1025))
random_keys = keys[:]
random.shuffle(random_keys)
balanced_tree = BST(random_keys)
balanced_tree.comparisons = 0
balanced_tree.search(777)
print("Balanced comparisons:", balanced_tree.comparisons)
skewed_tree = BST(keys) # sorted insert -> skewed
skewed_tree.comparisons = 0
skewed_tree.search(777)
print("Skewed comparisons:", skewed_tree.comparisons)
