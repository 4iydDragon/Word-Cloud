import io
import wordcloud
import matplotlib.pyplot as plt

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "not", "in", "may", "then", "theres", "for", "on", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Remove punctuations from the text
    for char in file_contents:
        if char in punctuations:
            file_contents = file_contents.replace(char, "")

    # Convert the text to lowercase and split it into words
    words = file_contents.lower().split()

    # Remove uninteresting words from the list of words
    filtered_words = [word for word in words if word not in uninteresting_words]

    # Create a dictionary of word frequencies
    word_freq = {}
    for word in filtered_words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    # Create a WordCloud object and generate the image
    cloud = wordcloud.WordCloud()
    # wordcloud = WordCloud(width=800, height=400, max_words=50, background_color="white").generate(text)
    cloud = wordcloud.WordCloud(width=1366, height=768,background_color="black")
    cloud.generate_from_frequencies(word_freq)
    return cloud.to_array()

def _upload():
    uploaded_file = input("Upload a file:")
    with open(uploaded_file, 'r') as f:
        file_contents = f.read() 
    # Call the calculate_frequencies() function with the file contents
    myimage = calculate_frequencies(file_contents)

    # Display the word cloud image using matplotlib
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()

_upload()
