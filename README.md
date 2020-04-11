# MacGuyver maze

## Help Mac Guyver to escape!

Simple maze that where you'll have to take all the items in the game before getting in front of the guardian.

If you have all of them then you'll win, otherwise 
you'll lose.

### Prerequisites

You'll need python3+ and pygame 1.9+ to play the game.

Python3 should be already intall on most OS but if it's not the case you can install it and pip by doing the following

Debian based
 
```
sudo apt-get install python3 python3-pip
```

For windows and mac user you can find it here:

Windows: [Python3 for windows](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe)
MacOS: [Python3 for Mac](https://www.python.org/ftp/python/3.7.7/python-3.7.7-macosx10.9.pkg)

Pipenv allows you to install pygame as a independent environnement allows more flexibility. To install it enter this command:

```
sudo pip3 install pipenv
```

After that you just need to run this command in the project folder. In my case I intalled pygame 2.0.0.dev6:

```
pipenv install pygame==2.0.0.dev6
```

## HOW TO PLAY THE GAME

To play the game you have to be in the pipenv shell. To do that enter:

```
pipenv shell
```

From there, you can run the program by doing the following:

```
python main.py
```

Enjoy!

