from graphics import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400



def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # TODO: your code here!
    
    rect = canvas.create_rectangle(0, 0, 260, 30, 'yellow')
    text = canvas.create_text(10,10, font_size = 15, text='Play PaperScissorsRock with Karel')
    
    #set player's seat
    canvas.create_image_with_size(60, 50, 80,80, "karel.png")
    text = canvas.create_text(180, 80, font_size = 25, text='VS')
    text = canvas.create_text(240, 80, font_size = 25, text='You')
    
    title = canvas.create_text(60, 150, font_size = 20, text="Click to make your choice:")
    
    text = canvas.create_text(30, 320, font_size = 15, text="Karel's Choice:")
    text = canvas.create_text(240, 320, font_size = 15, text="Your Choice:")
    
    
    
    rock = canvas.create_image_with_size(60, 200, 60, 60, "rock.png")
    paper = canvas.create_image_with_size(160, 200, 60, 60, "paper.png")
    scissors = canvas.create_image_with_size(260, 200, 60, 60, "scissors.png")
    
    #wait fot player to choose
    canvas.wait_for_click()
    
    #show karel's choice
    karel_choice = get_karel_choice()
    if karel_choice == 'rock':
        karel_rock = canvas.create_image_with_size(60, 350, 30, 30, "rock.png")
    elif karel_choice == 'paper':
        karel_paper = canvas.create_image_with_size(60, 350, 30, 30, "paper.png")
    elif karel_choice == 'scissors':
        karel_scissors = canvas.create_image_with_size(60, 350, 30, 30, "scissors.png")
    
    #show player's choice
    player_choice = get_player_choice(canvas)
    if player_choice == 'rock':
        player_rock = canvas.create_image_with_size(270, 350, 30, 30, "rock.png")
    elif player_choice == 'paper':
        player_paper = canvas.create_image_with_size(270, 350, 30, 30, "paper.png")
    elif player_choice == 'scissors':
        player_scissors = canvas.create_image_with_size(270, 350, 30, 30, "scissors.png")
    
    #show result
    canvas.delete(rock)  # Remove rock
    canvas.delete(paper)  # Remove paper
    canvas.delete(scissors)  # Remove scissors
    canvas.delete(title)  # Remove old title
    title = canvas.create_text(60, 150, font_size = 20, text="The result:")
    result= caculate_result(karel_choice, player_choice)
    text = canvas.create_text(130, 220,font_size = 25, text=result)
    

def get_karel_choice():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return 'rock'
    elif random_number == 2:
        return 'paper'
    elif random_number == 3:
        return 'scissors'
    
   
def get_player_choice(canvas):
    click = canvas.get_last_click()
    if click[1]> 200 and click[1] < 260:
        if click[0]>60 and click[0]<120:
            return 'rock'
        elif click[0]>160 and click[0]<220:
            return 'paper'
        elif click[0]>260 and click[0]<320:
            return 'scissors'
        else:
            return 0
    else:
        return 0

 
def caculate_result(karel_choice, player_choice):
    if karel_choice == player_choice:
        return "It's a tie!"
    if karel_choice == 'rock' and player_choice == 'paper':
        return 'You win!'
    if karel_choice == 'rock' and player_choice == 'scissors':
        return 'You lose!'
    if karel_choice == 'paper' and player_choice == 'rock':
        return 'You lose!'
    if karel_choice == 'paper' and player_choice == 'scissors':
        return 'You win!'
    if karel_choice == 'scissors' and player_choice == 'rock':
        return 'You win!'
    if karel_choice == 'scissors' and player_choice == 'paper':
        return 'You lose!'
    if player_choice == 0:
        return 'Invalid Choice'

if __name__ == '__main__':
    main()
