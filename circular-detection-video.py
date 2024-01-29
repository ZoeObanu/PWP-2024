import cv2 
import numpy as np 
  
# Read image. 
cap = cv2.VideoCapture("test_images/canvid.MOV")
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
        
    # Convert to grayscale. 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    # Blur using 3 * 3 kernel. 
    blurred = cv2.blur(gray, (3, 3))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

      
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(blurred,  
                       cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
                   param2 = 150, minRadius = 100, maxRadius = 325) 
      
    # Draw circles that are detected. 
    if detected_circles is not None: 
      
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
      
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
      
            # Draw the circumference of the circle. 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 15) 
      
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 15) 
            cv2.imshow("Detected Circle", frame) 

            break


cap.release()
cv2.destroyAllWindows()
