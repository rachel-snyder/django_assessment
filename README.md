# Assessment 3: DJANGO API

![Alt Text](./resources/ecom.png)

In this assessment you will create an E-commerce RESTful API with Django, Django Rest Frameworks, and PostgreSQL. This API will have CRUD and Token authentication capabilities.

## Important Grading Information

- You need to get a 70% or higher to pass. `10 out of 14 tests`
- There will be one retake available for this assessment.
  - 5% penalty: If you complete and submit the retake within one week of receiving your grade.
  - 10% penalty: If you complete and submit the retake afterwards.

## Rules / Process

- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals

## Scenario

Code Platoon wants to create an E-Commerce site that will offer new Code Platoon students a one stop shop for different material and equipment they may need to better prepare them for their career. Code Platoon has given us a `JSON` file holding the `items` they would like to be able to sell upon launching their online store and has tasked you with creating the Back-End API for this full-stack application

## Requirements

- Clients will be able to `sign up`, `log in`, `log out`, and confirm their information.

```bash
http://127.0.0.1:8000/api/v1/users/signup/  name="signup"
# signup will create a user, the users cart, and the users token
http://127.0.0.1:8000/api/v1/users/login/   name="login"
# login will get or create a users token
http://127.0.0.1:8000/api/v1/users/logout/  name="logout"
# logout will delete a users token
http://127.0.0.1:8000/api/v1/users/info/    name="info"
```

- Clients will be able to view all items.

```bash
http://127.0.0.1:8000/api/v1/items/   name="all_items"
```

- Clients will be able to view items by category.

```bash
http://127.0.0.1:8000/api/v1/items/category/<str:category>/ name="items_by_category"
```

- Clients will be able to view a single item and add it to their Cart.

```bash
http://127.0.0.1:8000/api/v1/items/<int:item_id>/   name='an_item'
```

- Clients will be able to view all Cart Items in their Cart and the total price.

```bash
http://127.0.0.1:8000/api/v1/cart/    name="cart"
```

- Clients will be able to increase or decrease the quantity of an item in their Cart. If the item quantity reaches 0 the Cart Item should be deleted

```bash
http://127.0.0.1:8000/api/v1/cart/method/<str:method>/cart_item/<int:cart_item_id>/

name="cart_item_quantity"
# should handle `add` or `sub` as a method argument. 
# if add increment quantity
# if sub decrement quantity  
```

- Clients will be able to remove items from their Cart regardless of quantity.

```bash
http://127.0.0.1:8000/api/v1/cart/<int:cart_item_id>/  name="delete_item"
```

## Set Up

- Create and activate your python venv
- Create `ecom_db` in `PostgreSQL`
- Change directory into `ecom_proj`
- Install dependencies from `requirements.txt`
- Install fixture data in `item_app/fixtures`
- run the test directory with `python manage.py test tests`
- START with the `Client` model in `user_app.models`

## Test Details

Each test is located within it's own file and holds a short description of what it is that it's expecting from your product. Please go through each test case and take the time to read them before attempting to code the next feature. The test suite is designed to run from top to bottom.
