# whats_for_dinner
Given a fridge full of items presented as a CSV list and a collection of JSON formatted recipes,
produce output of what to cook for dinner tonight.

To get output from this program copy the ingredients csv file and recipes json file to source_files
folder and then do steps below to setup and run the program.

"This is a console application and will return the output in console."

## Setup

Assumption is that the machine that's running this program has pip and python installed.

`If above is not installed please install pip and python3.`

- Run below commands:

``pip install yarn``
``yarn add pandas``

If above doesn't work then:
``pip install pandas``

``python what_to_cook.py``


It will give the output of either the recipe name or call for takeout. Otherwise it'll throw
an exception if there's a problem with the input.
