'''
finite element method, steady-state
'''

import numpy as np

def steady():
    pass






def findKeywordLine(kw, file_lines):
    kw_line = -1
    kw_line_i = -1

    for line_i in range(len(file_lines)):
        line = file_lines[line_i]
        if line.find(kw) >= 0:
            kw_line = line
            kw_line_i = line_i

    return kw_line, kw_line_i



meshFile = 'hex_box.msh'

with open(meshFile, 'r') as f:
    flines = f.readlines()

nn = int(flines[1])
print(f'Number of nodes: {nn}')

keyword = '$ELM'
kw_line, kw_line_i = findKeywordLine(keyword, flines)
ne = int(flines[kw_line_i+1])
print(f'Number of elements: {ne}')
