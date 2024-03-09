class System:
    def __init__(self, nbNodes, nbSecrets, secrets, nodes, fallbackActions, stolenSecrets, nodesStates, NodesKernels):
        self.nbNodes = nbNodes
        self.nbSecrets = nbSecrets
        self.secrets = secrets
        self.nodes = nodes
        self.fallbackActions = fallbackActions
        self.stolenSecrets = stolenSecrets
        self.nodesStates = nodesStates
        self.NodesKernels = NodesKernels




    def TransitionOne(self, node):
        # F to N
        subsetR = 0
        cumulatedcost = 0

        for ainput in node.inputs:
            if ainput.isOpen:
                if node.roles[ainput.roleIndex].categ == 'mandatory' and self.nodesStates[self.nodes.index(node.name)] == 'sB':
                    self.nodesStates[self.nodes.index(node.name)] = 'sN'
                    break
                elif self.nodesStates[self.nodes.index(node.name)] == 'sM':

                    cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost
                    
                    self.nodesStates[self.nodes.index(node.name)] = 'sN'
                elif node.roles[ainput.roleIndex].categ == 'optional' and self.nodesStates[self.nodes.index(node.name)] == 'sB':
                    subsetR += 1

                if subsetR > node.actThreshold:
                    self.nodesStates[self.nodes.index(node.name)] = 'sN'
                else:
                    print(":')")
            else:
                if ainput.position == 'peer':
                    # print("we can do a transition")
                    pass
                else:
                    # print("we can't do a transition")
                    pass
        print(subsetR)

    def TransitionTwo(self, node):
        pass



    def TransitionThree(self, node):
        #F to M

        if  self.nodesStates[self.nodes.index(node.name)] == 'sF':
        #just checking if we are in functional state first enable the transition then 
            for ainput in node.inputs:
                if self.nodesStates[ainput.sourceNodeIndex] == 'sM':
                    
                    self.nodesStates[self.nodes.index(node.name)] = 'sM'
                    break


    def TransitionFour(self, node):
        # F to F
        for asecret in node.secrStore:
            if asecret == True : 
                print('there still a secret not stolen locally stored')

        #if there exists at least one interpretation of type remote steal of secret keys pointing to one of the roles of n.
        for ainput in node.inputs:
            if ainput.isOpen :
                pass
                break
        
        # update self.stolenSecrets 
            
        self.nodesStates[self.nodes.index(node.name)] = 'sF'

    def TransitionFive(self, node):
        # M to M
        for asecret in node.secrStore:
            if asecret == True : 
                print('there still a secret not stolen locally stored')
        
        # update self.stolenSecrets 
                
        self.nodesStates[self.nodes.index(node.name)] = 'sM'






    def StepChecker(self, stepinitials, stepresults):
        stepinitials = {
            'stolenSecrets': [False, False, False, False, False],
            'nodesStates': ['sF', 'sF', 'sM', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF'],
            'Cumulated cost': 0,
            'Number of steps': 0
        }

        stepresults = {
            'stolenSecrets': [False, False, False, False, False],
            'nodesStates': ['sF', 'sF', 'sM', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sF', 'sB'],
            'Cumulated cost': 55,
            'Number of steps': 1
        }

        if stepinitials['stolenSecrets'] == stepresults['stolenSecrets']:
            # it means we have a state change 
            
            #compare and find which state has changed 
            #for a given state change if it changed from 'sF' to 'sB' 
            #loopcheck using reverseTransionDetection to find which transition happend 
            pass