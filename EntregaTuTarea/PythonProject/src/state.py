class State(object):
    def __init__(self):
        pass
    def enter(self):
        pass

    def exit(self):
        pass

    def reason(self):
        pass

    def act(self):
        pass


class StateMachine(object):

    def __init__(self, host, first_state=None):
        self.host = host
        self.current_state = first_state

    def transition(self, new_state):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.host = self.host
        self.current_state.fsm = self
        self.current_state.enter()

    def update(self):
        if self.current_state:
            new_state = self.current_state.reason()

            if new_state: 
                self.transition(new_state)
            else:
                self.current_state.act()
