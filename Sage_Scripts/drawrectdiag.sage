##############################################################################################
def drawrectdiag(vertexset, rededges,iteration):
#### This will save the tikzfile to your computer as a .txt file
    import numpy as np
    import sys
    sys.stdout = open('RectangularDiagramtizkfile.txt','a')
    print('This is the diagram from iteration: ',iteration )
    print("\\begin{tikzpicture}")
    # First, we draw the horizontal lines remembering that our y's are negative
    vsy = [j for i, j in vertexset]
    miny: int = min(vsy)
    vsyarray = np.array(vsy)
    for i in range(miny, 0):
        currentvertices = np.where(vsyarray == i)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        print("\\draw[black, very thick] ", vertex1, ' -- ', vertex2, ';')

    print('')
    print('')

    # Next, we need to draw the white rectangles because we don't want to figure out how to use the knots package in tikz.
    vsx = [i for i, j in vertexset]
    maxx: int = max(vsx)
    vsxarray = np.array(vsx)
    for i in range(1, maxx + 1):
        currentvertices = np.where(vsxarray == i)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        realv1 = (vertex1[0] - .05, vertex1[1] - .25)
        realv2 = (vertex2[0] + .05, vertex2[1] + .25)
        print("\\filldraw[white, very thick] ", realv1, ' rectangle ', realv2, ';')

    print('')
    print('')

    # Next, we draw a small circle around each vertex, and draw red ones on red edges
    for i in vertexset:
        if i[0] in rededges:
            print("\\filldraw[red] ", i, ' circle (1.5pt) node[anchor=west]{};')
        else:
            print("\\filldraw[black] ", i, ' circle (1.5pt) node[anchor=west]{};')

    print('')
    print('')

    # Lastly, we draw the vertical lines, where we need to check for redness.
    for i in range(1, maxx + 1):
        currentvertices = np.where(vsxarray == i)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        if i in rededges:
            print("\\draw[red, very thick] ", vertex1, ' -- ', vertex2, ';')
        else:
            print("\\draw[black, very thick] ", vertex1, ' -- ', vertex2, ';')

    print('\\end{tikzpicture}')

#########################################################################################
