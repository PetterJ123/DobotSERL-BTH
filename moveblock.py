import clawfunc

homeX = 207
homeY = -5
homeZ = 40
homeR = -3
temp = 0
rEndEff = 21
velrat = 100
accrat = 200

# stack variables
STACK1X = 242.50
STACK1Y = -16.7
STACK2X = -10.4
STACK2Y = 242.3
STACKZ = 117.4
BOTTOM = -71
BLOCK_HEIGHT = 29

# stack to put objects
amt_stack1 = 0
stack1_height = 0
attachment = "suction"	# Change this value to either "claw" or "suction"

# stack to take objects from
# ==========================
amt_stack2 = 3
stack2_height = 0
#===========================

# make sure cmd queue is clear
dType.SetQueuedCmdClear(api)

# start control of endeffector suction cup
enable_ctrl = 1
on_status = 0
dType.SetEndEffectorSuctionCup(api, enable_ctrl, on_status, 1)	# starts control of suction cup

#dtypecoordinateparams
dType.SetPTPCoordinateParams(api,200,200,200,200)

#setptpcommonparams
#(api, velocity ratio, acceleration ratio)
dType.SetPTPCommonParams(api, velrat, accrat)

#setptpjumpparams
#api, jumpheight, zlimit
dType.SetPTPJumpParams(api, 20, 200)

# calibrates the dobot magician
dType.SetHOMEParams(api,  homeX,  homeY,  homeZ,  homeR, 1)
dType.SetHOMECmd(api, temp, 1)

# @param ctrl: enable or disable the control of end effector
# @param onst: start or turn off end effector
def turn_off_end(ctrl, onst):
	dType.SetEndEffectorSuctionCup(api, ctrl,  onst, 1)

# @param x, y, z: coordinates in carteesian system
# @param re: rotational coordinate for end effector
def move_neutral(x, y, z, re):
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, rEndEff, 1)

if attachment == "suction":
	while(True):
		# move arm to stack it is supposed to move objects from (stack2)
		dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK2X, STACK2Y, STACKZ, rEndEff, 1)

		# start suctioncup
		on_status = 1
		dType.SetEndEffectorSuctionCup(api, enable_ctrl, on_status, 1)
		on_status = 0

		# change speed
		#dType.SetPTPCommonParams(api, 20, 200)

		# move straight down
		if amt_stack2 > 0:
			stack2_height = amt_stack2 * BLOCK_HEIGHT
			STACK2_TOP = stack2_height + BOTTOM
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK2X, STACK2Y, STACK2_TOP, rEndEff, 1)
			amt_stack2 -= 1
			dType.SetPTPCommonParams(api, 100, 200)
		else:
			turn_off_end(0, 0)	# Turns off end effector
			move_neutral(homeX, homeY, homeZ, 0)		# move to a neutral position
			break

		# move arm to stack it is supposed to put objects (stack1)
		dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK1X, STACK1Y, STACKZ, rEndEff, 1)

		# move arm downward
		if amt_stack2 >= 0:
			#dType.SetPTPCommonParams(api, 20, 200)

			if amt_stack1 == 0:
				STACK1_TOP = BOTTOM + BLOCK_HEIGHT
			elif amt_stack1 > 0:
				STACK1_TOP += BLOCK_HEIGHT

			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK1X, STACK1Y, STACK1_TOP, rEndEff, 1)

		# executes the turnoff of suction cup
		dType.SetEndEffectorSuctionCup(api, enable_ctrl, on_status, 1)
		amt_stack1 += 1

		dType.SetPTPCommonParams(api, 100, 200)
elif suction == "claw":
	use_claw()
	
# === FEATURES TO BE DEVELOPED ===
# - Functionality to also use the gripper-attachment
# - Functionality to specify a user made structure and then the robot will build it
# - This file shall only contain code for the suctioncup-attachment, like done with claw-attachment
# - Main.py file shall call the other modules (suctionfunc.py, clawfunc.py)
# - 
