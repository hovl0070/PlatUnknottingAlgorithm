
def NuttyKnotter(bridges, iterations):
    import random
    load('left_normal_to_string.sage')   
    n=2*bridges #This is the braid group
    Hilden_Generators=[[1],[2,1,1,2]]
    Flips=[]
    for i in range(1,n/2):
        Hilden_Generators.append([2*i+1])
        Hilden_Generators.append([2*i,2*i-1,2*i+1,2*i])
    #This gives all positive generators, you will want to add negatives to the end too to ensure really messing it up.
    initialbraidword=[i for i in range(2,n,2)] #(it is the std n bridge unknot)
    i=0
    Braidgroup=BraidGroup(n,'s'); #The generators are s_0-s_(n-2) I would like to change this to numbers but I dont know how yet.
    while i<iterations:
        x=random.choice(Hilden_Generators)
        y=random.choice(Hilden_Generators)
        braidword=x+initialbraidword+y #This could be iterated many times 
        insertat=random.choice(range(len(braidword)))
        flipbetween=random.choice(range(2,n-1))
        k=flipbetween
        cointoss=random.choice([0,1])
        if cointoss==1:
            left=list(range(1,k+1))*k
            right=list(range(-(n-1),-k+1))*(n-k)
            flipk=left+right
            braidword.insert(insertat,flipk)
        else:
            left=list(range(-(k-1),0))*k
            right=list(range(k+1,n-1))*(n-k)
            flopk=left+right
            braidword.insert(insertat,flopk)
        braidword=flatten(braidword)
        Braid1=Braidgroup(braidword)
        Braid2=Braid1.left_normal_form()
        initialbraidword=left_normal_to_string(Braid2,n)
        i=i+1
    Finalbraidword=Braidgroup(braidword)
    #plot=Finalbraidword.plot(orientation='left-right', figsize=10)
    #show(plot)
    return braidword
    #I have not used any negative double coset moves add those to hilden subgroup. 
