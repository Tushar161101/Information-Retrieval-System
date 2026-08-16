# Add your import statements here
import nltk
import os
import ast
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')

# Add your utility functions here
# Load NLTK stopwords
nltk_stopwords = set(stopwords.words('english'))


def corpus_stopword_analysis():
    # Load tokenized documents
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "output", "tokenized_docs.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        tokenized_docs = ast.literal_eval(f.read())

    word_counts = Counter()

    for doc in tokenized_docs:
        for sentence in doc:
            for word in sentence:
                word_counts[word.lower()] += 1

    total_words = sum(word_counts.values())

    threshold = 0.004
    corpus_stopwords = set()

    for word, count in word_counts.items():
        if count / total_words > threshold:
            corpus_stopwords.add(word)

    overlap = nltk_stopwords.intersection(corpus_stopwords)
    only_nltk = nltk_stopwords - corpus_stopwords
    only_corpus = corpus_stopwords - nltk_stopwords

    print("\n----- Stopword Analysis -----")

    print("NLTK Stopwords:", len(nltk_stopwords))
    print("Corpus Stopwords:", len(corpus_stopwords))
    print("Overlap:", len(overlap))

    print("\nWords only in NLTK:")
    print(list(only_nltk)[:20])

    print("\nWords only in Corpus:")
    print(list(only_corpus)[:20])


def test_sentence_segmentation():
    # Import inside function to avoid circular import
    from sentenceSegmentation import SentenceSegmentation
    segmenter = SentenceSegmentation()
    sentences = [
        "M.S. Dhoni led CSK to multiple IPL titles with his cool captaincy.",
        "I submitted my NLP assignment at 11:59 p.m. sharp.",
        '"Will India win the next World Cup?" asked the nervous cricket fan.',
        "The algorithm's accuracy is 98.5% on this dataset.",
        "1. Start the simulation. 2. Analyze the loss function.",
        'He said, "Dhoni is the best finisher!" The whole stadium cheered.',
        "Visit www.iitm.ac.in to check the M.Tech admission results for 2026.",
        "What?! Jadeja hit a six on the last ball!! Unbelievable!",
        "Dr. APJ Abdul Kalam remains an inspiration for every Indian student.",
        "The match starts in 15 minutes...please hurry up to the MA Chidambaram Stadium.",
        "Contact the HOD at cseoffice@institute.ac.in for elective queries.",
        "The U.S. and India are collaborating on advanced AI research projects.",
        '"Wait!" the umpire shouted, "The bowler has overstepped the line!"',
        "The price of the signed cricket bat was 75,000.50 at the auction.",
        "Prof. Sutanu's lecture on NLP was great...looking forward to the next one."
    ]

    print("\n\n----- Sentence Segmentation Test -----")
    for i, text in enumerate(sentences):
        print("\n----------------------------")
        print("Sentence", i+1)
        print(text)

        print("\nNaive:")
        print(segmenter.naive(text))

        print("\nPunkt:")
        print(segmenter.punkt(text))

        print("\nspaCy:")
        print(segmenter.spacySegmenter(text))

if __name__ == "__main__":
    corpus_stopword_analysis()
    test_sentence_segmentation()