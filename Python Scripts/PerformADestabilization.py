def performADestabilization(listofthreevertices, vertexset):
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

    vertexset.append((newx,newy))
    vertexset.remove((oldx,oldy))
    vertexset.remove((oldx, newy))
    vertexset.remove((newx, oldy))

    vertexset = [(i - 1, j) for i, j in vertexset if i > oldx]
    vertexset = [(i, j + 1) for i, j in vertexset if j < oldy]

    return vertexset