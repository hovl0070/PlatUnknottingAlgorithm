#############################################################################
def left_normal_to_string(leftnormbraid,n_from_braidgroup):
    #This will take a left normal braid, removes the garside elements and turns it back into a string


    A=str(flatten(leftnormbraid))
    if A[1]=='1':                              #If there is not a garside element it puts a 1 there. This removes it.
        A=A[4:-1]
    elif A.find('^') != -1:                    #This will remove the garside elements. We will have to duplicate the string however many times                                                 and append to the beginning.  For now it wont do that.
        A=A[A.find('^')+4:-1]
    else:
        A=A[2:-1]                             #This will remove the [ ] and just leave the braid word
    A=A.replace("*",',').replace(' ','')
    A=A[::-3]                                # This is me being sneaky, I grab only the numbers in reverse order, then flip back
    A=A[::-1]
    #print('This is the positive left normal form combed', A)                             # REMOVE THIS LATER!
    B=list(map(int, str(A)))                 #This is now in string format again.
    B = [x+1 for x in B]  #this changes it from 0-(n-2) to (1-n-1) like it should be!

    return B
#####################################################################################

