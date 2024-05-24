import random
file_path = "./words/CET4.txt"  # 你的txt文件路径
position = 3  # 你想要筛选的单词在每行的位置
target_word = 'a'


# 加载文件
def load_file(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list


# 长度
def filter_words_by_length(desired_length, word_list):
    filtered_words = [word for word in word_list if len(word) == desired_length]
    return filtered_words

def random_get(result):
    random_word = random.choice(result)
    return random_word
# 包含字母
def filter_words_by_specific_words(specific_words, result):
    result1 = []
    for word in result:
        if all(specific_word in word for specific_word in specific_words):
            result1.append(word)
    return result1


# 字母位置
def filter_words_by_position(position, target_word, word_list):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            if len(words) >= position and words[position - 1] == target_word:
                return (line.strip())


# 指定特定长度的单词
desired_length = int(input("请输入要筛选的单词的长度："))
word_list = load_file(file_path)
result = filter_words_by_length(desired_length, word_list)
print("Filtered words:", result)

state1 = int(input("输入1随机生产 输入2开始筛选："))
print(state1)
if state1 == 1:
    random_word = random_get(result)
    print(random_word)
elif state1 == 2:
    # 获取用户输入的特定单词
    specific_words = input("请输入要筛选的特定单词，用空格分隔：").split()
    result1 = filter_words_by_specific_words(specific_words, result)
    state2 = int(input("输入1确定 输入2开始按照字母位置筛选："))
    if state2 == 1:
        print("Filtered words1:", result1)
    elif state2 == 2
        state2 = int(input("输入字母和位置："))
        result2 = filter_words_by_position(position, target_word, word_list)
        print("Filtered words2:", result2)
    # print(word_list)

else:
    print("输入1随机生产 输入2开始筛选!")






