#Chapter 3 Review Questions
>Name: Yashwanth Reddy Muddireddy

>Course: 5143 Operating Systems

>Date: 2 Mar 2016

###3.4. What does it mean to preempt a process?
Process preemption occurs when the processor interrupts an executing process so that another process can be executed. i.e., for example, that process A is running at a given priority level, and process B, at a higher priority level, is blocked. If the OS learns that the event upon which process B has been waiting has occurred, moving B to a ready state, then it can interrupt process A and dispatch process B. We say that the OS has preempted process. 

###3.5. What is swapping and what is its purpose?
Swapping is a solution to a problem associated with multi programming. Swapping involves moving part or all of a process from main memory to disk. When none of the processes in main memory is in the Ready state, the OS swaps one of the blocked processes out on to disk into a suspend queue. This is a queue of existing processes that have been temporarily kicked out of main memory, or suspended. The OS then brings in another process from the suspend queue, or it honors a new-process request. Execution then continues with the newly arrived process. Swapping, is an I/O operation, and therefore there is the potential for making the problem worse, not better. But because disk I/O is generally the fastest I/O on a system (e.g., compared to tape or printer I/O), swapping will usually enhance performance. 

###3.9. List three general categories of information in a process control block?
   1. Process identification.
   2. Processor state information.
   3. Process control information.

###3.10. Why are two modes (user and kernel) needed?
A user program executes in a user mode, in which certain areas of memory are protected from the user’s use and in which certain instructions may not be executed. The monitor executes in a system mode, or what has come to be called kernel mode, in which privileged instructions may be executed and in which protected areas of memory may be accessed. It can also be explained as, it is necessary to protect the OS and key operating system tables, such as process control blocks, from interference by user programs. In the kernel mode, the software has complete control of the processor and all its instructions, registers, and memory. This level of control is not necessary and for safety is not desirable for user programs. 

###3.12. What is the difference between an interrupt and a trap?
An interrupt is due to some sort of event that is external to and independent of the currently running process, such as the completion of an I/O operation. A trap relates to an error or exception condition generated within the currently running process, such as an illegal file access attempt.
###3.13 Give three examples of an interrupt.
   1. Clock interrupts.
   2. I/O interrupts.
   3. Memory fault.

###3.14. What is the difference between a mode switch and a process switch?
A mode switch may occur without changing the state of the process that is currently in the Running state. A process switch involves taking the currently executing process out of the Running state in favor of another process. The process switch involves saving more state information.




