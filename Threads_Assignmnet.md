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

Join() operation makes sure that child threads need to finish bfore parent thread terminates.In our case when we remove join() main method finish first then threadA and threadB terminates.

##4.What happens if you try to Ctrl-C out of the program before it terminates?

When we try to terminate the process it won't do untill child threads finish their work.It will print a value by making small fraction of gap while executing though. 

##5.Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

When threadA access sharedNumber it will assign it as 1 and prints some statement and when threadB access the same variable it will reassign it as 2 and print some statements.Thus it purely depends on which thread gets executed first and access the shared variable.

                                                  
                  sharedNumber = 1                          
                  if sharedNumber != 1:                     
                     print 'A: that was weird'                  

##6.Does uncommenting the lock operations clear up the problem in question 5?

This has solved our problem by locking the variable when some thread is using it.So that no other process can manipulate data.In our case threadA assigns 1 and do nothing, threadB assigns 2 and do nothing.ThreadA and threadB terminates without printing any statements and finally main method terminates.


