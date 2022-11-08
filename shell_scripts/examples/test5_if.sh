#!/bin/bash

echo "Pick a number from 1 to 10!"
read num
if [ $num == 3 ];
    then echo "Congratulation! You picked the right number";
    else echo "Sorry, You missed! Maybe next time.";
fi;