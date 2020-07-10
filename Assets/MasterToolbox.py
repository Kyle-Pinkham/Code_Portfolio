# ---------------------------MasterToolboxV2---------------------------
import maya.cmds as cmds
import random as rand

class MasterToolbox():
    def __init__(self):
        self.mWindow = 'kpToolbox'
    
    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow, title='Toolbox', sizeable=True, menuBar=True)
        #MainTab
        self.mMainTab= cmds.tabLayout(parent=self.mWindow)
        self.mColorControlGrid = cmds.gridLayout(parent=self.mMainTab, numberOfRows=4, numberOfColumns=8, cellWidthHeight= (30, 20))
        self.mtextButton1=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0.016, 0.373), rpt=True, command = lambda : self.RecolorSelected(0))
        self.mtextButton2=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(.000, .000, .000), rpt=True, command = lambda : self.RecolorSelected(1))
        self.mtextButton3=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(.247, .247, .247), rpt=True, command = lambda : self.RecolorSelected(2))
        self.mtextButton4=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(.498, 0.498, 0.498), rpt=True, command = lambda : self.RecolorSelected(3))   
        self.mtextButton5=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.608, 0, 0.157), rpt=True, command = lambda : self.RecolorSelected(4))
        self.mtextButton6=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0, 1), rpt=True, command = lambda : self.RecolorSelected(5))
        self.mtextButton7=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0.275, 0.094), rpt=True, command = lambda : self.RecolorSelected(6))
        self.mtextButton8=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.145, 0, 0.263), rpt=True, command = lambda : self.RecolorSelected(7))
        self.mtextButton9=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.78, 0, 0.78), rpt=True, command = lambda : self.RecolorSelected(8)) 
        self.mtextButton10=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.537, 0.278, 0.2), rpt=True, command = lambda : self.RecolorSelected(9))
        self.mtextButton11=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.243, 0.133, 0.122), rpt=True, command = lambda : self.RecolorSelected(10))
        self.mtextButton12=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.6, 0.145, 0), rpt=True, command = lambda : self.RecolorSelected(11))
        self.mtextButton13=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(1, 0, 0), rpt=True, command = lambda : self.RecolorSelected(12))   
        self.mtextButton14=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 1, 0), rpt=True, command = lambda : self.RecolorSelected(13))
        self.mtextButton15=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0.255, 0.6), rpt=True, command = lambda : self.RecolorSelected(14))        
        self.mtextButton16=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(1, 1, 1), rpt=True, command = lambda : self.RecolorSelected(15))
        self.mtextButton17=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(1, 1, 0), rpt=True, command = lambda : self.RecolorSelected(16))
        self.mtextButton18=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.388, 0.863, 1), rpt=True, command = lambda : self.RecolorSelected(17))   
        self.mtextButton19=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.263, 1, 0.635), rpt=True, command = lambda : self.RecolorSelected(18))
        self.mtextButton20=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(1, 0.686, 0.686), rpt=True, command = lambda : self.RecolorSelected(19))
        self.mtextButton21=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.89, 0.675, 0.475), rpt=True, command = lambda : self.RecolorSelected(20))
        self.mtextButton22=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(1, 1, 0.384), rpt=True, command = lambda : self.RecolorSelected(21))   
        self.mtextButton23=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0.6, 0.325), rpt=True, command = lambda : self.RecolorSelected(22))
        self.mtextButton24=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.627, 0.412, 0.188), rpt=True, command = lambda : self.RecolorSelected(23))
        self.mtextButton25=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.62, 0.627, 0.188), rpt=True, command = lambda : self.RecolorSelected(24))
        self.mtextButton26=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.408, 0.627, 0.188), rpt=True, command = lambda : self.RecolorSelected(25)) 
        self.mtextButton27=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.188, 0.627, 0.365), rpt=True, command = lambda : self.RecolorSelected(26))
        self.mtextButton28=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.188, 0.627, 0.627), rpt=True, command = lambda : self.RecolorSelected(27))
        self.mtextButton29=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.188, 0.404, 0.627), rpt=True, command = lambda : self.RecolorSelected(28))   
        self.mtextButton30=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0.435, 0.188, 0.627), rpt=True, command = lambda : self.RecolorSelected(29))
        self.mtextButton31=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(.498, .498, .498), rpt=True, command = lambda : self.RecolorSelected(30))
        self.mtextButton32=cmds.iconTextButton(parent=self.mColorControlGrid, bgc=(0, 0, 0), rpt=True, command = lambda : self.RecolorSelected(31)) 
                              
        #SecondTab 
        self.mSecondTab= cmds.tabLayout(parent=self.mWindow)
        self.mCol2 = cmds.columnLayout(parent=self.mSecondTab, adjustableColumn=True)
        self.nameField = cmds.textField(placeholderText='Enter new name')
        self.renameButton = cmds.button(label="Rename It", command = lambda x: self.rename_objects(self.getSelections(), cmds.textField(self.nameField, q=True, text=True) ) )
        #ThirdTab
        self.mThirdTab = cmds.tabLayout(parent=self.mWindow)
        self.mCol3 = cmds.columnLayout(parent=self.mThirdTab, adjustableColumn=True)
        self.mStretchyIKSetupButton = cmds.button(label= "StretchyIKSetup", command = lambda x: self.StretchyIkSetup(self.getSelections()))
        self.placeholder = cmds.text(label = "")
        self.mJointFKSetupButton = cmds.button(label= "FKJointSetup",command = lambda x: self.ObjectCtrlCreator(self.getSelections()))
        #FourthTab
        self.mFourthTab = cmds.tabLayout(parent=self.mWindow)
        self.mCol4 = cmds.columnLayout(parent=self.mFourthTab, adjustableColumn=True)
        self.RandoObjectMovementButtom = cmds.button(label="RandomMovement", command = lambda x: self.MoveObjects(self.getSelections()))
        self.placeholder = cmds.text(label = "")
        self.DuplicateItemButton = cmds.button(label="Duplicate Objects" , command = lambda x: self._DuplicateObjects(self.getSelections(),cmds.intField(self.dupeNumField, q=True, value=True) ) )
        self.dupeNumLabel = cmds.text(label = "Number of Duplicates")
        self.dupeNumField = cmds.intField(annotation='Number of Duplicates')
        #FifthTab
        #self.mFifthTab = cmds.tabLayout(parent=self.mWindow)
        #self.mCol5 = cmds.columnLayout(parent=self.mFifthTab, adjustableColumn=True)
        #self.controlGridLayout = cmds.gridLayout(cellWidthHeight= (60,40))
        #self.circleButt = cmds.button(parent=self.controlGridLayout, label = "WIP")
        #self.squareButt = cmds.button(parent=self.controlGridLayout, label = "WIP")
        
        cmds.tabLayout(self.mMainTab, edit=True, tabLabel=[self.mColorControlGrid, "NurbsColorGrid"])
        cmds.tabLayout(self.mSecondTab, edit=True, tabLabel=[self.mCol2, "Rename Tool"])
        cmds.tabLayout(self.mThirdTab, edit=True, tabLabel=[self.mCol3, "Auto-Rig-Setups"])
        cmds.tabLayout(self.mFourthTab, edit=True, tabLabel=[self.mCol4, "Extra Tools"])
       
        
        cmds.showWindow(self.mWindow)
        
        
    
    def delete(self):
        if cmds.window(self.mWindow, q=True, exists=True):
            cmds.deleteUI(self.mWindow)
