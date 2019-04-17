# scanSnippetsVsc
## import all optional arguments used in command line
import argparse, sys
# create a parser
parser = argparse.ArgumentParser()
# read sublime text snippets
with open(sys.argv[1], 'r') as fileInput:
    contents = fileInput.readlines()
parser.add_argument(sys.argv[1])
for x in ["-vsc", "-atom", "-sublime", "-vim", "-all"]:
    parser.add_argument(x, action="store_true")
# add an argument to get our arguments from parser
args = parser.parse_args()

# find description between <description> </description>

# find prefix between <tabTrigger> </tabTrigger>





