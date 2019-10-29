# Dobot project at SERL Lab at BTH

## What is this?
This is a script that I have developed for a customer at BTH (Blekinge Tekniska Högskola in Sweden), the goal of the script is to move LEGO-bricks from some sort of stack to build a structure of some sort. The minimum goal is to move the bricks stacked from one position to another. If I during the course time manage to develop a more dynamic structure of it, giving the user an easier way of giving the Dobot Magician a structure it is supposed to build.

Feel free to improve this repository as you wish!

The master branch is the "official release" of this project. It has the features that are tested and "guaranteed" to work. The devel branch is branch for development where new features are worked on and pushed to before they can be qualified for "release". 

## Installation

**Attention!**
Before you begin installing any Dobot related, you should make sure you have Python installed. This link should help:
**Windows:**[Python 3 Windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

**Mac OS X:**[Python 3 OS X](https://programwithus.com/learn-to-code/install-python3-mac/)

### Windows

1. Download and install [DobotStudio](https://www.dobot.cc/downloadcenter/dobot-magician.html).
    - Choose the download corresponding to the version of Windows you use.
    - The installation will probably also install drivers for the Dobot, make sure this runs.

2. Download this repository (with https or ssh).

3. Open DobotStudio and click on script (You may need to change language on first start, do so in to right corner).

4. In the "script mode open the moveblock.py script that you downloaded from this repository.

5. Connect the Dobot with "Connect"-button in top left corner. (Given you have already set up the Dobot Magician).

Read under title "Running the code" below to run the code.

### OS X

1. Download and install [DobotStudio](https://www.dobot.cc/downloadcenter/dobot-magician.html)
    - **!!Important!!** In the installation there shall be a folder named attachment, install the drivers located in ``attachment/Drive/Hardware1.0.0.0/Mac/SiLabsUSBDriverDisk.dmg``.

2. Download this repository (with https or ssh).

3. Open DobotStudio and click on script (You may need to change language on first start, do so in top right corner).

4. In the "script-mode" open the moveblock.py script that you downloaded from this repository.

5. Connect the Dobot with "Connect"-button in top left corner. (Given you have already set up the Dobot Magician).

Read under title "Running the code" below to run the code.

### Setting up Dobot Magician

Read this for overview of what parts the Dobot magician contains and a better guide of assembling: [Dobot Magician](https://github.com/SERLatBTH/DobotMagician).

1. Unpack Dobot Magician, all cables, suction cup, compressor module and wifi module (Wireless-2).

2. Attach the suction cup attachment to the front of the arm, held in a screw under front of arm.
   - Connect the green cable into GP1 port on top of arm.

3. Connect power cable and USB-B cable to the Dobot at the back.

4. Connect the compressor module to the Dobot.
   - Connect the red connector to Dobot's SW1 port.
   - Connect the green connector to Dobot's GP1 port.
   - Connect the tube to the suction-cup attachment.

5. Connect the wireless module to the Dobot's communication interface.

6. Connect USB-cable to your computer and push start button on Dobot base (chrome button).

## Connecting to the Dobot Magician and running the code
1. Open DobotStudio and press the script button (You also may need to change language on first start, top right corner).

2. Open the script you downloaded from this repository.
3. Want to connect wirelessly? Read **Connecting wirelessly**.
4. Plug in the USB-cable to your computer.
5. When there is an entry in the drop-down list (next to connect-button) you can press the connect button.

**Connecting wirelessly:** Before doing step 5 above go to settings in DobotStudio (top right corner).
Click on wifi in left menu, there you shall enter the same SSID and password as this computer, then click save.

### Understanding the code
Since there is no user interface and the code is dependent on the DobotStudio software the only way to interact with the robot is to edit the code. Maybe GUI will be a feature in the future.

The variable to keep track of is `amt_stack2`, this is the amount of LEGO-bricks in the stack the robot shall pick from.

#### Running the code
First you need to place the LEGO-bricks at a specific coordinate and you probably need to do a test run to take note of where it will pick up bricks. The bricks is 2x2 LEGO-bricks and shall be placed on the side, 15 centimeters away from the base on the side of the power button.

Now you just need to decide how many LEGO-bricks there should be in the stack the robot shall pick from and write this value at the `amt_stack2` variable.
