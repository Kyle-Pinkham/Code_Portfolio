import maya.cmds as cmds
import random as rand


###### --------------------- OC DON'T STEAL!!!!1!   -------------------------####


armSels=cmds.ls(sl=1)

cmds.addAttr( attributeType="float", longName='FK_IK_Switch', defaultValue=0.5, minValue=0, maxValue=1, hidden=False, readable=True, keyable=True)

class RiggingSetups:
# ------------- Initiate Self ---------------------# 
    def __init__(self):
        self.WhyisPythonWierd = "¯\_(?)_/¯"
        print(self.WhyisPythonWierd)
# ------------- Get Selecitons ---------------------#        
    def getSelections(self):
        sels = cmds.ls(sl=True)
        print(sels)
        return sels
        
# ------------- Link Constraints ---------------------#        
    def LinkConstraints(self, objName, attributeName, constraintName, constraintAtt):
        cmds.connectAttr((objName + "." + attributeName), (constraintName + "." + constraintAtt), f=1)
        
              
# ---TAG: 3JS ------------- Three Joint Setup, From RK to IK and FK -------------#
            
    def ThreeJointSetup(self, RKarmSels):        

        RKarmSels = RKarmSels
        FKJoints = cmds.duplicate(RKarmSels, name = RKarmSels[0]+"_FK")
        IKJoints = cmds.duplicate(RKarmSels, name = RKarmSels[0]+"_IK")
        
        for RKJoint in RKarmSels:
            cmds.select(RKJoint)
            cmds.addAttr( attributeType="float", longName='IK_Weight', defaultValue=1, minValue=0, maxValue=1, hidden=False, readable=True, keyable=True)

            cmds.addAttr( attributeType="float", longName='FK_Weight', defaultValue=1, minValue=0, maxValue=1, hidden=False, readable=True, keyable=True)
            
            
              
        # -- FK setup -- #
        def FKJointSetup(self, fKtoSetup):
           
            ctrlGroupArray = []
            ctrlArray = []
            
            for object in fKtoSetup:
                self.objectPOS = cmds.xform(object, q=1, t=1, ws=True)
                self.objectROT = cmds.xform(object, q=1, ro=1, ws=True)

                self.ctrlName = object + "_Ctrl";
                self.ourControl = cmds.circle( c=(0, 0, 0), n=self.ctrlName)
                self.ourControlGrp = cmds.group(n=(object + "_Ctrl_Grp"), em=True)
                cmds.move(self.objectPOS[0],self.objectPOS[1],self.objectPOS[2], self.ourControlGrp)
                cmds.rotate(self.objectROT[0],self.objectROT[1],self.objectROT[2], self.ourControlGrp)
                cmds.parent(self.ctrlName , self.ourControlGrp)
                cmds.move(0,0,0, self.ourControl, ls=True)
                cmds.rotate(0,0,0, self.ourControl)

                cmds.parentConstraint(self.ourControl, object, mo=True)
                cmds.scaleConstraint(self.ourControl, object, mo=True)
                ctrlArray.append(self.ourControl)
                ctrlGroupArray.append(self.ourControlGrp)
            
            cmds.parentConstraint(ctrlArray[0],ctrlGroupArray[1],mo=True)
            cmds.parentConstraint(ctrlArray[1],ctrlGroupArray[2],mo=True)
           
        # -- IK setup -- #

        def StretchyIkSetup(self, armSels):

            if hasattr(armSels, '__getitem__'):

                #declare variables for the various joints
                self.firstJointPos=cmds.xform(armSels[0], q=1, ws=1, t=1)
                self.secondJointPos=cmds.xform(armSels[1], q=1, ws=1, t=1)
                self.lastJointPos=cmds.xform(armSels[2], q=1, ws=1, t=1)
                self.lastJointRot=cmds.xform(armSels[2], q=1, ws=1, ro=1)
                self.secondJointPosLocal=cmds.xform(armSels[1], q=1, t=1)
                self.lastJointPosLocal=cmds.xform(armSels[2], q=1, t=1)

            #Create an IK handle on first and last Joints.
                self.tempIKName= str(armSels[0]) + "IK_Hndl"
                self.ikName=cmds.ikHandle(ee=armSels[2], sj=armSels[0], n=self.tempIKName)

            #Create locators for the first and last joint. 
                self.jnt1Loc=cmds.spaceLocator(p=(0, 0, 0))
                cmds.move(self.firstJointPos[0], self.firstJointPos[1], self.firstJointPos[2])
                self.jnt2Loc=cmds.spaceLocator(p=(0, 0, 0))
                cmds.move(self.lastJointPos[0], self.lastJointPos[1], self.lastJointPos[2])
                self.jnt1LocShape=cmds.listRelatives(self.jnt1Loc, s=1)
                self.jnt2LocShape=cmds.listRelatives(self.jnt2Loc, s=1)

            #create a control for the IK handle, give it a stretchy attribute.
                self.ikCtrlTempName = str(armSels[0]) + "_IK_Ctrl"
                self.ikJointControl = cmds.circle(c=(0, 0, 0), n=self.ikCtrlTempName)
                cmds.addAttr(ln="Stretchy", at="float", keyable=True)
                self.ourControlGrp = cmds.group(n=(str(armSels[0]) + "_IK_Ctrl_Grp"), em=True)
                cmds.move(self.lastJointPos[0], self.lastJointPos[1], self.lastJointPos[2], self.ourControlGrp, ws=1)  
                cmds.rotate(self.lastJointRot[0], self.lastJointRot[1], self.lastJointRot[2], self.ourControlGrp, ws=1)  
                cmds.parent(self.ikCtrlTempName , self.ourControlGrp)
                cmds.move(0,0,0, self.ikJointControl, ls=True)
                cmds.rotate(0,0,0, self.ikJointControl)

            #create a "Distance between" Node for... well. getting the distance between the two nodes. 
                self.distanceTest=str(cmds.shadingNode('distanceBetween', asUtility=1))

            #create all of these nodes for all the different things we need to set up for the system.
                self.arm01DistanceNode=str(cmds.shadingNode('multiplyDivide', asUtility=1))
                cmds.setAttr((self.arm01DistanceNode + ".input1X"), self.secondJointPosLocal[0])
                self.arm02DistanceNode=str(cmds.shadingNode('multiplyDivide', asUtility=1))
                cmds.setAttr((self.arm02DistanceNode + ".input1X"), self.lastJointPosLocal[0])
                self.chainLengthPMA=str(cmds.shadingNode('plusMinusAverage', asUtility=1))
                self.distanceScalar=str(cmds.shadingNode('multiplyDivide', asUtility=1))
                cmds.setAttr((self.distanceScalar + ".operation"), 2)
                self.stretchCondition=str(cmds.shadingNode('condition', asUtility=1))
                cmds.setAttr((self.stretchCondition + ".operation"), 2)
                self.colorBlendNode=str(cmds.shadingNode('blendColors', asUtility=1))
                cmds.setAttr((self.colorBlendNode + ".color2R"), 1)
                self.arm01ScaleMD=str(cmds.shadingNode('multiplyDivide', asUtility=1))
                self.arm02ScaleMD=str(cmds.shadingNode('multiplyDivide', asUtility=1))


            #connect them attributes
                self.LinkConstraints(self.jnt1LocShape[0], "worldPosition[0]", self.distanceTest, "point1")
                self.LinkConstraints(self.jnt2LocShape[0], "worldPosition[0]", self.distanceTest, "point2")
                self.LinkConstraints(self.arm01DistanceNode, "outputX", self.chainLengthPMA, "input1D[0]")
                self.LinkConstraints(self.arm02DistanceNode, "outputX", self.chainLengthPMA, "input1D[1]")
                self.LinkConstraints(self.chainLengthPMA, "output1D", self.distanceScalar, "input2X")
                self.LinkConstraints(self.distanceTest, "distance", self.distanceScalar, "input1X")
                self.LinkConstraints(self.distanceTest, "distance", self.stretchCondition, "firstTerm")
                self.LinkConstraints(self.chainLengthPMA, "output1D", self.stretchCondition, "secondTerm")
                self.LinkConstraints(self.distanceScalar, "outputX", self.stretchCondition, "colorIfTrueR")
                self.LinkConstraints(self.stretchCondition, "outColorR", self.colorBlendNode, "color1R")
                self.LinkConstraints(self.arm01DistanceNode, "outputX", self.arm01ScaleMD, "input1X")
                self.LinkConstraints(self.arm02DistanceNode, "outputX", self.arm02ScaleMD, "input1X")
                self.LinkConstraints(self.colorBlendNode, "outputR", self.arm01ScaleMD, "input2X")
                self.LinkConstraints(self.colorBlendNode, "outputR", self.arm02ScaleMD, "input2X")
                self.LinkConstraints(self.arm01ScaleMD, "outputX", armSels[1], "translateX")
                self.LinkConstraints(self.arm02ScaleMD, "outputX", armSels[2], "translateX")
                self.LinkConstraints((str(armSels[0]) + "_IK_Ctrl"), "Stretchy", self.colorBlendNode, "blender")
                cmds.parentConstraint(self.ikCtrlTempName, self.tempIKName,  mo=True )
                cmds.parentConstraint(self.ikCtrlTempName, self.jnt2Loc,  mo=True )
                cmds.scaleConstraint(self.ikCtrlTempName, self.tempIKName,  mo=True )
                cmds.scaleConstraint(self.ikCtrlTempName, self.jnt2Loc,  mo=True )

            else:
                print("Generic Error Message")
                return            
            
        
        
        
        # ---------------------- RK Initalizer ----------------
        def RKInitalizer(self, IKChain, FKChain, RKChain,):
        #setup initial joint chain for RK
            i = 0
            for chain in RKChain:
                RKTempString = str(RKChain[i])                
                IKTempString = str(IKChain[i])
                FKTempString = str(FKChain[i])
                print(RKTempString, IKTempString)
                constraintNumber = cmds.parentConstraint(IKChain[i],FKChain[i], RKChain[i], name=str(RKChain[i])+ "_Parent_Constraint")
                print(str(RKChain[i])+ "_Parent_Constraint")
               # LinkConstraints(self, RKChain[i], 'FK_Weight', constraintNumber,FKChain[i] + "W" +[i])           
                cmds.connectAttr((str(RKTempString) + "." + 'IK_Weight'), (str(RKChain[i]) + "_Parent_Constraint" + "." + str(IKTempString) + "W0"),  f=1)
                cmds.connectAttr((str(RKTempString) + "." + 'FK_Weight'), (str(RKChain[i]) + "_Parent_Constraint" + "." + str(FKTempString) + "W1"),  f=1)
                i = i + 1
        

            # -- Function Calls -- #

        # TESTING, OK!! ----
        FKJointSetup(self, FKJoints)
        StretchyIkSetup(self, IKJoints)
        RKInitalizer(self, IKJoints, FKJoints,RKarmSels)
       ## end 3JS ##

       
# ------------------ End Rigging Setup Class ------------------ # 

# ------------------ End Rigging Setup Class ------------------ # 
my_object = RiggingSetups()

my_object.ThreeJointSetup(armSels)
