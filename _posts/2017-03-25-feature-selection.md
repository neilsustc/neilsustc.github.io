---
layout: post
title: Feature Selection
---

<div class="excerpt">
    A review of feature selection
</div>

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_SVG'></script>

## Contents

- [Filter Model](#filter-model)
    - [Feature Ranking](#feature-ranking)
    - [Subset Selection](#subset-selection)

---

Background
: too many features (tens or hundreds of thousands of variables)

Objective
: - better performance
  - more efficiency
  - better understanding (of data)

## Filter Model

2 categories:

- feature ranking
- subset selection

based on whether *evaluate* the goodness of features *individually* or through feature *subset*s

### Feature Ranking

Pros: low complexity  
Cons: don't remove redundancy

Ranking criterion:

####  Correlation Criteria

e.g. 'pearson correlation coefficient'

$$ R(i) = \frac{cov(X_i, Y)}{\sqrt{var(X_i)var(Y)}} $$

while \\(X_i\\) is the random variable of a feature, \\(Y\\) is the random variable of the target

- 'Relief'

### Subset Selection

2 measure:

- consistency
- correlation (CFS)

Cons: high complexity
