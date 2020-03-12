from AutomataTheory import *


def generator(inp):
    print('\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print "Regular Expression: ", inp
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()
    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()
    minDFA = dfaObj.getMinimisedDFA()
    print "\nNFA: "
    nfaObj.displayNFA()
    print "\nDFA: "
    dfaObj.displayDFA()
    print "\nMinimised DFA: "
    dfaObj.displayMinimisedDFA()
    if isInstalled("dot"):
        drawGraph(dfa, "dfa")
        drawGraph(nfa, "nfa")
        drawGraph(minDFA, "mdfa")
        print "\nGraphs have been created in the code directory"
        print minDFA.getDotFile()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
