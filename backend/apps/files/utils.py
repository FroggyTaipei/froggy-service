import string
import random
import os


def generate_filename(filename):

    def random_string(length=6):
        """Generate a random string of letters and digits """
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))

    name, ext = os.path.splitext(filename)
    return f'{name}-s{random_string()}{ext}'
