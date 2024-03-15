#####################################################################################

#This will partition the string into non-decreasing parts. The commented out part will also partition it into non-decreasing and also decreasing parts (there is a slight issue with parts of the braid word like 121 )

#def syllable_string_partitioning(B):
#    syllable=[]
#    syllables=[]
#    for i in range(len(B)-1):
#        if (B[i]+1 == B[(i+1)] or B[i]-1==B[(i+1)]):
#            syllable.append(B[i])
#        else:
#            syllable.append(B[i])
#            syllables.append(syllable)
#            syllable=[]
#    return syllables
#################################################################################################
#If you want only increasing syllables you can run this one.
def syllable_string_partitioning(B):
    syllable=[]
    syllables=[]
    for i in range(len(B)-1):
        if (B[i]+1 == B[(i+1)]):
            syllable.append(B[i])
        else:
            syllable.append(B[i])
            syllables.append(syllable)
            syllable=[]
    if B[len(B)-1]-1==B[len(B)-1]:
        syllable.append( B[len(B)])
    else: syllables.append([B[len(B)-1]])
    return syllables
##############################################################################
