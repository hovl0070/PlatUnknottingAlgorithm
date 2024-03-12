def Check_for_Destabilization(x, vertexset):
    # Vertex set and red edges just describe a rectangular diagram.
    # x is the x-value that we need to check if there's a destabilization.
    import numpy as np
    vsx = [i for i, j in vertexset]
    vsxarray = np.array(vsx)
    vsy = [j for i, j in vertexset]
    vsyarray = np.array(vsy)

    # This is figuring out the corners of the red edge at point x
    redindices = np.where(vsxarray == x)[0]
    print(redindices)
    y1 = vertexset[redindices[0]][1]
    y2 = vertexset[redindices[1]][1]

    # Now we need to find the x values for the vertices that are at y1 and y1.
    y1index = np.where(vsyarray == y1)[0]
    x11 = vertexset[y1index[0]][0]
    x12 = vertexset[y1index[1]][0]
    adjx1 = [x11, x12]
    adjx1.remove(x)
    adjx1 = adjx1[0]
    # print(adjx1)

    y2index = np.where(vsyarray == y2)[0]
    x21 = vertexset[y2index[0]][0]
    x22 = vertexset[y2index[1]][0]
    adjx2 = [x21, x22]
    adjx2.remove(x)
    adjx2 = adjx2[0]
    # print(adjx2)

    # This code handles both left and right red edges by using the max/min stuff for top/bottom and left/right
    # Now, we check for a destabilization along the x vertical edge and along the horizontal edge at height y1
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
            # print('forloop')
            isempty = 1
            topedge = max(y1, y2)
            bottomedge = min(y1, y2)
            leftedge = min(x, testx)
            rightedge = max(x, testx)

            checkedys = []
            lefttorightstrands = []
            for y in range(bottomedge + 1, topedge):
                # print('forloop2')
                if y in checkedys:
                    # print('skip')
                    continue
                yindex = np.where(vsyarray == y)[0]
                x1 = vertexset[yindex[0]][0]
                x2 = vertexset[yindex[1]][0]
                leftx = min(x1, x2)
                rightx = max(x1, x2)
                if leftx > rightedge:  # fully to the right of the bypassing disc
                    continue
                    # print(1)
                elif leftx < leftedge:
                    if rightx < leftedge or rightx > rightedge:  # fully to the left or fully underneath the bp disc
                        continue
                        # print(2)
                    else:  # starts to the left and makes a turn inside the rectangle
                        testpoint = (rightx, y)
                        currentstrand = [testpoint , (leftx , y)]
                        while testpoint[0] < rightedge and bottomedge < testpoint[
                            1]:  # this is tracking where all the turns go
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
                            if testpoint[0] < leftx:
                                checkedys.append(testpoint[1])
                                nexty = 1
                                break
                            elif temptp[1] > topedge:
                                return 0
                            checkedys.append(testpoint[1])  # this allows us to skip over small segments later on
                            # print(3)
                        if nexty == 1:
                            continue
                        elif testpoint[1] < bottomedge:
                            return 0
                        else:
                            lefttorightstrands += [currentstrand]

                elif rightx > rightedge:  # We're allowed to know that this strand came in from above because of the checkedys business.
                    return 0
                
                else:  # the strand didn't immediately leave, so now we need to chase it down through the rectangle.
                    testpoint = (rightx, y)
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
                        checkedys.append(testpoint[1])
                        # print(8)

                    if testpoint[1] > bottomedge:
                        return 0
                    elif testpoint[0] < rightedge:
                        continue
                    elif temptp[0] < rightedge:
                        continue
                    else:
                        return 0

                # print("isempty = ", isempty)
                # print("testx", testx)
                # print()

                if testx == adjx1:
                    return [(x, y1), (x, y2), (adjx1, y1)]
                if testx == adjx2:
                    return [(x, y1), (x, y2), (adjx2, y2)]

    return 0
