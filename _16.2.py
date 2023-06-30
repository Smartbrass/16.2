class turtle(object):

    x = 0
    y = 0
    s = 2


    def go_up(self):
        self.y += self.s
        return self.y


    def go_down(self):
        self.y -= self.s
        return self.y


    def go_left(self):
        self.x -= self.s
         

    def go_right(self):
        self.x += self.s


    def evolve(self):
        self.s += 1
        return self.s

    def degrade(self):
        if self.s >= 1:
            self.s -= 1
            return self.s
        else:
            return("ERROR s")


    def count_moves(self, x, y):

        
        step = (x - self.x) + (y - self.y) 

        return step


T = turtle()


print(T.count_moves(5, 6))


