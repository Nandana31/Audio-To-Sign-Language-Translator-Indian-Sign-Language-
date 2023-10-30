#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A2SL.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Try installing "
            "your PYTHONPATH environment variable and don't "
            "forget to activate a virtual environment"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
