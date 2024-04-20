num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_even_squares(num_list: list[int]):
    """使用【列表推導式(List Comprehension)】返回 num_list 中所有偶數的平方值列表

    Args:
        num_list (list[int]): 整數列表

    Returns:
        list[int]: 偶數的平方值列表
    """
    return [i**2 for i in num_list if not i % 2]


def get_odd_cubes(num_list: list[int]):
    """使用【迴圈】返回 num_list 中所有奇數的 3 次方值列表

    Args:
        num_list (list[int]): 整數列表

    Returns:
        list[int]: 奇數的 3 次方值列表
    """
    result = []
    for i in num_list:
        if i % 2:
            result.append(i**3)
    return result


def get_sliced_list(num_list: list[int]):
    """使用【切片】返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表

    Args:
        num_list (list[int]): 整數列表

    Returns:
        list[int]: 第 5 個元素開始到最後一個元素(包含最後一個)的子列表
    """
    return num_list[4:]


def format_numbers(numbers: list[int]):
    """返回一個新列表,其中每個數字都被格式化為 8 個字元的寬度,並靠右對齊

    Args:
        numbers (list[int]): 數字列表

    Returns:
        list[str]: 格式化後的數字
    """
    return ",".join("{:>8}".format(str(i)) for i in numbers)


print(format_numbers(get_even_squares(num_list)))
print(format_numbers(get_odd_cubes(num_list)))
print(format_numbers(get_sliced_list(num_list)))
