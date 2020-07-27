from .fsm.fsm import Fsm
from .fsm.state import State
from .fsm.transition import Transition
from .fsm.functions import tick


class Bootstrapper(object):
    """" boot the simple fsm """
    def __init__(self):
        self.fsm = Fsm(self)
        # add states
        self.fsm.add_state("IDLE", IDLE(self.fsm))
        self.fsm.add_state("ON", ON(self.fsm))
        self.fsm.add_state("OFF", OFF(self.fsm))
        # add transition
        self.fsm.add_transition("TO_IDLE", Transition('IDLE'))
        self.fsm.add_transition("TO_ON", Transition('ON'))
        self.fsm.add_transition("TO_OFF", Transition('OFF'))

    def execute(self):
        try:
            self.fsm.execute()
        except Exception as ex:
            print('Error: {0}'.format(ex))

    def run(self):
        self.fsm.set_state('IDLE')
        self.execute()
        transition = ["TO_ON", "TO_OFF", "TO_IDLE"]
        i = 0
        while True:
            try:
                self.fsm.to_transition(transition[i])
                self.execute()
                i = i+1
                if i > 2:
                    i = 0
            except Exception as ex:
                print('Error: {0}'.format(ex))

# States


class IDLE(State):
    """ leerlauf do nothing"""
    def __init__(self, fsm):
        super(IDLE, self).__init__(fsm)

    def enter(self):
        print("\t>>>IDLE enter")
        super(IDLE, self).enter()

    def execute(self):
        print('\t>> State IDLE execute')
        tick()

    def exit(self):
        print("\t> IDLE exit")


class ON(State):
    """ run fsm """
    def __init__(self, fsm):
        super(ON, self).__init__(fsm)

    def enter(self):
        print("\t\t>>>ON enter")
        super(ON, self).enter()
        print(ON.__mro__) # method resolution order

    def execute(self):
        print("\t\t>> State ON execute")
        tick()

    def exit(self):
        print("\t\t> State ON exit")


class OFF(State):
    """ stop fsm """
    def __init__(self, fsm):
        # call the init from state and set the name of the class
        super(OFF, self).__init__(fsm)

    def enter(self):
        print("\t\t\t>>>OFF enter")
        super(OFF, self).enter()

    def execute(self):
        print("\t\t\t>> State OFF execute")
        tick()

    def exit(self):
        print("\t\t\t> State OFF exit")
