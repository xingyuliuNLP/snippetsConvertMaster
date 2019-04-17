import argparse, sys
# create a parser
parser = argparse.ArgumentParser()
with open(sys.argv[1], 'r') as fileInput:
    contents = fileInput.readlines()
parser.add_argument(sys.argv[1])
for x in ["-vsc", "-atom", "-sublime", "-vim", "-all"]:
    parser.add_argument(x, action="store_true")
# add an argument to get our arguments from parser
args = parser.parse_args()

# import sys
# with open(sys.argv[1], 'r') as fileInput:
#     contents = fileInput.readlines()


def listPositionHash(contents):
    positionOfHashes = []
    for lineNumber, lineContent in enumerate(contents):
        if lineContent.startswith('#') and not lineContent.startswith('##'):
            positionOfHashes.append(lineNumber)
    return positionOfHashes
if args.vsc:
    positionOfHashes = listPositionHash(contents)

print(positionOfHashes)