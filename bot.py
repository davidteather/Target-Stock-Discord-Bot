import discord
import asyncio
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import random

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        self.outOfStock = []
        self.checkUrls = []
        super().__init__(*args, **kwargs)


    def checkStock(self, DPCI, zipcode):
        # Selenium stuff

        with open('proxies.txt', 'r') as proxies:
            proxiesArray = proxies.readlines()

        proxyADDR = random.choice(proxiesArray)

        desired_capability = webdriver.DesiredCapabilities.FIREFOX
        desired_capability['proxy'] = {
            "proxyType": "manual",
            "httpProxy": proxyADDR,
            "ftpProxy": proxyADDR,
            "sslProxy": proxyADDR
        }

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(desired_capabilities=desired_capability,options=options, executable_path=r'geckodriver.exe')
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)

         # Tests proxy
        validProxy = True


        # Gets webpage
        if validProxy == True:
            driver.get("https://brickseek.com/target-inventory-checker/")
            time.sleep(1)
            driver.find_element_by_id('inventory-checker-form-sku').send_keys(DPCI)
            driver.find_element_by_id('inventory-checker-form-zip').send_keys(zipcode)
            driver.find_elements_by_xpath('//button')[1].click()
            time.sleep(2)

            # Product Stats
            img = driver.find_element_by_xpath('//div/img').get_attribute('src')
            time.sleep(0.2)
            productUrl = driver.find_elements_by_xpath("//a[@class='item-overview__actions-item']")[1].get_attribute('href')

            # Gets the near stores
            store1 = driver.find_elements_by_xpath("//div[@class='table__row']")[0]
            store2 = driver.find_elements_by_xpath("//div[@class='table__row']")[1]


            stock1 = driver.find_elements_by_xpath("//div[@class='table__row']/div[@class='table__cell inventory-checker-table__availability']/div/div/span")[0].text.strip()
            addr1 = driver.find_elements_by_xpath("//div[@class='table__row']/div[@class='table__cell table__cell--align-left inventory-checker-table__store']/div/address")[0].text.strip().replace("Google Maps", "").replace("Apple Maps", "")


            stock2 = driver.find_elements_by_xpath("//div[@class='table__row']/div[@class='table__cell inventory-checker-table__availability']/div/div/span")[1].text.strip()
            addr2 = driver.find_elements_by_xpath("//div[@class='table__row']/div[@class='table__cell table__cell--align-left inventory-checker-table__store']/div/address")[1].text.strip().replace("Google Maps", "").replace("Apple Maps", "")

            driver.quit()

            if stock1 == "In Stock":
                return (False, True, img, addr1, "Yes", productUrl)
            elif stock2 == "In Stock":
                return (False, True, img, addr2, "Yes", productUrl)
            elif stock1 == "Limited Stock":
                return (False, True, img, addr1, "Limited Stock", productUrl)
            elif stock2 == "Limited Stock":
                return (False, True, img, addr1, "Limited Stock", productUrl)
            else:
                return (False, False, img, addr1, "No", productUrl)



    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!target'):
            text = message.content

            (outofStock, inStore, img, address, msg, url) = self.checkStock(text.split("!target ")[1].split(" ")[0], text.split("!target ")[1].split(" ")[1])

            embed=discord.Embed(title=text.split("!target ")[1].split(" ")[0], url=url)
            embed.set_thumbnail(url=img)
            embed.add_field(name="In Stock?", value=msg, inline=True)
            embed.add_field(name="Location", value=address, inline=True)
            await message.channel.send(embed=embed)

with open('settings.json', 'r') as data:
    json = json.load(data)
    token = json['discord_token']

client = MyClient()
client.run(token)