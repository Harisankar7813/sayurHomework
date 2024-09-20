'''Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."'''

def count_consective_words():
    words=[]
    str1=input("Enter a Passage with consective words:")
    passage=str1.split()
    words.extend(passage)

    consective_count=0
    for i in range(len(words)+1):
        if words[i].strip().lower()==words[i+1].strip().lower():
            consective_count+=1
    print(f"no of consective words in passage:{consective_count}")
    
count_consective_words()