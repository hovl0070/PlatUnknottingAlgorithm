def performADestabilization(listofthreevertices, vertexset, rededges):
    import numpy as np
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

    # preliminaries
    vsx = [i for (i, j) in vertexset]
    vsxarray = np.array(vsx)
    vsy = [j for (i, j) in vertexset]
    vsyarray = np.array(vsy)

    # Finding the two vertices which live on our new x-coordinate
    newxindex = np.where(vsxarray == newx)[0]
    newy1 = vertexset[newxindex[0]][1]
    newy2 = vertexset[newxindex[1]][1]

    # For the top one, we find the x value of the point which shares newy1 and isnt at newx
    newy1index = np.where(vsyarray == newy1)[0]
    newnewx11 = vertexset[newy1index[0]][0]
    newnewx12 = vertexset[newy1index[1]][0]
    if newnewx11 == newx:
        newx1 = newnewx12
    else:
        newx1 = newnewx11

    # Same for newy2
    newy2index = np.where(vsyarray == newy2)[0]
    newnewx21 = vertexset[newy2index[0]][0]
    newnewx22 = vertexset[newy2index[1]][0]
    if newnewx21 == newx:
        newx2 = newnewx22
    else:
        newx2 = newnewx21

    # Now, we find the x value of the other vertex that wasn't used in the bypass.
    newyindex = np.where(vsyarray == newy)[0]
    unusedx1 = vertexset[newyindex[0]][0]
    unusedx2 = vertexset[newyindex[1]][0]
    if unusedx1 == oldx:
        unusedx = unusedx2
    else:
        unusedx = unusedx1

    if newx1 < newx:
        if newx2 < newx:
            redx = newx
        else:
            redx = unusedx
    else:
        if newx2 > newx:
            redx = newx
        else:
            redx = unusedx

    print(unusedx, unusedx1, unusedx2)
    print(newx1, newx2, newx, redx)

    vertexset.append((newx, newy))
    vertexset.remove((oldx, oldy))
    vertexset.remove((oldx, newy))
    vertexset.remove((newx, oldy))

    # we need to figure out which edge is the new red edge.
    # basically, we need to see which edge forms the bridge.

    vsx = [i for (i, j) in vertexset]
    vsy = [j for (i, j) in vertexset]
    newvsx = []
    for i in vsx:
        if i > oldx:
            i -= 1
        newvsx.append(i)

    newvsy = []
    for j in vsy:
        if j < oldy:
            j += 1
        newvsy.append(j)

    newvs = list(zip(newvsx, newvsy))

    rededges.remove(oldx)
    rededges.append(redx)
    newrededges = []
    for x in rededges:
        if x < oldx:
            newrededges.append(x)
        else:
            x = x - 1
            newrededges.append(x)

    newrededges.sort()

    return [newvs, newrededges]
