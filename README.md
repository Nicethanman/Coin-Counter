# Coin-Counter
This is a python program that determines the minimum amount of change in a group of Canadian coins when given the cost of an item. Working as a cashier before, I thought this would be a great idea to help customers get rid of their pocket change.

A recursive approach was taken for calculating the best combination of coins to minimize the amount of change returned to the customer and to maximize the amount of change given away. You can find the approach in maxChangeCalculator.py. The program incorporates OpenCV for image recognition and PYQT for the user interface.


# Things I Learned:
- Image recognition using openCV - finding/drawing contours
- Creating GUI's with PYQT
- Using QT Threads to capture video and make calculations simultaneously

To test it out, ensure you have OpenCV and PYQT installed. Then run the mainGui.py file with

```
  py mainGui.py
```
