from platform import node


class UserNode:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends  
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def get_name(self, user_id):
        node = self.find(self.root, user_id)
        return node.name if node else f"User{user_id}"

    def insert(self, root, user_id, name, friends_list):
        if root is None:
            return UserNode(user_id, name, friends_list)

        if user_id < root.user_id:
            root.left = self.insert(root.left, user_id, name, friends_list)
        elif user_id > root.user_id:
            root.right = self.insert(root.right, user_id, name, friends_list)

        return root


    def find(self, root, user_id):
        if root is None:
            return None

        if user_id == root.user_id:
            return root
        elif user_id < root.user_id:
            return self.find(root.left, user_id)
        else:
            return self.find(root.right, user_id)

    def inorder_traversal(self, root, result):
        if root is not None:
            self.inorder_traversal(root.left, result)
            result.append(root.user_id)
            self.inorder_traversal(root.right, result)

    def find_max(self, root):
        while root.right is not None:
            root = root.right
        return root

    def delete(self, root, user_id):
        if root is None:
            return None

        if user_id < root.user_id:
            root.left = self.delete(root.left, user_id)
        elif user_id > root.user_id:
            root.right = self.delete(root.right, user_id)
        else:
            
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
        
            temp = self.find_max(root.left)
            root.user_id = temp.user_id
            root.name = temp.name
            root.friends = temp.friends
            root.left = self.delete(root.left, temp.user_id)

        return root

    def suggest_friends(self, user_id, max_suggestions):
        user = self.find(self.root, user_id)
        if user is None:
            return []

        direct_friends = set(user.friends)
        fof_count = {}

        for friend_id in user.friends:
            friend_node = self.find(self.root, friend_id)
            if friend_node:
                for fof_id in friend_node.friends:
                    if fof_id != user_id and fof_id not in direct_friends:
                        fof_count[fof_id] = fof_count.get(fof_id, 0) + 1

        sorted_fof = sorted(fof_count.items(), key=lambda x: x[1], reverse=True)

        return [self.get_name(uid) for uid, _ in sorted_fof[:max_suggestions]]

    def get_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def is_balanced(self, root):
        if root is None:
            return True

        diff = abs(self.get_height(root.left) - self.get_height(root.right))
        if diff > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)

   
    def get_leaf_count(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self.get_leaf_count(root.left) + self.get_leaf_count(root.right)

def get_all_nodes(root):
    if root is None:
        return []
    return get_all_nodes(root.left) + [root] + get_all_nodes(root.right)




import networkx as nx
import matplotlib.pyplot as plt

def visualize_friends(tree):
    G = nx.Graph()

    def add_edges(root):
        if root:
            for f in root.friends:
                G.add_edge(tree.get_name(root.user_id), tree.get_name(f))
            add_edges(root.left)
            add_edges(root.right)

    add_edges(tree.root)

    nx.draw(G, with_labels=True, node_size=2000, font_size=10)
    plt.title(
    "Dynamic Social Network Graph: Friend-of-Friend Recommendation System\n"
    "Graph-Based Relationship Mapping with Mutual Connection Weighting",
    fontsize=12,
    fontweight='bold'
)
    plt.show()



def visualize_bst(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + f"{root.name} ({root.user_id})")
        visualize_bst(root.left, level + 1, "L--- ")
        visualize_bst(root.right, level + 1, "R--- ")

def show_complexity(tree):
    n = len(get_all_nodes(tree.root))
    height = tree.get_height(tree.root)

    print("\n--- Complexity Analysis ---")
    print(f"Total Users (n): {n}")
    print(f"Tree Height: {height}")

    if tree.is_balanced(tree.root):
        print("Tree is Balanced → Operations ≈ O(log n)")
    else:
        print("Tree is Unbalanced → Operations ≈ O(n)")




tree = BST()

tree = BST()

tree.root = tree.insert(tree.root, 30, "Alice", [20])
tree.root = tree.insert(tree.root, 20, "Bob", [30])
tree.root = tree.insert(tree.root, 40, "Charlie", [])
tree.root = tree.insert(tree.root, 10, "David", [])
tree.root = tree.insert(tree.root, 50, "Eve", [])

print("Sparse Network - Suggested friends for Alice:")
print(tree.suggest_friends(30, 3))

visualize_bst(tree.root)
visualize_friends(tree)
show_complexity(tree)