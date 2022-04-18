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
