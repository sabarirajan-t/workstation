#Airplane seating arrangement

As per the given problem statement, I have filled the seats according to number of passengers with the given constraints.

I have written the code in Python3 as it was convenient to access the list of list(instead dynamic 2d array).

Steps I followed:

1. Received the number of blocks of seats from user

2. Received the size of each block from user

3. Received the number of passengers from user

4. Initialized all the seats as -1

5. To fill the aisle seats, I check the last column of the first block, first and last columns of inbetween blocks and first column of last block, if the seats are not filled, I fill in row-wise(top-bottom) with the #filled variable which I use to take count of filled seats.

6. To fill the window seats, I check the first column of first block and last column of last block, if they are not filled, I fill in row-wise.

7. To fill the center seats, I fill the remaining seats which are not filled yet according to the number of passengers.

8. Finally I print the filled seats by traversing row-wise.