# 二叉堆代码练习
# 二叉堆的尾节点上浮和节点下沉的操作

def up_adjust(array=[]):
    """
    二叉堆的尾节点上浮操作
    :param array: 原数组
    :return:
    """
    child_index = len(array) - 1
    parent_index = (child_index - 1) // 2
    # temp保存插入的叶子节点值，用于最后的赋值
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        # 无需真正交换，单向赋值即可
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (parent_index - 1) // 2
    array[child_index] = temp

def down_adjust(parent_index, length, array=[]):
    """
    二叉堆的节点下沉操作
    :param parent_index: 待下沉的节点下标
    :param length: 堆的长度范围
    :param array: 原数组
    :return:
    """
    # tmp保存父节点值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 如果有右孩子，且右孩子的值小于左孩子的值，则定位到右孩子
        if child_index + 1 < length and array[child_index + 1] < array[child_index]:
            child_index += 1
        # 如果父节点的值小于任何一个孩子的值，直接跳出
        if temp <= array[child_index]:
            break
        # 无需真正交换，单向赋值即可
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp

def build_heap(array=[]):
    """
    二叉堆的构建操作
    :param array:原数组
    :return:
    """
    # 从最后一个非叶子节点开始，依次下沉调整
    for i in range((len(array) - 2) // 2, -1, -1):
        down_adjust(i, len(array),array)

my_array = list([1,3,2,6,5,7,8,9,10,0])

up_adjust(my_array)
print("up_adjust:")
print(my_array)

my_array = list([1,3,4,5,6,7,0,8,10,9,11])
down_adjust(0,9,my_array)
print("down_adjust:")
print(my_array)

build_heap(my_array)
print("build_heap:")
print(my_array)


a = [1,2,3]
print(a[0],a[1])
a[0] = a[1]

print(a[0],a[1],a)