# Solve Light Challenge
Intelligent Shopping Cart Problem Proposed by Solve Light to internship candidates.


[![NPM](https://img.shields.io/npm/l/react)](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/LICENCE) 

# About the project

The intelligent shopping cart is a problem proposed by the technology company Solve Light to candidates who want to intern at the company. The proposed problem states that the developed algorithm should allow a user, when running the code, to set up a shopping cart that allows for the registration of up to 10 products per cart. Upon closing the cart, the system should display all items purchased, the total value of the purchase, and the minimum number of bills needed to pay this total. In other words, this shopping cart should work as follows:

1- Upon running the system, we are already in the shopping cart waiting for the first product to be registered.

2- To register a product, the user must define the name and value of the product.

3- After registering the first product, the system should allow the user to register a new product or allow the user to finish the cart.

4- If the user decides to register one more product, the same process as item 3 repeats.

5- If the user decides to finish the cart, the system should display all purchased products, the total value of the cart, and the minimum number of bills required to pay for this cart. (Only the following bills should be considered: 100, 50, 20, 10, 5, 2, and 1).

## Introducing the Algorithm
This is the first version of the proposed code, was developed in Pascal using the software VISUALG 3, since it is a generic and fast development language for simple problems.
### Step one
The user must choose whether they want to start the system or end it.

If the number 1 is pressed, the user will be directed to the shopping cart. 

If number 2 is pressed, the system will be terminated.

![W1](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1_menu.png) ![W2](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1.1_menu.png)

### Step two
After the user starts the system, the shopping cart will begin with the total value up to that point. Then, the user can choose a product to be registered and its value. If they wish to continue, they simply need to type "Yes", and then the product and its value will be stored, and the total purchase value will be displayed on the screen. Thus, the user can keep adding items as long as they do not exceed the maximum limit of 10 items defined by the system.

![W3](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/2_carrinho.png) ![W4](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/3_cad_product.png) ![W5](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/4_new_prodct.png) 

### Step three
Then, the system will end, return the total purchase value, count the minimum notes, and indicate how much of each note will be necessary to make this transaction. The system will end if the user registers 10 products or wishes to end before registering the limit number by typing "No" for the question "Do you want to continue shopping?".

![W6](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/5_end_program.png)
![W7](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/6_result.png)

# Tecnologias utilizadas
## Back end
- Pascal
- Python (Not implemented yet)
- JavaScript (Not implemented yet)
## Front end
-(Not implemented yet)

# Como executar o projeto

- Dowloading and executing the software: VisualG 3.
- Clone this repository
- Open the code .ARG on VisualG 3.
- Execute it pressing F9

# Autor

Andrei Fernando Erhardt

https://www.linkedin.com/in/erhardtandrei/
