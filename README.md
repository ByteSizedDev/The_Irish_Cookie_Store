# The Irish Cookie Store

## Project Overview

The Irish Cookie Store is located in Co.Waterford. They make fresh artisan cookies. The company were looking to add a website for e-commerce to sell their products online easily and for the customer to be able to safely make a transaction.

# UX

## Site Owner Goals

* Sell their products online.

* Have a website to direct to their users from social media accounts.

* See what products they have to offer.

* Safe payments.

## Site Owner User Stores

* For our customers to be able to buy our cookies online.

* For our customers to be able to view flavors and information about our products.

* For our customers to pay safely online.

* For our customers to be able to buy cookies individually and as a box.

## User Goals

* Buy cookies.

* See flavors, pictures and images of products.

* Pay safely.

## User Stories

* As a user I would like to be able to purchase my cookies safely and securely over the internet.

* As a user I would like to see information about the cookies.

* As a user I would like to be able to purchase cookies individually or as a selection box.


## Structure

* The website is build using multipal pages, using Django apps. 

* Each page has a navbar and footer container social links.

* For mobile view there is a collapsible navbar.

* Each webpage has it own content, for its intended use.
 
## Features

This website has the following features: 

* A products page where the user can view, browse and buy the cookies.

* A cakes page displaying some cakes made by the company with some information if the user would like to get in touch to purchase one.

* An about us page telling the using some more information about the company.

* The website has login and logout functionality after regeristering as a user.

* There is a profile page for the user the view there orders and shopping history.

* A shopping cart for the user the see what they are buying and how much they are spending is displayed.

* Stripe payments is user so the user can securely shop online and make safe transactions.

* The Admin/Superuser can also add, edit and delete products.

## Colours

* The project is mainly done in black and white. The background is white and the font is back

* Colors come from the images been used in the project.

* On the home page there is a "Cookie" colored font used.

## Fonts

The font used in this project is "Roberto Condensed".

## Icons

I got my icons from [Font Awesome](https://fontawesome.com/).
They were used in the following areas:

* Navbar: To display my shopping cart, profile & search bar.

* Product details page: For the quantity bar, to increment and decrement.

* Footer: To show social accounts.

* I made a favicon also of the logo to display in the browser.

## Images

All images used in the project were owned and taken by the owner. All images were of the company products.

* The home page has an image of a selection of cookies.

* The products page has images of the selected cookies.

* The cakes page has images of cakes made by the company.

* The about page also has an image of a selection of cookies.

## Wireframes

# Technologies Used

Here are a list of all the languages and technologies I've used in this project.

### Languages

* HTML

* CSS

* Javascript

* Python

### Frameworks/Librarays/Tools

* Bootstrap

* Django

# Testing

* Links and templates have been tested to make sure they arrive at the right place.

* Buttons have also been tested to see they complete the required actions.

* Forms have been tested so required fields are mandatory to complete the forms.

* My code has been run through W3C Validators.

* Tests have been done to make sure Stripe payments is correctly connected to the application.

* Products have been added, edited and deleted in the application(CRUD)

# Bugs

## Unsolved Bugs

I am aware that I still have 

# Running Locally

To run this project locally:

* Open your text editor.

* Copy the link from the repository on "Clone or download"

* Type git clone, then the URL you copied. git clone https://github.com/ByteSizedDev/The_Irish_Cookie_Store.git

* Press Enter. Your local clone will be created.

* Using: pip3 Install virtualenv.

* Then: pip3 install > requirements.txt

* Followed by: python3 manage.py migrate

* Set secret keys for Stripe and Django in env.py file.

* Create superuser: python3 manage.py createsuperuser

* Finally start your application: python3 manage.py runserver

# Deployment


# Credits

* I would like to thank the team at The Code Institute for helping me learn these technologies. To the various tutors that also helped me understand topics and fundamentals I was having issues with.

* I used the mini project "Boutique Ado" alot as a reference for this project as I have a good friend that wanted to build an e-commerce website for their business.

* Most of my backend came from the examples and videos on the topic. They were very helpful in describing what each part of the project was doing.
