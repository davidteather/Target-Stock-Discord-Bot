# Target-Stock-Discord-Bot

This is a discord bot that was comissioned to find products using a specific DHCI number of a product for [target](https://www.target.com). 

## Getting Started

The following instructions will help you get you running this software.

### Prerequisites

To install the python requirements please run the command below.

```
pip install discord.py asyncio selenium
```

### Installing

Have python 3.x installed. This was tested with 3.7.3

You need to have firefox installed. Download [here](https://www.mozilla.org/en-US/firefox/new/)

### Linux
```
sudo apt install firefox
```

You also need to download geckodriver and include it in your path. Download it [here](https://github.com/mozilla/geckodriver/releases)

### Linux
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz 
tar -C /opt -xzf /tmp/geckodriver.tar.gz 
sudo chmod 755 /opt/geckodriver 
sudo ln -fs /opt/geckodriver /usr/bin/geckodriver 
sudo ln -fs /opt/geckodriver /usr/local/bin/geckodriver
```

or the combined command
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz && tar -C /opt -xzf /tmp/geckodriver.tar.gz && sudo chmod 755 /opt/geckodriver && sudo ln -fs /opt/geckodriver /usr/bin/geckodriver && sudo ln -fs /opt/geckodriver /usr/local/bin/geckodriver
```

### Windows

First download the geckodriver [here](https://github.com/mozilla/geckodriver/releases), tested with version v0.24.0

Then add geckodriver to your path [here's](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) a tutorial on how to do that.


### Configuring some things

Example settings.json
```
{
    "discord_token": "123456798"
}
```

**discord_token** Your discord API token for your bot. [Here](https://www.writebots.com/discord-bot-token/) is a good article on how to get your bot's api token.

### Executing the program

Once you have all of the json files configured as you would like simpily run the command below.

```
python main.py
```

To use the bot just type in any channel the bot has permission to just use
```
!target-search <DHCI> <ZipCode>
```

Example
```
!target-search 049-08-0605 20001
```

## Built With

* [Python 3.7](https://www.python.org/) - The language used

## Authors

* **David Teather** - *Initial work* - [davidteather](https://github.com/davidteather)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details