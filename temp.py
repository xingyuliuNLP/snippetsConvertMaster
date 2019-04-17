# import the argparse module
import argparse
# create a parser
parser = argparse.ArgumentParser()
for x in ["-vsc", "-atom", "-sublime", "-vim", "-all"]:
    parser.add_argument(x, action="store_true")
# add an argument to get our arguments from parser
args = parser.parse_args()



def transformBody(bodyContent):
    # transform prompt in body
    for a, b in enumerate(bodyContent):
        if "$" in b and ":" in b and ("\"" not in b):
            bodyContent[a] = "${" + bodyContent[a].replace("\"","")[1:] + "}"
            bodyContent[a] = bodyContent[a].replace(",","")
            bodyContent[a] = bodyContent[a].replace('\"', '\\\"') + ","
        if "$" in b and ":" in b and "\"" in b:
            bodyContent[a] = "\"" + "${" + bodyContent[a].replace("\"","")[1:] + "}" + "\""
            bodyContent[a] = bodyContent[a].replace(",","")
        if "\"" in b:
            bodyContent[a] = bodyContent[a].replace('\"', '\\\"') + ","
    body = ' '.join(bodyContent)
    return body

def writeVsc(fileOutput1):
    # transform description and prefix
    for key in allDescription.keys():
        fileOutput1.write('\n' + '"' + allDescription.get(key, "")[:-1] + '": {' + '\n')
        fileOutput1.write('\t' + '"prefix": "' + allPrefix.get(key, "")[:-1] + '",' + '\n')
        fileOutput1.write('\t' + '"body": [' + '\n')
        # transform body
        for n in range(positionOfHashes[key] + 2, positionOfHashes[key+1]):
            if not lines[n].startswith('#'):
                bodyContent = lines[n].split()
                transformedBody = transformBody(bodyContent)
                fileOutput1.write('\t'*2 + '"' + transformedBody + '",' + '\n')
        fileOutput1.write('\t' + '],' + '\n')
        # exclude last
        if i == (len(positionOfHashes) - 2):
            fileOutput1.write('\t"description": "' + allDescription.get(key, "")[:-1] + '"' + '\n' + '}\n')
        else:
            fileOutput1.write('\t"description": "' + allDescription.get(key, "")[:-1] + '"' + '\n' + '},\n')

def writeSublime(fileOutput2):
    for key in allDescription.keys():
        fileOutput2.write('<snippet>\n')
        fileOutput2.write('\t<content><![CDATA[\n')
        # transform body
        for n in range(positionOfHashes[key] + 2, positionOfHashes[key+1]):
            if not lines[n].startswith('#'):
                bodyContent = lines[n].split()
                transformedBody = transformBody(bodyContent)
                fileOutput2.write(transformedBody + "\n")
        fileOutput2.write(']]></content>\n')
        # transform description and prefix
        fileOutput2.write('\t<description>' + allDescription.get(key, "")[:-1] + '</description>\n')
        fileOutput2.write('\t<tabTrigger>' + allPrefix.get(key, "")[:-1] + '</tabTrigger>\n')
        fileOutput2.write('</snippet>\n\n')

def writeAtom(fileOutput3):
    for key in allDescription.keys():
        # transform description and prefix
        fileOutput3.write("'" + allDescription.get(key, "")[:-1] + "':\n")
        fileOutput3.write("\t'prefix':" + "'" + allPrefix.get(key, "")[:-1] + "'\n")
        fileOutput3.write("\t'body':" + '"""\n')
        # transform body
        for n in range(positionOfHashes[key] + 2, positionOfHashes[key+1]):
            if not lines[n].startswith('#'):
                bodyContent = lines[n].split()
                transformedBody = transformBody(bodyContent)
                fileOutput3.write("\t\t" + transformedBody + "\n")
        fileOutput3.write('\t"""\n\n')

def writeVim(fileOutput4):
    for key in allDescription.keys():
        # transform prefix
        fileOutput4.write('snippet ' + allPrefix.get(key, ""))
        # transform body
        for n in range(positionOfHashes[key] + 2, positionOfHashes[key+1]):
            if not lines[n].startswith('#'):
                bodyContent = lines[n].split()
                transformedBody = transformBody(bodyContent)
                fileOutput4.write(transformedBody + "\n")
        fileOutput4.write('endsnippet\n\n')

with open("snippetsPraat.txt") as file:
    lines = file.readlines()
    # create a list which contains all line numbers of hashes
    positionOfHashes = []
    # create a dictionary which contains all
    allDescription = {}
    allPrefix = {}
    for lineNumber, lineContent in enumerate(lines):
        if lineContent.startswith('#') and not lineContent.startswith('##'):
            positionOfHashes.append(lineNumber)
    for i in range(len(positionOfHashes) - 1):
        # exclude the comment line with three hashes
        if not lines[positionOfHashes[i] + 1].startswith('#'):
            # content after hash is description
            description = lines[positionOfHashes[i]].split('# ')[1]
            allDescription[i] = description
            # content of the first line after hash is prefix
            prefix = lines[positionOfHashes[i] + 1]
            allPrefix[i] = prefix
if args.vsc:
    with open("snippetsPraatVsc.txt", "w") as fileOutput1:
        writeVsc(fileOutput1)
if args.sublime:
    with open("snippetsPraatSublime.txt", "w") as fileOutput2:
        writeVsc(fileOutput2)
if args.atom:
    with open("snippetsPraatAtom.txt", "w") as fileOutput3:
        writeVsc(fileOutput3)
if args.vim:
    with open("snippetsPraatVsc.txt", "w") as fileOutput4:
        writeVsc(fileOutput4)




