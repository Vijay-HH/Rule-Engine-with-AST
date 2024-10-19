from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_name = db.Column(db.String(100), nullable=False)
    rule_ast = db.Column(db.Text, nullable=False)  # Store AST as text (JSON)

    def save_ast(self, ast_node):
        self.rule_ast = json.dumps(ast_node.__dict__)  # Convert AST Node to JSON format

    def load_ast(self):
        return json.loads(self.rule_ast)  # Convert stored JSON back to AST Node representation


def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
