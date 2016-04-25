---
layout: hiddenpage
title: Notes - Numerical Analysis
---

Last modified: 2016-04-25  
[Edit on GitHub](https://github.com/neilsustc/Notes/blob/master/2016%20Spring/Numerical%20analysis.md)

---

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

Textbooks:

- A First Course in Numerical Analysis, Anthony Ralston, Philip Rabinowitz, 2 ed.
- 数值分析，李庆扬等，第五版

## Contents

- [Preliminaries](#preliminaries)
- [Chapter 1 Introduction](#chapter-1)
  - [Sources of Error](#sources-of-error)
- [Chapter 3 Interpolation](#chapter-3-interpolation)
  - [Lagrangian Interpolation](lagrangian-interpolation)
  - [Newton polynomial](#newton-polynomial)
  - [Hermite Interpolation](#hermite-interpolation)
  - [Spline Interpolation](#spline-interpolation)
- [Chapter 4 Numerical Differentiation/Quadrature and Summation](#chapter-4-numerical-differentiation-numerical-quadrature-and-summation)
  - [Numerical Differentiation](#numerical-differentiation)
    - [Richardson Extrapolation](#richardson-extrapolation)
  - [Numerical Quadrature: The General Problem](#numerical-quadrature-the-general-problem)
  - [Newton-Cotes Quadrature Formulas](#newton-cotes-quadrature-formulas)
  - [Composite Quadrature Formulas](#composite-quadrature-formulas)
  - [Gaussian Quadrature](#gaussian-quadrature)

# Preliminaries

## Taylor series

The *taylor series* of a function \\(f(x)\\) that is infinitely differentiable at \\(a\\) is the power series

$$ \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n $$

# Chapter 1 

## What is Numerical Analysis

Numerical analysis is <mark>the study of algorithms</mark> that use *numerical approximation* (as opposed to *general symbolic manipulations*) for the problems of mathematical analysis (as distinguished from *discrete mathematics*).

## Sources of Error

Roughly in 2 areas:

- those inherent in the mathematical formulation of the problem
- those incurred in finding the solution numerically

Formly:

- approximation to the physical situation
- inaccuracies in the physical data
- blunder (careless)
- truncation error (it often is the result of <mark>truncating an infinite process to get a finite process</mark>, i.e., summation or integration)
- roundoff error (numbers have infinite decimal representations which must be rounded)

## Error Definitions and Related Matters

- true value
- relative error

...

# Chapter 3 Interpolation

Interpolation is a method of <mark>constructing new data points</mark> within the range of <mark>a discrete set of known data points</mark>.

## Polynomial interpolation

We know \\((x_i,\ y_i)\\), and we want to know coefficients \\(a_k\\)

$$ \left[
 \begin{matrix}
 1 & x_0 & \dots & x_0^n \\
 1 & x_1 & \dots & x_1^n \\
 \vdots & \vdots & & \vdots \\
 1 & x_n & \dots & x_n^n
 \end{matrix}
 \right]
 \left[
 \begin{matrix}
 a_0 \\
 a_1 \\
 \vdots \\
 a_n
 \end{matrix}
 \right] = 
 \left[
 \begin{matrix}
 y_0 \\
 y_1 \\
 \vdots \\
 y_n
 \end{matrix}
 \right] $$

**Theorem** There exists a unique interpolating polynomial \\(P(x)\\) of degree \\(\le n\\) on a set of \\((n+1)\\) distinct points. 

## Lagrangian Interpolation

The interpolation polynomial in the Lagrange form

$$ L(x) := \sum_{k = 0}^n y_k l_k(x) $$

is a *linear combination* of Lagrange basis polynomials

$$ l_k(x) := \prod_{0 \le m \le n \atop m \ne k}\frac{x - x_m}{x_k - x_m} $$

\\(\prod_{0 \le m \le n \atop m \ne k}(x - x_m)\\) makes \\(l_k(x) = 0\\) when \\(x \ne x_k\\)

![lagrangian interpolation](/static/imgs/Lagrange_polynomial.svg.png)

**Define**

$$ \omega_{n+1}(x)=(x-x_0)(x-x_1)\dots(x-x_n). $$

then

$$ \omega_{n+1}^{\prime}(x_k)=(x_k-x_0)\dots(x_k-x_{k-1})(x_k-x_{k+1})\dots(x_k-x_n). $$

### Remainder

$$ R_n(x)=f(x)-L_n(x)=\frac{f^{n+1}(\xi)}{(n+1)!}\omega_{n+1}(x) $$

The remainder can <mark>be bound as</mark>

$$ |R_n(x)|\le\frac{\max_{x_0\le\xi\le x_n}|f^{n+1}(\xi)|}{(n+1)!}|\omega_{n+1}(x)| $$

$$ \left( |\omega_{n+1}(x)|\le (x_n-x_0)^{n+1},\ x_0\le x_1\le\dots\le x_n \right) $$

*Notice* that \\(n+1\\) is the number of points.

## Newton Polynomial

**Definition** Given data points as a function \\(f\\)

$$(x_0, f(x_0)), ..., (x_k, f(x_k)) $$

the *forward* **divided differences**(均差) are defined as:

$$ f[x_k] := f(x_k) $$

$$ f[x_{i},\ ...,\ x_{i+j}]:=\frac{f[x_{i+1},\ ...,\ x_{i+j}]-f[x_{i},\ ...,\ x_{i+j-1}]}{x_{i+j}-x_{i}} $$

$$ \scriptstyle i \in \{0,\ ...,\ k-j\},\ j \in \{1,\ ...,\ k\}. $$

---

The interpolation polynomial in the Newton form can be written as

$$ N(x) = f[x_0]+f[x_0,\ x_1](x-x_0)+\dots+f[x_0,\ x_1,\dots,\ x_n](x-x_0)\dots(x-x_{n-1}). $$

$$ R_n(x)=f(x)-N_n(x)=f[x,\ ,x_0,\ \dots,\ x_n]\omega_{n+1}(x) $$

*Newton polynomial can be easily recalculated when new data points come*

### Interpolation at Equal Intervals (\\(x_k=x_0+kh\\))

**Finite difference**(差分)

Assume that \\(f_k=f(x_k)\\), then \\(\Delta^n f_k=\Delta^{n-1}f_{k+1}-\Delta^{n-1}f_{k}\\).

牛顿前插公式：

$$ P_n(x_0+th)=f_0+t\Delta f_0+\frac{t(t-1)}{2!}\Delta^2f_0+\dots+\frac{t(t-1)\dots(t-n+1)}{n!}\Delta^nf_0 $$

$$ R_n(x)=\frac{t(t-1)\dots(t-n)}{(n+1)!}h^{n+1}f^{n+1}(\xi),\ \xi\in(x_0,x_n). $$

## Hermite Interpolation

实际上泰勒插值是牛顿插值的极限形式

Hermite interpolation matches an unknown function both in observed value, and the observed value of its first \\(m\\) *derivatives*.

(Textbook)

-----

<mark>分段低次插值</mark>

**Runge's phenomenon**

## Spline Interpolation

In mathematics, a *spline* is a numeric function that is piecewise-defined by polynomial functions, and which possesses a high degree of smoothness at the places where the polynomial pieces connect (which are known as knots).

In interpolating problems, spline interpolation is often preferred to polynomial interpolation because it yields similar results to interpolating with higher degree polynomials while avoiding instability due to **Runge's phenomenon**.

The most commonly used splines are *cubic splines*.

Besides the definition of cubic splines, we need another 2 equations in order to obtain the form of \\(S(x)\\)

Three types of boundary conditions

## 数值分析46页，评注

# Chapter 4 Numerical Differentiation, Numerical Quadrature and Summation

## Numerical Differentiation

Algorithms for estimating the *derivative* of a mathematical function using *values of the function* (and perhaps other knowledge about the function).

e.g.

$$ f^{\prime}(a)\approx G(h)=\frac{f(a+h)-f(a-h)}{2h} $$

with Taylor expansions

$$ G(h)=f^{\prime}(a)+\frac{h^2}{3!}f^{\prime\prime\prime}(a)+\frac{h^4}{5!}f^{(5)}(a)+\dots $$

Truncation error: ...

Roundoff error:

$$ |f^{\prime}(a)-G(h)|\le\frac{|\varepsilon_1|+|\varepsilon_2|}{2h}=\frac{\varepsilon}{h} $$

### Richardson Extrapolation

$$ T_m(h)=\frac{4^m G_{m-1}(\frac{h}{2})-G_{m-1}(h)}{4^m -1},\ m=1,\ 2,\ \dots $$

## Numerical Quadrature: The General Problem

$$ \int_a^b f(x)\mathrm{d}x\approx\sum_{k=0}^n A_kf(x_k) $$

**代数精度** 如果某个求积公式对于次数不超过\\(m\\)的多项式均能准确成立，但对于\\(m+1\\)次多项式就不准确成立，则称该求积公式具有\\(m\\)次代数精度

### Interpolation Quadrature Formula

### Residue

### Convergence and Stability

## Newton-Cotes Quadrature Formulas

## Composite Quadrature Formulas

## Gaussian Quadrature

# Chapter 6 Functional Approximation: Least-Squares Techniques

中文教材第3章 函数逼近与快速傅里叶变换

## 3.1 函数逼近的基本概念

**空间**：具有某种关系/“空间结构”的*集合*，**线性相关/无关**，**基**，**坐标**

<hr class="quarter" />

**范数** 3个条件（正定性，齐次性，三角不等式）（是向量长度概念的直接推广）

**赋范线性空间** 线性空间与范数一起

**\\(\infty\\)-范数**或**最大范数**，**1-范数**，**2-范数**

<hr class="quarter" />

数域\\(X\\)上的**内积** 4个条件

**内积空间** 定义了内积的线性空间

**共轭**，**正交** 内积为0，是向量相互垂直概念的推广

**柯西-施瓦兹不等式**

$$ |(u,v)^2|\le(u,u)(v,v) $$

**格拉姆（Gram）矩阵** (...)

某区间上，**权函数** 2个条件

带权的内积和范数

$$ (f(x),g(x))=\int_a^b\rho(x)f(x)g(x)\ \mathrm{d}x. $$

$$ ||f(x)||_2^2=(f(x),f(x))^{\frac{1}{2}}=\left[\int_a^b\rho(x)f^2(x)\ \mathrm{d}x\right]^{\frac{1}{2}}. $$

<hr class="quarter" />

**最佳逼近多项式** 给定\\(f(x)\in C[a,b]\\)，若\\(P^*(x)\in H_n\\)使误差

$$ ||f(x)-P^*(x)||=\min_{P\in H_n}||f(x)-P(x)|| $$

则称\\(P^{*}(x)\\)是\\(f(x)\\)在\\([a,b]\\)上的<mark>最佳逼近多项式</mark>

范数取*最大范数*时为**最优一致逼近**  
范数取*2-范数*时为**最佳平方逼近**

若\\(f(x)\\)是\\([a,b]\\)上的一个列表函数（即给出的是若干\\(f(x_i)\\)的值），可求**最小二乘拟合**

## 3.2 正交多项式

\\(f(x)\\)，\\(g(x)\\)*带权\\(\rho(x)\\)正交*

某区间上，带权\\(\rho(x)\\)的**正交函数族**（与除自己之外的函数带权正交），**标准正交函数族**（与自己带权内积恒等于1）

e.g. 三角函数族是\\([-\pi,\pi]\\)上的正交函数族

某区间上，带权的**n次正交多项式**

**正交化** Gram-Schmidt Orthogonaliztion

$$ \varphi_0=1 $$

$$ \varphi_n=x^n-\frac{(x^n,\varphi_0)}{(\varphi_0,\varphi_0)}\varphi_0-\frac{(x^n,\varphi_1)}{(\varphi_1,\varphi_1)}\varphi_1-\dots-\frac{(x^n,\varphi_{n-1})}{(\varphi_{n-1},\varphi_{n-1})}\varphi_{n-1} $$

<hr class="quarter" />

**勒让德多项式** 当区间为\\([-1,1]\\)，权函数\\(\rho(x)\equiv 1\\)时，由\\({1,x,\dots,x^n,\dots}\\)正交化得到的的多项式

3个性质：

- 正交性
- 奇偶性 n为偶数时是偶函数，奇数时是奇函数
- 递推关系

$$ (n+1)\mathrm{P}_{n+1}(x)=(2n+1)x\mathrm{P}_{n}(x)-n\mathrm{P}_{n-1}(x),\ n=1,2,\dots. $$

<hr class="quarter" />

**切比雪夫多项式**

## 3.3 最佳平方逼近

**法方程** 假设\\(S(x)=\sum_{j=0}^n a_j\varphi_j(x)\\)，相当于求\\(a_0,a_1,\dots,a_n\\)使得\\(\int_a^b\rho(x)\left[\sum_{j=0}^na_j\varphi_j(x)-f(x)\right]^2\ \mathrm{d}x\\)取得最小值，作微分即有

$$ \sum_{j=0}^n(\varphi_k(x),\varphi_j(x))a_j=(f(x),\varphi_k(x)),\ k=0,1,\dots,n. $$

即关于\\(a_0,a_1,\dots,a_n\\)的线性方程组。

最佳平方逼近的*误差*

若取\\(\varphi_k(x)=x^k\\)，\\(\rho(x)=1\\)，\\(f(x)\in C[0,1]\\)，

$$ H\vec{a}=\vec{d} $$

称\\(H\\)为希尔伯特矩阵

当n较大时直接求解法方程是相当困难的，通常是采用正交多项式作基

<hr class="quarter" />

用正交函数组作最佳平方逼近

## 3.4 曲线拟合的最小二乘法

## 3.5 有理逼近
