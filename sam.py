from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)



def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = "".join(random.choice(characters) for _ in range(length))
    return password

    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) != length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password



def index():
    if request.method == "POST":
        length = int(request.form["length"])
        include_numbers = "numbers" in request.form
        include_special = "special" in request.form

        # Generate the password
        password = generate_password(length, include_numbers, include_special)
        return render_template("index.html", password=password)

    return render_template("index.html", password=None)

if __name__ == "__main__":
    app.run(debug=True)


