# Pong-Game
This is the Code for the classic Pong Game written using the Turtle Module in Python. 

Here is the link to the turtle documentation that has helped me greatly in building this project:
https://docs.python.org/3/library/turtle.html

If you want to recreate this project, you may want to break it in parts such as:
1. Creating the screen 
	- setting its height width and colour using different methods

2. Creating two paddles on two ends and moving them 
	- each of them will be an object of the turtle class and then their shape is modified 
	- using screen.listen(), and screen.onkey() methods

3. Creating a ball and making it move 
	- the ball is another object of the turtle class 
	- by getting the x and y coordinates and increasing it by a small amount, say 10 in a loop the paddles can be moved

4. Detecting collision with the ball and bounce
	- by taking the y coordinates using the ycor() method, checked to see if it touches the end of the screen
	- if yes the bounce method basically multiplies the y increment with -1

5. Detecting collision with paddle
	- by using the distance() method and the xcor() method
	- bounce method is the same as before, multiply the x increment with -1 

6. Detecting misses
	- by checking if the ball surpasses a certain point in the x axis, beyond the paddles

7. Keep Score
	- by using the write() method
	- if left paddle misses, increase the points of the right player by 1
	- if write paddle misses, increase the points of the left player by 1
