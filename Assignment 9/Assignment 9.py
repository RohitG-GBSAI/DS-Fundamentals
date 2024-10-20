import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

file_path = 'input.txt'

with open(file_path, 'r') as file:
    reviews = file.readlines()

sia = SentimentIntensityAnalyzer()

positive_reviews = []
neutral_reviews = []
negative_reviews = []

for review in reviews:
    sentiment_score = sia.polarity_scores(review)
    compound = sentiment_score['compound']

    if compound >= 0.5:
        positive_reviews.append(review)
    elif compound <= -0.2:
        negative_reviews.append(review)
    else:
        neutral_reviews.append(review)

print(f"Positive reviews: {len(positive_reviews)}")
print(f"Neutral reviews: {len(neutral_reviews)}")
print(f"Negative reviews: {len(negative_reviews)}")

labels = ['Positive', 'Neutral', 'Negative']
counts = [len(positive_reviews), len(neutral_reviews), len(negative_reviews)]

plt.bar(labels, counts, color=['green', 'gray', 'red'])
plt.title('Sentiment Analysis of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Define function to check if a review contains pronouns
def contains_pronoun(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        if tag in ['PRP', 'PRP$']:
            return True
    return False

# Filter out reviews containing pronouns
def filter_reviews(reviews):
    filtered_reviews = [review for review in reviews if not contains_pronoun(review)]
    return filtered_reviews

# Summarize reviews using NLTK
def nltk_summarizer(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    word_freq = nltk.FreqDist(words)
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:6]
    summary = ' '.join(top_sentences)
    return summary

# Filter and summarize positive, neutral, and negative reviews
filtered_positive_reviews = filter_reviews(positive_reviews)
filtered_neutral_reviews = filter_reviews(neutral_reviews)
filtered_negative_reviews = filter_reviews(negative_reviews)

positive_text = "\n".join(filtered_positive_reviews)
neutral_text = "\n".join(filtered_neutral_reviews)
negative_text = "\n".join(filtered_negative_reviews)

positive_summary = nltk_summarizer(positive_text)
neutral_summary = nltk_summarizer(neutral_text)
negative_summary = nltk_summarizer(negative_text)

file_path_positive = 'fpositive_summary.txt'
file_path_neutral = 'fneutral_summary.txt'
file_path_negative = 'fnegative_summary.txt'

with open(file_path_positive, 'w') as pos_file:
    pos_file.write(positive_summary)

with open(file_path_neutral, 'w') as neu_file:
    neu_file.write(neutral_summary)

with open(file_path_negative, 'w') as neg_file:
    neg_file.write(negative_summary)

print("Filtered summaries for positive, neutral, and negative reviews have been saved.")
