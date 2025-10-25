from __future__ import annotations
from typing import Optional, Iterable, Any

class Node:
    __slots__ = ("key", "left", "right")
    def __init__(self, key: Any):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    def __init__(self, values: Optional[Iterable[Any]] = None):
        self.root: Optional[Node] = None
        self.comparisons: int = 0
        if values:
            for v in values:
                self.insert(v)

    #def insert(self, key: Any) -> None:
    #"""Insert key into BST. Ignore duplicates."""
    #raise NotImplementedError
    def insert(self, key: Any) -> None:
        def _insert(node: Optional[Node], key: Any) -> Node:
            if node is None:
                return Node(key)
            self.comparisons += 1
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
                # equal: do nothing (ignore duplicates)
            return node
        self.root = _insert(self.root, key)

    #def search(self, key: Any) -> bool:
    #"""Return True if key is in the BST, else False."""
    #raise NotImplementedError
    def search(self, key: Any) -> bool:
        node = self.root
        while node:
            self.comparisons += 1
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    #def inorder(self) -> List[Any]:
    #"""Return inorder traversal (sorted sequence)."""
    #raise NotImplementedError
    def inorder(self) -> list[Any]:
        result = []
        def _inorder(node: Optional[Node]) -> None:
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result


    #def preorder(self) -> List[Any]:
    #raise NotImplementedError
    def preorder(self) -> list[Any]:
        result = []
        def _preorder(node: Optional[Node]) -> None:
            if node:
                result.append(node.key)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    #def postorder(self) -> List[Any]:
    #raise NotImplementedError
    def postorder(self) -> list[Any]:
        result = []
        def _postorder(node: Optional[Node]) -> None:
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.key)
        _postorder(self.root)
        return result


    #def level_order(self) -> List[Any]:
    #"""Breadth-first traversal."""
    #raise NotImplementedError
    def level_order(self) -> list[Any]:
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    #def min(self) -> Optional[Any]:
    #raise NotImplementedError\
    def min(self) -> Optional[Any]:
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.key

    #def max(self) -> Optional[Any]:
    #raise NotImplementedError
    def max(self) -> Optional[Any]:
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.key

    #def delete(self, key: Any) -> bool:
    #""Delete key if present. Return True if deleted."""
    #raise NotImplementedError
    def delete(self, key: Any) -> bool:
        deleted = False

        def _delete(node: Optional[Node], key: Any) -> Optional[Node]:
            nonlocal deleted
            if node is None:
                return None

            self.comparisons += 1

            # Move left if smaller
            if key < node.key:
                node.left = _delete(node.left, key)
            # Move right if larger
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Found node to delete
                deleted = True

                # Case 1: No children (leaf)
                if node.left is None and node.right is None:
                    return None

                # Case 2: One child
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                # Case 3: Two children
                # Find the inorder successor (smallest in right subtree)
                succ_parent = node
                succ = node.right
                while succ.left:
                    succ_parent = succ
                    succ = succ.left

                # Replace node's key with successor's key
                node.key = succ.key

                # Delete the successor
                if succ_parent.left is succ:
                    succ_parent.left = succ.right
                else:
                    succ_parent.right = succ.right

            return node

        # Start deletion from the root
        self.root = _delete(self.root, key)
        return deleted
    
    def is_valid_bst(self) -> bool:
        def _check(n: Optional[Node], low, high) -> bool:
            if not n: return True
            if (low is not None and n.key <= low) or (high is not None and n.key >= high):
                return False
            return _check(n.left, low, n.key) and _check(n.right, n.key, high)
        return _check(self.root, None, None)
