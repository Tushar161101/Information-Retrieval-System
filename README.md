# Information Retrieval System using TF-IDF and Vector Space Model

An Information Retrieval (IR) system implemented using the **Vector Space Model (VSM)** and **TF-IDF** document representation. The project covers the complete IR pipeline, from document indexing and retrieval to evaluating retrieval effectiveness on the **Cranfield Dataset** using standard IR metrics. :contentReference[oaicite:0]{index=0}

---

## Features

- TF-IDF based document representation
- Vector Space Model (VSM)
- Cosine Similarity based document ranking
- Inverted Index construction
- Query preprocessing and retrieval
- Cranfield Dataset evaluation
- Comprehensive IR evaluation metrics
- Performance visualization

---

## Implementation

The retrieval system follows the traditional Information Retrieval pipeline:

1. Document preprocessing
   - Tokenization
   - Lowercasing
   - Stop-word removal

2. Document indexing
   - TF-IDF Vectorization
   - Sparse document-term matrix generation

3. Query processing
   - Query preprocessing
   - TF-IDF transformation
   - Cosine similarity computation

4. Ranking
   - Documents ranked according to cosine similarity scores. :contentReference[oaicite:1]{index=1}

---

## Assignment Tasks

### Part 1 – Toy Information Retrieval System

- Tokenization
- Stop-word removal
- Inverted Index construction
- TF-IDF computation
- Boolean Retrieval
- Cosine Similarity computation
- Document Ranking
- Analysis of word sense ambiguity

### Part 2 – Building the IR System

Implemented:

- TF-IDF Vector Space Model
- Build Index function
- Rank function
- Cosine Similarity based retrieval

### Part 3 – Evaluation

Implemented the following evaluation metrics:

- Precision@k
- Recall@k
- F0.5 Score
- Average Precision (AP)
- Mean Average Precision (MAP)
- nDCG
- Mean Reciprocal Rank (MRR)

Evaluation performed for **k = 1 to 10** using the Cranfield Dataset. :contentReference[oaicite:2]{index=2}

---

## Experimental Results

Average evaluation metrics include:

| Metric | Description |
|---------|-------------|
| Precision@k | Relevance among retrieved documents |
| Recall@k | Fraction of relevant documents retrieved |
| F0.5 Score | Precision-weighted harmonic mean |
| MAP | Mean Average Precision |
| nDCG | Normalized Discounted Cumulative Gain |
| MRR | Mean Reciprocal Rank |

The report also includes evaluation plots illustrating metric variation with increasing values of **k**. :contentReference[oaicite:3]{index=3}

---

## Observations

- Precision decreases as more documents are retrieved.
- Recall increases with larger values of *k*.
- MAP improves gradually as additional relevant documents are retrieved.
- nDCG remains relatively stable, indicating consistent ranking quality.
- High MRR indicates that relevant documents are often ranked near the top. :contentReference[oaicite:4]{index=4}

---

## Runtime

Total execution time for indexing, retrieval, and evaluation:

```
13.7083 seconds
```

:contentReference[oaicite:5]{index=5}

---

## Technologies Used

- Python
- NumPy
- scikit-learn
- SciPy
- Matplotlib

---

## Dataset

- Cranfield Collection
- Cranfield Query Set
- Cranfield Relevance Judgments (qrels)

---

## Learning Outcomes

This project demonstrates:

- Information Retrieval fundamentals
- Vector Space Model (VSM)
- TF-IDF weighting
- Inverted Index construction
- Cosine Similarity ranking
- IR evaluation metrics
- Query analysis and retrieval effectiveness

---

## Report

A detailed report describing the implementation, mathematical formulation, evaluation metrics, experimental results, and analysis is included in this repository.
