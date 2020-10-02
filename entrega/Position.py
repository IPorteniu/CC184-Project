class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def set_position(self, x, y):
        self.x, self.y = x, y

    def get_y_axis(self):
        return self.y

    def get_x_axis(self):
        return self.x
