class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root.children.append(Node(data))

    def weight(self, node):
        if node is None:
            return 0
        else:
            return len(node.children) + sum(self.weight(child) for child in node.children)

    def order(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.order(child) for child in node.children) if node.children else 1

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(child) for child in node.children) if node.children else 1

# Uso del código
tree = Tree()

while True:
    data = input('Ingresa un nodo (o "salir" para terminar): ')
    if data.lower() == 'salir':
        break
    tree.add_node(data)

print('Peso del árbol:', tree.weight(tree.root))
print('Orden del árbol:', tree.order(tree.root))
print('Altura del árbol:', tree.height(tree.root))
