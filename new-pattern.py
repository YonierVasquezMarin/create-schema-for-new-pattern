import os

pattern_name = input('Pattern name: ')

folder = os.path.dirname(os.path.abspath(__file__))

try:
    os.makedirs(folder+'/'+pattern_name)
    os.makedirs(folder+'/'+pattern_name+'/examples')
    os.makedirs(folder+'/'+pattern_name+'/pattern-info')
    with open(folder+'/'+pattern_name+'/pattern-info/readme.md', 'w'):
        pass
except:
    print('There is a error creating folders')
