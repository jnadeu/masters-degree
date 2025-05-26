Below is an example Python script that does the following:

1. Uses the **requests** library and **BeautifulSoup** to fetch the HTML from the given Wikipedia page and extract the first paragraph.
2. Uses **nltk** to tokenize the paragraph into sentences and selects the first three sentences.
3. For each sentence, it tokenizes into words, removes stopwords, then shows both lemmatized and stemmed versions.

Make sure to install the required packages (e.g. via `pip install requests beautifulsoup4 nltk`) before running the script.

```python
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download required NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# URL to fetch the content
url = "https://en.wikipedia.org/wiki/Natural_language_processing"

# Fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract only the first meaningful paragraph from the article.
# Wikipedia pages often include several <p> tags; here, we assume the first non-empty <p> is the one we need.
paragraphs = soup.find_all('p')
paragraph_text = ""
for p in paragraphs:
    text = p.get_text().strip()
    if text:
        paragraph_text = text
        break

# Tokenize the paragraph into sentences and take the first 3 sentences.
sentences = sent_tokenize(paragraph_text)
selected_sentences = sentences[:3]

# Initialize NLTK tools for text processing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Process each selected sentence
processed_sentences = []
for sentence in selected_sentences:
    # Tokenize into words and remove punctuation tokens (keeping only alphabetic tokens)
    words = [word for word in word_tokenize(sentence) if word.isalpha()]
    
    # Remove stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatize the filtered words (convert words to lowercase for consistency)
    lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in filtered_words]
    
    # Stem the lemmatized words
    stemmed_words = [stemmer.stem(word) for word in lemmatized_words]
    
    processed_sentences.append({
        'original': sentence,
        'tokens': words,
        'filtered': filtered_words,
        'lemmatized': lemmatized_words,
        'stemmed': stemmed_words
    })

# Display the results
for i, proc in enumerate(processed_sentences, 1):
    print(f"Sentence {i}: {proc['original']}\n")
    print("Tokens:", proc['tokens'])
    print("After Stopword Removal:", proc['filtered'])
    print("Lemmatized:", proc['lemmatized'])
    print("Stemmed:", proc['stemmed'])
    print("\n" + "-"*50 + "\n")
```

### Explanation

- **Fetching and Parsing HTML:**  
  The script uses `requests.get` to fetch the page content and BeautifulSoup to parse the HTML. It then finds all `<p>` tags and picks the first one that contains text.

- **Sentence Tokenization:**  
  Using `nltk.sent_tokenize`, the script splits the paragraph into sentences and selects the first three.

- **Word Processing:**  
  For each sentence:
  - It tokenizes the sentence into words (ignoring punctuation).
  - Filters out stopwords using NLTK's list.
  - Applies lemmatization (with `WordNetLemmatizer`) to get the base form of each word.
  - Applies stemming (with `PorterStemmer`) to reduce each word to its stem.

This script provides a clear demonstration of using BeautifulSoup to extract content from a webpage and then using NLTK for basic text normalization techniques.