# Dog Fitness & Training

<a name="table-of-contents"></a>
## Table of Contents

* [Description](#description)
* [User Stories](#user-stories)
* [Wireframe](#wireframe)
    * [Homepage](#homepage)
    * [Fitness Plan](#fitness-plan)
    * [Nutrition Plan](#nutrition-plan)
    * [Product Page](#product-page)
    * [Product Detail](#product-detail)
    * [Shopping Cart](#shopping-cart)
    * [Order Summary](#order-summary)
    * [Contact](#contact)
* [Structure](#structure)
    * [App Flow](#app-flow)
    * [Data Schema](#data-schema)
* [Models](#models)
* [Features](#features)
* [Colors Used](#colors-used)
* [Am I Responsive](#am-i-responsive)
* [Testing](#testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Content](#content)

<a name="description"></a>
## Description

Dog Fitness & Nutrition is a website aimed at dog owners seeking to improve their dogs health. There are three main parts to the website: ***Fitness Plan***, ***Nutrition Plan*** and ***Products***

- ***Fitness Plan***

In the fitness plan section, the site user can view fitness advice for dogs, benefits to keeping their dog fit and the option to subscribe to a fitness plan which includes personal or group meetups with a professional instructor. The meetups consist of exercises that the dog owners can do with their dog ranging from basic exercises to advance agility training depending on the dogs physical abilities and needs.

- ***Nutrition Plan***

In the nutrition plan section, the site user can view nutritional advice for dogs, benefits to feeding their dog a healthy diet and the option to subscribe to a nutrition plan which includes a delivery of food and suppliments specific to the dogs needs and a plan for feeding times and quantity.

- ***Products***

In the products section, the site user can browse the online store and purchase fitness and nutrition supplies for dogs. The site user can browse by categories or view all products. The site user can select a product to view the product page which displays a description of the product, price, images, product rating, reviews as well as being able to add the product to the shopping cart. The site user can also rate and review individual products.

[Back to top](#table-of-contents)

<a name="user-stories"></a>
## User Stories

### Viewing and Navigation
| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ---- | ---- | ---- |
| shopper | view a list of products | select something to purchase |
| shopper | individual product details | identify the description, price, images, product rating and reviews |
| shopper | easily view the total of my purchases at any time | avoid spending too much |

### Registration and User Accounts
| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ---- | ---- | ---- |
| site user | easily register for an account | have a personal account and be able to view my profile |
| site user | easily login or logout | access my personal account information |
| site user | easily recover my password in case I forget it | recover access to my account |
| site user | receive an email confirmation after registering | verify that my account registration was successful |
| site user | have a personalized user profile | view my personal order history and order confirmations, and save my payment information |

### Sorting and Searching
| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ---- | ---- | ---- |
| shopper | sort the list of available products | easily identify the best rated, best priced and categorically sorted products |
| shopper | sort a specific category of product | find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| shopper | sort multiple categories of products simultaneously | find the best-priced or best-rated products across broad categories, such as "Fitness", "Dry Food" or "Supplements" |
| shopper | search for a product by name or description | find a specific product I would like to purchase |
| shopper | easily see what I have searched for and the number of results | quickly decide whether the product I want is available |

### Purchasing and Checkout
| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ---- | ---- | ---- |
| shopper | easily select the size and quantity of a product when purchasing it | ensure I don't accidentally select the wrong product, quantity or size |
| shopper | view items in my bag to be purchased | identify the total cost of my purchase and all items I will receive |
| shopper | adjust the quantity of individual items in my bag | easily make changes to my purchase before checkout |
| shopper | easily enter my payment information | check out quickly and with no hassles |
| shopper | fee my personal and payment information is safe and secure | confidently provide the needed information to make a purchase |
| shopper | view an order confirmation after checkout | verify that I haven't made any mistakes |
| shopper | receive an email confirmation after checking out | keep the confirmation of what I have purchased for my records |

### Admin and Store Management
| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ---- | ---- | ---- |
| store owner | add a product | add new items to my store |
| store owner | edit/update a product | change product prices, descriptions, images and other product criteria |
| store owner | delete a product | remove items that are no longer for sale |

[Back to top](#table-of-contents)

<a name="wireframe"></a>
## Wireframe

<a name="homepage"></a>
### Homepage

##### Desktop
![homepage-desktop](docs/desktop/homescreen-desktop.jpeg)
##### Tablet
![homepage-tablet](docs/tablet/homescreen-tablet.jpeg)
##### Mobile
![homepage-mobile](docs/mobile/homescreen-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="fitness-plan"></a>
### Fitness Plan

##### Desktop
![fitness plan](docs/desktop/fitnessplans-desktop.jpeg)
##### Tablet
![fitness plan](docs/tablet/fitnessplans-tablet.jpeg)
##### Mobile
![fitness plan](docs/mobile/fitnessplan-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="nutrition-plan"></a>
### Nutrition Plan

##### Desktop
![nutrition plan](docs/desktop/nutritionplans-desktop.jpeg)
##### Tablet
![nutrition plan](docs/tablet/nutritionplans-tablet.jpeg)
##### Mobile
![nutrition plan](docs/mobile/nutritionplan-mobile.jpeg)


[Back to top](#table-of-contents)

<a name="product-page"></a>
### Product Page

##### Desktop
![product page](docs/desktop/productpage-desktop.jpeg)
##### Tablet
![product page](docs/tablet/productpage-tablet.jpeg)
##### Mobile
![product page](docs/mobile/productpage-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="product-detail"></a>
### Product Detail

##### Desktop
![product detail](docs/desktop/productdetail-desktop.jpeg)
##### Tablet
![product detail](docs/tablet/productdetail-tabet.jpeg)
##### Mobile
![product detail](docs/mobile/productdetail-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="shopping-cart"></a>
### Shopping Cart

#### Step 1
##### Desktop
![shopping cart step 1](docs/desktop/shoppingcart-step1-desktop.jpeg)
##### Tablet
![shopping cart step 1](docs/tablet/shoppingcart-step1-tablet.jpeg)
##### Mobile
![shopping cart step 1](docs/mobile/shoppingcart-step1-mobile.jpeg)

#### Step 2
##### Desktop
![shopping cart step 2](docs/desktop/shoppingcart-step2-desktop.jpeg)
##### Tablet
![shopping cart step 2](docs/tablet/shoppingcart-step2-tablet.jpeg)
##### Mobile
![shopping cart step 2](docs/mobile/shoppingcart-step2-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="order-summary"></a>
### Order Summary

##### Desktop
![order summary](docs/desktop/ordersummary-desktop.jpeg)
##### Tablet
![order summary](docs/tablet/ordersummary-tablet.jpeg)
##### Mobile
![order summary](docs/mobile/ordersummary-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="contact"></a>
### Contact

##### Desktop
![contact](docs/desktop/contact-desktop.jpeg)
##### Tablet
![contact](docs/tablet/contact-tablet.jpeg)
##### Mobile
![contact](docs/mobile/contact-mobile.jpeg)

[Back to top](#table-of-contents)

<a name="struture"></a>
## Structure

<a name="app-flow"></a>
### App Flow

#### Guest User
![guest user](docs/guest-user.png)

#### Authenticated User
![authenticated user](docs/authenticated-user.png)

#### Admin
![admin](docs/admin.png)

[Back to top](#table-of-contents)

<a name="data-schema"></a>
### Data Schema

#### Products
![products](docs/products.png)

#### Orders
![orders](docs/orders.png)

#### Contact
![orders](docs/contact.png)

[Back to top](#table-of-contents)

<a name="models"></a>
## Models

### ProductCategory

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| name | | CharField | max_length=254 |
| friendly_name | | CharField | max_length=254 |

### Products

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| category | FK (ProductCategory) | | null=True, on_delete=models.SET_NULL |
| name | | CharField | max_length=254 |
| description | | TextField | |
| sizes | | BooleanField | default=False, null=True, blank=True |
| price | | DecimalField | max_digits=6, decimal_places=2 |
| rating | | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True |
| image_url | | URLField | max_length=1024, null=True, blank=True |
| image | | ImageField | null=True, blank=True |


### Order

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| user_profile | FK (UserProfile) | | null=True, related_name='orders', on_delete=models.SET_NULL |
| order_number | | CharField | max_length=32, null=False, editable=False |
| full_name | | CharField | max_length=50, null=False, blank=False |
| email | | EmailField | max_length=254, null=False, blank=False |
| phone_number | | CharField | max_length=20, null=False, blank=False |
| country | | CharField | max_length=40, null=False, blank=False |
| postcode | | CharField | max_length=20, null=False, blank=False |
| town_or_city | | CharField | max_length=20, null=False, blank=False |
| street_address1 | | CharField | max_length=80, null=False, blank=False |
| street_address2 | | CharField | max_length=80, null=True, blank=True |
| region | | CharField | max_length=80, null=True, blank=True |
| date | | DateTimeField | auto_now_add=True |
| delivery_cost | | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| order_subtotal | | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| order_total | | DecimalField | max_length=10, decimal_places=2, null=False, default=0 |

### Contact Form

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| name |  | CharField | max_length=50 null=False, blank=False |
| email |  | EmailField | max_length=254 null=False, blank=False |
| dogs_name |  | CharField | max_length=50 null=False, blank=False |
| dogs_age |  | CharField | max_length=50 null=False, blank=False |
| dogs_breed |  | CharField | max_length=50 null=False, blank=False |
| fitness_plan | FK (FitnessPlan) | | null=True, on_delete=models.SET_NULL |
| nutrition_plan | FK (NutritionPlan) | | null=True, on_delete=models.SET_NULL |
| message |  | CharField | max_length=2000 null=False, blank=False |

### Fitness Plan

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| sessions |  | BooleanField | default=False, null=False, blank=False |

### Nutrition Plan

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| dogs_gender |  | BooleanField | default=False, null=False, blank=False |
| dogs_weight |  | CharField | max_length=50 null=False, blank=False |
| dogs_physique |  | BooleanField | default=False, null=False, blank=False |
| active_level |  | BooleanField | default=False, null=False, blank=False |
| eating_habit |  | BooleanField | default=False, null=False, blank=False |
| does_not_eat |  | CharField | max_length=50 null=True, blank=True |
| allergies |  | CharField | max_length=50 null=True, blank=True |
| food_preference |  | BooleanField | default=False, null=False, blank=False |
| outcome_goal |  | BooleanField | default=False, null=False, blank=False |

[Back to top](#table-of-contents)

<a name="features"></a>
## Features

* ***Brand*** image for website
![brand](docs/brand.png)
* ***Homepage*** where the site user can read about the company and navigate to different areas of the website
* ***Fitness plan*** page where the site user can read about the benefits of keeping their dog fit
* Option to ***subscribe*** to a ***fitness plan***
* ***Nutrition plan*** page where the site user can read about the benefits of feeding their dog a healthy diet
* Option to ***subscribe*** to a ***nutrition plan***
* ***Product page*** where the site user can browse the online store
* Option to ***make purchases*** from the store
* ***Product detail*** page where the site user can view details on a specific product
* Option to view and leave ***ratings and reviews***
* ***Shopping cart*** page where the site user can view the products that they have put in the cart
* Option to proceed to ***checkout*** to complete product purchases
* ***Checkout page*** where the site user can enter their details and complete their purchase
* ***Contact page*** where the site user can find contact information of the company
* Option to ***send a message*** directly from the contact page

[Back to top](#table-of-contents)

<a name="colors-used"></a>
## Colors Used

| #000958 | #FDE7CB | #F2F2F2 | #FFFAF5 | #FFFFFF |
| ---- | ---- | ---- | ---- | ---- |
| ![#000958](docs/colors/000958.png) | ![#FDE7CB](docs/colors/FDE7CB.png) | ![#F2F2F2](docs/colors/F2F2F2.png) | ![#FFFAF5](docs/colors/FFFAF5.png) | ![#FFFFFF](docs/colors/FFFFFF.png) |

[Back to top](#table-of-contents)

<a name="am-i-responsive"></a>
## Am I Responsive

[Back to top](#table-of-contents)

<a name="testing"></a>
## Testing

[Back to top](#table-of-contents)

<a name="validator-testing"></a>
## Validator Testing

[Back to top](#table-of-contents)

<a name="bugs"></a>
## Bugs
* Fixed

* Unfixed

[Back to top](#table-of-contents)

<a name="deployment"></a>
## Deployment

[Back to top](#table-of-contents)

<a name="credits"></a>
## Credits

[Back to top](#table-of-contents)

<a name="content"></a>
## Content

* Brand image created on https://express.adobe.com/
* Images sourced from https://unsplash.com/
* Bootstrap cdn sourced from https://bootswatch.com/4/united/

[Back to top](#table-of-contents)