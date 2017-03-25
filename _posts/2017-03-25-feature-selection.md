---
layout: post
title: Feature Selection
---

<div class="excerpt">
    A review of feature selection
</div>

## Contents

- [Filter Model](#filter-model)
    - [Feature Ranking](#feature-ranking)
    - [Subset Selection](#subset-selection)

---

Background: too many features

Objective:

- better performance
- more efficiency
- better understanding (of data)

## Filter Model

2 categories: feature ranking and subset selection

based on whether evaluate the goodness of features individually or through feature subsets

### Feature Ranking

Pros: low complexity  
Cons: don't remove redundancy

Ranking criterion:

- correlation criteria: e.g. 'Pearson correlation coefficient' (limits: )

- 'Relief'

### Subset Selection

2 measure:

- consistency
- correlation (CFS)

Cons: high complexity
