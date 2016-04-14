---
layout: hiddenpage
title: Notes - Discrete Mathematics
---

Last modified: 2016-04-14  
[Edit on GitHub](https://github.com/neilsustc/Notes/blob/master/2016%20Spring/Discrete%20mathematics.md)

---

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

Textbook: Discrete Mathematics and Its Applications 

**Discrete mathematics** is the study of mathematical structures that are fundamentally *discrete* rather than *continuous*.  
Discrete mathematics therefore excludes topics in *"continuous mathematics"* such as **Calculus** and **Analysis**.

# Contents

- [1 The Foundations: Logic and Proofs](#chapter-1-the-foundations-logic-and-proofs)
  - [1.1 Propositional Logic](#propositional-logic)
  - [1.3 Propositional Equivalences](#propositional-equivalences)
  - [1.4 Predicates and Quantifiers](#predicates-and-quantifiers)
  - [1.5 Nested quantifiers](#nested-quantifiers)
- [2 Basic Structures: Sets, Functions, Sequences, Sums, and Matrices](#chapter-2-basic-structures-sets-functions-sequences-sums-and-matrices)
  - [2.1 Sets](#sets)
  - [2.2 Set Operations](#set-operations)
  - [2.3 Functions](#functions)
  - [2.4 Sequences and Summations](#sequences-and-summations)
  - [2.5 Cardinality of Sets](#cardinality-of-sets)
- [3 Algorithms](#algorithms)
- [4 Number Theory and Cryptography](#number-theory-and-cryptography)

# Chapter 1 The Foundations: Logic and Proofs

## Propositional Logic

Proposition: a *declarative* statement that is <mark>either true or false</mark>

Compound proposition: formed from existing propositions using *logic operators* (also called connectives)

Logical connectives:

- negation
- conjunction
- disjunction
- conditional (false when p is true and q is false, and true otherwise)
- biconditional (true when p and q have the same truth values)

## Propositional Equivalences

The compound propositions p and q are called **logically equivalent** if p ↔ q is a tautology.  
The notation p ≡ q denotes that p and q are logically equivalent.

### Important Logical Equivalences

De Morgan's laws:

    ¬(p ∨ q) ≡ ¬p ∧ ¬q  
    ¬(p ∧ q) ≡ ¬p ∨ ¬q

Others:

    p → q ≡ ¬p ∨ q

## Predicates and Quantifiers

### Predicates

Informally, a **predicate** is a statement that may be true or false depending on the values of its variables.  
In mathematics, a **predicate** is commonly understood to be a <mark>boolean-valued function</mark> \\(P: X → \{true, false\}\\), called the predicate on \\(X\\).

### Quantifiers

A quantified expression is said to be quantified over the predicate (such as "the natural number \\(x\\) has a successor") whose <mark>free variable is bound by</mark> the **quantifier**.

- universal quantifier ∀
- existential quantifier ∃
- uniqueness quantifier ∃! or ∃<sub>1</sub> (can be avoided)


    ∃!x P(x) ≡ ∃x (P(x) ∧ ∀y (y ≠ x) → ¬P(y))

### Negation of Quantiﬁers

De Morgan's laws for quantiers

    ¬∃x P(x) ≡ ∀x ¬P(x)  
    ¬∀x P(x) ≡ ∃x ¬P(x)

## Nested quantifiers

### The Order of Quantifiers

The order of nested quantifiers *matters* if quantifiers are of *different* type.  
The order of nested quantifiers *does no matter* if quantifiers are of the *same* type.

### Negating Nested Quantifiers

...

## Rules of Inference, Introduction to Proofs, Proof Methods and Strategy

Example: Prove that \\(\sqrt{2}\\) is irrational

# Chapter 2 Basic Structures: Sets, Functions, Sequences, Sums, and Matrices

## Sets

A **set** is an unordered collection of objects, called *elements* or *members* of the set. (naive set theory)

### Venn Diagrams, Subsets

...

### The Size of a Set 

Let S be a set. If there are exactly n distinct elements in S where n is a nonnegative integer, we say that S is a finite set and that n is the **cardinality** of S. The cardinality of S is denoted by \\(\|S\|\\).

### Power sets

the set of <mark>all subsets</mark> of the set S

### Cartesian Product

A × B = \{(a, b) \| a ∈ A ∧ b ∈ B\}.

A subset of the Cartesian product A × B is called a **relation** from the set A to the set B.

## Set Operations

union, intersection, difference(, symmetric difference), complement

### Computer Representation of Sets

1. explicitly store the elements in a list
2. assign a bit in a *bit string* to each element in the universal set and set the bit to 1 if the element is in the set otherwise 0.

## Functions

Let \\(A\\) and \\(B\\) be nonempty sets. A function \\(f\\) from \\(A\\) to \\(B\\) is an assignment of exactly one element of \\(B\\) to each element of \\(A\\). We write \\(f(a) = b\\) if \\(b\\) is the unique element of \\(B\\) assigned by the function \\(f\\) to the element \\(a\\) of \\(A\\). If \\(f\\) is a function from \\(A\\) to \\(B\\), we write \\(f:A \rightarrow B\\).

image, preimage, domain, codomain, range

\\( f_1 + f_2,\ f_1f_2\ \ \ \ (f_i: A \rightarrow R) \\)

injection (one-to-one)  
surjection (onto)  
bijection (one-to-one correspondance)

{::comment}The end of lec04{:/comment}

inverse function, invertible

The **composition of the functions** \\(f\\) and \\(g\\), denoted by \\(f \circ g\\), is defined by \\((f \circ g)(x) = f (g(x))\\)

$$ (f^{-1} \circ f)(a)=a $$

$$ (f \circ f^{-1})(b)=b $$

floor/ceiling function

## Sequences and Summations

### Sequences

A **sequence** is a *function* from a subset of the set of integers (usually either the set {0, 1, 2, ...} or the set {1, 2, 3, ...}) to s set \\(S\\). We use notation \\(a_n\\) to denote the image of the integer \\(n\\).

We use the notation \\({a_n}\\) to describe the sequence.

geometric progression (\\(ar^n\\))/arithmetic progression (\\(a+nd\\))

A **recurrence relation** is said to <mark>recursively define</mark> a sequence. (e.g. Fibonacci sequence)

### Summations

Some useful summation formulae

## Cardinality of Sets

The sets A and B have *the same cardinality* if and only if there is a *one-to-one correspondence* from A to B, denoted by \\(\|A\|=\|B\|\\)

If there is a one-to-one function(*injection*) from A to B, the cardinality of A is less than or the same as the cardinality of B, denoted by \\(\|A\| \leq \|B\|\\).

### Countable Sets

A set that is <mark>either finite</mark> or <mark>has the same cardinality as the set of positive integers</mark> \\(\mathrm{Z}^+\\) is called **countable**. A set that is not countable is called **uncountable**.

**Theorem** The set of (positive) rational numbers is countable.

### Uncountable Sets

**Theorem** The set of real numbers is uncountable. (Proof by contradiction)

{::comment}The end of lec05{:/comment}

# Algorithms

An **algorithm** is a finite sequence of *precise instructions* for performing a computation or for solving a problem.

## The Growth of Functions

**Definition** Let f and g be functions from the set of integers or the set of real numbers to the set of real numbers. We say that \\(f(x)\\) is \\(O(g(x))\\) if there are constants \\(C\\) and \\(k\\) such that

$$ |f(x)| \leq C|g(x)| $$

whenever \\(x > k\\).

**Remark** Intuitively, the definition that \\(f(x)\\) is \\(O(g(x))\\) says that \\(f(x)\\) grows slower than some fixed multiple of \\(g(x)\\) as \\(x\\) grows without bound.

The growth of combinations of functions (\\(f_1+f_2,\ f_1f_2\\))

$$ \Omega,\ \Theta $$

## Complexity of Algorithms

Time and Space Complexity

Three cases of analysis

{::comment}The end of lec06{:/comment}

# Number Theory and Cryptography

## Divisibility and Modular Arithmetic

Division ...

### Congruence

congruence of sums and products

\\(a \equiv b \pmod m\\) and \\(a \bmod b = b\\) are *different*

- \\(a \equiv b \pmod m\\) is a *relation*(congruence relation) on the set of integers
- In \\(a \bmod b = b\\), the notation \\(\bmod\\) denotes a *function*

**Definition** \\( \mathbf{Z}_m;\ +_m,\ ._m \\)

properties: closure, ...

## Integer Representations and Algorithms

base b expansions (decimal, binary, octal, hexadecimal)

## Primes and Greatest Common Divisors

prime/composite

If n is composite, then n has a prime divisor less than or equal to \\(\sqrt{n}\\)

GCD/LCM

## Euclidean Algorithm

{::comment}The end of lec07{:/comment}

**Bezout's Theorem** If \\(a\\) and \\(b\\) are positive integers, then there exist integers \\(s\\) and \\(t\\) such that \\(\mathrm{gcd}(a,b)=sa+tb\\). This is called *Bezout's identity*.

----------------

# Lectures

## Week 7 Wed.

Euler's totient function \\(\phi(n)\\)

用总个数减掉含有公因子的数的个数

费马小定理是欧拉定理的特殊情况，证明方法类似