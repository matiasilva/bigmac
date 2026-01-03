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
