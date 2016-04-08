## Review Questions

- Name: Yashwanth Reddy

- Course: 5143 Operating Systems

- Date: 08 Feb 2016

- MID: M20215871

##1.Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Threads2 has shared variable between two threads threadA and threadB.Each of those can access the variable and manipulate the data that will effect correctness of data among threads. While Threads1 has seperate local variables for each thread.

                Threads2.py
                //global sharedCounter
                  print 'A:', k, sharedCounter
                       
##2.After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

After applying lock on shared variable it will make sure that any thread has to wait for a variable to access untill lock get released. In our case threadA can access the variable and threadB has to wait till it completes.

                self.lock.acquire()
                if k % 100000 == 0:
                print 'A:', k, sharedCounter
                sharedCounter += 1
                self.lock.release()

##3.Comment out the join statements at the bottom of the program and describe what happens.

Join() operation makes sure that child threads need to finish than parent thread.

##4.What happens if you try to Ctrl-C out of the program before it terminates?

Main thread finish its execution first and then if we interrupt the execution process(Cntl+C) of child threads, compiler ignores by printing the values of variables at that time and continues till finish its job. 

##5.Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

In Threads4.py we have a variable that is shared between two threads.When  threadA starts execution it will assign the value as 'sharedNumber=1' and checks 'if(sharedNumber!=1)' then print 'A: that was weird'. Now assume threadB access the shared variable and reassign it as 2 and prints its appropriate statements.So every time shared variable is getting reassigned thus makes our more ridiculous race condition.

                                                  
                  sharedNumber = 1                          
                  if sharedNumber != 1:                     
                     print 'A: that was weird'                  

##6.Does uncommenting the lock operations clear up the problem in question 5?

Uncommenting the lock operations has solved race condition problem, because when a thread access sharedNumber it will get lock untill threadA completes all its operations on that variable and release lock.Thus everytime when if(condition) expression evaluates it will come false and nothing is gonna print. At the end main thread finish its work after threads terminates.


