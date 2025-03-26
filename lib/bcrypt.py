import bcrypt

def hashpw (password):
    """
    Genera un hash seguro para la contraseña proporcionada.
    """
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash

def checkpw (userPassword, password):
    """
    Verifica si una contraseña coincide con su hash almacenado.
    """
    return bcrypt.checkpw(userPassword.encode("utf-8"), password)
