

class Fsm(object):
    """ fine state machine """
    def __init__(self, state):
        self.state = state
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.preview_state = None
        self.trans = None

    def add_transition(self, trans_name, transition):
        self.transitions[trans_name] = transition
        print('FSM method add_transition name: {0}, transition: {1}'
              .format(trans_name, transition.to_state))

    def add_state(self, state_name, state):
        self.states[state_name] = state
        print('FSM state : {0}, preview: {1}, current: {2}'
              .format(state_name, state.fsm.preview_state, state.fsm.current_state))

    def set_state(self, state_name):
        self.preview_state = self.current_state
        self.current_state = self.states[state_name]
        print('FSM state: {0}'.format(state_name))

    def to_transition(self, to_trans):
        self.trans = self.transitions[to_trans]
        print('FSM trans: {0}'.format(to_trans))

    def execute(self):
        print('>>FSM execute')
        if self.trans:
            print('>>>>>FSM execute trans: {0}'.format(self.trans.to_state))
            self.current_state.exit()
            self.trans.execute()
            self.set_state(self.trans.to_state)
            self.current_state.enter()
            self.trans = None
        self.current_state.execute()

