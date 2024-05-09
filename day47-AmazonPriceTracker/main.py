import requests
from bs4 import BeautifulSoup
import smtplib

YOUR_SMTP_ADDRESS="smtp.gmail.com"
YOUR_EMAIL=""
YOUR_PASSWORD=""
URL = "https://www.flipkart.com/tyy/4io/~cs-f80dhsumkt/pr?sid=tyy%2C4io&collection-tab-name=realme12x+5G"
# Send a GET request to the URL
response = requests.get(URL)
print(response.status_code)
# Check if the request was successful
if response.status_code == 200:
    print("codework1")
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the price
    item = soup.find('div', class_="Nx9bqj _4b5DiR")
    print("codework2")
    # Check if the item is found
    if item:
        # Extract and print the price
        item_price = item.get_text()
        item_price = int(item_price.replace('₹', '').replace(',', '').strip())
        print(item_price)

        title = soup.find('div', class_="KzDlHZ").getText().strip()

        BUY_PRICE = 90000
        print("codework3")
        if item_price < BUY_PRICE:
            message = f"{title} is now {item_price}"
            print("codework4")
            with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
                connection.starttls()
                result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
                connection.sendmail(
                    from_addr=YOUR_EMAIL,
                    to_addrs=YOUR_EMAIL,
                    msg=f"Subject: AMAZONN PRICE ALERT!\n\n{message}\n{URL}".encode("utf-8")
                )
            print("message should be sent")
    else:
        print("Price not found on the page.")




