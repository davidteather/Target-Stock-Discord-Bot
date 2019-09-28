import discord
import asyncio
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        self.outOfStock = []
        self.checkUrls = []
        super().__init__(*args, **kwargs)

    def checkStock(self, DPCI):
        # Selenium stuff
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)

        # Gets webpage
        driver.get("https://www.target.com/s?searchTerm=" + str(DPCI))
        time.sleep(1)

        outofStock = True
        try:
            url = driver.find_element_by_xpath("//div[@class='h-display-flex']/a").get_attribute('href')
        except:
            url = "google.com"
            outofStock = True
            
        
        driver.get(url)
        time.sleep(1)

        try:
            thing = driver.find_element_by_xpath('//div[@data-test="store-out-of-stock-message"]')
            outofStock = True
        except:
            try:
                thing = driver.find_element_by_xpath('//span[@class="h-text-greenDark h-display-inline-block h-text-bold"]')
                outofStock = False
                inStore = True
            except:
                thing = driver.find_element_by_xpath('//span[@class="h-text-orangeDark h-display-inline-block h-text-bold"]')
                inStore= False

        driver.quit()

        return (outofStock, inStore)



    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!target-search'):
            text = message.content

            (outofStock, inStore) = self.checkStock(text.split("!target-search ")[1])

            if outofStock == True and inStore == False:
                await message.channel.send("That product is not in stock!")
            elif inStore == True:
                await message.channel.send("That product is in stock!")
            else:
                await message.channel.send("That product is in stock!")

with open('settings.json', 'r') as data:
    json = json.load(data)
    token = json['discord_token']

client = MyClient()
client.run(token)