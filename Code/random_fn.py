import random
PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" :
"class %%% has-a __init__ that takes self and *** parameters.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function named *** that takes self and @@@ parameters.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, and call it with parameters self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}
snippets = list(PHRASES.keys())
print(snippets)
random.shuffle(snippets)
print('\n\n' , snippets)
for snippet in snippets:
    phrase = PHRASES[snippet]
    print('\n', phrase.capitalize().strip()) 
#class_names = [w.capitalize() for w in random.sample(snippets, 2)]#, snippets.count("%%%"))]
#print (class_names)