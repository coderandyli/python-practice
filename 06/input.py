import json
import re


def parse(text):
    # 去除标点符号和换行
    text = re.sub(r'[^\w ]', ' ', text)
    # 转换为小写
    text.lower()
    # 单词列表
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None, word_list)
    # 生成单词和词频的字典
    word_cnt_dic = {}
    for word in word_list:
        if word not in word_cnt_dic:
            word_cnt_dic[word] = 0
        word_cnt_dic[word] += 1

    # 按照词频排序
    dic_sorted_by_value = sorted(word_cnt_dic.items(), key=lambda x: x[1])
    return dic_sorted_by_value


# readline版本的parse，练习1
# 处理文本
def parse_readline(infile):
    word_cnt = {}
    while True:
        text = infile.readline() # 按行读取文本
        if len(text) == 0: # 终止循环
            break
        print(text)

        # 词频字典拼接
        for word, cnt in parse(text):
            if word not in word_cnt:
                word_cnt[word] = cnt
            else:
                word_cnt[word] += cnt

    # 按词频排序
    dic_sorted_by_value = sorted(word_cnt.items(), key=lambda x: x[1])
    return dic_sorted_by_value


if __name__ == "__main__":
    """
    name = input("名字: ")
    gender = input("男的(Y/N): ")

    welcome_str = "欢迎到来，{prefix}{name}"
    welcome_dic = {
        "prefix": "Mr." if gender == 'Y' else "Mrs.",
        "name": name
    }
    print(welcome_str.format(**welcome_dic))
    """

    # 文件输入
    with open('in.txt', 'r') as fin:
        text = fin.read()

    word_and_freq = parse(text)
    print(json.dumps(word_and_freq))
    print(len(word_and_freq))

    with open("out.txt", "w") as fout:
        for word, freq in word_and_freq:
            fout.write('{} {}\n'.format(word, freq))

    # JSON的使用
    params = {
        "symbol": "123456",
        "type": "limit",
        "price": 123.4,
        "amount": 23
    }
    params_str = json.dumps(params)  # 序列化
    print("序列化以后")
    print("类型{},值{}".format(type(params_str), params_str))

    original_params = json.loads(params_str)
    print("在去序列化之后")
    print("类型{},值{}".format(type(original_params), original_params))  # type = dict

    # 思考题1
    with open("in.txt", "r") as fin:
        word_and_freq = parse_readline(fin)
        print(json.dumps(word_and_freq))
        print(len(word_and_freq))

    with open("out_readline.txt", "w") as fout:
        for word, freq in word_and_freq:
            fout.write('{} {}\n'.format(word, freq))