# --------------- Rename Thing ------------
            
    def rename_objects (self, sels, newName):
            
            
            self.newNumPad = ""
            self.newNum = 0
            self.numPad = 0
            for sel in sels:
                self.newNum = self.newNum +1
            
            for sel in sels:
            
                self.newNumPad = ""
                self.numPadDiff = len(str(self.numPad)) - len(str(self.newNum))
                
                for var in range(0, self.numPadDiff):
                
                    self.newNumPad = self.newNumPad + "0"
                
    
                self.newNumPadTemp = self.newNumPad + str(self.newNum)
                cmds.rename(sel, (newName + "_" + self.newNumPadTemp))
            
            
    def getSelections(self):
        sels = cmds.ls(sl=True)
        return sels
                        
    def RecolorSelected(self, thisColor):
            sels = cmds.ls(sl=True)
            selShapes = cmds.listRelatives(shapes=1)
            for item in selShapes:
                print(item)
                cmds.setAttr (item + ".overrideEnabled", 1) 
                cmds.setAttr (item + ".overrideColor", thisColor) 
# ------------------  Randomly Move Objects ----------------            
    def MoveObjects(self, selections):

    	for items in selections:
    		self.xRand=float(rand.randrange(-30, 30))
    		self.zRand=float(rand.randrange(-30, 3))
    		self.xPos=float(cmds.getAttr(str(items) + ".tx"))
    		self.zPos=float(cmds.getAttr(str(items) + ".tz"))
    		cmds.setAttr((str(items) + ".tx"), (self.xPos * 0 + self.xRand))
    		cmds.setAttr((str(items) + ".tz"), (self.zPos * 0 + self.zRand))
    		
    	return 
