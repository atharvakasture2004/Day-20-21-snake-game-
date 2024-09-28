from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.high_score= int(file.read())
        
        self.color("white")
        self.penup()
        self.goto(x=-50,y=270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",font=("Arial",24,"normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",'w') as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update()      
   
    def increment_score(self):
        self.score+=1
        self.update()  

