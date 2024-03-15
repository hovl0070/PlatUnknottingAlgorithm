#NOTE TO SETH: YOU CURRENTLY USING AN OUT OF DATE FILE IN THE VERY FIRST FUNCTION.  YOU WILL WANT TO UPDATE IT AS YOU UPDATE ALL YOUR FUNCTIONS LIST





#############################################################
#This is a prototype of the full function to take a braid word to a rectangular diagram
def braid_word_to_rectangular_diagram(W):
    #The input is an array containing the braid word, for instance sigma_1 sigma_3 sigma_2^{-1} would be input as [1,3,-2].
    attach('ALLFUNCTIONS3_5.sage')  #This is my latest version of all functions 
    #Initialization
    n_from_braidgroup=max(abs(i)+1 for i in W) #This is needed for left_normal_to_string function, we need to know the braid group.
    iteration=1    #This is for the later algorithm its not needed right now
    #Step 1: Make the braid word all positive
    positiveW=braid_to_positive_braid(W)
    #Step 2: Put it into left-greedy normal form
    W_normal_form=positiveW.left_normal_form()
    #Step 3: Remove the Garside element, turn into a string in a more readable form
    W_normal_form_string=left_normal_to_string(W_normal_form,n_from_braidgroup)
    # Step 4: Partition into increasing substrings.  These are the syllables we need. 
    W_normal_form_syllables=syllable_string_partitioning(W_normal_form_string)
    # Step 5: Break into beginning and end of syllables for plat to rectangular diagram input
    W_input=[[W_normal_form_syllables[i][0],W_normal_form_syllables[i][-1]] for i in range(len(W_normal_form_syllables))]
    
    #Step 6: Input into PlatToRectangularDiagram
    [V,E]=plat2rectdiag(W_input)   #The output printed is the vertex set and the red edges
    #drawrectdiag(V, E,iteration)  #This will give a tikzpicture for the rectangular diagram! 
    return [V,E]
#####################################################################


##############################################################################################################################################################
def rectangulardiagram_to_orientedrectangulardiagram(V):
    #Input is the vertex set of the rectangular diagram
    #The goal is to add an additional entry to the vertex set, either an 0 or 1 this will serve as the orientation. We need on each horizontal and vertical a 0 and a 1.  
    #Add a 0 to the first vertex in the vertex set
    oriented_vertex_set=[V[0]+(0,)]
    #Delete that element from the vertex set
    V.pop(0)
    
    while V: #While the vertex set is non-empty we will add a 0 or 1 to each vertex and then add that to the oriented_vertex_set
        
            xindex=[j for j in range(len(V)) if (V[j][0]==oriented_vertex_set[-1][0])] #This will find the index in vertex set of vertex sharing the horizontal with the last element added to the oriented_vertex_set.
            yindex=[j for j in range(len(V)) if (V[j][1]==oriented_vertex_set[-1][1])] #This will find the index in vertex set of vertex sharing the vertical with the last element added to the oriented_vertex_set.
            
            if xindex!=[]:  # If there is a vertex on the horizonal strand that is the one we will add to the oriented_vertex_set
                oriented_vertex_set.append(V[xindex[0]]+((oriented_vertex_set[-1][2]+1) % 2,)) #This adds the updated oriented vertex 
                V.pop(xindex[0]) #That shared horizontal vertex is deleted. 
            elif yindex!=[]:     #Maybe you do not have a vertex sharing the same horizontal in vertex_set (its already in oriented_vertex_set) so find the vertex sharing a vertical
                oriented_vertex_set.append(V[yindex[0]]+((oriented_vertex_set[-1][2]+1) % 2,)) #add this to the oriented vertex set
                V.pop(yindex[0])
            else:
                #print('Something is wrong with your vertex set')
                break
    return oriented_vertex_set


##############################################################################################################################################################

def findproblemhorizontals(oriented_vertex_set):
    horizontals=[]
    problemhorizontals=[]
    for k in oriented_vertex_set:
        khorizontal=[j for j in oriented_vertex_set if j[1]==k[1]] #This gives k and the other vertex on the same horizontal
        horizontals.append(khorizontal)  
        #oriented_vertex_set.remove(khorizontal[1]) #Otherwise your khorizontal will contain two entries for each horizontal
    horizontals = {tuple(h) for h in horizontals}
    horizontals=set(horizontals) #this removes duplicate tuples 
    for i in horizontals:
        zero_vertex=[j for j in i if j[2]==0]
        one_vertex=list(set(i)-set(zero_vertex))
        if zero_vertex[0][0]>one_vertex[0][0]:#this means the orientation is incorrect here
            problemhorizontals.append(i)
    return problemhorizontals          


##############################################################################################################################################################


   ####### Above this line I have found the horizontals that need to be changed they are in the list problemhoizontals, which contains two tuples######
def closedbraiddiagram(oriented_vertex_set_1,problemhorizontals):
    widthofdiagram=len(oriented_vertex_set_1)/2
    problemsaboveset=[]
    OVSclosedbraid=[]
    badyvalues=[h[0][1] for h in problemhorizontals]
    for i in oriented_vertex_set_1:
        problemsabove=0
        yval=i[1]
        xval=i[0]
        for h in problemhorizontals:
            if yval<h[0][1]:
                problemsabove=problemsabove+1
        problemsaboveset.append(problemsabove)
