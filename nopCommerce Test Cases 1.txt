Nop Commerce:
Ecommerce Test Cases:

----------------------------
User Registration and Login:
----------------------------
Test Case 1: Register User
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Register' button
5. Verify register title 'nopCommerce demo store. Register'
6. Enter personal details, company details, subscribe to newsletter, password, confirm password
7. Click 'Register' button
8. Verify that 'Your registration completed' is visible
9. Click 'Continue' button
10. Verify that 'My account' is visible (Which is in nav bar)
11. Click on 'Log out'
12. Verify that 'Log in' is visible


Test Case 2: Login User with correct email and password or Logout User
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Verify that 'My account' is visible
9. Click on 'Log out'
10. Verify that 'Log in' is visible


Test Case 3: Login User with incorrect email and password
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter incorrect email an password
7. Click on 'LOG IN'
8. Verify error 'Login was unsuccessful. Please correct the errors and try again.
The credentials provided are incorrect' is visible



Test Case 4: Register User with existing email
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Register' button
5. Verify register title 'nopCommerce demo store. Register'
6. Enter personal details(give already registered email address), company details, subscribe to newsletter, password, confirm password
7. Click 'Register' button
8. Verify error 'The specified email already exists' is visible


Test Case 5: Successfully submit contact us form
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Click on 'Contact us' link
4. Verify that 'Contact Us' heading is visible
5. Enter nam in the 'Enter your name' field
6. Enter a valid email in the 'Enter your email' field
7. Enter an inquiry in the 'Enter your enquiry' field.
8. Click 'SUBMIT' button
9. Verify success message 'Your enquiry has been successfully sent to the store owner.' is visible

---------------------------
Product Catalog and Search:
---------------------------
Test Case 6: Verify All Products and product detail page
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Computers' category menu in the top navigation.
5. Click on 'Notebooks' sub-category
6. Verify that page 'Notebooks' is visible and a list of products is displayed
7. Click on the product title or image for 'Apple MacBook Pro'
8. Verify that the product detail page is visible
9. Verify that the following details are correctly displayed:
- Product Name (Apple MacBook Pro)
- Short Description (visible below the product name)
- Product price ($1,800.00)
- Add to Cart button is visible
10. Verify the 'Full Description' and 'Product Specifications' tabs/section are visible below the product image

Test Case 7: Product Search
1. Launch browser
2. Navigate to url
3. Verify that home page is visible successfully.
4. Enter 'Apple MacBook Pro' in the search bar
5. Click on 'Search' button
6. Verify that the search results page displays the Apple MacBook Pro
7. Verify the only relevant products are listed


------------------------------
Add to cart and Shopping Cart:
------------------------------
Test Case 8: Add Product to Cart from Category Page  (test_add_to_cart nad page_add_to_cart)
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Hover over 'Electronics' menu and click on 'Cell phones'
4. Locate the product HTC One M8 Android L 5.0 Lollipop.
5. Click the 'Add to Cart' button directly from the product grid.
6. Verify green success notification 'The product has been added to your shopping cart' appears at the top
7. Verify the 'Shopping cart' link at the top shows '(1)' item

Test Case 9: Add Product to Cart with required Attributes
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Click on the product Build your own computer.
4. Attempt to click 'Add to cart'
 without selecting mandatory options.
5. Verify the error messages appear for required attributes (e.g., 'Please select RAM')
6. Select Processor, RAM, HDD, and OS options.
7. Click 'Add to cart' button.
8. Verify the product is added successfully.


Test Case 10: Update Quantity in Shopping Cart
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Add any product to the cart and click on 'Shopping cart' at the top right.
4. Locate the 'Qty.' input box for the item.
5. Change the value from '1' to '3'.
6. Verify that the 'Total' price is recalculated correctly.
7. Verify the subtotal reflects the price of 3 units.


Test Case 11: Remove Product from shopping cart
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Add a product to the cart and navigate to the 'Shopping Cart' page.
4. Click the 'X' (Remove) button located in the far right column of the product row.
5. Verify the product is removed from the list.
6. Verify the message 'Your Shopping Cart is empty!' is displayed.


Test Case 12: Mini-Cart Functionality
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Add a product like the Apple MacBook Pro 13-inch to the cart
4. Hover the mouse over the 'Shopping cart' link in the top header.
5. Verify a mini-cart dropdown appears showing the product image, name, and price.
6. Click the 'Go to cart' button within the mini-cart dropdown.
7. Verify the user is redirected to the full Shopping Cart page.


----------

Test Case 13: Place Order - Register while Checkout (clicking check box for same address for shipping and billing)
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully.
4. Add a product to the cart (ex: Apple MacBook Pro 13-inch)
5. Click on 'Shopping cart' link at the top.
6. Check the 'I agree with the terms of service' checkbox and click 'Checkout'.
7. Click the 'Register' button under the 'New Customer' section on the checkout/login page.
8. Fill in all mandatory registration details (First Name, Last Name, Email)
9. Click the 'Register' button.
10. Verify registration confirmation and click 'Continue' to return to the checkout process.
11. Complete the checkout steps:
- Billing Address: Select address and Click 'Continue'
- Shipping Method: Select 'Ground' and click 'Continue'
- Payment Method: Select 'Check / Money Order' and click 'Continue'
- Payment Information: Click 'Continue'
- Confirm Order: Verify details and click 'Confirm'
12. Verify the message 'Your order has been successfully processed!' is visible.
13. Verify that order number is displayed.


