homeX = 207
homeY = -5
homeZ = 40
homeR = -3
temp = 0
rEndEff = 21

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

# stack to take objects from
amt_stack2 = 3
stack2_height = 0

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
dType.SetPTPCommonParams(api, 100, 200)

#setptpjumpparams
#api, jumpheight, zlimit
dType.SetPTPJumpParams(api, 20, 200)

# eshtablish home position
dType.SetHOMEParams(api,  homeX,  homeY,  homeZ,  homeR, 1)
dType.SetHOMECmd(api, temp, 1)

while(True):
	# move arm to stack it is supposed to move objects from (stack2)
	dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK2X, STACK2Y, STACKZ, rEndEff, 1)

	# start suctioncup
	on_status = 1
	dType.SetEndEffectorSuctionCup(api, enable_ctrl, on_status, 1)
	on_status = 0

	# change speed
	dType.SetPTPCommonParams(api, 10, 100)

	# move straight down
	if amt_stack2 > 0:
		stack2_height = amt_stack2 * BLOCK_HEIGHT
		STACK2_TOP = stack2_height + BOTTOM
		dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK2X, STACK2Y, STACK2_TOP, rEndEff, 1)
		amt_stack2 -= 1
		dType.SetPTPCommonParams(api, 100, 200)
	else:
		print("Empty stack error, put some blocks in the stack")
		break

	# move arm to stack it is supposed to put objects (stack1)
	dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK1X, STACK1Y, STACKZ, rEndEff, 1)

	# move arm downward
	if amt_stack2 >= 0:
		dType.SetPTPCommonParams(api, 10, 100)

		if amt_stack1 == 0:
			STACK1_TOP = BOTTOM + BLOCK_HEIGHT
		elif amt_stack1 > 0:
			STACK1_TOP += BLOCK_HEIGHT

		dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK1X, STACK1Y, STACK1_TOP, rEndEff, 1)

	# executes the turnoff of suction cup
	dType.SetEndEffectorSuctionCup(api, enable_ctrl, on_status, 1)
	amt_stack1 += 1

	dType.SetPTPCommonParams(api, 100, 200)


# == EXTRA FEATURES ==
# counter for amount of blocks picked up
# after amount reached ceiling, start other section of program
# other section being doing something else like engraving
