
# import the opencv library 
import cv2 
import numpy as np




# define a video capture object 
vid = cv2.VideoCapture(0)

x1sum = 0
y1sum = 0
x2sum = 0
y2sum = 0

x1total = 0
y1total = 0
x2total = 0
y2total = 0
        
  
while(True): 
      
    # Capture the video frame by frame 
    ret, frame = vid.read()

    # create a mask
    mask = np.zeros(frame.shape[:2], np.uint8)
    mask[400:1050, 550:1050] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(frame,frame,mask = mask)


    
      
    # Convert to grayscale. 
    gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY) 
  
    # Blur using 3 * 3 kernel. 
    blurred = cv2.blur(gray, (3, 3))

    edges = cv2.Canny(blurred, 80, 150)


    lines_list =[]
    lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=10, # Min allowed length of line
            maxLineGap=50 # Max allowed gap between line for joining them
            )
 
    # Iterate over points
    for points in lines:
         # Extracted points nested in the list
        x1,y1,x2,y2=points[0]
        # Draw the lines joing the points
        # On the original image
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),10)
        # Maintain a simples lookup list for points
        lines_list.append([(x1,y1),(x2,y2)])

        #cv2.line(frame,(int((x1+x2)/2)),(int((y1+y2)/2)),(0,255,0),10)

    


    
    # Display the resulting frame 
    cv2.imshow('frame', frame)



    




    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 


