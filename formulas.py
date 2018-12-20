# -*- coding: utf-8 -*-

"""
    Here I collect all formulas for Balazs regarding algebra in 8th class
"""
import random

# TODO alternatives a=-(-a)=a+0=1*a=1/(1/a)
# Todo: cserelje meg az oldalakat is!!!
# TODO: muvelet precedencia: kellene ilyen dobd el a felesleges zarojeleket feladat
# TODO: definitions
"""
Mindenkepp kell:
    - tedd ki/tuntesd el a szorzas jelet
    - emelj ki egy tényezőt a szorzatból
    - bonstd fel a zárójelet
    - szorzatból összeg összegból szorzat:
        - bonyolultabb számolások bontása: pl. 12*15 = 10*15 + 2*15
    - tortek
    - szorzotabla -10..10 fejben
    - szorzotabla -20..20 10+x-re bontva + disztributive szabaly
    - negyzetszamok -20..20-ig fejbol
    - primtenyezos szorzat -20..20-ig fejbol
"""
formulas = {
    'algebra': {
        'single operations': {
            'negation': [
                dict(formula='-(-a)=a'),
                dict(formula='-a=-(-(-a))'),
            ],
            'addition': {
                'neutral element': [
                    dict(formula='a+0=a'),
                    dict(formula='0+a=a'),
                ],
                'commutativity': [
                    dict(formula='a+b=b+a'),
                ],
                'associativity': [
                    dict(formula='(a+b)+c=a+b+c'),
                    dict(formula='a+(b+c)=a+b+c'),
                ],
            },
            'subtraction': {
                'neutral element': [
                    dict(formula='a-0=a'),
                    dict(formula='0-a=a'),
                ],
                'anti-commutativity': [
                    dict(formula='a-b=-(b-a)'),
                ],
                'associativity': [
                    dict(formula='(a+b)+c=a+b+c'),
                    dict(formula='a+(b+c)=a+b+c'),
                ],
            },
            'multiplication': {
                'neutral element': [
                    dict(formula='a*1=a'),
                    dict(formula='1*a=a'),
                ],
                'commutativity': [
                    dict(formula='a*b=b*a'),
                ],
                'associativity': [
                    dict(formula='(a*b)*c=a*b*c'),
                    dict(formula='a*(b*c)=a*b*c'),
                ],
            },
            'reciprocal': {
                'idempotency': [
                    dict(formula='1/(1/a)=a'),
                    dict(formula='1/a=1/(1/(1/a))'),
                ],
            },
            'division': {
                'neutral element': [
                    dict(formula='a/1=a'),  # Well, I won't introduce group theory here eliminating inverse operations
                ],
                'anti-commutativity': [
                    dict(formula='a/b=1/(b/a)'),
                ],
                'anti-associativity': [
                    dict(formula='(a/b)/c=a/b/c'),
                    dict(formula='a/(b/c)=(a*c)/b'),
                ],
            },
            'power': {
                'zero': [
                    dict(formula='a^0=1', special_cases=['0^0=1']),
                ],
                'idempotency': [
                    dict(formula='a^1=a', special_cases=['0^1=0']),
                ],
                'power of power': [
                    dict(formula='(a^n)^m=a^(n*m)'),
                ],
                'complex exponent': [
                    dict(formula='a^(n+m)=(a^n)*(a^m)'),
                    dict(formula='a^(-n)=1/(a^n)'),
                    dict(formula='a^(n-m)=(a^n)/(a^m)'),
                ],
                'complex bases': [
                    dict(formula='(-a)^n=(-1)^n*(a^n)',
                         special_cases=['-1^0=1', '-1^1=-1', '-1^2=1', '-1^3=-1', '-1^4=1', '-1^5=-1']),
                    dict(formula='(a*b)^n=(a^n)*(b^n)'),
                    dict(formula='(a/b)^n=(a^n)/(b^n)'),
                ]
            }
        },
        'multiple operations': {
            'negation': [
                dict(formula='-a=(-1)*a'),
                dict(formula='-a=0-a'),
                dict(formula='a+(-b)=a-b'),
                dict(formula='-(a+b)=-a-b'),
                dict(formula='-(a-b)=-a+b'),
                dict(formula='(-a)*b=-(a*b)'),
                dict(formula='a*(-b)=-(a*b)'),
                dict(formula='(-a)/b=-(a/b)'),
                dict(formula='a/(-b)=-(a/b)'),
                dict(formula='(-a)^n=(-1)^n*(a^n)'),
            ],
            'distributive rules': [
                dict(formula='a*(b+c)=a*b+a*c'),
                dict(formula='(a+b)*c=a*c+b*c'),
                dict(formula='a*(b-c)=a*b-a*c'),
                dict(formula='(a-b)*c=a*c-b*c'),
            ],
            'square': [
                dict(formula='(a+b)^2=a^2+2*a*b+b^2'),
                dict(formula='(a-b)^2=a^2-2*a*b+b^2'),
            ],
        },
    },
    'geometry': {
        'pythagoras': [
            dict(formula='a^2+b^2=c^2',
                 where="where c represents the length of the hypotenuse and a and b the lengths of other two sides"),
            dict(formula='a^2-c^2=b^2',
                 where="where c represents the length of the hypotenuse and a and b the lengths of other two sides"),
            dict(formula='b^2-c^2=a^2',
                 where="where c represents the length of the hypotenuse and a and b the lengths of other two sides"),
        ]
    },
}


def depth_first(nested_dict, visitor):
    """ Visit a nested dict until a non-dict object is found and considered as leaf """
    assert isinstance(nested_dict, dict)
    for key in nested_dict:
        child = nested_dict[key]
        leaf = not isinstance(child, dict)
        visitor.visit(key, child, leaf=leaf)
        if not leaf:
            depth_first(child, visitor)
        visitor.leave()


class FlattenerVisitor:
    def __init__(self):
        self.path = []
        self.flattened_tree = []

    def visit(self,
              key,
              node,
              leaf):
        self.path.append(key)
        if leaf:
            assert isinstance(node, list)
            self.flattened_tree += [(item, self.path.copy()) for item in node]

    def leave(self):
        self.path.pop()


def create_exercise_with_numbers(formula):
    numbers = list(range(-20, 0)) + list(range(1, 21))
    parameter_names = dict(
        a=numbers, b=numbers, c=numbers, d=numbers,
        n=[2], m=[1, 3],
    )
    exercises = []
    for exercise in formula.split('='):
        for p in parameter_names:
            if formula.count(p) > 0:
                number = random.choice(parameter_names[p])
                exercise = exercise.replace(p, "(%d)" % number if number < 0 else "%d" % number)
        exercises.append(exercise)
    return exercises


def main():
    flattener = FlattenerVisitor()
    depth_first(formulas, flattener)
    exercises_with_numbers = []
    for item in flattener.flattened_tree:
        exercises_with_numbers += create_exercise_with_numbers(item[0]['formula'])
    random.shuffle(exercises_with_numbers)
    for exercise in exercises_with_numbers:
        reference = eval(exercise.replace('^', '**'))
        ratio = [0, 1]
        while True:
            answer = input(exercise + "=")
            try:
                for idx, number in enumerate(answer.split("/")):
                    ratio[idx] = float(number)
                break
            except ValueError:
                exercise = answer
        answer = ratio[0] / ratio[1]
        print("good" if abs(answer - reference) < 1e-6 else "bad")


if __name__ == '__main__':
    main()
