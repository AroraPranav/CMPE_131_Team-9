## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. Change password 
6. Buy item 
7. See all items available from all of the sellers 
8. Find items 
9. User profiles 
10. Add pictures for items 
11. Add items 
12. Filter buttons 

## Non-functional Requirements

1. Compatibility
2. Usability
3. Performance
4. Environmental

## Use Cases
### Login

### Logout

### Create new account

### Delete account

### Add pictures for items  (Eleasha Dela Cruz)
- **Pre-condition:** Need to be login, create a listing, Need an image to upload.

- **Summary:** This feature allows a seller to add photographs to their product.

- **Actors:** User and Server

- **Trigger:** 
    1. Click "Create Listing"
    2. Click "Upload Image"
   
  
- **Primary Sequence:**
    1. User Login 
    2. User create a new listing
    3. User upload image to show
 
    
- **Primary Postconditions:** Users will see a new created listing with images

- **Alternate Sequence:** 
  1. User login
  2. User go to her personal account 
  2. User create listing
  3. User can upload multiple photos

###  See all items available from all of the sellers (Eleasha  Dela Cruz)
- **Pre-condition:** Should already have an account, Logged in as customer, Should have a seller decided.

- **Summary:** This feature allows user to see all the products by the seller.

- **Actors:** User and Server

- **Trigger:** Choose a seller
  
- **Primary Sequence:**
    1. User may login
    2. User can search a seller.
    3. User clicks on "Show all listings"
    
- **Primary Postconditions:** User will see all availble listing 

- **Alternate Sequence:** 
  1. User needs to login
  2. User search the place or the seller
  3. Click on "See all Listing"

### Find items (Hemanth Jammalamadaka)
- **Pre-condition:** User is already viewing splash page
 
- **Summary:** This feature allows user to find a item to buy.

- **Actors:** User and Server

- **Trigger:** User clicks on "Find".

- **Primary Sequence:**
  
  1. User clicks on search bar.
  2. User selects "type", "locality" and "city" search parameters of product to narrow down results
  3. User clicks on "Find" to initiate action.
 
- **Primary Postconditions:** User can see a list of all the products that match the search criterion.

### User Profiles (Hemanth Jammalamadaka)
- **Pre-condition:** Should already have an account , be logged into said account. 

- **Summary:** This feature allows user to view a sellers profile.

- **Actors:** User and Server

- **Trigger:** User clicks on profile display picture, and consequently "view proflie"

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User clicks on desired user's profile picture.
  3. User clicks on "view profile" to confirm action. 
 
- **Primary Postconditions:** User can see all products listed by the user as well as all the ratings posted by the user.

### Change Password (Pranav Arora)
- **Pre-condition:** Should already have an account, be logged in as a customer. 

- **Summary:** This feature allows a user to change the password of their account.

- **Actors:** User and Server

- **Trigger:** Customer enters the new password and clicks on submit.

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User clicks on their profile.
  3. User enters the new password. 
  4. User clicks on "Submit" to update the password.
 
- **Primary Postconditions:** User will see their profile with their listings.

### Buy Item (Pranav Arora)
- **Pre-condition:** Should already have an account, be logged in as a customer, and have already chosen a product. 

- **Summary:** This feature allows a user to buy an item they want to buy.

- **Actors:** User and Server

- **Trigger:** Customer clicks on "Purchase".

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User clicks on purchase item.
  4. User confirms the payment.
 
- **Alternate Sequence:** 
  
  1. User logs into their account.
  2. User goes to the market.
  3. User directly clicks on the "Purchase Item" button in the listing.
  4. User confirms the purchase.

### Add Item (Vincent Pham) ###
- **Summary:** Seller can add items such as their property for sale

- **Pre-condition:** User has signed in to their registered account

- **Actors:** User and Server

- **Trigger:** Seller selects 'Create listing' 

- **Primary Sequence:**

    1. User logs into their account
    2. User selects 'Create Listing'
    3. User inputs the information required for the listing (Location, property type, price, bid/no bid (see use case "Bid Item), a picture (see use case "Add pictures for Items")
    4. User presses submit
    5. Server receives that listing and saves it into the database
    6. User logs out and closes the tab

- **Primary Post-condition:** Listing is received in the database to be queried by users

- **Alternative Sequence:** 

    1. User logs into their account
    2. User selects 'Create Listing' 
    3. User does not input enough information required for the listing
        - Server displays an error message to the user
        - Server prompts user to enter all required information
        
### Filter Buttons (Vincent Pham)
- **Summary:** These filter buttons allow a user to search the place according to their needs.

- **Pre-condition:** User should be loggend in to their account.
 
- **Actors:** User and Server

- **Trigger:** User logs in and come sto the home page.

- **Primary Sequence:**

    1. User logs into their account.
    2. User navigates to Home.
    3. User clicks on the filter button to search according to their needs.
    4. Server checks database for houses that match the entry.
    5. Server shows available houses on sale in the area.

### Compatibility
- This website is compatible on Google Chrome.

### Usability
- This is a basic marketplace website where people can buy or sell products

### Performance
- Every action by a user is responded within 5 seconds. 

### Environmental
- The system will be working on a computer and a cell phone which has google chrome as their browser.

