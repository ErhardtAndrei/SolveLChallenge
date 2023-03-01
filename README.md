# Solve Light Challenge
Intelligent Shopping Cart Problem Proposed to Solve Light internship candidates

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/LICENCE) 

# About the project

The intelligent shopping cart is a problem proposed by the technology company Solve Light to candidates who want to intern at the company. The proposed problem states that the developed algorithm should allow a user, when running the code, to set up a shopping cart that allows for the registration of up to 10 products per cart. Upon closing the cart, the system should display all items purchased, the total value of the purchase, and the minimum number of bills needed to pay this total. In other words, this shopping cart should work as follows:

1- Upon running the system, we are already in the shopping cart waiting for the first product to be registered.

2- To register a product, the user must define the name and value of the product.

3- After registering the first product, the system should allow the user to register a new product or allow the user to finish the cart.

4- If the user decides to register one more product, the same process as item 3 repeats.

5- If the user decides to finish the cart, the system should display all purchased products, the total value of the cart, and the minimum number of bills required to pay for this cart. (Only the following bills should be considered: 100, 50, 20, 10, 5, 2, and 1).

## Introducing the Algorithm
This is the first version of the proposed code, developed in Pascal using the software VISUALG 3, since it is a generic and fast development language for simple problems.
### Step one
The user must choose whether they want to start the system or end it.

If the number 1 is pressed, the user will be directed to the shopping cart. 

If number 2 is pressed, the system will be terminated.

![W1](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1_menu.png) ![W2](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/1.1_menu.png)

### Step two
After the user starts the system, the shopping cart will begin with the total value up to that point. Then, the user can choose a product to be registered and its value. If they wish to continue, they simply need to type "Yes", and then the product and its value will be stored, and the total purchase value will be displayed on the screen.

![W3](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/2_carrinho.png) ![W4](https://github.com/ErhardtAndrei/SolveLChallenge/blob/main/imgs/3_cad_product.png)
### Layout web
![Web 1](https://github.com/acenelio/assets/raw/main/sds1/web1.png)

![Web 2](https://github.com/acenelio/assets/raw/main/sds1/web2.png)

## Modelo conceitual
![Modelo Conceitual](https://github.com/acenelio/assets/raw/main/sds1/modelo-conceitual.png)

# Tecnologias utilizadas
## Back end
- Java
- Spring Boot
- JPA / Hibernate
- Maven
## Front end
- HTML / CSS / JS / TypeScript
- ReactJS
- React Native
- Apex Charts
- Expo
## Implantação em produção
- Back end: Heroku
- Front end web: Netlify
- Banco de dados: Postgresql

# Como executar o projeto

## Back end
Pré-requisitos: Java 11

```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto back end
cd backend

# executar o projeto
./mvnw spring-boot:run
```

## Front end web
Pré-requisitos: npm / yarn

```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto front end web
cd front-web

# instalar dependências
yarn install

# executar o projeto
yarn start
```

# Autor

Wellington Mazoni de Andrade

https://www.linkedin.com/in/wmazoni
