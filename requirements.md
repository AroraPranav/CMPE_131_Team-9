## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. User Ratings
6. Bid item
7. See all items available from all of the sellers
8. Find items
9. User profiles
10. Add pictures for items
11. Add items
12. Splash page

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

### Find items (Hemanth Jammalamadaka)
- **Pre-condition:** User is already viewing splash page

- **Actors:** User and Server

- **Trigger:** User clicks on "Find".

- **Primary Sequence:**
  
  1. User clicks on search bar.
  2. User selects "type", "locality" and "city" search parameters of product to narrow down results
  3. User clicks on "Find" to initiate action.
 
- **Primary Postconditions:** User can see a list of all the products that match the search criterion.

### User Profiles (Hemanth Jammalamadaka)
- **Pre-condition:** Should already have an account (), be logged into said account. 

- **Actors:** User and Server

- **Trigger:** User clicks on profile display picture, and consequently "view proflie"

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User clicks on desired user's profile picture.
  3. User clicks on "view profile" to confirm action. 
 
- **Primary Postconditions:** User can see all products listed by the user as well as all the ratings posted by the user.

### User Rating (Pranav Arora)
- **Pre-condition:** Should already have an account, be logged in as a customer, and have already chosen a product. 

- **Actors:** User and Server

- **Trigger:** Customer clicks on "Reviews".

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User clicks on the product they want to buy.
  4. User clicks on "Reviews" to check the user ratings.
 
- **Primary Postconditions:** User will see a list of reviews/comments regarding the product.

- **Alternate Sequence:** 
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User directly clicks on the star logo under the product title. 

### Bid Item (Pranav Arora)
- **Pre-condition:** Should already have an account, be logged in as a customer, and have already chosen a product. 

- **Actors:** User and Server

- **Trigger:** Customer clicks on "Place Bid".

- **Primary Sequence:**
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User clicks on the product they want to bid on.
  4. User clicks on "Place Bid".
  5. User enters the amount for the bid.
  6. User clicks on confirm.
 
- **Primary Postconditions:** User will see that their bid is confirmed and after that they'll see an option on how they will be updated about the bids on the product. 

- **Alternate Sequence:** 
  
  1. User logs into their account.
  2. User chooses to buy a product.
  3. User directly clicks on the "Bid" button under the product title.
  4. User adds the amount to the text box.
  5. User confirms the amount.
