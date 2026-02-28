# Session 5: FPGAs

FPGAs are devices that implement programmable digital designs, allowing
designers to run their synthesized RTL at speeds that appear native compared to
simulation. They're immensely useful tools during the chip design process, both
before and after tape-out.

> [!NOTE]
>
> A note on FPGA terminology: the chip that contains the logic cells and
> programmable routing is referred to as the FPGA. However, these alone are of
> little practicality and must be mounted on a development board to be used. The
> development boards provide external interfaces like USB and SPI flash and are
> responsible for regulating power to the board as well as providing a crystal
> for clocking.
>
> This distinction is important; FPGA vendors rarely make their own dev boards
> and they have different concerns to the user of the FPGA dev board.

As with any circuit component, it's paramount to know what's inside in order to
best make use of its resources. Internally, FPGAs consist of a sea of look-up
tables (LUT), each representing some logic function like ‘x OR y AND z’ and some
programmable routing. A LUT is characterized by its number of inputs, so we say
4-LUT or 6-LUT to describe a 4 or 6 input look-up table. LUTs store the truth
table of a logic function and by chaining together LUTs in specific
arrangements, we can compute vastly large combinational and sequential logic.

Just like with regular ASICs, we use a hardware description language (HDL) like
SystemVerilog to can describe the behavior we want our FPGA to 'execute' and the
FPGA synthesis tool will convert this into thousands of logic functions, which
we can then program onto the LUTs in the FPGA. Note that execute is in quotation
marks, HDL cannot be 'run' in the same sense as code in C or Python can. The
FPGA is simply a target for our hardware implementation as are ASICs. ASICs are
the 'real deal'; they compute logic functions using logic gates, while FPGAs
compute logic functions by connecting together LUTs containing pre-computed
values representing our design that produce equivalent (nearly) behavior.

## The logic cell

There are a large number of FPGA varieties and families out there, each
targeting its own segment of the market. At their core, though, they all share a
good number of fundamental components, the most important of which is the logic
cell.

FPGAs contain logic cells in the many thousands and they're behind the "Gate
Array" of FPGA. A logic cell contains a LUT, a bypass mux and a D-flop.
Together, these components allow the logic cell to implement sequential or
combinational logic. The inputs to the LUT are pre-programmed and come from the
bitstream produced by the FPGA synthesis tool.

## The TangNano family
