def count_words(s):
    # 初始化单词计数器和当前单词的长度
    word_count = 0
    current_word_length = 0

    # 遍历字符串中的每个字符
    for char in s:
        # 如果字符不是空格，增加当前单词的长度
        if char != ' ':
            current_word_length += 1
            # 如果字符是空格并且当前单词长度大于0，表示一个单词结束了
        elif current_word_length > 0:
            word_count += 1
            current_word_length = 0  # 重置当前单词长度

    # 检查字符串末尾是否有一个单词（没有以空格结束）
    if current_word_length > 0:
        word_count += 1

        # 返回单词的总数
    return word_count


# 示例字符串
example_string = "Hello, world! This is a test string with multiple words."
# 调用函数并打印结果
print(count_words(example_string))