# this allows invalid characters to be detected
def has_invalid_characters(string):
    valid = 'abcdefghijklmnopqrstuvwxyz0123456789.'

    for character in string:
        if character not in valid:
            return True
    return False


# .count is used to make sure each email address only use one @ sign
def is_valid(email):
    if email.count("@") != 1:
        return email + " is invalid"

# this checks that the prefix of the email is not left empty
    prefix, domain = email.split("@")

    if len(prefix) == 0:
        return email + " is invalid"

# this check that the domain contains dots e.g .com
    if domain.count(".") != 1:
        return email + " is invalid"

# makes sure the domain name and extension are not empty e.g gmail.com
    domain_name, extension = domain.split(".")

    if len(domain_name) == 0:
        return email + " is invalid"

    if len(extension) == 0:
        return email + " is invalid"

# here the invalid characters function is used to check for invalid characters in the prefix and domain
    if has_invalid_characters(prefix):
        return email + " is invalid"

    if has_invalid_characters(domain):
        return email + " is invalid"

    return email + " is valid"


emails = [
    "seynab@example.co.uk",
    "saynab@outlook.com",
    "saynab@gmail",
    "not an email",
    "invalid@email",
    "s>@",
    "saynab@@example.com",
    "saynab@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]
for email in emails:
    print (is_valid(email))