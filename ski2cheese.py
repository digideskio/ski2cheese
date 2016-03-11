# -*- coding: utf-8 -*-
import pyparsing as pp

def ski2cheese(s):
    # Combinators
    combs = ['S', 'K', 'I']
    variables = ['チーズ', 'さけるチーズ', '地図']
    # variables = ['__0', '__1', '__2']

    numOfArgsDict = {'S': 3, 'K': 2, 'I': 1}
    expressiondict = {'S': lambda args: wrapParen(args[0] + 'と' + args[1] + 'と' + args[2] + 'のある地、伊豆'),
                      'K': lambda args: wrapParen(args[1] + 'を避ける' + args[0]),
                      'I': lambda args: wrapParen('裂けてる' + args[0])}

    # Take n elements from a given list
    class Taker:
        def __init__(self, l):
            self.cur = 0
            self.l = l
        def nextCur(self):
            self.cur += 1
            return self.cur - 1
        def take(self, d):
            return [self.l[self.nextCur()] if not self.isAllTaken() else variables[self.nextCur() - 1] for i in range(d)]
        def takeRest(self):
            return [self.l[self.nextCur()] for i in range(len(self.l)) if not self.isAllTaken()]
        def isAllTaken(self):
            return self.cur >= len(self.l)

    def wrapParen(string):
        return '「' + string + '」'

    def toString(l):
        # If the input is not a combinator
        if type(l) == str and not l in combs:
            return l
        taker = Taker(l)
        head = taker.take(1)[0]
        numOfArgs = numOfArgsDict[head] if head in combs else 0
        args = taker.take(numOfArgs)
        rest = taker.takeRest()

        ret = expressiondict[head](map(toString, args)) if head in combs else toString(head)
        for i in rest:
            ret = wrapParen(ret + "に捧げる" + toString(i))
        return ret

    s = '(' + s + ')'
    s = ''.join(map(lambda x: x + " ", s))
    a = pp.nestedExpr('(',')', pp.Word(pp.alphanums)).parseString(s).asList()
    s = toString(a)
    return s

s = raw_input()
print ski2cheese(s)