"""
    可迭代对象工具集
"""

class IterableHelper:
    """
        可迭代对象助手类:对可迭代对象常用的高阶函数
    """
    # 静态方法:不操作实例成员/类成员
    @staticmethod
    def find_single(iterable, condition):
        """
            在可迭代对象中,查找满足条件的第一个元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的查找条件
        :return: 满足条件的第一个元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable,condition):
        """
            在可迭代对象中,查找满足条件的所有元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的查找条件
        :return: 生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def sum(iterable,condition):
        """
            在可迭代对象中,查找条件累加
        :param iterable: 可迭代对象
        :param condition: 函数类型的累加条件
        :return: 数值类型,累加和
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)
        return sum_value

    @staticmethod
    def delete_all(iterable,condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def select(iterable,condition):
        """
            在可迭代对象中根据条件选择成员
        :param iterable: 可迭代对象
        :param condition: 函数类型的选择策略
        :return: 生成器,推算出元素的成员
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def get_count(iterable,condition):
        """
            在可迭代对象中计算满足条件的元素数量
        :param iterable: 可迭代对象
        :param condition: 函数类型的条件
        :return: int类型,数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):
        """
            在可迭代对象中,根据条件查找
        :param iterable: 可迭代对象
        :param condition: 函数类型,查找策略
        :return: 最大值
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def is_repeat(iterable, condition):
        """
            在可迭代对象中根据条件判断是否有重复的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型,判断条件
        :return: bool类型,True表示有重复,Flase表示没有重复
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) == condition(iterable[c]):
                    return True
        return False

    @staticmethod
    def order_by(iterable, condition):
        """
            根据条件对可迭代对象升序排列
        :param iterable: 可迭代对象
        :param condition: 函数类型,排序依据
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
