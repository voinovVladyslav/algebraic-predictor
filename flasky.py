import os
from app import create_app, db
import dotenv


dotenv.load_dotenv()

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
