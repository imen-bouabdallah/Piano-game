class Keys:
    """docstring for Keys
    this class represents the keys of the piano that appears
    by culumn"""

    def __init__(self, width = 2, height = 100, speed = 1, x = 1, env):
        super(Keys, self).__init__()

        self.width = width #the width is constant usualy and doesn't take so much so that we can have
                            #multiple keys at a time, but the keys need to be on diffrent lines
        self.height = height
        self.speed = speed
        self.x = x #the coordinate of the wall
        self.env = env #a type representing the environment we work at

        self.body_unit = 1 #the unit used to represent a key in the array
        self.body = np.ones(shape = (self.height, self.width)) #the wall's body_unit
        self.out_of_range = False #used so that we can delete a wall from screen when it reaches the limit

        def move(self):
            """ move the key according to speed while cheking it still in range"""
            self.x = self.speed
            self.out_of_range = True if ((self.x)>self.env.height) else False  #if the keys coordinate reaches the range
                                                                                #the key is dismissed from screen
