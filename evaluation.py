from util import *

# Add your import statements here
import math

class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		relevantRetrieved = 0

		retrievedDocs = query_doc_IDs_ordered[:k]

		for docID in retrievedDocs:

			if docID in true_doc_IDs:
				relevantRetrieved += 1

		precision = relevantRetrieved / k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries
		"""
		meanPrecision = -1

		#Fill in code here
		totalPrecision = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in qrels:

				if qrel["query_num"] == str(query_id):
					true_doc_IDs.append(int(qrel["id"]))

			# summing up precision of each query
			totalPrecision += self.queryPrecision(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		#avg precicion
		meanPrecision = totalPrecision / len(query_ids)
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query
		"""
		recall = -1

		#Fill in code here
		relevantRetrieved = 0

		retrievedDocs = query_doc_IDs_ordered[:k]

		for docID in retrievedDocs:

			if docID in true_doc_IDs:
				relevantRetrieved += 1

		if len(true_doc_IDs) == 0:
			recall = 0
		else:
			recall = relevantRetrieved / len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries
		"""
		meanRecall = -1

		#Fill in code here
		totalRecall = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in qrels:

				if qrel["query_num"] == str(query_id):
					true_doc_IDs.append(int(qrel["id"]))
			#summing up recall of each query
			totalRecall += self.queryRecall(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		# avg recall
		meanRecall = totalRecall / len(query_ids)
		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query
		"""
		fscore = -1

		#Fill in code here
		beta = 0.5

		precision = self.queryPrecision(
			query_doc_IDs_ordered,
			query_id,
			true_doc_IDs,
			k
		)

		recall = self.queryRecall(
			query_doc_IDs_ordered,
			query_id,
			true_doc_IDs,
			k
		)

		if precision == 0 and recall == 0:
			fscore = 0
		else:
			betaSquared = beta ** 2

			fscore = ((1 + betaSquared) * precision * recall) / \
					((betaSquared * precision) + recall)
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries
		"""
		meanFscore = -1

		#Fill in code here
		totalFscore = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in qrels:

				if qrel["query_num"] == str(query_id):
					true_doc_IDs.append(int(qrel["id"]))
			#summing up fscore of each query
			totalFscore += self.queryFscore(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		#avg fscore
		meanFscore = totalFscore / len(query_ids)
		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query
		"""
		nDCG = -1

		#Fill in code here


		retrievedDocs = query_doc_IDs_ordered[:k]

		relevanceDict = {}

		for item in true_doc_IDs:

			relevanceDict[item[0]] = item[1]

		DCG = 0

		for i, docID in enumerate(retrievedDocs):

			relevance = relevanceDict.get(docID, 0)

			DCG += relevance / math.log2(i + 2)

		idealRelevances = sorted(relevanceDict.values(), reverse=True)[:k]

		IDCG = 0

		for i, relevance in enumerate(idealRelevances):

			IDCG += relevance / math.log2(i + 2)

		if IDCG == 0:
			nDCG = 0
		else:
			nDCG = DCG / IDCG
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries
		"""
		meanNDCG = -1

		#Fill in code here
		totalNDCG = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in qrels:

				if qrel["query_num"] == str(query_id):

					true_doc_IDs.append((int(qrel["id"]), 5 - int(qrel["position"])))
			#summing up ndcg of each query
			totalNDCG += self.queryNDCG(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		#avg ndcg
		meanNDCG = totalNDCG / len(query_ids)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)
		"""
		avgPrecision = -1

		#Fill in code here
		relevantCount = 0
		precisionSum = 0

		retrievedDocs = query_doc_IDs_ordered[:k]

		for i, docID in enumerate(retrievedDocs):

			if docID in true_doc_IDs:

				relevantCount += 1

				precisionAtI = relevantCount / (i + 1)
				#summing up precision at each pos
				precisionSum += precisionAtI

		if len(true_doc_IDs) == 0:
			avgPrecision = 0
		else:
			avgPrecision = precisionSum / len(true_doc_IDs)
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries
		"""
		meanAveragePrecision = -1

		#Fill in code here
		totalAP = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in q_rels:

				if qrel["query_num"] == str(query_id):
					true_doc_IDs.append(int(qrel["id"]))
			#summing up ap of each query
			totalAP += self.queryAveragePrecision(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		#mean AP
		meanAveragePrecision = totalAP / len(query_ids)
		return meanAveragePrecision



	def queryReciprocalRank(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of reciprocal rank for a single query

		Parameters
		----------
		arg1 : list
			Ranked list of document IDs
		arg2 : int
			Query ID
		arg3 : list
			List of relevant document IDs
		arg4 : int
			The k value

		Returns
		-------
		float
			Reciprocal rank value
		"""

		reciprocalRank = -1

		#Fill in code here
		retrievedDocs = query_doc_IDs_ordered[:k]

		reciprocalRank = 0

		for i, docID in enumerate(retrievedDocs):

			if docID in true_doc_IDs:
				# reciprocal rank of first relevant
				reciprocalRank = 1 / (i + 1)

				break
		return reciprocalRank


	def meanReciprocalRank(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of Mean Reciprocal Rank (MRR)
		averaged over all queries

		Parameters
		----------
		arg1 : list
			List of ranked document lists
		arg2 : list
			Query IDs
		arg3 : list
			Relevance judgments
		arg4 : int
			The k value

		Returns
		-------
		float
			MRR value
		"""

		meanReciprocalRank = -1

		#Fill in code here
		totalRR = 0

		for i, query_id in enumerate(query_ids):

			true_doc_IDs = []

			for qrel in qrels:

				if qrel["query_num"] == str(query_id):
					true_doc_IDs.append(int(qrel["id"]))
			# summing up reciprocal rank of each query
			totalRR += self.queryReciprocalRank(
				doc_IDs_ordered[i],
				query_id,
				true_doc_IDs,
				k
			)
		#mrr
		meanReciprocalRank = totalRR / len(query_ids)
		return meanReciprocalRank
