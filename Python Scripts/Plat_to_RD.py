def plat2rectdiag(syllablelist):
    # This is figuring out what braid group we're in by looking at the max crossing number. In a larger program this can be done sooner, and eliminated from this program.
    syllableends = [j for i, j in syllablelist]
    maxcrossing: int = max(syllableends)
    if maxcrossing % 2 == 1:
        n = (maxcrossing + 1) / 2
    else:
        n = (maxcrossing + 2) / 2
    n = int(n)

    # This is initializing the rectangular diagram: strands are initially in the first 2n positions, and each bridge starts on the next column.
    strands = list(range(1, (2 * n) + 1))
    vertexset = []
    i = 1
    while i <= n:
        vertexset.append((i, 2 * i - 1))
        vertexset.append((i, 2 * i))
        i += 1


    # For each syllable, we add two new vertices to the vertexset and update where each strand is
    # print(strands)
    k=1
    while syllablelist:
        # print('step ', k)
        currentsyllable = syllablelist[0]
        newvertextop = (n + k, strands[currentsyllable[0] - 1])
        newvertexbot = (n + k, strands[currentsyllable[1]] + 1)
        vsx = [i for i, j in vertexset]
        vsy = [j for i, j in vertexset]
        shiftedindices = list(filter(lambda x: vsy[x] >= strands[currentsyllable[1]] + 1, range(len(vsy))))
        for i in shiftedindices:
            vsy[i] = vsy[i] + 1
        vertexset = list(zip(vsx, vsy))
        vertexset = vertexset + [newvertextop, newvertexbot]
        # print(vertexset)

        # Now we need to update where the strands are. It's an annoying list manipulation, but nothing complicated.
        strands.insert(currentsyllable[1], strands[currentsyllable[1]])
        strandchange = list(range(currentsyllable[1] + 1, len(strands)))
        for i in strandchange:
            strands[i] += 1
        strands.pop(currentsyllable[0] - 1)
        # print(strands)
        syllablelist.pop(0)
        k += 1
    # print('end of for loop')
    # print('k = ',1)
    # print(strands)

    # Now we need to close off the plat where strands 1&2 are, 3&4 are, etc.
    for i in range(1, n + 1):
        vertexset.append((n+ k + i - 1, strands[2 * i - 2]))
        vertexset.append((n + k + i - 1, strands[2 * i - 1]))

    # Lastly, we'll make our vertex set go in the negative y direction, it'll make our pictures look how we want them to.
    vsx = [i for i, j in vertexset]
    vsy = [j for i, j in vertexset]
    negvsy = [-x for x in vsy]
    vertexset = list(zip(vsx, negvsy))

    # Here we can initialize where our red edges are, indicating only what x values they're at. This can be changed depending on our needs.
    rededges = list(range(1, n + 1)) + list(range(n + k , (2 * n) + k ))


    print(vertexset)
    print(rededges)