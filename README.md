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
This is the first version of the proposed code, was developed in Pascal using the software VISUALG 3, since it is a generic and fast development language for simple problems. The next versions will be made in different languages such Python and JavaScript.

This challenge has an extra step, which would be to develop a registration screen for users. This step can be seen from Step Four. With the main logic developed, a graphical interface for user registration is then developed. This interface was developed in Python using the *tkinter* library. 

The following steps demonstrate the functioning of the product registration system. From "Step one" to "Step four," only the programming logic used to develop the registration is presented, with the same logic in both Pascal and Python. From there, the graphical interface for the user is presented.

### Step one
The user must choose whether they want to start the system or end it. If the number 1 is pressed, the user will be directed to the shopping cart. 
If number 2 is pressed, the system will be terminated.

![W1](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1_menu.png) ![W2](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1.1_menu.png)

### Step two
After the user starts the system, the shopping cart will begin with the total value up to that point. Then, the user can choose a product to be registered and its value. If they wish to continue, they simply need to type "Yes", and then the product and its value will be stored, and the total purchase value will be displayed on the screen. Thus, the user can keep adding items as long as they do not exceed the maximum limit of 10 items defined by the system.

![W3](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/2_carrinho.png) ![W4](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/3_cad_product.png) ![W5](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/4_new_prodct.png) 

### Step three
Then, the system will end, return the total purchase value, count the minimum notes, and indicate how much of each note will be necessary to make this transaction. The system will end if the user registers 10 products or wishes to end before registering the limit number by typing "No" for the question "Do you want to continue shopping?".

![W6](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/5_end_program.png)
![W7](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/6_result.png)

### Step four
When executing the code, the login window will be displayed for the user to connect to the system.
![W8](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/7_login.png)

In case the user does not have a registration yet, he can click on the 'Logon' button to register.
![W9](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/8_logon_screen.png)

### Step five
The user must enter data that are valid for the registration to be carried out by clicking on 'Cadastrar'.
![W10](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/9_logon.png)

If the user fills in all the fields correctly, his registration will be registered and saved in the database, otherwise, the system returns an error informing what is wrong when filling in the data.
![W11](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/10.1_error_pass.png)
![W12](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/10_confirm_user_cad.png)
![W13](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/11_db_SQLite.png)

### Step six
Then, the user must return to the login screen and enter the registered user and password. If the user fills in the fields with the correct data, the system will connect and allow him to register products, otherwise, it will return an error and ask the user to correct the data entered.
![W14](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/12.1_error_connect.png)
![W15](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/12_connected_user.png)

### Step seven
Once the user is connected, the system redirect from the initial page to the products cadastration area. The user must introduce the product name and the value, respectively. 

![W16](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/registerarea_13.png)
![W17](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/registerarea_13.1.png)

### Step ten
After registering the product, it will be stored in a vector for the system to calculate the ballots. Then, clicking "Encenrrar cadastro" the system will show how many ballots is needed to pay the shopping cart.

![W18](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/registerarea13.2.png)
![W19](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/15_ex1.png)
![W20](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/14_result.png)

## Back end
- Pascal
- Python 
- SQLite3 (as data base)
- JavaScript (Not implemented yet)
## Front end
- Python

# How to execute the project
## Pascal
- Dowload and execute the software: VisualG 3.
- Download MainCodePascal in this repository.
- Save as .ARG extension.
- Open the file .ARG at the software VisualG 3.
- Execute it pressing F9.
## Python
- Download MainCodePython in this repository.
- Save as .py extension.
- Open the file .py in your preferred Python editor.
- Run the project.

## Python user interface
- Clone this repository.
- Dowload and install SQLite software (DB Browser) for creating and storing .db data.
- You may or may not keep the .db file in the destination folder. The interface will automatically generate a .db file if one is not already created.
- Make sure the figure *solve-img.png* is in the right patch.
- Execute the main code Cadastro.py.

# Author

Andrei Fernando Erhardt

https://www.linkedin.com/in/erhardtandrei/
