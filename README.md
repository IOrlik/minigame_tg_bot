# minigame_tg_bot

-------------
Telegram mini-game mod is a small battle happening inside your telegram chat. You create the characters, and then each of them is randomly making turns. Implementation of random functions make it so the outcome of the battle is always unique so it's more interesting to watch. 
Also use of OOP allows modifying the code in order to create new characters with new abilities and so on. 
--------------

Handlers handles all of user's inputs. So if a user clicks a button to create a character, this action is managed by commands if it's a general info button, for example help, or by callbacks if it's connected to the battle, like create new character. 

Keyboard is all the buttons seen in telegram's chat. 

Data.py contains all possible names of characters. Each name is chosen randomly. 

antiflood.py manages all flood from the user.

fight.py contains the fight itself, all the characters, their abilities and so on are written here. 

