"""
定义和使用集合

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    # pop() 会从集合中移除并返回一个元素。
    # 由于集合是无序的，pop() 方法并不保证移除的元素是什么，但通常会移除集合中的第一个元素
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()
