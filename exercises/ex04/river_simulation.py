from bear import Bear
from fish import Fish

class River: 

    def__init__ (self, num_fish: int, num_bears: int) :
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]
        self.day = 0 
    
    def view_river(self):
        print (f"~~~ Day {self.day}: ~~~")
        print (f"Fish population: {len(self.fish)}")
        print (f"Bear population: {len(self.bears)}")

    def one_river_week(self) :
        for _ in range(7):
            self.one_river_day()

my_river.one_river_week()
my_river.view_river()