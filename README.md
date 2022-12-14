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
* [Marketing](#marketing)
* [Colors Used](#colors-used)
* [Testing](#testing)
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
| shopper | feel my personal and payment information is safe and secure | confidently provide the needed information to make a purchase |
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

<details>
<summary>Desktop</summary>

![homepage-desktop](docs/desktop/homescreen-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![homepage-tablet](docs/tablet/homescreen-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![homepage-mobile](docs/mobile/homescreen-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="fitness-plan"></a>
### Fitness Plan

<details>
<summary>Desktop</summary>

![fitness plan-desktop](docs/desktop/fitnessplans-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![fitness plan-tablet](docs/tablet/fitnessplans-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![fitness plan-mobile](docs/mobile/fitnessplan-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="nutrition-plan"></a>
### Nutrition Plan

<details>
<summary>Desktop</summary>

![nutrition plan-desktop](docs/desktop/nutritionplans-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![nutrition plan-tablet](docs/tablet/nutritionplans-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![nutrition plan-mobile](docs/mobile/nutritionplan-mobile.jpeg)
</details>


[Back to top](#table-of-contents)

<a name="product-page"></a>
### Product Page

<details>
<summary>Desktop</summary>

![product page-desktop](docs/desktop/productpage-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![product page-tablet](docs/tablet/productpage-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![product page-mobile](docs/mobile/productpage-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="product-detail"></a>
### Product Detail

<details>
<summary>Desktop</summary>

![product detail-desktop](docs/desktop/productdetail-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![product detail-tablet](docs/tablet/productdetail-tabet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![product detail-mobile](docs/mobile/productdetail-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="shopping-cart"></a>
### Shopping Cart

#### Step 1

<details>
<summary>Desktop</summary>

![shopping cart step 1](docs/desktop/shoppingcart-step1-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![shopping cart step 1](docs/tablet/shoppingcart-step1-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![shopping cart step 1](docs/mobile/shoppingcart-step1-mobile.jpeg)
</details>

#### Step 2

<details>
<summary>Desktop</summary>

![shopping cart step 2](docs/desktop/shoppingcart-step2-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![shopping cart step 2](docs/tablet/shoppingcart-step2-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![shopping cart step 2](docs/mobile/shoppingcart-step2-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="order-summary"></a>
### Order Summary

<details>
<summary>Desktop</summary>

![order summary](docs/desktop/ordersummary-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![order summary](docs/tablet/ordersummary-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![order summary](docs/mobile/ordersummary-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="contact"></a>
### Contact

<details>
<summary>Desktop</summary>

![contact](docs/desktop/contact-desktop.jpeg)
</details>

<details>
<summary>Tablet</summary>

![contact](docs/tablet/contact-tablet.jpeg)
</details>

<details>
<summary>Mobile</summary>

![contact](docs/mobile/contact-mobile.jpeg)
</details>

[Back to top](#table-of-contents)

<a name="struture"></a>
## Structure

<a name="app-flow"></a>
### App Flow

<details>
<summary>Guest User</summary>

![guest user](docs/guest-user.png)
</details>

<details>
<summary>Authenticated User</summary>

![authenticated user](docs/authenticated-user.png)
</details>

<details>
<summary>Admin</summary>

![admin](docs/admin.png)
</details>

[Back to top](#table-of-contents)

<a name="data-schema"></a>
### Data Schema

<details>
<summary>Products</summary>

![products](docs/products.png)
</details>

<details>
<summary>Orders</summary>

![orders](docs/orders.png)
</details>

<details>
<summary>Contact</summary>

![contact](docs/contact.png)
</details>

<details>
<summary>Newsletter</summary>

![newsletter](docs/newslettermodel.png)
</details>

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

----

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

----

### Contact Form

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| name |  | CharField | max_length=50 null=False, blank=False |
| email |  | EmailField | max_length=254 null=False, blank=False |
| message |  | CharField | max_length=2000 null=False, blank=False |

### Fitness Plan

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| your_name |  | CharField | max_length=50 null=False, blank=False |
| dogs_name |  | CharField | max_length=50 null=False, blank=False |
| dogs_age |  | CharField | max_length=50 null=False, blank=False |
| dogs_breed |  | CharField | max_length=50 null=False, blank=False |
| sessions |  | ChoiceField | default=False, null=False, blank=False |
| email |  | EmailField | max_length=254 null=False, blank=False |
| message |  | CharField | max_length=2000 null=False, blank=False |

### Nutrition Plan

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| your_name |  | CharField | max_length=50 null=False, blank=False |
| dogs_name |  | CharField | max_length=50 null=False, blank=False |
| dogs_breed |  | CharField | max_length=50 null=False, blank=False |
| dogs_age |  | CharField | max_length=50 null=False, blank=False |
| dogs_gender |  | ChoiceField | default=False, null=False, blank=False |
| dogs_weight |  | CharField | max_length=50 null=False, blank=False |
| dogs_physique |  | ChoiceField | default=False, null=False, blank=False |
| active_level |  | ChoiceField | default=False, null=False, blank=False |
| eating_habit |  | ChoiceField | default=False, null=False, blank=False |
| does_not_eat |  | CharField | max_length=50 null=True, blank=True |
| allergies |  | CharField | max_length=50 null=True, blank=True |
| food_preference |  | ChoiceField | default=False, null=False, blank=False |
| outcome_goal |  | ChoiceField | default=False, null=False, blank=False |
| email |  | EmailField | max_length=254 null=False, blank=False |
| message |  | CharField | max_length=2000 null=False, blank=False |

----

### Subscribers

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| email | | EmailField | null=True |
| date | | DateTimeField | auto_now_add=True |

### Newsletter

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ---- |
| title | | CharField | max_length=100, null=True |
| message | | TextField | null=True |

----

[Back to top](#table-of-contents)

<a name="features"></a>
## Features

* ***Brand*** image for website.
    <details>
    <summary>Image</summary>

    ![Brand](docs/brand.png)
    </details>

---

* ***Homepage*** where the site user can read about the company and navigate to different areas of the website.
    <details>
    <summary>Image</summary>

    ![Homepage](docs/pagehome.png)
    </details>

---

* ***Fitness plan*** page where the site user can read about the benefits of keeping their dog fit.
    <details>
    <summary>Image</summary>

    ![Fitnesspage](docs/pagefitness.png)
    </details>

    <details>
    <summary>Image</summary>

    ![Fitness-benefits](docs/fitness-benefits.png)
    </details>

* Option to ***subscribe*** to a ***fitness plan***.
    <details>
    <summary>Image</summary>

    ![Fitness-plans](docs/fitness-plans.png)
    </details>

    <details>
    <summary>Image</summary>

    ![Fitness-form](docs/fitness-form.png)
    </details>

---

* ***Nutrition plan*** page where the site user can read about the benefits of feeding their dog a healthy diet.
    <details>
    <summary>Image</summary>

    ![Nutritionplan](docs/pagenutrition.png)
    </details>

    <details>
    <summary>Image</summary>

    ![Nutrition-benefits](docs/nutrition-benefits.png)
    </details>

* Option to ***subscribe*** to a ***nutrition plan***.
    <details>
    <summary>Image</summary>

    ![Nutrition-plans](docs/nutrition-plans.png)
    </details>

    <details>
    <summary>Image</summary>

    ![Nutrition-form](docs/nutrition-form.png)
    </details>

---

* ***Product page*** where the site user can browse the online store.

* Option to ***make purchases*** from the store.
    <details>
    <summary>Image</summary>

    ![Productpage](docs/pageproduct.png)
    </details>

---

* ***Product detail*** page where the site user can view details on a specific product.

* Option to view and leave ***ratings and reviews***.
    <details>
    <summary>Image</summary>

    ![Productdetail](docs/pagedetail.png)
    </details>

---

* ***Shopping cart*** page where the site user can view the products that they have put in the cart.

* Option to proceed to ***checkout*** to complete product purchases.
    <details>
    <summary>Image</summary>

    ![Shoppingcart](docs/pageshoppingbag.png)
    </details>

---

* ***Checkout page*** where the site user can enter their details and complete their purchase.
    <details>
    <summary>Image</summary>

    ![Checkoutpage](docs/pagecheckout.png)
    </details>

---

* ***Contact page*** where the site user can find contact information of the company.
    <details>
    <summary>Image</summary>

    ![Contactpage](docs/pagecontact.png)
    </details>

* Option to ***send a message*** directly from the contact page.

---

* ***Newsletter*** where the site user can subscribe by entering their email and receive updates from the site admin.
    <details>
    <summary>Image</summary>

    ![Newsletter-subscribe](docs/newsletter-subscribe.png)
    </details>

* Site admin can ***send a message*** to anyone who has subscribed to the newsletter.
    <details>
    <summary>Image</summary>

    ![Newsletter-message](docs/newsletter-message.png)
    </details>

---

* ***404 error page*** when the site user navigates to a page that doesn't exist.
    <details>
    <summary>Image</summary>

    ![404-page](docs/404-page.png)
    </details>

* Option to navigate to ***home*** page.

---

[Back to top](#table-of-contents)

<a name="marketing"></a>
## Marketing

### Social Media

Facebook - https://www.facebook.com/profile.php?id=100086354232340

I have used Facebook as a marketing strategy for Dog Fitness and Nutrition.

![fbheading](docs/facebook-heading.png)

In the intro section, the user can view contact details as well a link to the website.

![fbbody](docs/facebook-body.png)

The admin can post updates to the store with a link to the relevant website page.
The user can comment, share and like the post.

![fbpost](docs/facebook-post.png)

The user can view directions to where the fitness sessions are held.

![fbinfo](docs/facebook-info.png)


---

[Back to top](#table-of-contents)

<a name="colors-used"></a>
## Colors Used

These are the primary colors that I have used throughout the website. I wanted to use soft background colors so that the content can be the main focus. I used red for the buttons so that they can stand out and a soft blue/grey color for the footer and text as I felt that the contrast with the lighter colors have a pleasant look.

| #6B7A8F | #FF3B3F | #F2F2F2 | #FDE7CB | #FFFFFF |
| ---- | ---- | ---- | ---- | ---- |
| ![#6B7A8F](docs/6B7A8F.png) | ![#FF3B3F](docs/FF3B3F.png) | ![#F2F2F2](docs/F2F2F2.png) | ![#FDE7CB](docs/FDE7CB.png) | ![#FFFFFF](docs/FFFFFF.png) |

[Back to top](#table-of-contents)

<a name="testing"></a>
## Testing

### Python

| File Name | File Path | Rated | Comment |
| ----- | ----- | ----- | ----- |
| BAG |  | 10.00/10 |  |
|  |  |  |  |
| admin.py | bag/admin.py | 10.00/10 |  |
| apps.py | bag/apps.py | 10.00/10 |  |
| contexts.py | bag/contexts.py | 10.00/10 |  |
| urls.py | bag/urls.py | 10.00/10 |  |
| views.py | bag/views.py | 10.00/10 |  |
|  |  |  |  |
| CHECKOUT |  | 6.52/10 |  |
|  |  |  |  |
| admin.py | checkout/admin.py | 10.00/10 |  |
| apps.py | checkout/apps.py | 6.67/10 |  |
| forms.py | checkout/forms.py | 9.44/10 |  |
| models.py | checkout/models.py | 6.08/10 |  |
| signals.py | checkout/signals.py | 2.86/10 | |
| urls.py | checkout/urls.py | 10.00/10 |  |
| views.py | checkout/views.py | 6.81/10 |  |
| webhook_handler.py | checkout/webhook_handler.py | 6.18/10 |  |
| webhooks.py | checkout/webhooks.py | 8.89/10 |  |
|  |  |  |  |
| CONTACT |  | 6.32/10 |  |
|  |  |  |  |
| admin.py | contact/admin.py | 10.00/10 |  |
| apps.py | contact/apps.py | 10.00/10 |  |
| forms.py | contact/forms.py | 10.00/10 |  |
| models.py | contact/models.py | 2.86/10 |  |
| urls.py | contact/urls.py | 10.00/10 |  |
| views.py | contact/views.py | 10.00/10 |  |
|  |  |  |  |
| DOG_FITNESS_AND_NUTRITION |  | 9.62/10 |  |
|  |  |  |  |
| asgi.py | dog_fitness_and_nutrition/asgi.py | 10.00/10 |  |
| settings.py | dog_fitness_and_nutrition/settings.py | 10.00/10 |  |
| urls.py | dog_fitness_and_nutrition/urls.py | 8.75/10 |  |
| views.py | dog_fitness_and_nutrition/views.py | 3.33/10 |  |
| wsgi.py | dog_fitness_and_nutrition/wsgi.py | 10.00/10 |  |
|  |  |  |  |
| FITNESS_PLANS |  | 10.00/10 |  |
|  |  |  |  |
| apps.py | fitness_plans/apps.py | 10.00/10 |  |
| forms.py | fitness_plans/forms.py | 10.00/10 |  |
| urls.py | fitness_plans/urls.py | 10.00/10 |  |
| views.py | fitness_plans/views.py | 10.00/10 |  |
|  |  |  |  |
| HOME |  | 10.00/10 |  |
|  |  |  |  |
| admin.py | home/admin.py | 10.00/10 |  |
| apps.py | home/apps.py | 10.00/10 |  |
| models.py | home/models.py | 10.00/10 |  |
| urls.py | home/urls.py | 10.00/10 |  |
| views.py | home/views.py | 10.00/10 |  |
|  |  |  |  |
| NEWSLETTER |  | 6.71/10 |  |
|  |  |  |  |
| admin.py | newsletter/admin.py | 10.00/10 |  |
| apps.py | newsletter/apps.py | 10.00/10 |  |
| forms.py | newsletter/forms.py | 8.00/10 |  |
| models.py | newsletter/models.py | 0.91/10 |  |
| urls.py | newsletter/urls.py | 10.00/10 |  |
| views.py | newsletter/views.py | 8.18/10 |  |
|  |  |  |  |
| NUTRITION_PLANS |  | 9.83/10 |  |
|  |  |  |  |
| apps.py | nutrition_plans/apps.py | 10.00/10 |  |
| forms.py | nutrition_plans/forms.py | 10.00/10 |  |
| urls.py | nutrition_plans/urls.py | 10.00/10 |  |
| views.py | nutrition_plans/views.py | 9.67/10 |  |
|  |  |  |  |
| PRODUCTS |  | 7.04/10 |  |
|  |  |  |  |
| admin.py | products/admin.py | 10.00/10 |  |
| apps.py | products/apps.py | 10.00/10 |  |
| forms.py | products/forms.py | 5.33/10 |  |
| models.py | products/models.py | 5.00/10 |  |
| urls.py | products/urls.py | 10.00/10 |  |
| views.py | products/views.py | 8.55/10 |  |
| widgets.py | products/widgets.py | 10.00/10 |  |
|  |  |  |  |
| PROFILES |  | 7.44/10 |  |
|  |  |  |  |
| apps.py | profiles/apps.py | 10.00/10 |  |
| forms.py | profiles/forms.py | 9.44/10 |  |
| models.py | profiles/models.py | 4.00/10 |  |
| urls.py | profiles/urls.py | 10.00/10 |  |
| views.py | profiles/views.py | 9.60/10 |  |

[Back to top](#table-of-contents)

### CSS

| File Name | File Path | Result | Error/Warning | Comment |
| ----- | ----- | ----- | ----- | ----- |
| base.css | /base.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) | 7 warnings -  [link](docs/basecss.png) |
| home.css | home/home.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) |  |
| profile.css | profiles/profile.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) |  |
| fitness_plans.css | fitness_plans/fitness_plans.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) |  |
| nutrition_plans.css | nutrition_plans/nutrition_plans.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) |  |
| contact.css | contact/contact.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) | 3 warnings -  [link](docs/contactcss.png) |
| checkout.css | checkout/checkout.css | ![CSS](http://jigsaw.w3.org/css-validator/images/vcss-blue) | 1 warning -  [link](docs/checkoutcss.png) |

### JS

| File Name | File Path | JSHint | Comment |
| ----- | ----- | ----- | ----- |
| countryfield.js | profiles/countryfield.js | [link](docs/countryfield-js-test.png) |
| stripe_elements.js | checkout/stripe_elements.js | [link](docs/stripe-elements-js-test.png) |

### Lighthouse

| Page Name | Desktop/Mobile | Comment |
| ----- | ----- | -----|
| Home | [link](docs/lighthousehomedesk.png) / [link](docs/lighthousehomemob.png) |
| Fitness Plan | [link](docs/lighthousefitnessdesk.png) / [link](docs/lighthousefitnessmob.png) |
| Nutrition Plan | [link](docs/lighthousenutritiondesk.png) / [link](docs/lighthousenutritionmob.png) |
| Products | [link](docs/lighthouseproductdesk.png) / [link](docs/lighthouseproductmob.png) |
| Products Detail | [link](docs/lighthousedetailsdesk.png) / [link](docs/lighthousedetailsmob.png) |
| Shopping Cart | [link](docs/lighthousebagdesk.png) / [link](docs/lighthousebagmob.png) |
| Order Summary | [link](docs/lighthousecheckoutdesk.png) / [link](docs/lighthousecheckoutmob.png) |
| Contact | [link](docs/lighthousecontactdesk.png) / [link](docs/lighthousecontactmob.png) |

[Back to top](#table-of-contents)

<a name="deployment"></a>
## Deployment
This project was deployed using Heroku
* Steps for deployment
  * Create a Heroku app
  * Change `DEBUG` in ***settings.py*** to `False`
  * Link the Heroku app to the repository
  * Click on deploy

The live link can be found here - https://dog-fitness-and-nutrition.herokuapp.com/

[Back to top](#table-of-contents)

<a name="credits"></a>
## Credits

* Simen Daehlin (Mentor)
* Code Institude
    * This project was largely based off the Boutique Ado project

[Back to top](#table-of-contents)

<a name="content"></a>
## Content

* Images sourced from https://unsplash.com/
* Wireframe created on https://app.uizard.io/
* Fonts sourced from https://fonts.google.com/
* Email testing done on https://mailtrap.io/

[Back to top](#table-of-contents)