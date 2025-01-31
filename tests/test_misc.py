from chtoolbox import misc
import os

def test_generate_test_data():
    cases = {'case1': {'a': 1, 'b': 2}, 
             'case2': {'a': 3, 'b': 4},
             'case3': {'a': 5, 'b': 6}}
    
    def add(a, b):
        return a+b
    
    res = misc.generate_test_data(add, cases)

    for key, value in res.items():
        assert value['output'] == value['input']['a'] + value['input']['b'] 

def test_generate_test_data_csv():
    cases = os.path.join(os.path.dirname(__file__), 'data\data.csv')
    
    f1 = lambda a,b,c: a+b-c

    res1 = misc.generate_test_data(f1, cases)

    for key, value in res1.items():
        assert value['output'] == value['input']['a'] + value['input']['b'] - value['input']['c']

    def f2(a,b,c):
        x = {'sum': a+b,
             'diff': a-b}
        
        return x
    
    res2 = misc.generate_test_data(f2, cases)

    for key, value in res2.items():
        assert value['output']['sum'] == value['input']['a'] + value['input']['b']
        assert value['output']['diff'] == value['input']['a'] - value['input']['b']


