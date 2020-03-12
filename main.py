from generator import generator

regular_expressions = [
    'a(a+b)*a+b(a+b)*b',
    'a(a+b)*',
    '(bb*a)*bb*(a+b)b*',
    '(a+b)a*',
    '(a+b)*(a+bb)',
    '(0+1)*00(0+1)*'
]

for regular_expression in regular_expressions:
    generator(regular_expression)
