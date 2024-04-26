class System:
    def __init__(self, nbNodes, nbSecrets, secrets, nodes, fallbackActions, stolenSecrets, nodesStates, NodesKernels):
        self.nbNodes = nbNodes
        self.nbSecrets = nbSecrets
        self.secrets = secrets
        self.nodes = nodes
        self.fallbackActions = fallbackActions
        self.stolenSecrets = stolenSecrets  ####
        self.nodesStates = nodesStates  ####
        self.NodesKernels = NodesKernels



#the point here is not to change the state of the node it's already happening in uppaal, we just need to see if the conditions where checked or not 
    def TransitionOne(self, node):
        # F to N
        subsetR = 0
        cumulatedcost = 0

        for ainput in node.inputs:
            if ( ainput.position == 'peer') : # and (ainput.isOpen)
                if node.roles[ainput.roleIndex].categ == 'mandatory' and (self.nodesStates[ainput.sourceNodeIndex] == 'sN' or self.nodesStates[ainput.sourceNodeIndex] == 'sB'):
                    print("condition one checked") 
                    if (self.nodesStates[ainput.sourceNodeIndex] == 'sN'):
                        cumulatedcost += node.roles[ainput.roleIndex].nCodeInjectCost
                    else:
                        cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost

                elif node.roles[ainput.roleIndex].categ == 'optional' and (self.nodesStates[ainput.sourceNodeIndex] == 'sN' or self.nodesStates[ainput.sourceNodeIndex] == 'sB'):
                    subsetR += 1 

                elif self.nodesStates[ainput.sourceNodeIndex] == 'sM':
                    cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost
                    print("condition three checked")
        for ainput in node.inputs:
            if ( ainput.position == 'peer') : 
                if node.roles[ainput.roleIndex].categ == 'optional' and (self.nodesStates[ainput.sourceNodeIndex] == 'sN' or self.nodesStates[ainput.sourceNodeIndex] == 'sB'):
                    if (self.nodesStates[ainput.sourceNodeIndex] == 'sN'):
                        if  sum(node.inputs) - subsetR < node.actThreshold:
                            print("condition two checked")
                            cumulatedcost += node.roles[ainput.roleIndex].nCodeInjectCost
                    else:
                        if  sum(node.inputs) - subsetR < node.actThreshold:
                            print("condition two checked")
                            cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost
        #print(subsetR)
        print(cumulatedcost)



    def TransitionTwo(self, node):
        #F to B
        subsetRb = 0
        cumulatedcost = 0

        for ainput in node.inputs:
            if ( ainput.position == 'peer') : # and (ainput.isOpen)
                #if iterpretation
                if node.roles[ainput.roleIndex].categ == 'mandatory' and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    
                    cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost
                    print("condition 1.1 two checked")

                elif node.roles[ainput.roleIndex].categ == 'optional'and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    subsetRb += 1

                elif self.nodesStates[ainput.sourceNodeIndex] == 'sM':
                    cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost
                    print("condition three checked")

            elif ( ainput.position == 'side') :
                if node.roles[ainput.roleIndex].categ == 'mandatory' and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    
                    cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost
                    print("condition 1.1 two checked")

                elif node.roles[ainput.roleIndex].categ == 'optional'and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    subsetRb += 1
                    

                elif self.nodesStates[ainput.sourceNodeIndex] == 'sM':
                    cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost #25
                    print("condition three checked")
                
                cumulatedcost += ainput.protBreakCosts.theft
            
            else : #ainput.position == 'mitm'
                pass

        for ainput in node.inputs:
            if ( ainput.position == 'peer') : # and (ainput.isOpen)
                if node.roles[ainput.roleIndex].categ == 'optional'and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    if subsetRb > node.plausThreshold:
                        print("condition 1.2 two checked")
                        cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost
                        
            elif ( ainput.position == 'side') :
                if node.roles[ainput.roleIndex].categ == 'optional'and self.nodesStates[ainput.sourceNodeIndex] == 'sB':
                    if subsetRb > node.plausThreshold:
                            print("condition 1.2 two checked")
                            cumulatedcost += node.roles[ainput.roleIndex].bCodeInjectCost
        print(cumulatedcost)           


                
  

        



    def TransitionThree(self, node):
        #F to M

        for ainput in node.inputs:
            if(ainput.position == 'peer'):
                if(self.nodesStates[ainput.sourceNodeIndex] == 'sM'):
                        
                    cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost 
                    
            elif ( ainput.position == 'side') :

                cumulatedcost += node.roles[ainput.roleIndex].mCodeInjectCost 
                cumulatedcost += ainput.protBreakCosts.theft 

            else : #ainput.position == 'mitm'
                pass

            


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
            
        self.nodesStates[ainput.sourceNodeIndex] = 'sF'

    def TransitionFive(self, node):
        # M to M
        for asecret in node.secrStore:
            if asecret == True : 
                print('there still a secret not stolen locally stored')
        
        # update self.stolenSecrets 
                
        self.nodesStates[ainput.sourceNodeIndex] = 'sM' 






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

        #somehow extract the info that RevProxy went from sF to sB 
        #with a cumulated cost of 55 

        if stepinitials['stolenSecrets'] == stepresults['stolenSecrets']:
            # it means we have a state change 
            
            #compare and find which state has changed 

            pass
        else:
            # it means states didn't change but we have a stolen key 
            pass


        #for a given state change if it changed from 'sF' to 'sB' 
        #loopcheck using reverseTransionDetection to find which transition happend 

        #next step figure how the cost is being calculated 
        