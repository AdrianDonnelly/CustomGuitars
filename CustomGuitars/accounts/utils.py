import pyotp
import qrcode
from datetime import datetime,timedelta
from django.core.mail import send_mail

def send_otp(request):
    totp=pyotp.TOTP(pyotp.random_base32(),interval=60)
    otp = totp.now()
    request.session['otp_secret_key']=totp.secret
    valid_date = datetime.now()+timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)
    print(f"One Time Password:{otp}")
    return otp
    
def email_otp(otp,user_email):
    subject = "2FA token"
    message = "2FA token:"+otp
    from_email = "CustomGuitars@test.com"
    to_email = [user_email]
    send_mail(subject, message, from_email, to_email)
    
def generate_qr(data, issuer_name, account_name):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    
    uri = totp.provisioning_uri(
        name=account_name,
        issuer_name=issuer_name,
    )
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
    
    
    qr.add_data(uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img