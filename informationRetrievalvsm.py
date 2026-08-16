from util import *

# importing tfidf and cosine similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class InformationRetrieval():

	def __init__(self):

		# stores tfidf matrix
		self.index = None
	

	def buildIndex(self, docs, docIDs):
		"""
		builds the document index using tfidf vectors
		"""

		index = None
		
		self.docIDs = docIDs

		processedDocs = []

		for doc in docs:

			flattenedDoc = []

			# combining all sentences into one list
			for sentence in doc:

				flattenedDoc.extend(sentence)

			# converting tokens back into sentence
			processedDocs.append(" ".join(flattenedDoc))

		# converts text into tfidf vectors
		self.vectorizer = TfidfVectorizer()

		index = self.vectorizer.fit_transform(processedDocs)

		self.index = index


	def rank(self, queries):
		
		doc_IDs_ordered = []

		processedQueries = []

		for query in queries:

			flattenedQuery = []

			# flattening query sentences
			for sentence in query:

				flattenedQuery.extend(sentence)

			processedQueries.append(" ".join(flattenedQuery))

		# converting queries into tfidf vectors
		queryVectors = self.vectorizer.transform(processedQueries)

		# cosine similarity between query and docs
		similarities = cosine_similarity(queryVectors, self.index)

		for similarityScores in similarities:

			# sorting docs based on similarity
			rankedDocIndices = np.argsort(similarityScores)[::-1]

			rankedDocIDs = [self.docIDs[idx] for idx in rankedDocIndices]

			doc_IDs_ordered.append(rankedDocIDs)

		return doc_IDs_ordered