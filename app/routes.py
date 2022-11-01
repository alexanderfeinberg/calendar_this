from flask import Blueprint, render_template, redirect


bp = Blueprint("main", __name__, '/')


@bp.route('/')
def main():
    return render_template('main.html')
