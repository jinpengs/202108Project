#如何让计算机生成像人一样的话
#规则引擎


from icecream import ic
import random

grammar_rule = """
复合句子 = 句子 连词 复合句子 | 句子
句子 = 主语s 谓语 宾语s
主语s = 主语 和 主语 | 主语
宾语s = 宾语 和 宾语 | 宾语
主语 = 冠词 定语 代号
宾语 = 冠词 定语 代号
谓语 = 是 | 吃 | 喜欢
代号 = 名词 | 代词
名词 = 西瓜 | 饼干 | 杯子 | 衣服 | 纸巾 | 老宋 | 老李
代词 = 你 | 我 | 他 | 你们 | 我们 | 他们 | 它 | 它们
定语 = 奇怪的 | 美丽的 | 神秘的 | 明亮的 | 崭新的 | 美味的 | 聪明的
冠词 = 这个 | 那个 | 一个 
连词 = 和 | 或 | 而且 | 但是 | 只是 | 尽管
"""


def parse_grammar(rule):
    grammar = dict()
    for line in rule.split('\n'):
        if not line.strip(): continue
        # ic(line)
        target, expand = line.split('=')
        expands = expand.split('|')
        # ic(target)
        # ic(expand)
        # ic(expands)
        grammar[target.strip()] = [e.strip() for e in expands]
    return grammar
    # ic(grammar)


def gene(target, grammar):
    if target not in grammar: return target
    # ic(grammar[target])
    expand = random.choice(grammar[target])
    return ''.join([gene(e, grammar) for e in expand.split()])


if __name__ == '__main__':
    another_rule = """
    expression = ( math ) op ( math ) | math
    math = num op num
    num = sing_num num | sing_num
    sing_num = 1 | 2 | 3 | 4 
    op = + | - | * | /
    """
    for i in range (100):
        ic(gene('expression',parse_grammar(another_rule
                                           )))