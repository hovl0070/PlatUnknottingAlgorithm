###################################################################
def braid_to_positive_braid(W):
    #Input is an array [1 -2 3 5 -1 -2] etc.
    #Output is a positive braid.  This could be adjusted to output just the positive array!
    n=max(abs(i)+1 for i in W) #This is the braid group
    L=list(range(1,n)) #This will be used to generate the positive replacementwords
    positivewordreplacement=[]
    for j in range(1,n):
        positivewordreplacement.append(L[j-(n+1)::-1]+L+L[:j-1:-1]) #This array holds in each index the replacement positive word
        PositiveW=[];
    for i in W:
        if i>0:
            PositiveW.append(i)
        else:
             PositiveW.append(positivewordreplacement[i])
    PositiveW=flatten(PositiveW) #This is the positive braid word replacing the input W
    Braidgroup=BraidGroup(n,'s'); #The generators are s_0-s_(n-2) I would like to change this to numbers but I dont know how yet.
    PositiveBraidW=Braidgroup(PositiveW)
    return PositiveBraidW
#############################################################################
