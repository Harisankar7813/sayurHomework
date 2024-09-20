#Find out how many friends liked or disliked the movie.
count_liked=0
count_disliked=0
no_of_friends=int(input("Enter number of friends watched movie:"))
for i in range(no_of_friends):
    suggestion=input("Enter your suggestion(liked or disliked):")
    if (suggestion=="liked"):
        count_liked+=1
        print("number of friends liked the movie:",count_liked)
    elif(suggestion=="disliked"):
        count_disliked+=1
        print("number of friends liked the movie:",count_disliked)


