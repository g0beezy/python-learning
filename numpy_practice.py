#numpy
#1. 基础语法与数据类型
#题目： 编写一个程序，接受用户输入的一个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数。
#. 列表操作
#题目： 有一个列表 [1, 2, 3, 4, 5, 6, 7, 8]。请编写代码，将其变为 [1, 3, 5, 7, 2, 4, 6, 8]。即奇数在前，偶数在后，并保持各自的原始相对顺序。
#3. 字典与循环
#题目： 将两个列表合并为一个字典。
#列表1：keys = ['name', 'age', 'city']
#列表2：values = ['Alice', 25, 'London']
#要求输出：{'name': 'Alice', 'age': 25, 'city': 'London'}
#4. 函数应用
#题目： 编写一个函数 is_prime(n)，用于判断一个正整数 n 是否为素数（质数）。如果是，返回 True，否则返回 False。


#1. 基础语法与数据类型
def count_characters(input_string):
    letters = spaces = digits = others = 0
    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            others += 1
    return letters, spaces, digits, others

#2. 列表操作
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [n for n in numbers if n % 2 == 1] + [n for n in numbers if n % 2 == 0]
print(numbers)


#3. 字典与循环
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'London']
result_dict = dict(zip(keys, values))
print(result_dict)

#4. 函数应用

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for factor in range(3, 10, 2):  # 生成 3, 5, 7, ...
        if n % factor == 0:
            return False
    return True


# simple test
print(is_prime(), is_prime(42))

#句子到顺，不改变字母顺序
sentence = input("please inter a sentence:")


words = sentence.split()
words.reverse()
reversed_sentence = ' '.join(words)
print(reversed_sentence)




#CSV文件读写
import csv  
data = [
    ['Name', 'Score'],
    ['Alice', 85],
    ['Bob', 92],
    ['Charlie', 78],
    ['Diana', 95]
]

average_score = sum(row[1] for row in data[1:]) / (len(data) - 1)
data.append(['Average', average_score])
with open('scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Data written to scores.csv")
