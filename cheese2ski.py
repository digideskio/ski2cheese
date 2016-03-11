# -*- coding: utf-8 -*-
import pyparsing as pp

def cheese2ski(s):
    # Combinators
    variables = ['チーズ', 'さけるチーズ', '地図']
    # variables = ['__0', '__1', '__2']

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

    # Transform to parse-friendly form
    def preprocess(s):
        s = s.replace('「', '(')
        s = s.replace('」', ')')
        s = s.replace(variables[1], '1') # "さけるチーズ" must be replaced before "チーズ"
        s = s.replace(variables[0], '0')
        s = s.replace(variables[2], '2')
        s = s.replace('裂けてる', 'I')
        s = s.replace('を避ける', 'K')
        s = s.replace('のある地、伊豆', '')
        s = s.replace('と', 'S')
        s = s.replace('に捧げる', '')

        s = '(' + s + ')'
        s = ''.join(map(lambda x: x + " ", s))
        return s

    def toPrefix(l):
        taker = Taker(l)
        if type(l) == str:
            return l
        elif 'S' in l:
            arg1, _, arg2, _, arg3 = [toPrefix(taker.take(1)[0]) for _ in range(5)]
            rest = map(toPrefix, taker.takeRest())
            return ['S', arg1, arg2, arg3] + rest
        elif 'K' in l:
            # The order of the arguments of 'K' is reversed in the original cheese grammar
            arg2, _, arg1 = [toPrefix(taker.take(1)[0]) for _ in range(3)]
            rest = map(toPrefix, taker.takeRest())
            return ['K', arg1, arg2] + rest
        elif 'I' in l:
            _ = toPrefix(taker.take(1)[0])        
            arg1 = toPrefix(taker.take(1)[0])
            rest = map(toPrefix, taker.takeRest())
            return ['I', arg1] + rest
        else:
            rest = map(toPrefix, taker.takeRest())
            return rest

    def removeNums(l):
        if type(l) == str:
            return l
        return [removeNums(x) for x in l if x not in map(str, range(3))]

    def peelIfOne(l):
        if type(l) == str:
            return l
        else:
            if len(l) == 1 and type(l[0]) == str:
                return l[0]
            else:
                return map(peelIfOne,l)

    def list2comb(l):
        if type(l) == str:
            return l
        return '(' + "".join(map(list2comb, l)) + ')'

    s = preprocess(s)
    a = pp.nestedExpr('(',')', pp.Word(pp.alphanums)).parseString(s).asList()
    a = toPrefix(a)
    a = removeNums(a)
    a = peelIfOne(a)
    s = list2comb(a)
    return s

s = raw_input()
print cheese2ski(s)