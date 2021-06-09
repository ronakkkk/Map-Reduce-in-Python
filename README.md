# Map-Reduce-in-Python

So I have used regular expression to read each line of texts from the data.txt file. 

Converting all the words to lower case, if there are any and stored in a list. 

Then using inbuilt python function we sort the words of list.

Then we create a defaultdict variable which helps to create a dictionary of list where it won't through any errors if the key value passed to the dictionary isn't there.

Now passing each word from the sorted words of list to dictionary and append to it.

We get the same word from the above action and then using the dictionary values we get the requird similar words which shares the same character.

But even it includes all the words without having the similar words. So we remove it if the lenght of the list is 1. 

Map reduce works by mapping the code and then reducing the required output yield at mapper and reducer. 

Running the code in command line by writing the following command:

python assignment1.py data.txt > output.txt

In which the data.txt is the input file and the output is stored in the output.txt file. 
