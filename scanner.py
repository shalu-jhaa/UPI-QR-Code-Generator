import qrcode

# Input from user
upi_id = input("Enter your UPI ID: ")
name = input("Enter Recipient Name: ")
amount = input("Enter Amount (optional, press Enter to skip): ")
note = input("Enter Note/Message (optional, press Enter to skip): ")

# Base UPI payment link
upi_url = f"upi://pay?pa={upi_id}&pn={name}"

# Add amount if provided
if amount.strip() != "":
    upi_url += f"&am={amount}"

# Add note if provided
if note.strip() != "":
    upi_url += f"&tn={note}"

# Add a fixed merchant code (optional, but safe)
upi_url += "&cu=INR"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(upi_url)
qr.make(fit=True)

# Customize file
img = qr.make_image(fill_color="black", back_color="white")

# save file
filename = "upi_payment_qr.png"
img.save(filename)

print(f"\n QR Code generated successfully! Saved as {filename}")
img.show()
