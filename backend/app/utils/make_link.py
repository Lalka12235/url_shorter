from random import choices
import string

def generate_code(length: int = 6):
    return ''.join(choices(string.ascii_letters + string.digits, k=length))