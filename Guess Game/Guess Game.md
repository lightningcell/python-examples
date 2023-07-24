# <p style="color: aqua">Mad Guess Game</p>
**Author <a style="color: mediumpurple" href="https://github.com/lightningcell">@lightningcell</a>**

<p style="color: whitesmoke">Yes, this guessing game is mad. Because if this was just an ordinary guessing game, 
it wouldn't be this awesome. 
No more words... Check out my code structure and be impressed.</p> 

## What makes it awesome ?
- Definitely, modular structure. I know it sounds basic. But this is good. Because with this simple example, I want to explain how to program comfortably.


Let's look at the project structure:

```shell
   Guess Game/
   ├── gamedata.json
   ├── menus.py
   ├── run.py
   └── utils.py
```

**_NOTE_**: Don't forget to click the arrow on the left side of the file name. You can see the content of the file.

<details>
<summary>
<b style="color: whitesmoke">🔴 gamedata.json</b> <br>
</summary>

   _This file contains the game data. Here is the default content_

```json
   {"MIN_VALUE": 0, "MAX_VALUE": 100, "BEST_SCORE": "0"}
```
</details>
<br>

<details>

<summary>
<b>🟢 utils.py</b> 
</summary>
    <br>

   _This file contains the utility functions. We don't want to see utility functions chilling around.
   Probably, the file we're working with is already messed up. So, we can put them in a separate file._ <br>

   **An example from utils.py**:
   ```python
   def set_game_data(**kwargs) -> dict:
       data = get_game_data()
       for key in kwargs:
           data[key] = kwargs[key]
   
       with open("gamedata.json", "w") as data_file:
           data_file.write(json.dumps(data))
   
       return data   

   ```
  
   I'm sure you don't want to see this function in your main file. So, you can import it from utils.py and use it. That's all.
</details>
<br>

<details>
<summary>
<b>🟡 menus.py</b> <br>
</summary>
   
   _This file contains the menu actions of the game. In here, every function represents a menu. They don't
   affect each other. So, you can add or remove menus easily._ <br><br>

   This file uses the functions from utils.py. So, you can see the power of modular structure. <br>
   ```python
   from utils import *
   ```
   
   **An example from menus.py**:
   ```python
    def display_settings():
       data = get_game_data()
       print(f"""SETTINGS:
               MINIMUM NUMBER: {data['MIN_VALUE']}
               MAXIMUM NUMBER: {data['MAX_VALUE']}""")
   ```


</details>
<br>

<details>
<summary>
<b>🔵 run.py</b> <br>
</summary>
   
   _This file contains the main flow of the game. When you run this file, you play the game._
   <br>

   So, what makes this file special. Let's look at the code:
   ```python
   def flow():
       WELCOME_MESSAGE = "Welcome to the guessing game."
       print(WELCOME_MESSAGE)
       while True:
           # SHOW MAIN MENU
           action = main_menu()
   
           if action == 1:
               game()
           elif action == 2:
               display_best_score()
           elif action == 3:
                      ......
                      ....
                      ...
```

As you can see, this file is the main flow of the game. It's not messy. It's not complicated. It's just a flow.
And it's really easy to understand. When you want to change something of the game,
you can easily find the place you want to change. And you can change it. That's all.


</details>

## Next Features Challenge 
<p style="color: aquamarine">Created by GitHub Copilot. </p>

   - [ ] Add custom colors with colorama module.
   - [ ] Background music. Yeah, unnecessary but cool.
   - [ ] Add about menu, and display these:
     - [ ] Author
     - [ ] Version
     - [ ] GitHub Repository
     - [ ] License
     - [ ] Contact
     - [ ] Website

## 🌐 Socials:
[![JOIN DEVERDOCK](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&?label=JOIN%20DEVERDOCK&style=for-the-badge&logoColor=white)](https://discord.gg/eJ66WRUNTV) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/hamitlightning) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&style=for-the-badge&logoColor=white)](https://linkedin.com/in/hamitlightning) [![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?logo=stack-overflow&style=for-the-badge&logoColor=white)](https://stackoverflow.com/users/21601433) [![Hackerrank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)](https://www.hackerrank.com/developerflash31?hr_r=)
## 💰 You can help me by Donating:
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/hamidsimsek) 
