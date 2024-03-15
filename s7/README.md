
### Version 0 (Base Code)
-------------------------

**Target** 

Basic building block 


**Results** 

- Parameters: 13,952
- Best Train Accuracy: 98.24%
- Best Test Accuracy: 98.08%

**Analysis** 

- basic building block is working fine, 
- model seems to be overfit and 
- no. of parameters is more than 10,000

[Version 0 - Code](https://github.com/debnsuma/EVA-P1/blob/master/Week5/00_EVA5_Session5_Base_Code_Step_0.ipynb)

### Version 1 (with GAP)
-------------------------

**Target** 

Add GAP and remove the last BIG kernel in the Output Block of the CNN.

**Results** 

- Parameters: 14,112
- Best Train Accuracy: 99.62%
- Best Test Accuracy: 99.11%

**Analysis** 

- Model seems to be overfit. 
- And test accuracy is not yet there what we wanted 99.4

[Version 1 - Code](01_Session7_Base_Code_Step_1.ipynb)

### Version 2 (added Dropout)
-------------------------------

**Target** 

Added Dropout torawrds the last layers

**Results** 

- Parameters: 14,112
- Best Train Accuracy: 99.43%
- Best Test Accuracy: 99.21%

**Analysis** 

- Accuracy got improved a bit
- but no. of parameters are still more than 10000

[Version 2 - Code](02_Session7_Base_Code_Step_2.ipynb)

### Version 3 (with GAP)
---------------------------------

**Target** 

Aded GAP Layer

**Results** 

- Parameters: 7,702
- Best Train Accuracy: 99.29%
- Best Test Accuracy: 99.24 %

**Analysis** 

- accuracy got improved but didnt seem to overfit 
- no. of parameters got reduced

[Version 3 - Code](03_Session7_Base_Code_Step_3.ipynb)

### Version 4 (with LR Scheduler and ImageAugmentation)
--------------------------------------

**Target** 

Add rotation, try with 5-10 degrees

**Results** 

- Parameters: 7,702
- Best Train Accuracy: 99.03%
- Best Test Accuracy: 99.42 %

**Analysis** 

- accuracy got increased and was consistent for last 5 epocs, 
- played around with different combinations for LR Scheduler (step_size and gamma), and (step_size=.9 and gamma=.1) worked well with learing rate of .2
- Reached the accuracy of 99.4 % for last 4 epocs with total no. of parameters less than 8000

[Version 4 - Code](04_Session7_Base_Code_Step_4.ipynb)


