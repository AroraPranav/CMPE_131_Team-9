## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. Change account password 
6. Buy a property
7. Query all property listings published to the marketplace
8. Input text to query for a property listing based on specific properties of the listing (2881 Address Lane)
9. View the user's registered properties
10. Add pictures for property listings
11. Register a property listing
12. Search for properties based on general attributes (apartment, city)

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

### Add pictures for property listings  (Eleasha Dela Cruz)
- **Pre-condition:** Need to be login, navigate to 'Sell' page, need an image to upload.

- **Summary:** After inputting their Property's information, they can add a picture of the property to give a better idea of what their house looks like.

- **Actors:** User and Server

- **Trigger:** 
    1. Click "Sell"
    2. Click "Upload Image"
    3. Browse file system for desired image
    4. Submit
   
  
- **Primary Sequence:**
    1. User Login 
    2. User selects 'Sell' to create a listing
    3. User inputs general property information before selecting 'upload image'
    4. User inputs image
    5. System checks if proper file format
    6. System stores image to database
 
    
- **Primary Postconditions:** Users will see a new created listing with images

- **Alternate Sequence:** 
  1. User logs in
  2. User go to their personal account 
  2. User edits property listing
  3. System checks if proper file format
  4. System stores image to database

###  Query all property listings published to the marketplace (Eleasha  Dela Cruz)
- **Pre-condition:** Reached webpage, selected marketplace

- **Summary:** This feature allows user to see all the products by the sellers.

- **Actors:** User and Server

- **Trigger:** User navigates to Marketplace
  
- **Primary Sequence:**
    1. User may login
    2. User clicks on 'Marketplace'
    3. System queries all listings in the database
    4. System displays the queries to the user
    
- **Primary Postconditions:** User will see all available listing 

### Input text to query for a property listing based on specific properties of the listing (Hemanth Jammalamadaka)
- **Pre-condition:** User has reached webpage main search bar
 
- **Summary:** This feature allows user to find an item based on their specific input text like an address or zipcode

- **Actors:** User and Server

- **Trigger:** User clicks on "Search bar".

- **Primary Sequence:**
  
  1. User clicks on search bar.
  2. User selects category of "zipcode", "locality" and "city" search parameters of product to narrow down results
  3. User inputs text for that selected category
  4. Systems searches the database in that category for the inputted text
  5. System displays the listings based on the input

- **Alternate Sequence:** 
  1. User clicks on search bar
  2. User selects category of "Number of beds" search parameter of product to narrow down results
  3. User inptus text for that selected category
  4. System searches the database in that category for the inputted text
  5. System does not find the query, and lets the user know no entries were found

- **Primary Postconditions:** System has queried the database, and returned a result

### View the user's registered properties (Hemanth Jammalamadaka)
- **Pre-condition:** Should already have an account , be logged into said account. 

- **Summary:** This feature allows user to view a sellers profile.

- **Actors:** User and Server

- **Trigger:** User clicks on profile display picture, and consequently "view proflie"

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User clicks on desired user's profile picture.
  3. User clicks on "view profile" to confirm action. 
  4. User changes their password

- **Alternate Sequence:** 
  1. User logs into their account
  2. User clicks on desired user's profile picture
  3. User deletes their account
 
- **Primary Postconditions:** User can see all products listed by the user, and change their account settings

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
  4. System checks if they have enough money in the account
  5. User owns the property
 
- **Alternate Sequence:** 
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User clicks on purchase item.
  4. System checks if they have enough money in the account
  5. System denies purchase of the property

### Register a property listing (Vincent Pham) ###
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
        
### Search for properties based on general attributes (Vincent Pham)
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

