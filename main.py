from random import choice
from string import ascii_letters

special_symbols = "!$@&?#"
def password_generator(pass_length,custom_characters="",include_special_symbols=True):
    password=""
    if include_special_symbols:
        all_characters=ascii_letters+custom_characters+special_symbols
    else:
        all_characters=ascii_letters+custom_characters
    for i in range(pass_length):
        password+=choice(all_characters)
    return password