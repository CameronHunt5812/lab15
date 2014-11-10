#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 2
move = 10

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
		
		self.doun = Button(self.myContainer1)
		self.doun.configure(text="doun", background= "green")
		self.doun.grid(row=2,column=1)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="right", background= "green")
		self.right.grid(row=2,column=2)
		
		self.leaft = Button(self.myContainer1)
		self.leaft.configure(text="leaft", background= "green")
		self.leaft.grid(row=2,column=0)
		
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                self.doun.bind("<Button-1>",self.moveDoun)
                self.right.bind("<Button-1>",self.moveRight)
		self.leaft.bind("<Button-1>",self.moveLeaft)
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()
		
	def moveUp(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,-10)
    
        def moveDoun(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,10)
                
        def moveRight(self, event):   
		global player
		global drawpad
                drawpad.move(player,10,0)
                
        def moveLeaft(self, event):   
		global player
		global drawpad
                drawpad.move(player,-10,0)
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    # Insert the code here to make the target move, bouncing on the edges
	    #  This will trigger our collision detect function
            
	    drawpad.move(target,direction,0)
	    
            didWeHit = self.collisionDetect()
	    if tx2 > drawpad.winfo_width():
	        direction = -4
	        
	    if tx1 < 0:
	        direction = 4
	        
	    if didWeHit == False:
                drawpad.after(1,self.animate)
            
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                x1,y1,x2,y2 = drawpad.coords(player)
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                if (x1 > tx1) and (x2 < tx2) and (y1 > ty1) and (y2 < ty2):
                    return True
                else:
                    return False
                # Do your if statement - remember to return True if successful!
            
		
myapp = MyApp(root)

root.mainloop()