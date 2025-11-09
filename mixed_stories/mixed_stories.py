def raed_and_split():
    conter=1
    with open("mixed_stories.txt","r") as f:
        for l in f:
            if conter % 2 !=0:
                with open("story1.txt","a") as f:
                    f.write(l)
                conter+=1
            elif conter %2 ==0: 
                with open("story2.txt","a") as f:
                    f.write(l)
                conter+=1
raed_and_split()