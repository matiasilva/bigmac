# Session 4: Python-based verification

Our work in writing simple SystemVerilog testbenches has hopefully motivated the
need for a more robust, error-prone solution that treats verification for what
it is: a software problem. This session is therefore dedicated to introducing
Python-based verification as well as some basic methodologies for verifying
digital designs.

## Anatomy of a (co)simulation

SystemVerilog simulation is governed by a complex event loop with 19 separate
deltacycles that ... Recall that a simulator is just another C program running
on your machine and is thus capable of communicating with the outside world
through dedicated APIs and protocols. More specifically, simulators conform to a
set of standard functions for reading, writing and modifying data called PLI,
later GPI and DPI. You can invoke the simulator with compiled shared object
files and it is able to interoperate with code you've written elsewhere. This
concept is called co-simulation.

Combining compiled code in this way works well and is the premise for how
Verilator (an open source simulator) is meant to work. However, for
verification, especially for early stage prototyping, we'd like something more
dynamic and interactive that would massively speed up development cycles. The
solution here is to introduce an interpreted language with a host of helpful
properties: classes, a loose type system, and an intuitive REPL. One of the many
reasons why speed trumps efficiency in verification is that as chips become ever
more complex, the state space for tests increases exponentially and pouring time
into writing tests that run at near-native speed is a secondary concern to
covering more of that vastly large feature/bug space.

Of course, any use of DPI interfaces adds some overhead to each deltacycle,
since data must travel back and forth. By using an interpreted language like
Python, we're doubly increasing the overhead since Python must first invoke
dedicated C++ functions, called bindings, which themselves hook into DPI with
the simulator.

## On performance

Note that we're not _that_ concerned with performance for small designs since a)
suites of tests, called regressions, are often run overnight and are not
time-bound b) the productivity speedup and feature breadth for verification
afforded by Python is worth the penalty in performance.

For larger designs, it's worth re-thinking your approach either by profiling
your Python setup to eliminate the low hanging fruit, investing time into making
a non-cycle accurate C++ model of your hardware, writing C++ tests for lengthy
and complex tests with lots of DPI, using an emulation hardware stack, or even
FPGAs. While the plethora of options might seem like a recipe for decision
paralysis, each one comes with its own set of tradeoffs, adding to the beauty of
digital verification; it's a Swiss army knife of tools not a one stop shop.
