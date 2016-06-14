---
layout: hiddenpage
title: Notes - Computer Organization
---

Last modified: 2016-04-25  
[Edit on GitHub](https://github.com/neilsustc/Notes/blob/master/2016%20Spring/Computer%20organization.md)

---

Textbook: Computer Organization and Design - The Hardware/Software Interface 5th ed.

- Lecture 2: 1.6-1.11
- Lecture 3: 2.1-2.5
- Lecture 4: 2.6-2.8
- Lecture 5: 2.9-2.16
- Lecture 6: 3.1-3.4
- Lecture 7: 3.5-3.8
- Lecture 8: 4.1-4.3
- Lecture 9: 4.4-4.8

# Contents

- [1 Computer Abstractions and Technology](#computer-abstractions-and-technology)
  - [1.6 Performance](#performance)
  - [1.7 The Power Wall](#the-power-wall)
- [2 Instructions: Language of the Computer](#instructions-language-of-the-computer)
  - [2.1 Introduction](#introduction)
  - [2.2/2.3 Operations/Operands of the Computer Hardware](#operations-operands-of-the-computer-hardware)
  - [2.4 Signed and Unsigned Numbers](#signed-and-unsigned-numbers)
  - [2.5 Representing Instruction in the Computer](#representing-instruction-in-the-computer)
  - [2.6 Logic Operations](#logic-operations)
  - [2.7 Instrctions for Making Decisions](#instructions-for-making-decisions)
  - [2.8 Supporting Procedures in Computer Hardware](#supporting-procedures-in-computer-hardware)
  - 2.9 Communicating with People (representation of characters)
  - [2.10 MIPS Addressing for 32-bit Immediates and Addresses](#mips-addressing-for-32-bit-immediates-and-addresses)
  - ...
  - 2.13 A C Sort Example to Pull It All Together (Page 132)
  - ...
- [3 Arithmetic for Computers](arithmetic-for-computers)
  - [3.2 Addition and Subtraction](#addition-and-subtraction)
  - [3.3 Multiplication](#multiplication)
  - [3.4 Division](#division)
  - [3.5 Floating Point](#floating-point)
- [4 The Processor](#the-processor)

-----

# 1 Computer Abstractions and Technology

## 1.6 Performance

- **Response time** Also called **execution time**. The total time required for the computer to complete a task, including disk accesses, memory accesses, I/O activities, operating system overhead, CPU execution time, and so on.
- **CPU execution time** or simply **CPU time**, which recognizes this distinction, is the time the CPU spends computing for this task and does not include time spent waiting for I/O or running other programs.
- **Clock cycle**. Almost all computers are constructed using a clock that determines when events take place in the hardware. These discrete time intervals are called clock cycles.
- **Clock period**. The length of each clock cycle.
- **CPI**. Clock cucles per instruction

some equations:

    CPU Time = CPUClockCycles * ClockPeriod = CPUClockCycles / ClockRate  
    ClockCycles = InstructionCount * CyclePerInstruction(CPI)

If different instructions have different CPI, average CPI is affected by *instruction mix*.

## 1.7 The Power Wall

In CMOS IC technology

    Power ∝ 1/2 * CapacitiveLoad * Voltage ^ 2 * FrequencySwitched

*cost/performance trade-off*. In the PostPC Era the really critical resource is energy.

# 2 Instructions: Language of the Computer

## 2.1 Introduction

ISA - instruction set architecture

We will use **MIPS** as an example

Design principles:

- Simplicity favors regularity
- Smaller is faster
- Good design demands good compromises
- (Make the common case fast)

## 2.2/2.3 Operations/Operands of the Computer Hardware

![MIPS](/static/imgs/MIPS-opnds-oprs.png)

Register vs. Memory

The MIPS ISA has 32 registers (x86 has 8 registers)

## 2.4 Signed and Unsigned Numbers

base b expansion

least/most significant bit

**2's complement representation** has the advantage that all negative numbers have a 1 in the most siginificant bit.

**sign extension**

2 useful shortcuts working with 2's complement numbers:

- negation shortcut (a quick way to negate a 2's complement binary number)
  invert every bit (0 to 1, 1 to 0), add one to the result.
- sign extension shortcut
  take the sign bit(msb) from the small quantity and *replicate* it to fill the new bits of the barfer quantity.
  0010 -> 0000 0010
  1110 -> 1111 1110

## 2.5 Representing Instruction in the Computer

MIPS: R-type/format (for register), I-type (for immediate) and J-type (jump?)

## 2.6 Logic Operations

shift left/right, AND, OR, NOT

## 2.7 Instrctions for Making Decisions

`beq`, `bne`

`slt`(set on less than), `slti`

`j`, `jr` (unconditional)

## 2.8 Supporting Procedures in Computer Hardware

**procedure** (in other words, function in programming)

jump-and-link instrction `jal`: jump to an address and <mark>simultaneously save</mark> the `PC + 4`(the addr of the following instruction) to `$ra`(return addr)

Steps (naive version):

1. put parameters in `$a0-$a3`
2. `jal ProcedureAddr`
3. (perform procedure)
4. place the results in `$v0`, `$v1`
5. `jr $ra`

### Using More Registers

Any registers <mark>needed by the caller</mark> must be *restored* to the values that they contained before the procedure was invoked.

Stack pointer `$sp`. (By histoical precedent, stacks *"grow"* from higher addresses to lower addresses. *Adding* to the stack pointer *shrinks* the stack)

### Nested Procedures

Suppose that main program calls procedure A (`li $a0, 3`, `jal A`), A calls B (`li $a0, 7`, `jal B`). Since A <mark>hasn't finished its tasks</mark> yet, there is a conflict over the use of `$a0`, so does `$ra`.

One solution is to push all the other registers that must be preserved onto the stack.

Steps:

1. save relavent registers onto the stack (e.g. `addi $sp, $sp, -8`, `sw $ra, 4($sp)`, `sw $a0, 0($sp)`)
2. put parameters in `$a0-$a3`
3. `jal ProcedureAddr`
4. (perform procedure)
5. restore relavent registers from the stack if it is needed (e.g. if another procedure is called)
6. place the results in `$v0`, `$v1`
7. `jr $ra`

Key points (in my view):

- 1-3: caller; 4-7: callee
- Storing register is needed if the function is not *leaf* function
- Not all labels mean functions

### Saving Conventions

- caller saved: `$ra`, `$a0-a3`, `$t0-t9`(if you care)
- callee saved: `$s0-s7`    ???

**Example** Factorial (my implementation)

    .data
    strWelcome: .asciiz "Please input n (n >= 0) (close your IME): "

    .text
    main:
        la      $a0, strWelcome
        li      $v0, 4
        syscall                 # show tips
        li      $v0, 5
        syscall                 # read n
        move    $a0, $v0
        jal     factorial       # call factorial(n)
        move    $a0, $v0
        li      $v0, 1
        syscall                 # print n!
        j       Exit
    factorial:
        blt     $a0, $0, main   # n < 0
        bne     $a0, 0, NotZero # n != 0
        li      $v0, 1
        jr      $ra
    NotZero:
        addi    $sp, $sp, -8    # store $ra, $a0
        sw      $ra, 4($sp)
        sw      $a0, 0($sp)
        addi    $a0, $a0, -1
        jal     factorial       # call factorial(n-1)
        lw      $ra, 4($sp)     # restore
        lw      $a0, 0($sp)
        addi    $sp, $sp, 8
        mul     $v0, $a0, $v0   # n * factorial(n-1)
        jr      $ra
    Exit:
        li      $v0, 10
        syscall

- I use <mark>lowercase label</mark> to denote *function*(or *procedure*).
- It is slightly different from the code given in the textbook. In textbook, `sw`(the code block used to store registers onto the stack) is placed in the very front of the function `factorial`. I place it just before where another procedure is going to be called.

### Allocating Space for New Data on the Stack

Stack is also used to store variables that are local to the procedure.

`$fp` point to the first word of the frame of a procedure. (**procedure frame** the segment of the stack containing a procedure's saved registers and local vars)

We've been avoiding using `$fp` by avoiding changes to the `$sp` within a procedure.

### Allocating Space for New Data on the heap

![Memory allocation](/static/imgs/MIPS-memory-allocation.png)

## 2.10 MIPS Addressing for 32-bit Immediates and Addresses

### 32-Bit Immediate Operands

MIPS instructions are 32 bits long

32-bit constants, `lui`(*load upper immediate*; specifically to set the upper 16 bits of a constant in a register), `ori`

### Addressing in Branches and Jumps

The *conditional branch* instruction must specify two operands in addition to the branch addr, leaving only 16 bits for the branch addr.

Solution: *PC-relative addressing*

*Branch Far Away* If branch target is too far to encode with 16-bit offset, assembler rewrites the code

    beq $s0, $s1, L1
    =>
    bne $s0, $s1, L2
    j   L1
    L2:

### Summary

<div class="image-wrapper">
    <img src="/static/imgs/MIPS-addressing-modes.png" alt="MIPS addressing mode summary"/>
    <p class="image-caption">MIPS addressing mode summary</p>
</div>

## 2.13 A C Sort Example to Pull It All Together

Textbook, page 132

# 3 Arithmetic for Computers

## 3.2 Addition and Subtraction

Overflow conditions for addition and subtraction (4 cases)

`lbu`, `lhu`, `lb`, `lh`, `sb`, `sh`

**Saturating operation** means that when a calculation overflows, the result is set to the largest positive number (or most negative number), rather than a modulo calculation as in 2's complement arithmetic.

## 3.3 Multiplication

    Multiplicand       1000
    Multiplier         1001
                      -----
                       1000
                      0000
                     0000
                    1000
                   --------
    Product         1001000

Multiplication hardware simply *shift* and *add*.

Signed multiplication: first convert the two operands to positive numbers and then remember the original signs.

Faster multiplication: organize additions in parallel

`mult`, `multu`, `mflo`, `mfhi` (MIPS provides a separate pair of 32-bit registers to contain 64-bit product, called *Hi* and *Lo*)

## 3.4 Division

                       1001  Quotient
                  ---------
    Divisior 1000 | 1001010  Dividend
                    1000
                   -----
                       10
                       101
                       1010
                      -----
                         10  Remainder

Signed division: ...; conventionally, the dividend an remainder must have the same signs.

Faster division: (to be edited...); We accelerate division by predicting multiple quotient bits and then correcting mispredictions later.

`div`, `divu`

## 3.5 Floating Point

**scientific notation**, **normalized number**

### Floating-Point Representation

fraction, exponent

In general, floating-point numbers are of the form (-1)<sup>S</sup>×F×2<sup>E</sup>, and also could be of other form (-1)<sup>S</sup>×(1+F)×2<sup>(E-Bias)</sup> (IEEE 754 standard, making comparisons easier, ensuring exponent is unsigned)

| **precise** | **sign/exponent/fraction** | **Bias** |
| single | 1/8/23 | 127 |
| double | 1/11/52 | 1023 |

### Floating-Point Addition/Multiplication

(to be edited...)

# 4 The Processor

## 4.1 Introduction

Chapter 1 explains that the performance of a computer is determined by three key factors: *instrcution count*, *clock per instruction*(CPI), and *clock cycle time*.

Chapter 2 explains that the instruction set architecture determine the *instruction count* required for a given program.

The implementation of the processor determines both the *clock cycle time* and *CPI*.

We will examine two MIPS implementations

- a simplified version
- a more realistic pipelined version

### A Basic MIPS Implementation

(abbreviating *instruction* with *inst*)

- memory-reference insts (`lw`, `sw`)
- arithmetic-logical insts (`add`, `sub`, `AND`, `OR`, `slt`)
- branch and jump insts (`beq`, `j`)

For every inst, the first two steps are identical:

1. using the *program counter*(PC) to fetch the inst from memory
2. read one or two registers, using fields of the inst to select the registers to read

<div class="image-wrapper">
    <img src="/static/imgs/abstract-view-of-impl-MIPS.png" alt="An abstract view of the implementation of the MIPS subset"/>
    <p class="image-caption">An abstract view of the implementation of the MIPS subset</p>
</div>

<div class="image-wrapper">
    <img src="/static/imgs/basic-impl-of-MIPS.png" alt="A basic implementation of the MIPS subset"/>
    <p class="image-caption">A basic implementation of the MIPS subset</p>
</div>

## 4.2 Logic Design Conventions

组合逻辑电路(ALU etc.)，时序逻辑电路(register, memory etc.)

### Clocking Methodology

**Clocking methodology** The approach used to determine when data is valid and stable relative to the clock. A *clock methodology* defines when signals can be read and when they can be written.

## 4.3 Building a Datapath

Implementing R-type insts, lw/sw, J-type insts (some figures ...)

## 4.4 A Simple Implementation Scheme

## 4.5

-------

[MIPS Quick Tutorial](http://logos.cs.uic.edu/366/notes/mips%20quick%20tutorial.htm)

## Lab 1

Directives .data and .text

## Lab 2 Familiarization with MIPS32 Assembly Language

Register names and descriptions

Delayed load/branch ?

## Lab 3 Contorl Structures and *syscall* in MIPS

## Lab 4 MIPS Calling Convention

