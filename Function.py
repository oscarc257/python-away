def greet(person):
    return f"Hello there, {person}"


def divide(a, b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a and b must be integrers!'



def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        --------------------
        body: {body}
    """
    print(email)
send_email(subject="MEOW", to_email="scuanch@gmail.com",
           from_email="julissa@humans.com", body="How are you Scuanch?")    


def power(num, power=2):
    return num ** power