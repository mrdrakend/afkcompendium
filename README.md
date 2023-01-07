# AFK Compendium

Hello, Esperia!

Welcome to AFK Compendium! Your free and easy-to-use source of information outside Lilith's game!

So far we have only general information about all heroes in the game (including Legendary & Common), but our plan is to go further and create a standardized All-in-One application.

This is my first project and is being updated frequently. Be sure to visit this repo to check for new content and layout changes.

## Usage

If you wish to execute it locally, be sure to have PySide6 lib and the data.py file.

## How have things been made so far

As said before, this is my first project. To begin, I made a python version of [this project](https://github.com/venanciotayna/pokedex) through [this tutorial](https://www.youtube.com/watch?v=0GJj9mi--5g). I used Tkinter to do it but then decided to change the project to Qt. You can still access the [Tkinter main](https://github.com/mrdrakend/afkcompendium/blob/main/history/main%20tkinter.py).

### Dictionary

Being the most complex part to create, the info to fill the dictionary was gathered by using [one file](https://github.com/mrdrakend/afkcompendium/blob/main/history/support/html%20downloader.py) to download all heroes HTML from Wiki Fandom and [another](https://github.com/mrdrakend/afkcompendium/blob/main/history/support/png%20downloader.py) to download hero images and signature items.

As the HTML code doesn't have a standard structure, to gather hero info and make the entire dictionary, I've used my ETL skills combined with Excel. So far this method is also the most effective to me when it comes to Dictionary updates.

### Layout

The layout was made using Qt. The current layout isn't final and should suffer several changes in the future

## Credits

I would like to point out some people who should be on this section:

My wife, for supporting me all this time and for always pushing me forward! 😘

Telegram's [Python Brasil Group](https://t.me/pythonbr). You guys have been helping me a lot when I get stuck between walls with no hope. 😆

My AFKA's Guild, Camelot, got thrilled when I first posted the results of my work and is always asking for updates. You guys rock! 🤩