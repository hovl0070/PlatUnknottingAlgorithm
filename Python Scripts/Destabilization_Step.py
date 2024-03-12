def Destabilization_Step(vertexset, rededges):
    import numpy as np
    def Check_for_Destabilization(x, vertexset):
        import numpy as np
        vsx = [i for i, j in vertexset]
        vsxarray = np.array(vsx)
        vsy = [j for i, j in vertexset]
        vsyarray = np.array(vsy)

        redindices = np.where(vsxarray == x)[0]
        y1 = vertexset[redindices[0]][1]
        y2 = vertexset[redindices[1]][1]

        y1index = np.where(vsyarray == y1)[0]
        x11 = vertexset[y1index[0]][0]
        x12 = vertexset[y1index[1]][0]
        adjx1 = [x11, x12]
        adjx1.remove(x)
        adjx1 = adjx1[0]

        y2index = np.where(vsyarray == y2)[0]
        x21 = vertexset[y2index[0]][0]
        x22 = vertexset[y2index[1]][0]
        adjx2 = [x21, x22]
        adjx2.remove(x)
        adjx2 = adjx2[0]

        if abs(y2 - y1) == 1:
            if adjx1 < adjx2:
                if x < adjx1:
                    return [(x, y1), (x, y2), (adjx1, y1)]
                else:
                    return [(x, y1), (x, y2), (adjx2, y2)]
            else:
                if adjx1 > x:
                    return [(x, y1), (x, y2), (adjx2, y2)]
                else:
                    return [(x, y1), (x, y2), (adjx1, y1)]

        else:
            for testx in [adjx1, adjx2]:
                topedge = max(y1, y2)
                bottomedge = min(y1, y2)
                leftedge = min(x, testx)
                rightedge = max(x, testx)
                checkedys = []
                lefttorightstrands = []
                toptobottomstrands = []
                for y in range(bottomedge + 1, topedge):
                    nexty = 0
                    if y in checkedys:
                        continue
                    yindex = np.where(vsyarray == y)[0]
                    x1 = vertexset[yindex[0]][0]
                    x2 = vertexset[yindex[1]][0]
                    leftx = min(x1, x2)
                    rightx = max(x1, x2)
                    if leftx > rightedge:
                        continue
                    elif leftx < leftedge:
                        if rightx < leftedge or rightx > rightedge:
                            continue
                        else:
                            testpoint = (rightx, y)
                            currentstrand = [testpoint, (leftx, y)]
                            while testpoint[0] < rightedge and bottomedge < testpoint[1]:
                                tpxindex = np.where(vsxarray == testpoint[0])[0]
                                tp1 = vertexset[tpxindex[0]]
                                tp2 = vertexset[tpxindex[1]]
                                if tp1 == testpoint:
                                    temptp = tp2
                                else:
                                    temptp = tp1

                                tpyindex = np.where(vsyarray == temptp[1])[0]
                                tp1 = vertexset[tpyindex[0]]
                                tp2 = vertexset[tpyindex[1]]
                                if tp1 == temptp:
                                    testpoint = tp2
                                else:
                                    testpoint = tp1

                                currentstrand += [testpoint, temptp]
                                checkedys.append(testpoint[1])

                                if testpoint[0] < leftx:
                                    nexty = 1
                                    break
                                elif temptp[1] > topedge:
                                    return 0

                            if nexty == 1:
                                lefttorightstrands += [currentstrand]
                                continue
                            elif testpoint[1] < bottomedge:
                                return 0
                            else:
                                lefttorightstrands += [currentstrand]

                    elif rightx > rightedge:
                        return 0
                    else:
                        testpoint = (rightx, y)
                        currentstrand = [testpoint, (leftx, y)]
                        while testpoint[0] < rightedge and bottomedge < testpoint[1]:
                            tpxindex = np.where(vsxarray == testpoint[0])[0]
                            tp1 = vertexset[tpxindex[0]]
                            tp2 = vertexset[tpxindex[1]]
                            if tp1 == testpoint:
                                temptp = tp2
                            else:
                                temptp = tp1

                            tpyindex = np.where(vsyarray == temptp[1])[0]
                            tp1 = vertexset[tpyindex[0]]
                            tp2 = vertexset[tpyindex[1]]
                            if tp1 == temptp:
                                testpoint = tp2
                            else:
                                testpoint = tp1

                            currentstrand += [testpoint, temptp]
                            checkedys.append(testpoint[1])

                            if testpoint[0] < leftedge:
                                return 0
                            elif testpoint[1] > topedge:
                                nexty = 1
                                break

                        if nexty == 1:
                            toptobottomstrands += [currentstrand]
                            continue
                        elif testpoint[1] < bottomedge:
                            lefttorightstrands += [currentstrand]
                        else:
                            return 0

                if testx == adjx1:
                    return [(x, y1), (x, y2), (adjx1, y1)]
                if testx == adjx2:
                    return [(x, y1), (x, y2), (adjx2, y2)]

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

        if oldx < newx:
            if unusedx < newx:
                redx = unusedx
            else:
                redx = newx
        else:
            if unusedx > newx:
                redx = unusedx
            else:
                redx = newx

        # print(unusedx, unusedx1, unusedx2)
        # print(newx1, newx2, newx, redx)

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

    def drawrectdiag(vertexset, rededges):
        import numpy as np
        print("\\begin{figure}")
        print("\\centering")
        print("\\resizebox{\columnwidth}{!}{")
        print("\\begin{tikzpicture}")
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

    isthereadestab = 1

    while isthereadestab == 1:
        if len(vertexset) <= 4:
            break
        else:
            for x in rededges:
                ans = Check_for_Destabilization(x, vertexset)
                if ans == 0:
                    isthereadestab = 0
                else:
                    newdiag = performADestabilization(ans, vertexset, rededges)
                    isthereadestab = 1
                    vertexset = newdiag[0]
                    rededges = newdiag[1]
                    # drawrectdiag(vertexset, rededges)
                    break
    return [vertexset, rededges]