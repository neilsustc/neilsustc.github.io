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

## Contents

- [Evaluate A Feature - Feature Ranking](#evaluate-a-feature-feature-ranking)
    - [Correlation Criteria](#correlation-criteria)
    - [Single Variable Classifiers (Predictors)](#single-variable-classifiers-predictors)
    - [Information Theoretic Ranking Criteria](#information-theoretic-ranking-criteria)
- [Evaluate A subset of Features - Subset Selection](#evaluate-a-subset-of-features-subset-selection)

---

Background
: too many features

Objectives
: - better prediction performance
  - faster, more cost-effective predictor
  - better understanding (of the data)

Based on whether *evaluate* the goodness of features *individually* or *through feature subset*s, there are 2 categories:

- Feature ranking
- Subset selection

## Evaluate A Feature - Feature Ranking

Ranking criterion:

### Correlation Criteria

e.g.

Pearson correlation coefficient
: $$ R(i) = \frac{cov(X_i, Y)}{\sqrt{var(X_i)var(Y)}} $$
  
  where $ X_i $ designates the random variable of a feature, $ Y $ the random variable of the target, $ cov $ the covariance and $ var $ the variance

Limit: this $ R(i) $ only detect linear dependency between $ X_i $ and $ Y $.

A simple solution: use non-linear preprocessing (e.g. squaring) on $ X_i $.

### Single Variable Classifiers (Predictors)

Select features according to their *"individual predictive power"*

Criteria: the performance of a classifier (predictor) built with a single variable

### Information Theoretic Ranking Criteria

Mutual information
: $$ I(i) = \int_{x_i}\int_{y}p(x_i,y)\log\frac{p(x_i,y)}{p(x_i)p(y)}\,dxdy $$

The difficulty is that the densities $ p(x_i) $, $ p(y) $ and $ p(x_i, y) $ are all unknown and are hard to estimate from data.

The case of discrete variables is easy (because the integral becomes a sum), but the case of continuous variables is hard.

## Evaluate A subset of Features - Subset Selection

### Wrapper Methods

Wrapper Methods
: use *the prediction performance* of a *given learning machine* to evaluate the subsets of features

### Embedded Metheds

// TODO

### Filter Methods

Markov blanket algorithms [Koller and Sahami, 1996]

(IMO, nothing new)

---

TODO

Filter methods

- F-statistic
- Relief, ReliefF, RReliefF
- mRMR
- t-test
- information gain (in information theory)
- CFS
- FCBF
- INTERACT

// put these analysis into summary at the end of the post

Pros: low complexity  
Cons: don't remove redundancy

---

IMO, key questions

What're the candidates?

How do we evaluate their goodness?
