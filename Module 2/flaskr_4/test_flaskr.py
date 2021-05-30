import os
import unittest
import json

from flaskr import create_app
from models import setup_db, Book

class BookTest