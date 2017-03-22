# Program to print slices in a given string

text = "AOH4IlOghnht0mSAq13wzmDsstZZRQvvCQo5eKKy7Krw75uKv3GPseudorcaFZgIHv8sQNwylRe3zlRibPlO5G2G8RV0I2mr8mhPCVWRKiZ9Zo6vwhFaM1T1ISzNhQXvlpTyrotYSCbkiml8HZD5bK8yUd8OhZcLNcaninus6T3maCPBxOAQ6X.." # input string

a1 = 51 # start point 1
a2 = 59 # finish point 1
b1 = 161 # start point 2
b2 = 167 # finish point 2
text1 = text[a1:a2 + 1] # variable for saving first slice. Add 1 to the end point because stop position is not included
text2 = text[b1:b2 + 1] # variable for saving the second slice
print text1, text2 # print two slides, separated by a blank space