# smart-garage

## Abstract
#### This project was the final project for the summer-trainging period in HST (HLogic) Company
#### The project is about a samart garage system that enables the cars to know the number of empty locations in the garage also their places
#### The system takes a snapshot of the car when it enters and according to the period the car stayed in the garage it gives the car the parking fee when it leaves
#### It also knows which slot the car had taken so it doesn't display it as empty spot for the other cars to come
#### The garage has 2 cameras, one for the cars coming in and leaving the garage, the other one for the places inside to decide which is empty and which is not.

#### The Cameras used at first were analog cameras and the feed was taken to python using dvrs but i found out that it's really slow with a small frame rate 
#### so we used mobile cams to simulate the two camears inside the garage.
#### The gate was simulated by a servomotor that opens and closes according to whether there's a car or not if the camera detects a car it sends a signal to the arduino controller to open the gate, it also sens a signal to the arduino controller at the gate telling it the fee calculated to display it on 16x2 LCD screen for the comming cars.

#### The spots are marked by numbers and the camera inside the garage detects a number on the ground this means this spot is empty and it sends a signal to the arduino controller at the gate telling it which spots are available for the comming cars

### You will find a video of the whole project explained and working in the link below.
[Explanation](https://drive.google.com/drive/u/0/folders/1Idz0HSahc6OjwdI8v-egtqUrqa1SZp9e)