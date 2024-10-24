#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     
#Student Name:Lucas  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    baselabour=1000 #static cost
    treecost=100 
    length=float(input( " what is the length")) #input data
    width=float(input( " what is the width?"))
    trees=float(input( " how many trees do you want cutted down?"))
    grass=(input ( " enter grass. fescue, bentgrass, campus?"))
    widthlength= length*width
    
    if grass== "fescue":
       grasscost=0.05 *widthlength
    elif grass== "bentgrass":
        grasscost=0.02*widthlength
    elif grass== "campus":
        grasscost=0.01*widthlength
    else:
        print("error pick a vaild grass type") #making sure they pick a vaild grass type
    
    if widthlength >=5000:
        surface=500
    else:
        surface=0
    totaltreecost=treecost*trees
    
    finaltotal=totaltreecost+baselabour+surface+grasscost
    
    print(widthlength,"is your width*length" ) #showing them the results
    print(totaltreecost, "is your tree cost" )
    print(finaltotal, "is your totalcost" )




    # YOUR CODE ENDS HERE
main()