Test Case 14: Place Order - Register while Checkout (Not clicking check box for same address for shipping and billing)
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully.
4. Add a product to the cart (ex: Apple MacBook Pro 13-inch)
5. Click on 'Shopping cart' link at the top.
6. Check the 'I agree with the terms of service' checkbox and click 'Checkout'.
7. Click the 'Register' button under the 'New Customer' section on the checkout/login page.
8. Fill in all mandatory registration details (First Name, Last Name, Email)
9. Click the 'Register' button.
10. Verify registration confirmation and click 'Continue' to return to the checkout process.
11. Complete the checkout steps:
- Billing Address: Select address and Click 'Continue' 
- Shipping Address: Select address from drop down or add new address
- Shipping Method: Select 'Ground' and click 'Continue'
- Payment Method: Select 'Check / Money Order' and click 'Continue'
- Payment Information: Click 'Continue'
- Confirm Order: Verify details and click 'Confirm'
12. Verify the message 'Your order has been successfully processed!' is visible.
13. Verify that order number is displayed.


Test Case 15: Place Order - Checkout as Guest
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully.
4. Add a product to the cart (ex: Apple MacBook Pro 13-inch)
5. Click on 'Shopping cart' link at the top.
6. Check the 'I agree with the terms of service' checkbox and click 'Checkout'.
7. Click the 'Checkout as Guest' button on the welcome/login page.
8. Enter all mandatory Billing Address details:
- First name, Last name, and Email.
- Select Country (ex: India)
- City, Address 1, Zip/postal code, and Phone number
9. Click the 'Continue' button 
10. Select 'Shipping Method'(ex: Ground) and click 'Continue'.
11. Select 'Payment Method' (ex: Check/Money Order) and click 'Continue'.
12. Click 'Continue' on the Payment Information pane.
13. Verify all order details on the 'Confirm Order' screen and click 'Confirm'.
14. Verify the message 'Your order has been successfully processed!' is visible.
15. Click the 'Click here for order details' link to verify the guest order summary.


Test Case 16: Submit a Product Review (Registered User)
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Log in with a registered account (or register a new one).
4. Search for or click on a product
5. Click on the 'Add your review' link near the near the product rating stars.
6. Verify that the 'Product reviews' page is visible.
7. Enter a title in the 'Review text' area.
8. Enter your comments in the 'Review title' field.
9. Select a rating(1 to 5 stars).
10. Click the 'Submit review' button.
11. Verify success message 'Product review is successfully added.' is visible.
12. Verify review is added on the my product review page(My Account/My Product Reviews)


Test Case 17: Submit Review as Guest (Negative Case)
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Ensure you are not logged in.
4. Navigate to any product details page
5. Click on 'Add your review'.
6. Verify that the system displays an error message: 'Only registered users can write reviews'(or redirects you to the login page)


Test Case 18: Search Products and verify cart after login
1. Launch browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Enter 'Apple MacBook Pro' in the search bar and click 'Search'
5. Click on the product from the search results.
6. Click the 'Add to cart' button
7. Verify the product is added (Shopping cart link shows '(1)')
8. Click on the 'Log in' link in the top header.
9. Enter valid registered email and password.
10. Click the 'Log in' button.
11. Verify that the user is logged in successfully.
12. Click on the 'Shopping cart' link at the top right.
13. verify that the product added before login ('Apple MacBook Pro 13-inch') is still present in the cart.
14. Verify the quantity and price are correct.



Test Case 19: Verify My Account
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on My Account
9. Verify the My Account page is visible(information, address etc)



Test Case 20: Verify Wish list
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on Wish list 
9. if items are not available then add products to the Wish list(Click on like button to add products to the wish list)
10. if items are available then click on check box and add to cart
11. verify that shopping cart page is visible or not


Test Case 21: Verify product comparison
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on product comparison 
9. if items are not available then add products to the comparison list
10. if items are available then compare products 
11. After comparing the product click on the clear list
12. verify that message 'You have no items to compare' is visible


Test Case 22: Verify the currency conversion
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on Drop down to change the visibility of the currency
5. verify that currency is changing or not


test case 23: Add new Address in the my address page
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on My Account button
9. Click on address and then add new address
10. enter the details in the input fields and then click on save button
11. verify that added address is visible


test case 24: Delete Address in the my address page
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on My Account button
9. Click on delete
10. verify that address is deleted or not

test case 25: Billing address for new address(verify that shipping should not shown)
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on shopping cart and then click on check box and click on check out
9. verify that added address is visible in drop down or not
10. if not add new address with all information and click on continue
11. Check the new address is added in the my address page (Go to my account>address > verify the added address)



test case 26: shipping address for new address()
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Click on shopping cart and then click on check box and click on check out
9. verify that added address is visible in drop down or not (billing address)
11. in billing address clear check box for same shipping address
12. verify that added address is visible in drop down or not (shipping address)
12. if not add new address with all information and click on continue in shipping address
13. Check the new address is added in the my address page (Go to my account>address > verify the added address)


test case 27: Change password (Positive)
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Verify that 'My account' is visible
9. Click on My Account and Click on change password
10. Verify change password is visible
11. Fill the input fields and click on change password with correct old password
12. Verify popup notification message as 'Password was changed' is visible or not


test case 28: Change password (Negative)
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on 'Log in' button
5. Verify that 'Returning Customer' is visible
6. Enter correct email an password
7. Click on 'LOG IN'
8. Verify that 'My account' is visible
9. Click on My Account and Click on change password
10. Verify change password is visible
11. Fill the input fields and click on change password with incorrect old password
12. Verify message as 'Old password doesn't match' is visible or not



test case 29: Verify navigational link are working or not
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click on Navigation links and verify that windows are navigating or not


test case 30: Verify subscription in Home page
1. Launch Browser
2. Navigate to url 'https://demo.nopcommerce.com/'
3. Verify that home page is visible successfully
4. Click in input field which is below 















