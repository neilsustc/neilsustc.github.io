---
layout: hiddenpage
title: Notes - Operating System
---

Last modified: 2016-05-05  
[Edit on GitHub](https://github.com/neilsustc/Notes/blob/master/2016%20Spring/Operating%20system.md)

---

<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

## Contents

- Part 1 Overview
  - [1 Introduction](#introduction)
  - [2 Operating-System Structures](#operating-system-structures)
- Part 2 Process Management
  - [3 Processes](#processes)
    - [Process Concept](#process-concept)
    - [Process Scheduling](#process-scheduling)
    - [Operations on Processes](#operations-on-processes)
    - [Interprocess Communication](#interprocess-communication)
  - [4 Threads](#threads)
  - [5 Process Synchronization](#process-synchronization)

# 1 Introduction

Operating system: a *program* that acts as an *intermediary* between <mark>a user</mark> of a computer and the <mark>computer hardware</mark>

Four components of a computer system: *hardware* (CPU, memory, I/O devices, etc.), *operating system*, *application programs*, *users*

From the computer's point of view, OS is a *resource allocator* (for hardware) and a *control program* (for application programs)

"The one program running at all times on the computer" is the **kernel**, everything alse is either a system program or an application program

**bootstrap program** initial program loaded at power-up or reboot

**interrupt**, modern operating systems are *interrupt driven*

interrupt handling: polling, interrupt vertor

storage, cache

direct memory access ???

multiprocessor system

clustered system

**Multiprogramming**: switch to another job when a job needs to wait

**Multitasking**(or **Time sharing**): frequently switch among multiple jobs (a logical extension of multiprogramming)

Time sharing requires *response time* to be short

scheduling; swapping, virtual memory

## Dual-Mode and Multimode Operation

user mode, kernel mode; mode bit, privileged instructions

virtual machine manager

timer

## Process/Memory/Storage Management

## Computing Environments

- Traditional
- Mobile
- Distributed (network operating system)
- Client-Server
- Peer-to-Peer (another model of distributed system)
- Virtualization (emulation, interpretation)
- Cloud (types: public, private, hybrid, SaaS, PaaS, IaaS)
- Real-Time embedded (fixed time constraints)

# 2 Operating-System Structures

<div class="image-wrapper">
    <img src="/static/imgs/os-services.png" alt="OS services"/>
    <p class="image-caption">A view of OS services</p>
</div>

## System Calls

Parameter passing:

- register
- address of a block(array, table...)
- stack

## Types of System Calls

- Process control
- File Management
- Device management
- Information matainance (`time()`, `date()`, `dump()`...)
- Communication
- Protection

## System Programs

# 3 Processes

## 3.1 Process Concept

A **process** is an instance of a computer program that is *being executed*. (from wiki)

- stack
- heap
- data section
- text section (program code)

<div class="image-wrapper">
    <img src="/static/imgs/process-state.png" alt="process state"/>
    <p class="image-caption">Diagram of process state</p>
</div>

Process control block(**PCB**): a data structure containing the information needed to manage a particular process

- process state
- process number
- program counter
- CPU registers
- CPU scheduling info
- ...

Threads -> next chapter

## 3.2 Process Scheduling

Objective: maximize CPU utilization; quickly switch processes onto CPU for time sharing

**Scheduling queues**: job queue, ready queue, device queue

**Scheduler**:

- long-term(job): selects processes to be loaded into memory
- short-term(CPU): selects process to be executed next (from ready queue) and allocates CPU
- medium-term(swapping): move processes bewteen memory and storage(? e.g. disc)

**Context switch**

Context of a process represented in the PCB

## 3.3 Operations on Processes

### Creation

process identifier(pid)

List processes by using the `ps` command (Unix)

- `fork()` creates a new process
- `exec()` loads a binary file into memory and starts its execution
- `wait()` the parent call this to move itself off the ready queue until the termination of the child

Both processes (the parent and the child) continue execution at the instruction after the `fork()`, with one difference: the return code for the `fork()` is zero for the new (child) process, whereas the (nonzero) process identifier of the child is returned to the parent. (the parent need to know the identities of its children)

### Termination

**Cascading termination**: if a process terminates, then all its children must also be terminated (in some systems)

process table

`exit()` a parameter could be provided as exit status

If the parent don't invoke `wait()`, the *child* is

- **zombie**: child process terminated
- **orphans**: parent process terminated

## 3.4 Interprocess Communication

interprocess communication(IPC)

2 models:

- shared memory
- message passing

e.g. producer-consumer problem

### Shared Memory

### Message Passing

A message-passing facility provides at least two operations: send, receive

If processes P and Q want to communicate, a *communication link* must exist between them. This link can be implemented in a variety of ways.

direct (using name), indirect (using mailbox)

syn, asyn

buffering (capacity of the link, 0, finite or infinite)

## Communication in Client-Server Systems

- Sockets
- Remote Procedure Calls
- Pipes ???

# 4 Threads

Benefits of multithreaded programming:

- Responsiveness (may allow continued execution if part of process is blocked, especially important for user interfaces)
- Resource sharing (threads share resources of process, easier than IPC)
- Economy (cheaper than process creation, thread switching lower overhead than context switching)
- Scalability (process can take advantage of multiprocessor architectures)

## 4.2 Multicore Programming

- parallelism (perform more than one tack simultaneously)
- concurrency (support more than one task by allowing all the tasks to make progress, e.g. scheduler on single processor)

**Amdahl's Law**:

$$ speedup \le \frac{1}{S+\frac{1-S}{N}} $$

- \\(S\\) - portion of the application that must be performed serially
- \\(N\\) - number of processing cores

Hardware support: multiple threads can be loaded into one core for fast switching

## 4.3 Multithreading Models

between user threads and kernal threads ...

## 4.4 Thread Libraries

## 4.5 Implicit Threading

Thread pools, OpenMP and Grand Central Dispatch

## 4.6 Threading Issues

### `fork()` and `exec()` in Multithreaded Programs

Does the new process duplicate all threads, or just the one who invoked the `fork()` system call?

Some UNIX systems have chosen to have two versions of `fork()`.

`exec()` works in the same way as described in Chapter 3. That is, the program loaded will replace the entire process - including all threads.

### Signal Handling

???

# 5 Process Synchronization

*Concurrent access* to shared data may result in *data inconsistency*.

e.g. producer-consumer problem

race condition: the outcome of the execution depends on the particular order in which the access takes place

## 5.2 The Critical-Section Problem

entry section, **critical section**, exit section, remainder section

critical section: the process may be changing common variables, updating a table, writing a file, and so on.

no two processes are executing in their critical sections at the same time

requirements of a solution to the critical-section problem:

- Mutuual exclusion
- Progress
- Bounded waiting

## 5.3 Peterson's Solution

???

## 

lock, test_and_set, compare_and_swap

## 5.6 Semaphores

more robust

...
