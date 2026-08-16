from util import *

# Add your import statements here
# (Students may import required libraries such as nltk, WordNetLemmatizer, PorterStemmer, etc.)
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet', quiet=True)

class InflectionReduction:

	# This function performs stemming using the Porter Stemmer.
	# Stemming reduces words to their root form by removing common suffixes such as "ing", "ed", "ly", etc., using heuristic rules.
	# Each sentence is processed token by token and the stemmed version of each word is stored.
	def porterStemmer(self, text):
		"""
		Inflection Reduction using Porter Stemmer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed tokens representing a sentence
		"""

		reducedText = None

		# Fill in code here
		stemmer = PorterStemmer()

		reducedText = []

		for sentence in text:
			stemmed_sentence = []
			for word in sentence:
				stemmed_sentence.append(stemmer.stem(word))
			reducedText.append(stemmed_sentence)

		return reducedText


	# This function performs lemmatization using the WordNet Lemmatizer.
	# Lemmatization reduces words to their dictionary base form (lemma) using linguistic knowledge from WordNet. 
	# Unlike stemming, the output is usually a valid dictionary word.
	def wordnetLemmatizer(self, text):
		"""
		Inflection Reduction using WordNet Lemmatizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			lemmatized tokens representing a sentence
		"""

		reducedText = None

		# Fill in code here
		
		lemmatizer = WordNetLemmatizer()
		reducedText = []

		for sentence in text:
			lemma_sentence = []
			for word in sentence:
				lemma_sentence.append(lemmatizer.lemmatize(word))
			reducedText.append(lemma_sentence)

		return reducedText

	# This is a wrapper function for inflection reduction.
	# It allows selecting which reduction technique to apply (for example, stemming or lemmatization).
	# In the current implementation, the function calls the Porter Stemmer method and returns the stemmed text.
	def reduce(self, text):
		"""
		Wrapper function for inflection reduction.
		Students may choose which method to call
		or extend this function to support both options.
		"""

		reducedText = None

		# Fill in code here
		reducedText = self.porterStemmer(text)

		return reducedText