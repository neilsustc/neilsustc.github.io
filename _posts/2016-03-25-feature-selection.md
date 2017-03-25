---
layout: post
title: Feature Selection
---

## Contents

- [Feature Selection](#feature-selection)
    - [Filter Model](#filter-model)
        - [Feature Ranking](#feature-ranking)
        - [Subset Selection](#subset-selection)

## Feature Selection

Background: too many features

Objective:

- better performance
- more efficiency
- better understanding (of data)

### Filter Model

2 categories: feature ranking and subset selection

based on whether evaluate the goodness of features individually or through feature subsets

#### Feature Ranking

Pros: low complexity  
Cons: don't remove redundancy

Ranking criterion:

- correlation criteria: e.g. 'Pearson correlation coefficient' (limits: )

<!-- - 'Relief' -->

#### Subset Selection

2 measure:

- consistency
- correlation (CFS)

Cons: high complexity
