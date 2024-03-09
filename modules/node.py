class node:
    def __init__(self, name, softwareClass, text, kernelIndex, nbRoles, nbInputs, nodeType, plausThreshold, actThreshold, secrTheftCost, debug_fallbackActionNames, secrStore, monBypassCost, roles, inputs, fallbackActionIndex):
        self.name = name
        self.softwareClass = softwareClass
        self.text = text
        self.kernelIndex = kernelIndex
        self.nbRoles = nbRoles
        self.nbInputs = nbInputs
        self.nodeType = nodeType
        self.plausThreshold = plausThreshold
        self.actThreshold = actThreshold
        self.secrTheftCost = secrTheftCost
        self.debug_fallbackActionNames = debug_fallbackActionNames
        self.secrStore = secrStore
        self.monBypassCost = monBypassCost
        self.roles = roles
        self.inputs = inputs
        self.fallbackActionIndex = fallbackActionIndex





    # def ProtDestructCost(self, InputID, roleID, sourceNodeIndex, attackPosition, attackerState, NodesKernels):
    #     self.InputID = InputID
    #     self.roleID = roleID
    #     self.sourceNodeIndex = sourceNodeIndex 
    #     self.attackPosition = attackPosition 
    #     self.attackerState = attackerState 

    #     protCostBr = self.inputs[InputID].protBreakCosts[1]
    #     keyProtect = False
    #     protCost = self.inputs[InputID].protBreakCosts[0]
    #     kernelSId = NodesKernels[sourceNodeIndex]

    #     if (protCostBr== 'null' or (protCost!= 'null' and protCost<protCostBr)): protCostBr=protCost
    #     for i in range(0, 6):
    #         if(roleProtectKey[roleId][i]):
