class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = node(4)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(5)
root.right.right = node(7)
i = 0


def check_binary_search_tree_(root):
    if root is None:
        return True
    if root.left.data < root.data:
        return check_binary_search_tree_(root.left)
    else:
        return False

    if root.right.data > root.data:
        return check_binary_search_tree_(root.right)
    else:
        return False


print(check_binary_search_tree_(root))


# def check_binary_search_tree_2(root):
#     return is_valid(root, -999999, 999999)


# def is_valid(root, low, high):
#     if root is None:
#         return True

#     if root.data <= low or root.data >= high:

#         return False
#     print(root.data)
# return is_valid(root.left, low, root.data) and is_valid(root.right,
# root.data, high)


# print(check_binary_search_tree_2(root))