# ----------- Duplicate Objects -------------    	       
    def _DuplicateObjects(self, selections, numDupes):
    	
    	
    	for i in range(numDupes):
    		cmds.duplicate(rr=1)   
# --------------- Control Creator --------------    		
    def ObjectCtrlCreator(self, objectToSetup):

        for object in objectToSetup:
            
            objectPOS = cmds.xform(object, q=1, t=1, ws=True)
            objectROT = cmds.xform(object, q=1, ro=1, ws=True)
    
            ctrlName = object + "_Ctrl";
            ourControl = cmds.circle( c=(0, 0, 0), n=ctrlName)
            ourControlGrp = cmds.group(n=(object + "_Ctrl_Grp"), em=True)
            cmds.move(objectPOS[0],objectPOS[1],objectPOS[2], ourControlGrp)
            cmds.rotate(objectROT[0],objectROT[1],objectROT[2], ourControlGrp)
            cmds.parent(ctrlName , ourControlGrp)
            cmds.move(0,0,0, ourControl, ls=True)
            cmds.rotate(0,0,0, ourControl)
            
            cmds.parentConstraint(ourControl, object, mo=True)
            cmds.scaleConstraint(ourControl, object, mo=True)            
# -------------------------------- Stretchy IK Setup -----------------
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
        
    
 # ---------------- Set up Constraints ----------------   
    def LinkConstraints(self, objName, attributeName, constraintName, constraintAtt):
	
	cmds.connectAttr((objName + "." + attributeName), (constraintName + "." + constraintAtt), f=1)
# ---------------------- RK Initalizer ----------------
    def RKInitalizer(self, rkChain, chainToLink):
        #setup initial joint chain for RK
        i = 0
        if ((len(rkChain)) == (len(chainToLink))):
            print(len(rkChain))
            if (cmds.objExists("IK_ON_Switch")):
                print("Switches Already Established")
            else:
                self.ikSwitch = cmds.shadingNode('blendColors', asUtility=1, n="IK_ON_Switch")
                selffkSwitch =cmds.shadingNode('blendColors', asUtility=1, n="FK_ON_Switch")
            
            #while (i < len(rkChain)):
             #   cmds.parentConstraint(chainToLink[i], rkChain[i])
             #   cmds.scaleConstraint(chainToLink[i], rkChain[i])
    
            
            
            
            cmds.parentConstraint(chainToLink[0], rkChain[0])
            cmds.parentConstraint(chainToLink[1], rkChain[1]) 
            cmds.parentConstraint(chainToLink[2], rkChain[2])   
        
        else:
            print("Wrong Arugments: Expected Two Chains of 3 Joints Each")
            return
            
            
    def ObjectCtrlCreator(self, objectToSetup):
    
        for object in objectToSetup:
            
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

## ------------------------------- Make Control Shapes ----------------------
    def CreateControlShape(self, shape):
    
        if (shape == "circle"):
             self.circleCtrl = cmds.circle()

           
testWindah = MasterToolbox()
testWindah.create()