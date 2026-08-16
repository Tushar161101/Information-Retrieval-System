from util import *

# Add your import statements here
# (Students may import required libraries such as nltk, spacy, re, etc.)
import re
import nltk
import spacy
from nltk.tokenize import TreebankWordTokenizer


class Tokenization():

	# This function performs tokenization using a naive rule-based approach.
	# Each sentence is processed independently and tokens are extracted using a regular expression that captures alphanumeric word boundaries.
	# The regex \b\w+\b matches sequences of characters that form words.
	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		# Fill in code here
		tokenizedText = []

		for sentence in text:
			tokens = re.findall(r'\b\w+\b', sentence)
			tokenizedText.append(tokens)

		return tokenizedText



	# This function performs tokenization using the NLTK Penn Treebank tokenizer.
	# The Penn Treebank tokenizer is a rule-based tokenizer designed for English text and handles punctuation, 
	# contractions, and special cases according to the Penn Treebank tokenization conventions.
	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		# Fill in code here
		tokenizer = TreebankWordTokenizer()
		tokenizedText = []
		for sentence in text:
			tokens = tokenizer.tokenize(sentence)
			tokenizedText.append(tokens)

		return tokenizedText



	# This function performs tokenization using spaCy's NLP pipeline.
	# Each sentence is processed using the spaCy language model which applies rule-based and statistical methods to identify tokens.
	# The tokens are extracted from the spaCy Doc object and stored as a list of token strings.
	def spacyTokenizer(self, text):
		"""
		Tokenization using spaCy

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		# Fill in code here
		nlp = spacy.load("en_core_web_sm")

		tokenizedText = []

		for sentence in text:
			doc = nlp(sentence)
			tokens = [token.text for token in doc]
			tokenizedText.append(tokens)

		return tokenizedText