from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm, changePasssword, createListing, deleteUser, searchListing
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home', methods=["POST", "GET"])
def home_page():
    form = searchListing()
    purchase = PurchaseItemForm()
    if request.method=="POST":
        search = request.form
        #SEARCH BY CITY
        searches = Item.query.filter(Item.city==form.query.data).all()
        print(searches)
        return render_template('market.html', items=searches, form=purchase)
    return render_template('home.html', form=form)

#               BUTTON REDIRECTS                    #

@app.route('/home', methods=["POST", "GET"])
def listing_bed():
    form = searchListing()
    purchase = PurchaseItemForm()
    if request.method=="POST":
        search = request.form
        #SEARCH BY BED
        searches = Item.query.filter(Item.bed==form.query.data).all()
        print(searches)
        return render_template('market.html', items=searches, form=purchase)
    return render_template('home.html', form=form)

@app.route('/home', methods=["POST", "GET"])
def listing_bath():
    form = searchListing()
    purchase = PurchaseItemForm()
    if request.method=="POST":
        search = request.form
        #SEARCH BY BATH
        searches = Item.query.filter(Item.bath==form.query.data).all()
        print(searches)
        return render_template('market.html', items=searches, form=purchase)
    return render_template('home.html', form=form)

@app.route('/home', methods=["POST", "GET"])
def listing_zipcode():
    form = searchListing()
    purchase = PurchaseItemForm()
    if request.method=="POST":
        search = request.form
        #SEARCH BY ZIPCODE
        searches = Item.query.filter(Item.zip==form.query.data).all()
        print(searches)
        return render_template('market.html', items=searches, form=purchase)
    return render_template('home.html', form=form)


#               BUTTON REDIRECTS                    #

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    form = PurchaseItemForm()
    items = Item.query.all()

    return render_template('market.html', items=items, form=form) 


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, firstName=form.firstName.data, lastName=form.lastName.data,
                              email_address=form.email_address.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


@app.route('/city')
def listing_city():
    return render_template('listing_city.html')



@app.route('/apartments')
def listing_apartments():
    return render_template('listing_apartments.html')


@app.route('/sell', methods=["POST", "GET"])
@login_required
def add_item():
    form = createListing()
    items = Item.query.filter(Item.owner == current_user.username).all()
    # print(current_user.username)
    if request.method == "POST":
        listing = request.form
        listing_to_create = Item(price=form.price.data, description=form.description.data, owner=current_user.username, address=form.address.data, city= form.city.data, zip=form.zipcode.data, bed = form.bed.data, bath=form.bath.data)
        db.session.add(listing_to_create)
        db.session.commit()
        for item in items:
            a= str(f'Owner: {item.owner}, Address: {item.address}')
        return redirect('/sell')
    return render_template('createListing.html', form=form)


@app.route('/profile', methods = ['POST', 'GET'])
def getprofile():
    
    items = Item.query.filter(Item.owner == current_user.username).all()
    delete_user = deleteUser()
    form_change_password = changePasssword()

    if request.method == "POST":
        if form_change_password.validate_on_submit():
            new_password = form_change_password.new_password.data
            current_user.change_password(new_password)

            
        elif delete_user.validate_on_submit():
            db.session.delete(current_user)
            db.session.commit()
            flash("User deleted successfully")
            return redirect(url_for('login_page'))
    
    return render_template('profile.html', items=items, delete_user = delete_user, form_change_password = form_change_password)

