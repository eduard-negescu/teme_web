from validare_formular import app
from flask import render_template, url_for, flash, redirect
from validare_formular.forms import RegistrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your account has been created! You are now able to log in', "success")
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)
