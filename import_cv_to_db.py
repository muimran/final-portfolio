import pandas as pd
from myapp import app, db, CVEntry, Article  # Importing Article model as well


# Function to import CV entries
def import_cv_entries():
    cv_data = pd.read_csv('cv_table.csv')  # Adjust filename/path as needed
    cv_entries = cv_data.to_dict(orient='records')

    # Delete existing CV entries and add new ones
    CVEntry.query.delete()
    for entry in cv_entries:
        new_entry = CVEntry(**entry)
        db.session.add(new_entry)

# Function to import articles
def import_articles():
    articles_data = pd.read_csv('articles.csv', encoding='cp1252')  # Adjust filename/path as needed
    articles = articles_data.to_dict(orient='records')

    # Delete existing articles and add new ones
    Article.query.delete()
    for article in articles:
        new_article = Article(**article)
        db.session.add(new_article)

# Run the import functions within the app context
with app.app_context():
    import_cv_entries()
    import_articles()
    db.session.commit()
