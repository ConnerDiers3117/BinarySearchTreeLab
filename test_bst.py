# test_bst.py
from bst import BST
def test_insert_search_ordering():
    t = BST([10,5,15,2,7,18])
    assert t.search(7)
    assert not t.search(100)
    assert t.inorder() == [2,5,7,10,15,18]
    assert t.preorder()[0] == 10
    assert t.min() == 2
    assert t.max() == 18
    assert t.is_valid_bst()
def test_delete_cases():
    t = BST([10,5,15,2,7,18,6])
    # leaf
    assert t.delete(18)
    assert t.inorder() == [2,5,6,7,10,15]
    # one child
    assert t.delete(5) # after removing 5, tree should still be valid
    assert t.is_valid_bst()
    # two children
    t = BST([10,5,15,2,7,6,8])
    assert t.delete(5)
    assert t.inorder() == [2,6,7,8,10,15]
    assert t.is_valid_bst()
#Run:
#pip install pytest
#pytest -q
