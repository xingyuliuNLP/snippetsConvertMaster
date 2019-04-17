### convert praat snippet written according to hash format for its usage in Vscode, Sublime text, Atom and Vim

## get the content of description, prefix and body in original file by locating hash mark

import sys
# open praat snippets text file written by user
with open(sys.argv[1], 'r') as f:
    # read all lines in file
    contents = f.read()
    # locate hash positions and stock them in a list
    positionOfHashes = []
    # stock all description content in a dictionary with their line
    for lineNumber, lineContent in enumerate(contents):
        if lineContent.startswith('#') and not lineContent.startswith('##'):
            positionOfHashes = positionOfHashes.append(lineNumber)
            # content after hash in the same line is description
            description = lineContent.split('# ')[1]








## rewrite description, prefix and body in new file for Vscode