
# import the opencv library 
import cv2 
import numpy as np




# define a video capture object 
vid = cv2.VideoCapture(0)


        
  
while(True): 
      
    # Capture the video frame by frame 
    ret, frame = vid.read()

    
    # create a mask
    mask = np.zeros(frame.shape[:2], np.uint8)
    mask[100:1000, 500:1400] = 255

    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(frame,frame,mask = mask)


    
      
    # Convert to grayscale. 
    gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY) 
  
    # Blur using 3 * 3 kernel. 
    blurred = cv2.blur(gray, (7, 7), 0)

    # apply basic thresholding -- the first parameter is the image
    # we want to threshold, the second value is is our threshold
    # check; if a pixel value is greater than our threshold (in this
    # case, 200), we set it to be *black, otherwise it is *white*
    (T, threshInv) = cv2.threshold(blurred, 140, 255,
    	cv2.THRESH_BINARY_INV)

    masked = cv2.bitwise_and(frame, frame, mask=threshInv)

    """edges = cv2.Canny(blurred, 80, 150)


    lines_list =[]
    lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=10, # Min allowed length of line
            maxLineGap=50 # Max allowed gap between line for joining them
            )
    x1sum = y1sum = x2sum = y2sum = x1total = y1total = x2total = y2total = 0
    # Iterate over points
    for points in lines:
        
         # Extracted points nested in the list
        x1,y1,x2,y2=points[0]
        # Draw the lines joing the points
        # On the original image
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),10)
        # Maintain a simples lookup list for points
        lines_list.append([(x1,y1),(x2,y2)])

        x1sum += x1
        y1sum += y1
        x2sum += x2
        y2sum += y2

        x1total += 1
        y1total += 1
        x2total += 1
        y2total += 1
        

    cv2.line(frame,(int(x1sum/x1total),int(y1sum/y1total)),(int(x2sum/x2total),int(y2sum/y2total)),(255,0,0),10)

    


    
    # Display the resulting frame """
    cv2.imshow('frame', masked)



    




    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 


