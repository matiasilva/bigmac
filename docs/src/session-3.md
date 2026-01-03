# Session 3: Circuit design and HDLs

## Homework

Valid solutions must be fully justified.

1. This question is about a sequential and combinational logic circuit.

<p style="text-align:center"><img style="max-width: 80%" src="s3-hw1.png"></p>

> 1. Write out the truth table for the dashed area, using intermediate variables
>    as required.
> 1. Construct a digital timing diagram for the output `o` spanning a total of
>    10 cycles given the following information about the inputs:
>    - A is low for the first half and high on the second half of time.
>    - B toggles every cycle (1 -> 0 -> 1 -> ...).
>    - C is high for all time except on cycles 3 and 4.
> 1. Write valid HDL to model the circuit
> 1. Use a testbench to prove that your answer to part 2 is correct.

---

2. This question is about Boolean expressions and Karnaugh maps

Consider the design of a warning light system that alerts a car user to check
their engine. The design requirement is as follows:

A warning light should turn on when:

- The engine is running (A) and oil pressure is low (B), OR
- The engine is running (A) and temperature is high (C), OR
- Both oil pressure is low (B) and temperature is high (C)

> 1. Express the requirement as a Boolean expression.
> 1. Produce the circuit diagram that correctly turns on the light, using
>    Karnaugh maps or otherwise.

---

3. This question is about SystemVerilog.

You are tasked with designing a 4-bit counter that can count up or down,
controlled by two corresponding inputs. You should use the skeleton below to
guide your answer.

```verilog
module simple_counter (
    input  logic       clk,
    input  logic       rst_n,
    input  logic       count_up,
    input  logic       count_down,
    output logic [3:0] count
);

  // YOUR CODE HERE!

endmodule
```

> 1. Add sequential logic that achieves the desired functionality.
> 2. Extend the code to output a signal when the counter has overflowed.
> 3. Use a full adder to draw a circuit diagram for your answer to 1.

---

4. This question is about synchronous circuit design.

> [!NOTE]
>
> Answers to this question will count towards session 2 credits.

You are tasked with creating a 3-bit Gray code counter with T flip-flops and
some combinational logic.

A T flip-flop is a different kind of flop to the D-flop we've been introduced to
so far. It has a toggling output when its input is 1 and holds its previous
output when the input is 0. This property makes it very useful for counter
design.

Gray code is a number scheme in which consecutive numbers differ by only one
bit. The full 3 bit Gray code sequence is available below:

```
000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100 -> 000
```

> 1. Write down the number of T-flops required to represent a 3-bit Gray code
>    value.
> 1. Produce the excitation table for the T flip-flop.
>
> An excitation table contains the minimum inputs required to generate the next
> state given a current state. The three columns should be, in order, `Q`,
> `Q_next` and `T`, where `T` is the input to the T-flop.
>
> 1. Determine the inputs required to the T-flops to achieve the state
>    transitions required by the Gray code sequence
> 1. Using K-maps or otherwise, determine the combinational logic circuits
>    required to generate the correct T-flop inputs
> 1. Draw out the final circuit you have designed

Hint: think of the output of the T-flops as representing the current state. The
inputs to the T-flops are determined by the state.
