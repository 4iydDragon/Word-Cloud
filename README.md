# Word-Cloud
# A python program that generates a a word cloud image

This is a Python script that generates a word cloud image from a text file. The calculate_frequencies function takes a string file_contents and performs the following operations:

Removes punctuation characters from the string.
Converts the string to lowercase and splits it into words.
Removes a list of uninteresting words from the list of words.
Creates a dictionary of word frequencies, where the keys are the words and the values are the number of occurrences of each word in the list of words.
Creates a WordCloud object and generates an image from the word frequencies using the generate_from_frequencies method.
The _upload function takes user input of a file path, reads the contents of the file, and passes it to the calculate_frequencies function to generate the word cloud image. The image is then displayed using the imshow and show methods of the matplotlib.pyplot module.

In the calculate_frequencies function, the code has been modified to customize the WordCloud object with the following parameters:

width: The width of the generated image in pixels (1366).
height: The height of the generated image in pixels (768).
background_color: The background color of the generated image (black).
