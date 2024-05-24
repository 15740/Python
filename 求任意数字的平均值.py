def calculate_average(numbers):
    if not numbers:  # 检查列表是否为空
        return 0  # 或者你可以抛出一个异常，如 ValueError
    return sum(numbers) / len(numbers)


# 示例用法
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")