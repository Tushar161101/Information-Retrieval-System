from util import *

# Add your import statements here
import nltk
from nltk.corpus import stopwords


class StopwordRemoval():

	# This function removes stopwords from tokenized sentences using a predefined curated stopword list provided by NLTK.
	# Stopwords are common words such as "the", "is", "in", etc., that usually do not contribute significant meaning in information retrieval.
	# The function iterates through each sentence and removes tokens that appear in the NLTK English stopword list.
	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None

		#Fill in code here
		stop_words = set(stopwords.words('english'))

		stopwordRemovedText = []

		for sentence in text:
			filtered_sentence = []

			for word in sentence:
				if word.lower() not in stop_words:
					filtered_sentence.append(word)

			stopwordRemovedText.append(filtered_sentence)

		return stopwordRemovedText