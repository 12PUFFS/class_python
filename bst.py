class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        def _insert(node):
            if not node:
                return TreeNode(key, value)
            if key < node.key:
                node.left = _insert(node.left)
            elif key > node.key:
                node.right = _insert(node.right)
            else:
                node.value = value
            return node
        self.root = _insert(self.root)
    
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None
    
    def delete(self, key):
        def _delete(node):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left)
            elif key > node.key:
                node.right = _delete(node.right)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.key, node.value = min_node.key, min_node.value
                node.right = _delete_min(node.right)
            return node
        
        def _delete_min(node):
            if not node.left:
                return node.right
            node.left = _delete_min(node.left)
            return node
        
        self.root = _delete(self.root)
    
    def height(self):
        def _height(node):
            return 0 if not node else max(_height(node.left), _height(node.right)) + 1
        return _height(self.root)
    
    def is_balanced(self):
        def _check(node):
            if not node:
                return 0, True
            l_h, l_b = _check(node.left)
            r_h, r_b = _check(node.right)
            return max(l_h, r_h) + 1, l_b and r_b and abs(l_h - r_h) <= 1
        return _check(self.root)[1]
    
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append((node.key, node.value))
                _inorder(node.right)
        _inorder(self.root)
        return result


def main():
    bst = BinarySearchTree()
    
    print("=" * 50)
    print("БИНАРНОЕ ДЕРЕВО ПОИСКА")
    print("=" * 50)
    
  
    print("\n1. ВСТАВКА:")
    for k, v in [(50,"A"), (30,"B"), (70,"C"), (20,"D"), (40,"E"), 
                 (60,"F"), (80,"G"), (35,"H"), (45,"I")]:
        bst.insert(k, v)
        print(f"   ({k}:{v})", end=" ")
    print()
    
    
    print("\n2. ПОИСК:")
    for k in [40, 90, 35]:
        v = bst.search(k)
        print(f"   {k}: {'найден -> ' + v if v else 'не найден'}")
    
    
    print(f"\n3. ВЫСОТА: {bst.height()}")
    print(f"4. СБАЛАНСИРОВАНО: {bst.is_balanced()}")
    
    
    print("\n5. УДАЛЕНИЕ:")
    for k in [20, 40, 50]:
        bst.delete(k)
        print(f"   Удален {k}")
    
   
    print(f"\n6. ИТОГ (inorder): {[(k,v) for k,v in bst.inorder()]}")
    print("=" * 50)


if __name__ == "__main__":
    main()