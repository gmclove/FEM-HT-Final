
import numpy as np

def readMesh(meshFile):
    # with open(meshFile, 'r') as f:
    #     data = f.read().split()
    #     floats = []
    #     for elem in data:
    #         try:
    #             floats.append(float(elem))
    #         except ValueError:
    #             pass
    #     print(floats)

    with open(meshFile, 'r') as f:
        flines = f.readlines()

    for line in flines:
        if line == '$NOD'

    nn = int(flines[1])
    print(f'Number of nodes: {nn}')

    keyword = '$ELM'
    kw_line, kw_line_i = findKeywordLine(keyword, flines)
    ne = int(flines[kw_line_i+1])
    print(f'Number of elements: {ne}')

    print(flines)
    flines_split = np.empty()
    for line in flines:
        if line.startswith('$'):
            pass
        else:
            line_split = line.split()
            print(line_split)
            flines_split = np.append(line_split)
    mesh_int = flines_split.astype(int)
    print(flines_split)




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
readMesh(meshFile)
