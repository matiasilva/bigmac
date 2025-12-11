# Introduction

Hardware design is in vogue. If the 2010s were about bringing us great software
and cloud, then the 2020s are firmly about the lower layer of the stack, the
bare metal. Semiconductor companies like NVIDIA, Intel, and AMD continue to push
the limits of technological innovation in the world of AI, spurred on by massive
memory and compute demands.

Make no mistake, these are not software companies. According to some, software
engineers will evolve to become AI supervisors, merely inspecting and validating
the output of AI agents. Hardware engineers on the other hand must understand
Physics, Computer Architecture and Electronics to create — this set of skills
can never be replaced, only augmented.

## Course objective

The object of this course is to use neural network inference as a vehicle to
learn about chip design. The end goal is a fully functional FPGA-based inference
engine that can accelerate, in essence, matrix multiplication. This should set
you on a good path to understanding the fundamental hardware requirements and
constraints of artificial intelligence computations.

## Learning outcomes

- Understand the tradeoffs involved in hardware design
- Understand the interaction between the layers of abstraction in computer
  architecture
- Improve skills in PYthon, C and SystemVerilog
- Gain hands-on experience with FPGAs, HDLs and Python-based verification
- Gain intuition about machine learning computation and the mathematical
  operations underpinning them

## Deliverable

You will build an inference accelerator on an FPGA. Inference is the process of
extracting useful output from a pre-trained neural network, given a set of
inputs. This process can be slow and consumes wasteful compute power when run on
a CPU. Using FPGAs, we can build hardware accelerators that are custom tailored
to this particular type of computation.

Your neural network will be a digit classifier. This is the equivalent of ‘Hello
World’ in the AI world. A digit classifier takes an image as an input and
outputs 10 numbers, each representing a probability that the image corresponds
to a particular number.

## Useful links

* https://course.fast.ai/Lessons/lesson8.html
* https://www.deeplearningbook.org/lecture_slides.html
* http://neuralnetworksanddeeplearning.com/chap6.html
* https://distill.pub/
* https://colah.github.io/
* 3B1B
