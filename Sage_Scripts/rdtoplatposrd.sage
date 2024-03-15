################################################################################################
def rdtoplatposrd(vertexset, rededges):
    import numpy as np

    # Figuring out how many bridges we have
    n = len(rededges) / 2
    n = int(n)

    # Some initialization
    leftrededges = rededges[: n]
    rightrededges = rededges[n:]
    redvertices = []

# Notice that I'm using the assumption that all top bridges are above all bottom bridges. If we want to make this
# program more robust, we can definitely find a way to detect if the given red vertex is a left or right edge, and
# and sort like that. For the hard coded example I just brute forced it for simplicity. only lines 11-15 would need
# change to accomodate this.


# First, we do the left side, find the tops of each red edge:
    for m in leftrededges:
        vsx = [i for i, j in vertexset]
        vsxarray = np.array(vsx)
        currentvertices = np.where(vsxarray == m)[0]
        y1 = vertexset[currentvertices[0]][1]
        y2 = vertexset[currentvertices[1]][1]
        y = max(y1, y2)
        redvertices.append((m, y))


# Next, we need to find the minimum y value and add in 3 vertices, and update our left vertex list
# rvy is the red vertex y values.
    rvy = [j for i, j in redvertices]
    while rvy:
        # This part figures out which vertex we're changing. On a left edge we start with the lowest one, on a right
        # edge we start with the highest one.
        y = min(rvy)
        currentvertex = [(i, j) for (i, j) in redvertices if j == y]
        x = currentvertex[0][0]

        # Here we're removing the current vertex, and then making room for the new vertices that we're about to add.
        vertexset = [(i, j) for (i, j) in vertexset if (i, j) != (x, y)]
        vertexset = [(i + 1, j - 1) if j < y else (i + 1, j) for (i, j) in vertexset]

        # This is adding in the new vertices. Since we shift once, we can always add it to the first column.
        vertexset.append((1, y))
        vertexset.append((1, y - 1))
        vertexset.append((x + 1, y - 1))

        # Now, since we did a while loop we need to update rvy, and also our red vertices changes bc they got shifted
        # over. By processing the bottom vertex first, the y values of all the vertices above it don't change.
        rvy.remove(y)
        leftrededges.remove(x)
        leftrededges = [i + 1 for i in leftrededges]
        redvertices = [(i + 1, j) for (i, j) in redvertices if i + 1 in leftrededges]
        rightrededges = [i + 1 for i in rightrededges]

# Now, we do almost the same for the right vertices.

    # This is the same initialization as above, we just need to figure out which vertices we're using on the right side.
    for m in rightrededges:
        vsx = [i for i, j in vertexset]
        vsxarray = np.array(vsx)
        currentvertices = np.where(vsxarray == m)[0]
        y1 = vertexset[currentvertices[0]][1]
        y2 = vertexset[currentvertices[1]][1]
        y = min(y1, y2)
        redvertices.append((m, y))

    # Since we're adding things to the end of the diagram, we want to figure out where our diagram ends. That's c.
    c = max(vsx)

    # Updating rvy for red edges
    rvy = [j for i, j in redvertices]

    while rvy:
        c += 1
        # We need to start with the highest vertex on the right, same way as above.
        y = max(rvy)
        currentvertex = [(i, j) for (i, j) in redvertices if j == y]
        x = currentvertex[0][0]

        # Again we need to delete the correct vertex, shift everything down, and add in the correct new ones.
        vertexset = [(i, j) for (i, j) in vertexset if (i, j) != (x, y)]
        vertexset = [(i, j - 1) if j <= y else (i, j) for (i, j) in vertexset]
        vertexset.append((c, y))
        vertexset.append((c, y - 1))
        vertexset.append((x, y))

        # Again, updating our set of y values and updating the coordinates of our old list (they all move down by one)
        rvy.remove(y)
        rightrededges.remove(x)
        redvertices = [(i, j - 1) for (i, j) in redvertices if i in rightrededges]
        rvy = [j for i, j in redvertices]

    leftrededges = list(range(1, n + 1))
    rightrededges = list(range(c - n + 1, c + 1))
    rededges = leftrededges + rightrededges

    #print('vertexset = ', vertexset)
    #print('rededges = ', rededges)
    return[vertexset,rededges]
################################################################################################################
