import tkinter as tk
from PIL import Image, ImageTk 
from random import randint

MOVE_SPEED = 20
moves_per_second = 10
GAME_SPEED = 1000 // moves_per_second

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black")
        #to create a snake with initial length 3, place the snake image in 3 positions next to each other
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.score = 0
        self.direction = "Right" #initially the snake moves right
        self.bind_all("<Key>", self.on_key_press) # calls on_key_press if any key is pressed

        self.load_assets()  #loads all images
        self.create_objects()

        #calls the perfor_actions method after 75 ms
        self.after(GAME_SPEED, self.perform_actions)

    #loading the snake and food images
    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
            self.snake_food_image = Image.open("./assets/food.png")
            self.snake_food = ImageTk.PhotoImage(self.snake_food_image)

        except IOError:
            print(IOError)
            root.destroy()

    def create_objects(self):

        #create the user score in the top left corner
        self.create_text(
            100, 12, text=f"Score: {self.score}, (speed: {moves_per_second})", tag="score", 
            fill="#fff", font=("TkDefaultFont", 14)
        )

        #places the snake image in the initial 3 position
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")
        
        #places the food image
        self.create_image(self.food_position[0], self.food_position[1], image=self.snake_food, tag="food")

        #creates a inner rectangle closer to the initial width and height of 600 and 620
        #when the snake hits the inner rectangle, game should be over
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def move_snake(self):
        #snake's head is the first coordinate in the snake_positions tuple
        head_x_position, head_y_position = self.snake_positions[0]
        
        #chopping the tail and moving the snake to the new position by updating its head
        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_SPEED, head_y_position)
        
        if self.direction == "Right":
            new_head_position = (head_x_position + MOVE_SPEED, head_y_position)
        
        if self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_SPEED)

        if self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_SPEED)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1] #chops off the tail 
        #finds all the tags with snake, zip it with the new pos and update to the new position
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    
    def perform_actions(self):
        if self.check_collisions(): #game stops if snake collides 
            self.game_over()
            return
        self.check_food_collision() #check if the snake has colliding with the food before moving
        self.move_snake()
        #after 75 ms, moves the snake
        self.after(GAME_SPEED, self.perform_actions)


    #returns a boolean checking whether the snake is colliding
    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return (
            head_x_position in (0, 600) or 
            head_y_position in (20, 620) or
            (head_x_position, head_y_position) in self.snake_positions[1:] 
        )

    def on_key_press(self, event): #event gives which key was pressed
        new_direction = event.keysym
        all_directions = ("Up", "Down", "Left", "Right") #only allow arrow keys
        opposites = ({"Up", "Down"}, {"Left", "Right"}) #to prevent the snake from eating itself

        if(
            new_direction in all_directions and
            {new_direction, self.direction} not in opposites #sets don't care about order so Up, Down = Down, Up
        ):
            self.direction = new_direction

    #to check if snake is eating the food and to update its length and the score
    def check_food_collision(self):
        #if snake's head is colliding with the food
        if self.snake_positions[0] == self.food_position:
            self.score += 1 #increase the score by 1
            self.snake_positions.append(self.snake_positions[-1]) #increase the snake length by 1

            if self.score % 5 == 0:
                global moves_per_second 
                moves_per_second += 1

            self.create_image(
                self.snake_positions[-1][0], self.snake_positions[-1][1], #to make the increased tail appear
                image = self.snake_body,
                tag = "snake"
            )
            #since the snake has eaten the food, change the food position
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), *self.food_position)

            score = self.find_withtag("score")
            self.itemconfigure(
                score, 
                text=f"Score: {self.score} (speed: {moves_per_second})", 
                tag="score")

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_SPEED
            y_position = randint(3, 30) * MOVE_SPEED
            food_position = (x_position, y_position)

            #if the food is not in the snake's position return it
            if food_position not in self.snake_positions:
                return food_position
    
    #deletes everything and creates a gameover text
    def game_over(self):
        self.delete(tk.ALL) #deletes the canvas
        self.create_text(
            self.winfo_width() / 2, #to create the text in the center of 
            self.winfo_height() / 2,#the screen
            text=f"Game Over! Your score is {self.score}!",
            fill="#fff",
            font=("TkDefaultFont", 24)
        )
        



root = tk.Tk()
root.title("Snake game")
root.resizable(False, False)

board = Snake()

board.pack()
root.mainloop()
