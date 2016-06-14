---
layout: hiddenpage
title: Notes - Data Mining
---

Last modified: 2016-06-12  

---

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

# Chap 2 Data

importance of "knowing your data" **!!!**

## Types of Data

A **data set** often be viewed as a collection of **data object**s (or **record**, **sample** etc.)

In turn, data objects are described by a number of **attribute**s (or **field**, **feature** etc.)

### Attributes and Measurement

Measurement scale
: a rule (*function*) that associates *a numerical or symbolic value* with *an attribute of an object*

The *properties* of an attribute <mark>need not be the same</mark> as that of the values used to measure it.  
In other words, the values used to represent an attribute may have properties that are not properties of the attribute itself, and vice versa. **!!!**

For example, both employee *ID* and *age* can be represented as integers. However, while it is reasonable to talk about the average age of an employee, it makes no sense to talk about the average employee ID.

**Different types of attribute**

![attr types](/static/imgs/attr-types.png)

Asymmetric attributes
: certain attribute values are more important than the others. (e.g. one-hot)

### Types of Data Sets

General characteristics of data sets:

- dimensionality (number of attributes)
- sparsity
- resolution (measurement scale)

Data sets types:

- Record data
  - Data matrix
- Graph-based data
- Ordered data
  - Sequential data
  - Sequence data
  - Spatial data

## Data Quality

### Issues (...)

### Data Preprocessing

Goal: improve the data mining analysis with respect to time, cost, and quality.

Roughly 2 categories:

- selecting data objects and attributes for the analysis
- creating/changing the attributes

## Measures of Similarity and Dissimilarity

Similarity and dissimilarity bewteen (1) simple attributes (omitted); (2) data objects

- Euclidean *distance* (generally, Minkowski distance)
- For binary data: Simple matching coefficient (SMC), Jaccard coefficient
- Cosine similarity
- Extended Jaccard coefficient (Tanimoto coefficient)
- Pearson's correlation

### Issues in Proximity Calculation

What if:

- attributes have *different scales* / attributes are *correlated*
- data objects are composed of different types of attributes, e.g. quantitative and quanlitative
- attributes have different weights

### Selecting the Right Proximity Measure

For many types of *dense*, *continuous* data, metric *distance* measures (such as Euclideam distance) are often used.

For *sparse* data, which often consists of asymmetric attributes, the *cosine*, *Jaccard* measures are appropriate.

Practical consideration can also be important.

# Chap 4 Classification

Classification
: learning a *target function* \\(f\\) (classification model) that maps attributes set \\(X\\) to one of the predifined class label \\(y\\).

Classification techniques are most suited for predicting or describing data sets with *binary* or *nominal categories*.  
They are less effective for *ordinal categories* because they do not consider the implicit order among the categories. **???**  
Other forms of relationships among categories are also ignored.

Performance metric: accuracy, error rate, ...

Classification techniques:

- decision tree classifiers
- rule-based classifiers
- neural networks
- SVMs
- naive Bayes classifiers
- ...

## Decision Tree Induction

### How a Decision Tree Works ...

### How to Build a Decision Tree

Finding the optimal decision tree is *computationally infeasible* because of the exponential size of the search space (there are exponentially many decison trees that can be constructed from a given set of attributes).

Hunt's Algorithm
: (...) (greedy strategy)

Issues:

- Determine how to split the records
  - How to specify the attribute test condition (in other words, how to branch according to the attribute)
  - How to determine the best split
    - Gini index
    - Entropy
    - Misclassification error
- Determine when to stop splitting
  - all the records belong to the same class
  - all the records have similar attributes values
  - early termination (to be discussed later)

## Model Overfitting

### Estimation of Generalization Errors

### Handling Overfitting

prepruning, post-pruning **???**

### ROC

x: FPR; y: TPR

# Chap 6 Association Analysis

Itemset, support count

Association rule, support, confidence

Association rule discovery

- Frequent itemset generation
- Rule generation

## Frequent itemset generation

Apriori principle
: If an itemset is frequent, then all of its subsets must also be frequent.

Hash tree **???**

## Rule generation

## Compact Representation of Frequent Itemsets

Maximal frequent itemset
: ...

## FP-Growth Algorithm **???**

## Evaluation of Association Patterns

- lift
- interest factor I
- \\(phi\\)-coefficient
- IS

# Chap 8 Cluster Analysis

## Overview

Goal
: Minimize intra-cluster distances, maximize inter-cluster distances

### Different Types of Clusterings

### Different Types of Clusters


