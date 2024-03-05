def Plat_Position_RD_to_Plat(vertexset, rededges):
    import numpy as np

    # Counting the number of bridges
    n = len(rededges) / 2
    n = int(n)
    leftrededges = rededges[: n]
    syllablelist = []

    vsx = [i for i, j in vertexset]
    vsxarray = np.array(vsx)
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
    for i in range(n + 1, c - n + 1):
        currentsyllable = []
        currentstrands = np.where(vsxarray == i)[0]
        y1 = vertexset[currentstrands[0]][1]
        y2 = vertexset[currentstrands[1]][1]
        startingstrand = max(y1, y2)
        endingstrand = min(y1, y2)

        # need to find the index of the starting strand
        j = 0
        startingstrandindex = -1
        while j < len(strands):
            if strands[j] == startingstrand:
                startingstrandindex = j
                break
            else:
                j += 1
        if startingstrandindex == -1:
            return 'strand index issue'

        k = 0
        understrands = []
        while k < len(strands):
            if strands[k] > endingstrand and strands[k] < startingstrand:
                understrands.append(k)
            k += 1

        if len(understrands) != 0:
            currentsyllable = [(startingstrandindex + 1, max(understrands))]

        # Adding our syllable (it may be empty), and updating our strand list
        syllablelist += currentsyllable
        strands.remove(startingstrand)
        strands.append(endingstrand)
        strands.sort(reverse=True)

    return syllablelist
