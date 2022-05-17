class Playground(object):
    """docstring for Playground.
    Represents the field where the piano keys exists
    the arrays are arange in column (each column is an array)
    the zeros represents blacks whereas the ones represents the keys
    0 0 0 0 1 1 0 0 0 0
    0 0 0 0 1 1 0 0 0 0
    0 0 0 0 1 1 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 1 1 0 0 0 0 0 0
    0 0 1 1 0 0 0 0 0 0
    0 0 1 1 0 0 0 0 0 0
    0 0 1 1 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 1 1
    0 0 0 0 0 0 0 0 1 1
    0 0 0 0 0 0 0 0 1 1

    """

    def __init__(self, height = 10, width = 5):
        super(Playground, self).__init__()

        self.height = height #height of the screen
        self.width = width
        self.body = np.zeros(shape=(self.height, self.width)) #a numpy array filled with zeros

    def update_env(self, keys, agent):
        try:
            #initialize the environment with zeros
            self.body = np.zeros(shape=(self.height, self.width))
            #put the keys in the environment
            for key in keys:
                if not key.out_of_range:
                    self.body[:,key.x:min(key.x+key.height,self.height)] = key.body

            key_listener = keyboard.Listener(on_press=on_press)
            key_listener.start()

            with Listener(on_click=on_click) as listener:
                listener.join()

        except Exception as e:
            pass

def on_click(x, y, button, pressed):
    if pressed:
        print("mouse pressed")

def on_press(key):
    print("key is pressed")
