# 二叉树代码练习
# 二叉树创建&深度优先遍历（前序、中序、后序）

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree(input_list=[]):
    """
    构建二叉树
    :param input_list: 输入数列
    :return:

    """
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node

# print(create_binary_tree(list([1,2,3,4,5,6])))  <__main__.TreeNode object at 0x10e8a5b20>

def pre_order_traversal(node):
    """
    前序遍历
    :param node:二叉树节点
    :return:
    """
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node

def in_order_traversal(node):
    """
    中序遍历
    :param node: 二叉树节点
    :return:
    """
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    """
    后序遍历
    :param node:二叉树节点
    :return:
    """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node

my_input_list = list([1,2,None,None,3,None,4,5,6,None,None,None,7,8,9,None,None,10])
root = create_binary_tree(my_input_list)

print("前序遍历：")
pre_order_traversal(root)
print("中序遍历：")
in_order_traversal(root)
print("后序遍历：")
post_order_traversal(root)

# 广度优先遍历：层序遍历
from queue import Queue

def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
print('层序遍历：')
level_order_traversal(root)

