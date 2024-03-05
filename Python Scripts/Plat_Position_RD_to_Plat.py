def Plat_Position_RD_to_Plat(vertexset, rededges):
    import numpy as np
    # vertexset = [(4, -9), (5, -7), (6, -13), (7, -1), (7, -8), (8, -3), (8, -12), (9, -5), (9, -11), (10, -7), (10, -10),
    #             (11, -8), (11, -15), (12, -13), (12, -16), (13, -12), (14, -11), (14, -20), (15, -10), (15, -18),
    #             (16, -16), (17, -9), (3, -5), (3, -6), (4, -6), (2, -3), (2, -4), (6, -4), (1, -1), (1, -2), (5, -2),
    #             (18, -14), (18, -15), (13, -14), (19, -17), (19, -18), (17, -17), (20, -19), (20, -20), (16, -19)]
    # rededges =  [1, 2, 3, 18, 19, 20]
    # Counting the number of bridges
    n = len(rededges) / 2
    n = int(n)
    leftrededges = rededges[: n]
    syllablelist = []

    vsx = [i for i, j in vertexset]
    vsxarray = np.array(vsx)
    vsy = [j for i, j in vertexset]
    vsyarray = np.array(vsy)
    strands = []

    # Figuring out where the strands start.
    # Each red edge is a bridge, which gives the initial location of each strand.
    for m in leftrededges:
        currentstrands = np.where(vsxarray == m)[0]
        topstrand = vertexset[currentstrands[0]][1]
        bottomstrand = vertexset[currentstrands[1]][1]
        strands.append(topstrand)
        strands.append(bottomstrand)

    c = max(vsx)
    strandarray = np.array(strands)

    for i in range(n + 1, c - n + 1):
        cs = 0
        currentstrands = np.where(vsxarray == i)[0]
        y1 = vertexset[currentstrands[0]][1]
        y2 = vertexset[currentstrands[1]][1]
        startingstrand = max(y1, y2)
        endingstrand = min(y1, y2)
        startingstrandindex = np.where(strandarray == startingstrand)[0]
        startingstrandindex = startingstrandindex.item()
        crossingstrands = np.where((strandarray < startingstrand) & (strandarray > endingstrand))[0]
        if len(crossingstrands) > 0:
            for s in strandarray:
                understrands = np.where(vsyarray == s)[0]
                edge1 = vertexset[understrands[0]][1]
                edge2 = vertexset[understrands[1]][1]
                leftedge = min(edge1, edge2)
                rightedge = max(edge1, edge2)
                if leftedge < i < rightedge:
                    cs += 1
            currentsyllable = (startingstrandindex + 1, startingstrandindex + cs + 1)
            syllablelist.append(currentsyllable)
        np.delete(strandarray, startingstrand)
        np.append(strandarray, endingstrand)
        strandarray[::-1].sort()

    return syllablelist
