import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection


@login_required
def list_books(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            b.id,
            b.title,
            b.isbn,
            b.author,
            b.year_published,
            b.librarian_id,
            b.location_id
        from libraryapp_book b
        """)

        all_books = db_cursor.fetchall()

    template_name = 'books/list.html'
    return render(request, template_name, {'all_books': all_books})