/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: XXX
 * Created on: Sep 2020
 * This program can find the distance utlisiing a sonar. 
*/

//variable
let distanceObject:number = 0 

// start
basic.showIcon(IconNames.Happy)

//finds the distance with sonar 
input.onButtonPressed(Button.A, function(){
  basic.clearScreen()
  distanceObject = sonar.ping (
  DigitalPin.P1,
  DigitalPin.P2,
  PingUnit.Centimeters
)
  basic.showString((distanceObject) + " cm")
  basic.showIcon(IconNames.Happy)
})
