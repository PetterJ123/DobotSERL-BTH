# This file is for using the claw attachment

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

# enables the gripper
enable_ctrl = 1
on_status = 1
dType.SetEndEffectorGripper(api, enable_ctrl, on_status, 1)

# stack to take objects from
# ==========================
amt_stack2 = 3
stack2_height = 0
#===========================

def use_claw():
    while(True):
        BLOCK_HEIGHT /= 2
        dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK2X, STACK2Y, STACKZ, rEndEff, 1)

        on_status = 1
        dType.SetEndEffectorGripper(api, enable_ctrl, on_status, 1)
        on_status = 0

        if amt_stack2 > 0:
            stack2_height = amt_stack2 * BLOCK_HEIGHT
            STACK2_TOP = stack2_height + BOTTOM
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK2X, STACK2Y, STACK2_TOP, rEndEff, 1)
            amt_stack2 -= 1
            dType.SetPTPCommonParams(api, 100, 200)
        else:
            enable_ctrl = 0
            on_status = 0
            dType.SetEndEffectorGripper(api, enable_ctrl, on_status, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, homeX, homeY, homeZ, rEndEff, 1)
            break

        dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, STACK1X, STACK1Y, STACKZ, rEndEff, 1)

        if amt_stack2 >= 0:
            if amt_stack1 == 0:
                STACK1_TOP = BOTTOM + BLOCK_HEIGHT
            elif amt_stack1 > 0:
                STACK1_TOP += BLOCK_HEIGHT
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, STACK1X, STACK1Y, STACK1_TOP, rEndEff, 1)

        dType.SetEndEffectorGripper(api, enable_ctrl, on_status, 1)
        amt_stack1 += 1

        dType.SetPTPCommonParams(api, 100, 200)