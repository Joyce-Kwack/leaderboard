# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
score = 0

#-----initialize leaderboard----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?:")

#-----initialize turtle-----
t = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
color = "pink" 
shape = "turtle"
t.fillcolor(color)
t.shapesize(4)
t.shape(shape)
font_setup=("Arial",20,"normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#-----game functions--------
def t_clicked(x,y):
    global timer, timer_up
    if timer_up == False:
        update_score()
        change_position()
    else:
       t.hideturtle()
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-200,200)
    t.penup()
    t.goto(new_xpos,new_ypos)
    countdown()
def update_score():
    score_writer.penup()
    score_writer.goto(300,300)
    score_writer.clear()
    global score
    score += 1
    score_writer.write(score, font=font_setup)
def countdown():
  counter.penup()
  counter.goto(-300,300)
  counter.clear()
  global timer, timer_up
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global t

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, t, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, t, score)

#-----events----------------
t.onclick(t_clicked)
wn = trtl.Screen()
wn.mainloop()
