import random

def generate_otp(length=6):
    """Generates a random OTP (One-Time Password) of the specified length."""
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

# Example usage
otp_length = 6  # You can change this to generate OTPs of different lengths
otp = generate_otp(otp_length)
print(otp)

# you can also save the generated OTP to a file if needed. Here's how you can do that:

with open('otp.txt', 'w') as file:
    file.write(otp)