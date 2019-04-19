# snippetsConvertMaster
Convert text file in which snippets are writed according to certain rules

Convert snippets among Vsc(Visual Studio Code), Atom and Sublime Text.

This page is maintained by

* [Xiaoou WANG (phd student in speech science, master student in natural language processing)](http://xiaoouwang.github.io)
* [Xingyu LIU (passionate nlp lover)](https://github.com/xingyuliuNLP)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Why


## How to use
### Create a snippet text file and convert it for Vsc/Atom/Sublime Text
* Write your input text file according to the following rules
You could put all of your snippets in this input file and convert them all to the output file.

There is an example file in [exampleInput folder](https://github.com/xingyuliuNLP/snippetsConvertMaster/blob/master/exampleInput/snippetsPraat.txt)
1. Every snippet begins with a hash sign and a space <kbd># </kbd>
2. Description: append snippet's description just after the hash sign and space in the same line
3. Prefix: append snippet's prefix at the next line of description
4. Body: append snippet's main content from the next line of prefix
5. The whole file must be end with a hash sign in the last line

You could also classify your snippets with a title marked by 3 hashes in the first place
*Attention*

If there is a prompt information after dollar sign, the information should be joined together
```
### object creation
# create pitch object
crPitch
To Pitch: 0, 75, 600
### graphics
# set line form
setLineForm
$1:solidLine $0
#
```


* Convert processing in command line
1. Change the current working directory to your local project
2. List your arguments of convert file name, input file name, editor option after "python"

	 By now, there are 4 editor options:

	 <kbd>-vsc</kbd> for Visual Studio Code,

	 <kbd>-sublime</kbd> for Sublime Text,

	 <kbd>-atom</kbd> for Atom and if you want,

	 <kbd>-all</kbd> for all these above.

	 For example:
	 ```
   $python snippetsConvertMasterV4.py snippetsPraat.txt -vsc
	 ```
Then a text file for Vsc will be exported like below
```
{
"create pitch object": {
	"prefix": "crPitch",
	"body": [
		"To Pitch: 0, 75, 600",
	],
	"description": "create pitch object"
},
"set line form": {
	"prefix": "setLineForm",
	"body": [
		"${1:solidLine} $0"
},
}

```