from datetime import datetime;
import time;
import random;

times = 3;
odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59];

for timer in range(times - 1):

    right_this_minute = datetime.today().minute;
    wait_time = random.randint(1, 60);

    print("•••••••••••••••••");
    print("Response number " + (str(timer + 1)) + "/" + str(times));
    
    if right_this_minute in odds:
        print("This minute seems a little odd: " + str(right_this_minute));
    else:
        print("Not an odd minute: " + str(right_this_minute));

    print("Please, Wait " + str(wait_time) + " seconds!");
    time.sleep(wait_time);

print("•••••••••••••••••");
print("Response number " + str(times) + "/" + str(times));
if right_this_minute in odds:
    print("This minute seems a little odd: " + str(right_this_minute));
else:
    print("Not an odd minute: " + str(right_this_minute));
print("THE END OF PROGRAM");
print("•••••••••••••••••");
