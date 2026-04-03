class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None


def calculate_height(node):
    if node is None:
        return -1
    return max(calculate_height(node.left), calculate_height(node.right)) + 1


def calculate_node_height(node, target_name, level=0):
    if node is None:
        return -1

    if node.name == target_name:
        return level

    left = calculate_node_height(node.left, target_name, level + 1)
    if left != -1:
        return left

    return calculate_node_height(node.right, target_name, level + 1)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def is_balanced(node):
    if node is None:
        return True

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)



def find_category(node, name):
    if node is None:
        return None

    if node.name == name:
        return node

    left = find_category(node.left, name)
    if left:
        return left

    return find_category(node.right, name)


def find_path_to_root(node, name):
    if node is None:
        return None

    if node.name == name:
        return [node.name]

    left = find_path_to_root(node.left, name)
    if left:
        return left + [node.name]

    right = find_path_to_root(node.right, name)
    if right:
        return right + [node.name]

    return None


def lowest_common_ancestor(node, name1, name2):
    if node is None:
        return None

    if node.name == name1 or node.name == name2:
        return node

    left = lowest_common_ancestor(node.left, name1, name2)
    right = lowest_common_ancestor(node.right, name1, name2)

    if left and right:
        return node

    return left if left else right

def print_tree(node, level=0):
    if node is not None:
        print("    " * level + f"{node.name} ({node.post_count})")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)






root = CategoryNode(1, "Technology", 150)


root.left = CategoryNode(2, "Programming", 85)
root.right = CategoryNode(3, "Design", 65)


root.left.left = CategoryNode(4, "Python", 42)
root.left.right = CategoryNode(5, "Java", 30)
root.right.left = CategoryNode(6, "UI/UX", 38)
root.right.right = CategoryNode(7, "Graphics", 22)


root.left.left.left = CategoryNode(8, "Django", 18)
root.left.left.right = CategoryNode(9, "Flask", 12)


print_tree(root)

print("Tree height:", calculate_height(root))  


print("Height of 'Java':", calculate_node_height(root, "Java"))  


print("Total nodes:", count_nodes(root))  


print("Leaf nodes:", count_leaves(root))  

print("Is balanced:", is_balanced(root))  


node = find_category(root, "Python")
print("Find 'Python':", node.name if node else None)

path = find_path_to_root(root, "Django")
print("Path Django → root:", path)

lca = lowest_common_ancestor(root, "Django", "Java")
print("LCA (Django, Java):", lca.name if lca else None)