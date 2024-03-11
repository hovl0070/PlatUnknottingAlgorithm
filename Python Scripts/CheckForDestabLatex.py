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
                        currentstrand = [testpoint , (leftx , y)]
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
