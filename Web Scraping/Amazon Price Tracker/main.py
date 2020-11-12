import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from contants import TO_EMAIL


# TODO 47
# url = input("Enter the amazon product url: ")
url = "https://www.amazon.in/AMD-RyzenTM-3200G-RadeonTM-Graphics/dp/B07STGHZK8/ref=sr_1_3?dchild=1&keywords=3200g&qid=1604995530&sr=8-3"
# http://myhttpheader.com/
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice")
if price != None:
    price_text = price.get_text()
    price_num =  float(price.split(" ")[1])
    print(price_num)

    title = soup.find(id="productTitle").get_text().strip()
    print(title)

    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        email = ""
        password = ""
        result = connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )