def Destabilization_Step(vertexset, rededges):

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
        y1 = vertexset[redindices[0]][1]
        y2 = vertexset[redindices[1]][1]

        # Now we need to find the x values for the vertices that are at y1 and y1.
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

        # This code handles both left and right red edges by using the max/min stuff for top/bottom and left/right
        # Now, we check for a destabilization along the x vertical edge and along the horizontal edge at height y1
        for testx in [adjx1, adjx2]:
            # print('forloop')
            isempty = 1
            topedge = max(y1, y2)
            bottomedge = min(y1, y2)
            leftedge = min(x, testx)
            rightedge = max(x, testx)

            checkedys = [-2, -4]
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
                    isempty *= 1
                    # print(1)
                elif leftx < leftedge:
                    if rightx < leftedge or rightx > rightedge:  # fully to the left or fully underneath the bp disc
                        isempty *= 1
                        # print(2)
                    else:  # starts to the left and makes a turn inside the rectangle
                        testpoint = (rightx, y)
                        while testpoint[0] < rightedge and bottomedge < testpoint[1]:  # this is tracking where all the turns go
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
                            checkedys.append(testpoint[1])  # this allows us to skip over small segments later on
                            # print(3)
                        if testpoint[
                            0] < rightedge:  # x value below the right edge means y value above bottom edge => came out the bottom (bad)
                            isempty *= 0
                        elif testpoint[1] > bottomedge:  # y value above bottom edge means exited the right side (good)
                            isempty *= 1
                            # print(4)
                        elif temptp[
                            0] < rightedge:  # Now we need to use the previous vertex to see if it came out the side or the bottom.
                            isempty *= 0
                            # print(5)
                        else:
                            isempty *= 1
                            # print(6)
                elif rightx > rightedge:  # We're allowed to know that this strand came in from above because of the checkedys business.
                    isempty *= 0
                    # print(7)
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
                        # print(8)

                    if testpoint[1] > bottomedge:
                        isempty *= 0
                        # print(9)
                    elif testpoint[0] < rightedge:
                        isempty *= 1
                        # print(10)
                    elif temptp[0] < rightedge:
                        isempty *= 1
                        # print(11)
                    else:
                        isempty *= 0
                        # print(12)

                # print("isempty = ", isempty)
                # print("testx", testx)
                # print()
                if isempty == 0:  # if we've found a strand that stops a bypass at any point, the function is done.
                    # print(13)
                    continue
                if testx == adjx1 and isempty == 1:
                    return [(x, y1), (x, y2), (adjx1, y1)]
                if testx == adjx2 and isempty == 1:
                    return [(x, y1), (x, y2), (adjx2, y2)]

        return 0

    def performADestabilization(listofthreevertices, vertexset, rededges):
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

        vertexset.append((newx, newy))
        vertexset.remove((oldx, oldy))
        vertexset.remove((oldx, newy))
        vertexset.remove((newx, oldy))

        vertexset = [(i - 1, j) for i, j in vertexset if i > oldx]
        vertexset = [(i, j + 1) for i, j in vertexset if j < oldy]

        rededges.remove(oldx)
        rededges.append(newx)
        rededges.sort()

        return [vertexset, rededges]


    isthereadestab = 1

    while isthereadestab == 1:
        for x in rededges:
            ans = Check_for_Destabilization(x, vertexset)
            if ans == 0:
                isthereadestab = 0
            else:
                newdiag = performADestabilization(ans, vertexset, rededges)
                isthereadestab = 1
                vertexset = newdiag[0]
                rededges = newdiag[1]
                break


