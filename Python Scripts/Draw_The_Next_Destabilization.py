def drawrectdiag(vertexset, rededges, listofthreevertices):
    import numpy as np
    print("\\begin{figure}")
    print("\\centering")
    print("\\resizebox{\columnwidth}{!}{")
    print("\\begin{tikzpicture}")

    x1 = listofthreevertices[0][0]
    x2 = listofthreevertices[1][0]
    x3 = listofthreevertices[2][0]

    y1 = listofthreevertices[0][1]
    y2 = listofthreevertices[1][1]
    y3 = listofthreevertices[2][1]

    if x1 == x2:
        newx = x3
        oldx = x1
    elif x1 == x3:
        newx = x2
        oldx = x1
    elif x2 == x3:
        newx = x1
        oldx = x2
    else:
        return 'Not a valid destabilization'

    if y1 == y2:
        newy = y3
        oldy = y1
    elif y1 == y3:
        newy = y2
        oldy = y1
    elif y2 == y3:
        newy = y1
        oldy = y2
    else:
        return 'Not a valid destabilization'

    vsy = [j for i, j in vertexset]
    miny: int = min(vsy)
    vsyarray = np.array(vsy)
    for y in range(miny, 0):
        currentvertices = np.where(vsyarray == y)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        print("\\draw[black, very thick] ", vertex1, ' -- ', vertex2, ';')

    print('')
    print('')

    vsx = [i for i, j in vertexset]
    maxx: int = max(vsx)
    vsxarray = np.array(vsx)
    for x in range(1, maxx + 1):
        currentvertices = np.where(vsxarray == x)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        realv1 = (vertex1[0] - .05, vertex1[1] - .25)
        realv2 = (vertex2[0] + .05, vertex2[1] + .25)
        print("\\filldraw[white, very thick] ", realv1, ' rectangle ', realv2, ';')

    print('')
    print('')

    print("\\filldraw[red, opacity = 0.5] (", oldx, ", ", oldy, ") rectangle (", newx, ", ", newy, ");")

    # Next, we draw a small circle around each vertex, and draw red ones on red edges
    for v in vertexset:
        if v[0] in rededges:
            print("\\filldraw[red] ", v, ' circle (1.5pt) node[anchor=west]{};')
        else:
            print("\\filldraw[black] ", v, ' circle (1.5pt) node[anchor=west]{};')

    print('')
    print('')

    # Lastly, we draw the vertical lines, where we need to check for redness.
    for x in range(1, maxx + 1):
        currentvertices = np.where(vsxarray == x)[0]
        vertex1 = vertexset[currentvertices[0]]
        vertex2 = vertexset[currentvertices[1]]
        if x in rededges:
            print("\\draw[red, very thick] ", vertex1, ' -- ', vertex2, ';')
        else:
            print("\\draw[black, very thick] ", vertex1, ' -- ', vertex2, ';')

    print('\\end{tikzpicture}}')
    print('\\end{figure}')