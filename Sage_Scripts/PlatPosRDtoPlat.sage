################################################################################################################



def PlatPosRDtoPlat(vertexset,rededges):
    import numpy as np
    # Counting the number of bridges
    n = len(rededges) / 2
    #n = int(n)
    leftrededges = rededges[: n]
    syllablelist = []
    vertexset = matrix(vertexset)
    vsx = [i for i, j in vertexset]
    #vsxarray = np.array(vsx)
    vsy = [j for i, j in vertexset]
    #vsyarray = np.array(vsy)
    strands = []


    # Figuring out where the strands start.
    # Each red edge is a bridge, which gives the initial location of each strand.
    for m in leftrededges:
        currentstrands=[i for i in range(len(vsx)) if vsx[i]==m] #replacing line below
        #currentstrands = np.where(vsxarray == m)[0]
        topstrand = vertexset[currentstrands[0]][1]
        bottomstrand = vertexset[currentstrands[1]][1]
        strands.append(topstrand)
        strands.append(bottomstrand)


    c = max(vsx)
    #strandarray = np.array(strands)

    for i in range(n + 1, c - n + 1):
        cs = 0
        currentstrands=[j for j in range(len(vsx)) if vsx[j]==i] #replacing line below
        #currentstrands = np.where(vsxarray == i)[0]
        y1 = vertexset[currentstrands[0]]
        y2 = vertexset[currentstrands[1]]
        startingstrand = max(y1, y2)
        endingstrand = min(y1, y2)
        startingstrandindex=[k for k in range(len(strands)) if strands[k]==startingstrand]
        #replacing line below
        #startingstrandindex = np.where(strandarray == startingstrand)[0]
        if startingstrandindex ==[]: return syllablelist
        else:
            startingstrandindex = startingstrandindex[0]
            crossingstrands=[l for l in range(len(strands)) if (strands[l]<startingstrand and             strands[l]>endingstrand)]
                    #crossingstrands = np.where((strandarray < startingstrand) & (strandarray >                   endingstrand))[0]
            if len(crossingstrands) > 0:
                for s in strandarray:
                    understrands = np.where(vsyarray == s)[0]
                    edge1 = vertexset[understrands[0]][1]
                    edge2 = vertexset[understrands[1]][1]
                    leftedge = min(edge1, edge2)
                    rightedge = max(edge1, edge2)
                    if leftedge < i < rightedge:
                        cs = cs+1
            currentsyllable = [startingstrandindex[0]+1,startingstrandindex[0]+cs+1]
            syllablelist.append(currentsyllable)
            np.delete(strands, startingstrand)
            np.append(strands, endingstrand)
            strands[::-1].sort()
            return syllablelist

####################################################################################################################################################
