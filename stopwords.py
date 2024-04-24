import nltk
nltk.download('stopwords')
import re
from collections import Counter
from nltk.corpus import stopwords

# Read the contents of the file
with open("paragraphs.txt", 'r') as file:
    text = file.read()
# Remove punctuation and convert text to lowercase
text = re.sub(r'[^\w\s]', '', text)
text = text.lower()

# Remove stop words using NLTK
stop_words = set(stopwords.words('english'))
words = text.split()
filtered_words = [word for word in words if word not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display the word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
