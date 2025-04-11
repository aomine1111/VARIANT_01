class TreeNode:
    """
    Класс TreeNode представляет узел бинарного дерева.
    Каждый узел имеет значение и ссылки на левого и правого потомков.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Простейшая реализация бинарного дерева.
    """

    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, current_node, data):
        """
        Вставляет новый узел в левое поддерево.
        Если левый потомок существует, новый узел становится родителем для предыдущего левого узла.
        """
        new_node = TreeNode(data)
        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, data):
        """
        Вставляет новый узел в правое поддерево.
        Если правый потомок существует, новый узел становится родителем для предыдущего правого узла.
        """
        new_node = TreeNode(data)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node

    def inorder_traversal(self, node, result=None):
        """Обходит дерево в симметричном порядке (in-order)."""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

if __name__ == '__main__':
    # Пример использования бинарного дерева
    bt = BinaryTree(10)
    bt.insert_left(bt.root, 5)
    bt.insert_right(bt.root, 15)
    bt.insert_left(bt.root.left, 3)
    bt.insert_right(bt.root.left, 7)
    print("In-order обход дерева:", bt.inorder_traversal(bt.root))
