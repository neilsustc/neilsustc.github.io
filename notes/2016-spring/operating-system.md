---
layout: hiddenpage
title: Notes - Operating System
---

Last modified: 2016-04-25  
[Edit on GitHub](https://github.com/neilsustc/Notes/blob/master/2016%20Spring/Operating%20system.md)

---

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

## Contents

- [Part 1 Overview](#overview)
  - [1 Introduction](#introduction)
  - [2 Operating-System Structures](#operating-system-structures)
- [Part 2 Process Management](#process-management)
  - [3 Processes](#processes)
    - [Process Concept](#process-concept)
    - [Process Scheduling](#process-scheduling)
    - [Operations on Processes](#operations-on-processes)
    - [Interprocess Communication](#interprocess-communication)
  - [4 Threads](#threads)
  - [5 Process Synchronization](#process-synchronization)

# Overview

## 1 Introduction

Operating system: a *program* that acts as an *intermediary* between a user of a computer and the computer hardware
  
Four components of a computer system: hardware, operating system, application programs, users  

From the computer's point of view, OS is a *resource allocator* and a *control program*
  
"The one program running at all times on the computer" is the **kernel**

## 2 Operating-System Structures

# Process Management

## 3 Processes

### 3.1 Process Concept

A **process** is an instance of a computer program that is being executed. (from wiki)

Process state

![process state](/static/imgs/process_state.png)

Process control block(PCB): a data structure containing the information needed to manage a particular process

### 3.2 Process Scheduling

Objective: maximize CPU utilization; quickly switch processes onto CPU for time sharing

**Scheduling queues**

**Scheduler**: long-term(job), short-term(CPU), medium-term(swapping)

Context switch

### 3.3 Operations on Processes

*Creation*:

List processes by using the `ps` command (Unix)

- `fork()` creates a new process
- `exec()` loads a binary file into memory and starts its execution
- `wait()` the parent call this to move itself off the ready queue until the termination of the child

Both processes (the parent and the child) continue execution at the instruction after the `fork()`, with one difference: the return code for the `fork()` is zero for the new (child) process, whereas the (nonzero) process identifier of the child is returned to the parent. (the parent need to know the identities of its children)

*Termination*:

**Cascading termination**: if a process terminates, then all its children must also be terminated (in some systems)

process table

`exit()`

If the parent don't invoke `wait()`, the child is

- **zombie**: child process terminated
- **orphans**: parent process terminated

### 3.4 Interprocess Communication

interprocess communication(IPC)

2 models:

- shared memory
- message passing

...

## 4 Threads

### 4.2 Multicore Programming

- parallelism (perform more than one tack simultaneously)
- concurrency (support more than one task by allowing all the tasks to make progress, e.g. scheduler on single processor)

**Amdahl's Law**:

$$ speedup \le \frac{1}{S+\frac{1-S}{N}} $$

- \\(S\\) - portion of the application that must be performed serially
- \\(N\\) - number of processing cores

Hardware support: multiple threads can be loaded into one core for fast switching

### 4.3 Multithreading Models

between user threads and kernal threads

- many-to-one
- one-to-one
- many-to-many

### 4.4 Thread Libraries

### 4.5 Implicit Threading

Thread pools, OpenMP and Grand Central Dispatch

### 4.6 Threading Issues

## 5 Process Synchronization

Concurrent access to shared data may result in data inconsistency.

producer-consumer problem

race condition

### The Critical-Section Problem

entry section, **critical section**, exit section, remainder section


