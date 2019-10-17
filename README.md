# Dobot project at SERL Lab at BTH

## What is this?
This is a script that I have developed for a customer at BTH (Blekinge Tekniska Högskola in Sweden), the goal of the script is to move LEGO-bricks from some sort of stack to 
build a structure of some sort. The minimum goal is to move the bricks stacked from one position to another. If I during the course time manage to develop a more 
dynamic structure of it, giving the user an easier way of giving the Dobot Magician a structure it is supposed to build.

Feel free to improve this repository as you wish!

## Installation

**Attention!**
Before you begin installing any Dobot related, you should make sure you have Python installed. This link should help:
[Python 3 Installation]
(https://docs.python-guide.org/starting/install3/osx/)

### Windows

1. Download and install [DobotStudio](https://www.dobot.cc/downloadcenter/dobot-magician.html)
    - Choose the download corresponding to the version of Windows you use.

### OS X

1. Download and install [DobotStudio](https://www.dobot.cc/downloadcenter/dobot-magician.html)

- Download this repository (with https or ssh)

- Open DobotStudio and click on script (You may need to change language on first start, do so in top right corner).

- In the "script-mode" open the moveblock.py script that you downloaded from this repository.

- Connect the Dobot with "Connect"-button in top left corner. (Given you have already set up the Dobot Magician).

### Setting up Dobot Magician

Read this for overview of what parts the Dobot magician contains and a better guide of assembling: [Dobot Magician](https://github.com/SERLatBTH/DobotMagician)

1. Unpack Dobot Magician, all cables, suction cup, compressor module and wifi module (Wireless-2)

- Attach the suction cup attachment to the front of the arm, held in a screw under front of arm.
   - Connect the green cable into GP1 port on top of arm.

- Connect power cable and USB-B cable to the Dobot at the back.

- Connect the compressor module to the Dobot.
   - Connect the red connector to Dobot's SW1 port.
   - Connect the green connector to Dobot's GP1 port.
   - Connect the tube to the suction-cup attachment.

- Connect the wireless module to the Dobot's communication interface

- Connect USB-cable to your computer and push start button on Dobot base (chrome button).

## Connecting to the Dobot Magician and running the code
1. Open DobotStudio and press the script button (You also may need to change language on first start, top right corner).

- Open the script you downloaded from this repository.
- Want to connect wirelessly? Read [this](help)
- Plug in the USB-cable to your computer.
- When there is an entry in the drop-down list (next to connect-button) you can press the connect button

### Understanding the code
Since there is no user interface and the code is dependent on the DobotStudio software the only way to interact with the robot is to edit the code. Maybe GUI will be a feature in the future.

The variable to keep track of is `amt_stack2`, this is the amount of LEGO-bricks in the stack the robot shall pick from.

#### Running the code
First you need to place the LEGO-bricks at a specific coordinate and you probably need to do a test run to take note of where it will pick up bricks. The bricks is 2x2 LEGO-bricks and shall be placed on the side, 15 centimeters away from the base on the side of the power button.

Now you just need to decide how many LEGO-bricks there should be in the stack the robot shall pick from and write this value at the `amt_stack2` variable.
