# Session 7: Floating point

You may have heard the expression "we're only as good as our weakest link". It
turns out we can draw a direct parallel between this age-old adage and computer
architecture, more precisely that the slowest/least efficient part of a system
places an upper bound on its performance. It thus follows that if we're going to
optimize something, we ought to optimize the slowest thing.

## Motivation

One of these "slow things" in ASICs is floating point multiplication. This is an
interesting example of a type of computation that's relatively easy to calculate
for us humans but quite involved for computers. Most of this is due to
limitations imposed by a need to agree on a common standard for representing
decimals in binary (IEEE-754). What we gain in standardization we potentially
lost in optimization.

Floating point multipliers are logic-heavy, requiring a very large number of
adders, and slow, taking potentially multiple cycles to complete one operation.
They're such a common point of speedup that practically every CPU has a floating
point coprocessor and the gains to be had are significant! Since design of such
a multiplier is potentially a months-long endeavor, we're going to sidestep this
and instead perform all our multiplications with fixed-point numbers.

## Primer on floating point (IEEE-754)

Programmers first encounter floating point numbers when they either a) quite
literally see the word "float" in their C programs or b) try and spend hours
debugging why `1.5 + 1.5 != 3.0`.

## Fixed point

Train NN using TensorFlow/PyTorch Train Converge Accuracy > 95%

Load data, define model, train loop, evaluate. You'll also learn practical
things like batch sizes, learning rates, and overfitting

Stanford CS231N

Pipelining convolutions

Memory management

Convolution
