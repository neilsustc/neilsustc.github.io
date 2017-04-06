---
layout: post
title: Feature Selection
tags: research summary
---

<div class="excerpt">
    A review of feature selection
</div>

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]}});
</script>
<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_SVG'></script>

<!-- ## Contents -->

- [Overview](#overview)
- [Feature weighting](#feature-weighting)
    - [Correlation Criteria](#correlation-criteria)
    - [Information Theoretic Ranking Criteria](#information-theoretic-ranking-criteria)
    - [Others](#others)
- [Feature subset search](#feature-subset-search)
- [Others](#others)

---

## Overview

Why do we need feature selection?

- help understanding data
- improve prediction performance (avoid curse of dimensionality)
- reduce computation requirement
- ...

What we want is a subset of variables/features which is "good".

<!-- <ol start="0">
    <li style="color: rgba(0,0,0,0.5)">What are the candidates?</li>
    <li>How do we <em>evaluate</em> the "goodness" of those candidates?</li>
</ol> -->

<!-- 1. How do we *evaluate* the 'goodness' of those candidates?
2. There are too many subsets ($ 2^N $) as the number of features grows. -->

But how?

There are several different ways based on whether they evaluate the "goodness" of features *individually* or *through feature subsets*

- feature weighting
- feature subset search
- others

## Feature weighting

After assigning weight to each feature, we can select by setting a threshold, AKA **filter methods**.

### Correlation Criteria

e.g.

Pearson correlation coefficient
: $$ R(i) = \frac{cov(X_i, Y)}{\sqrt{var(X_i)var(Y)}} $$
  
  where $ X_i $ designates the random variable of a feature, $ Y $ the random variable of the target, $ cov $ the covariance and $ var $ the variance

Limit: this $ R(i) $ only detect linear dependency between $ X_i $ and $ Y $.

A simple solution: use non-linear preprocessing (e.g. squaring) on $ X_i $.

### Information Theoretic Ranking Criteria

Mutual information
: $$ I(i) = \int_{x_i}\int_{y}p(x_i,y)\log\frac{p(x_i,y)}{p(x_i)p(y)}\,dxdy $$

The difficulty is that the densities $ p(x_i) $, $ p(y) $ and $ p(x_i, y) $ are all unknown and are hard to estimate from data.

The case of discrete variables is easy (because the integral becomes a sum), but the case of continuous variables is hard.

### Others

- Relief, ReliefF, RReliefF
- ...

## Feature subset search

There are 2 questions,

1. How do we evaluate a subset of variables?
2. How can we effectively search through candidate feature subsets?

For question 1, of course we can still use correlation measure (e.g. CFS (correlation-based feature selection)) or others (e.g. consistency measure).  
If we use *the prediction performance* of a *given predictor* to evaluate the variable subset, then we get **wrapper methods**.

For question 2, it's about search strategies (exhaustive, heuristic and random search).

Combining these two parts, we will have many methods.

## Others

Clustering, ...

---

Feature selection vs. PCA  
[2014 A Survey on ...] Good features can be independent of the rest of the data (or irrelevant variables)

Why redundancy is bad?  
[2003 ICML Feature Selection for High-Dimensional ... #2.Related Work]  
[2003 JMLR An Introduction ...]