###the number problemsabove will tell us how much each vertex needs to shift down due to adding edges to a problem horizontal########
    for i in oriented_vertex_set_1:
        iindex=oriented_vertex_set_1.index(i)
        yval=i[1]
        xval=i[0]
        orientation=i[2]
        if yval in badyvalues: #its a vertex on a bad horiz 
            if orientation==0:
                OVSclosedbraid.append((xval,yval-problemsaboveset[iindex]-1,0))
                OVSclosedbraid.append((2*widthofdiagram+1,yval-problemsaboveset[iindex]-1,1))
                
            else:
                OVSclosedbraid.append((xval,yval-problemsaboveset[iindex],1))
                OVSclosedbraid.append((-1,yval-problemsaboveset[iindex],0))
  
        else:
            OVSclosedbraid.append((xval,yval-problemsaboveset[iindex],orientation))
    
    return [OVSclosedbraid,problemhorizontals]


###########################################################################################################################################################

def closed_braid_diagram_to_braid_word(V,E):
    #Input is a list of tuples [V,E] where V is the vertex set and E are the red edges.  This is the output from running the 
    # braid_word_to_rectangular_diagram(SOME PLAT BRAID WORD)
    
    #Output is a braid word whose braid closure is the same knot type as the rectangular diagram.
    
    VS=rectangulardiagram_to_orientedrectangulardiagram(V)
    problemhorizontals=findproblemhorizontals(VS)
    [OVSclosedbraid,problemhorizontals]=closedbraiddiagram(VS,problemhorizontals)
  
    numberofstrands=len(OVSclosedbraid)/2 #There are two vertices on each horizontal strand
    syllablelist=[]
    horizontals=[]
    for k in OVSclosedbraid:
        khorizontal=[j for j in OVSclosedbraid if j[1]==k[1]] #This gives k and the other vertex on the same horizontal
        horizontals.append(khorizontal)  
        horizontals = {tuple(h) for h in horizontals}
        horizontals=list(set(horizontals)) #this removes duplicate tuples
    
    verticals=[]
    for v in OVSclosedbraid:
        vvertical=[j for j in OVSclosedbraid if j[0]==v[0]] #This gives v and the other vertex on the same vertical
        verticals.append(vvertical)  
        verticals = {tuple(vert) for vert in verticals}
        verticals=list(set(verticals)) #this removes duplicate tuples
    for i in verticals:
        if i[0][0]==-1 or i[0][0]==max(i for i in verticals)[0][0]:
            verticals.remove(i)      
    #The first and last vertical correspond to -1 and end of braid word
    understrandscrossings=[]
    verticals_2=[]
    while verticals:
        startingvertical=min(k for k in verticals)
        topvertex=max(j for j in startingvertical)
        bottomvertex=min(j for j in startingvertical)
        crossings=0
        for h in horizontals:
                leftvertex=min(j for j in h)
                rightvertex=max(k for k in h)
                height=leftvertex[1]
                if (bottomvertex[1]<height<topvertex[1] and leftvertex[0]<topvertex[0]<rightvertex[0]):
                    crossings=crossings+1
        understrandscrossings.append(crossings)
        verticals.remove(startingvertical)
        verticals_2.append(startingvertical)
#### The above while loop looks for horizontals that cross behind each vertical strand if there are horizontal crossings behind a vertical the number is stored as understrandscrossings so that at verticals[i], the number of understrands crossing it is understrandscrossings[i]###################################################################   
    #When we shift up 
    
    
    
    for i in range(len(understrandscrossings)):
        strdnum=1 #strand number
        if (understrandscrossings[i]!=0 ):
            topvertex=max(j for j in verticals_2[i])
            for h in horizontals:
                rightvertex=max(k for k in h)
                leftvertex=min(j for j in h)
                height=leftvertex[1]
                if (height>topvertex[1] and leftvertex[0]< topvertex[0] <rightvertex[0]):
                    strdnum=strdnum+1
            if topvertex[2]==1:
                syllablelist.append((strdnum,strdnum+understrandscrossings[i]-1))
            else:  #if topvertex is a 0 then the crossings are negative
                v=(strdnum,strdnum+understrandscrossings[i]-1)
                v=[-i for i in v]
                v.reverse()
                syllablelist.append(tuple(v))
         
        
## the above code looks at all the verticals and finds the yvalue of the top vertex and determines how many horizontals are above it that intersect it, this determines the strand number, then we just add strand number and the understrandscrossings+1 to obtain the braid word.       
    braidword=flatten([list(range(syllablelist[i][0],syllablelist[i][1]+1)) for i in range(len(syllablelist))]) 
    return braidword

#############################################################################################################################################################






#HERE IS AN EXAMPLE OF HOW All THE ABOVE FUNCTIONS WORK
#from snappy import *
#from spherogram import ClosedBraid
#from sage.all import *
#GoertizUnknot1=[-2,-2,1,1,-3,-3,2,2,2]
#[V,E]=braid_word_to_rectangular_diagram(GoertizUnknot1)
#braidword=closed_braid_diagram_to_braid_word(V,E)
#braidword
#B = ClosedBraid(braidword)
#B.simplify()
#B.knot_floer_homology()
#B.jones_polynomial()  
#ClosedBraidword.plot()



    
