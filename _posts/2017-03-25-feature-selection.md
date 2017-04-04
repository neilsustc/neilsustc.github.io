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
- [Variable Ranking](#variable-ranking)
    - [Correlation Criteria](#correlation-criteria)
    - [Information Theoretic Ranking Criteria](#information-theoretic-ranking-criteria)
- [Variable Subset Selection](#variable-subset-selection)
    - [Wrapper Methods](#wrapper-methods)
    - [Embedded Metheds](#embedded-metheds)
    - [Filter Methods](#filter-methods)

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

There are 2 different ways,

- variable ranking
- variable subset selection

The first method is to evaluate the features *individually* and then select the good ones (usually using a threshold).

As for another method, we directly *search* through possible subsets (obviously, brute-force searching through all the $ 2^N $ subsets will not work as $ N $ the number of features grows)

## Variable Ranking

Ranking criterion:

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

## Variable Subset Selection

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
Cons: don't remove redundancy (???)

---

IMO, key questions

What're the candidates?

How do we evaluate their goodness?

---

feature selection vs. PCA [2014]  
good features can be independent of the rest of the data (or irrelevant variables)
