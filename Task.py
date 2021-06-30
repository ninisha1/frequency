w=input("enter the string ")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d

output=most_frequent(w)
dec = dict( sorted(output.items(),
        key=lambda item: item[1],
        reverse=True))

print(dec)
