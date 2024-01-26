def solve(s):
    l= s.split(' ')
    res= (i.capitalize() for i in l)
    return ' '.join(res)
