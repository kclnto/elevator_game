class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.current = current
        self.bottom = bottom
        self.top = top
    def up(self):
        """Makes the elevator go up one floor."""
        if (self.current + 1) < self.top:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if (self.current-1) > self.bottom:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.current > self.top:
            pass
        elif self.current < self.bottom:
            pass
        else:
            self.current = floor
            
    def __str__(self):
        return f"Current floor: {self.current}"
