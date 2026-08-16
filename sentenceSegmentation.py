from util import *

# Add your import statements here
import re
import nltk
import spacy
from nltk.tokenize import sent_tokenize
nltk.download('punkt', quiet=True)


class SentenceSegmentation():

	def __init__(self):
		# Load spaCy model (students may use this if needed)
		self.nlp = spacy.load("en_core_web_sm")


	# This function performs sentence segmentation using a naive rule-based approach.
	# The method assumes that sentences end with '.', '!' or '?'.
	# It splits the input text wherever these punctuation marks appear.
	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		# Fill in code here
		sentences = re.split(r'[.!?]+', text)
		segmentedText = [s.strip() for s in sentences if s.strip() != ""]
		return segmentedText


	# This function performs sentence segmentation using the NLTK Punkt tokenizer.
	# Punkt is a pre-trained unsupervised model that learns abbreviation patterns and sentence boundary detection rules from large corpora.
	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		# Fill in code here
		segmentedText = sent_tokenize(text)
		return segmentedText


	# This function performs sentence segmentation using spaCy's NLP pipeline.
	# spaCy detects sentence boundaries using linguistic features such as dependency parsing, punctuation rules, and statistical models.
	def spacySegmenter(self, text):
		"""
		Sentence Segmentation using spaCy

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		# Fill in code here
		doc = self.nlp(text)
		segmentedText = [sent.text.strip() for sent in doc.sents]
		return segmentedText