token={"subject":set(),"verb":set(),"article":set(),"predicate":set(),"adjective":set()}
output=open("output.txt",'w')
def getTokens():
    with open("tokens.txt") as f:
        for line in f:
            (key, val) = line.split(':')
            val=val[:-1]
            token[key].add(val)
def checkRule(string):
    last=string[-2]
    str=string[:-2].split()
    if(str[0] in token['subject']) and (str[1] in token['verb']) and (str[2] in token['article']) and (str[3] in token['adjective']) and (str[4] in token['predicate']) and last=='.':
        output.write(string[:-1].ljust(24)+"\t\t\t")
        output.write("(Valid. Supports Rule1)\n")
    elif(str[0] in token['subject']) and (str[1] in token['verb']) and (str[2] in token['article']) and (str[3] in token['predicate']) and last=='.':
        output.write(string[:-1].ljust(24) + "\t\t\t")
        output.write("(Valid. Supports Rule2)\n")
    elif(str[0].lower() in token['verb']) and (str[1] in token['subject']) and (str[2] in token['article']) and (str[3] in token['adjective']) and (str[4] in token['predicate']) and last=='?':
        output.write(string[:-1].ljust(24) + "\t\t\t")
        output.write("(Valid. Supports Rule3)\n")
    elif(str[0].lower() in token['verb']) and (str[1] in token['subject']) and (str[2] in token['article']) and (str[3] in token['predicate']) and last=='?':
        output.write(string[:-1].ljust(24) + "\t\t\t")
        output.write("(Valid. Supports Rule4)\n")
    else:
        output.write(string[:-1].ljust(24) + "\t\t\t")
        output.write("(Invalid)\n")

getTokens()
with open("input.txt") as f:
    for line in f:
        checkRule(line)
