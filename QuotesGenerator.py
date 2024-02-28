import requests as r
import time as t
import sys
print("This is program by me, inspired from a youtube video. My first program involving API's.")
print("This program generates random quotes using the 'Random Quotes API' by lukepeavey.")
print("github link: https://github.com/lukePeavey/quotable")
print("as mentioned in github, it's free and open source; so thanks to the author/team of quotable for this API")
url="https://api.quotable.io/random"
def getquote():
    q=r.get(url)
    q=q.json()
    #print(q)
    result=q.items()
    result=list(result)
    print(result[1][1])
    print(f"~{result[2][1]}")
print("NOTE: In one session only 5 quotes will be generated at max.;")
c=input("Generate a quote (y/n) ?: ")
if c=='y' or c=='Y':
    for i in range(0,5):
        getquote()
        ch=input("Generate another quote (y/n) ?: ")
        if ch=='y'or ch=='Y':
            getquote()
        else:
            sys.exit()
else:
    sys.exit()
        

    
