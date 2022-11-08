#!/bin/bash

for i in {1..10};

 do 
 if [ $i != 3 ]; 
 then echo "hello $i"
 else echo "Sorry, no $i allowed";fi; 
 done