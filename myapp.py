from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import gunicorn

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'e4808c3477f4b92fc8951c8a009b1e7fafa7fa92c7264ce1'  #  a random key

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


class CVEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(100), nullable=False)
    work_education = db.Column(db.String(100), nullable=False)
    position_degree = db.Column(db.String(100), nullable=False)
    organization_institution = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    key_responsibilities_education = db.Column(db.Text, nullable=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.cli.command('init-db')
def init_db():
    """Create the database tables."""
    db.create_all()
    print("Initialized the database.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    cv_entries = CVEntry.query.all()
    return render_template('about.html', cv_entries=cv_entries)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('thank_you'))  
    return render_template('contact.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_detail.html', article=article)

@app.route('/portfolio')
def portfolio():
    articles = Article.query.all()
    return render_template('portfolio.html', articles=articles)



if __name__ == '__main__':
    app.run(debug=True)
