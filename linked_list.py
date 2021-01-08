# --coding: utf8 --
"""
创建一个链表的，添加100个元素，每个元素是有符号的整型
赋值是随机的
取值范围是[-98, 97)

然后删掉其中的负数
"""
import random
import copy

class Node(object):
    """
    docstring
    """
    def __init__(self, val, _next):
        self.val = val
        self._next = _next


def gen_random():
    return random.randint(-98, 96)

def gen_node():
    val = gen_random()
    node = Node(val, None)
    return node


def gen_list():
    node_root = gen_node()
    node = node_root
    for i in range(99):
        new_node = gen_node()
        node._next = new_node
        node = new_node
    return node_root

def print_node(node):
    string = "["
    while True:
        if node._next == None:
            break
        string += str(node.val) + ","
        node = node._next
    string = string.rstrip(",")
    string += "]"
    print(string)

node = gen_list()
print_node(node)


def remove_negative(node_root):
    while True:
        if node_root._next is None:
            break
        if node_root.val > 0:
            break
        node_root = node_root._next
    node = node_root
    next_node = node._next
    while True:
        if next_node is None:
            print '---break next---', node.val, next_node.val
            node._next = None
            break
        if next_node._next is None:
            print '---break next next---', node.val, next_node.val
            # node._next = None
            next_node._next = None
            break
        if next_node.val < 0:
            next_node = next_node._next
            continue
        node._next = next_node
        node = next_node
        next_node = next_node._next
    return node_root

print("-----before delete--------")
node = remove_negative(node)
print_node(node)
