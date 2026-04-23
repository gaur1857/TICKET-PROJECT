pip install bcrypt
import bcrypt

# hash
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# verify
bcrypt.checkpw(password.encode(), hashed)
