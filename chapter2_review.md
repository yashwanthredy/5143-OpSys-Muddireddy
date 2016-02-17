#Chapter 2 Review Questions
>Name: Yashwanth Reddy Muddireddy

>Course: 5143 Operating Systems

>Date: 17 Feb 2016 

###1.What are three objectives of an OS design?

#####Main Objectives in OS design:
  - **Convenience** – makes computer user friendly.
  
  - **Efficiency** - allows computer to use resources efficiently.
  
  - **Ability to evolve** - constructed in a way to permit effective development, testing and introduction of new functions without         interfering with service. 

###2. What is the kernel of an OS?

The kernel is the central module or portion of the operating system software, which is used almost all the times. Usually, the kernel stays in main memory. The kernel runs in a privileged mode and is responsible for memory management, process and task management, and disk management. It connects the system hardware to the application software.

###3. What is multiprogramming?

When two or more programs are residing in memory at the same time, then sharing the processor is referred to the multiprogramming. Multiprogramming assumes a single shared processor. Multiprogramming increases CPU utilization by organizing jobs so that the CPU always has one to execute.

###4. What is a process?

A process is a program in execution. The execution of a process must progress in a sequential fashion. A process is defined as an entity, which represents the basic unit of work to be implemented in the system. A process is controlled and scheduled by the operating system.

###5. How is the execution context of a process used by the OS?

The execution context, also known as process state, it is an internal information which is used by operating system to manage and control the process. This internal information is separated from the process, because the operating system has information not permitted to the process. The context includes all of the information that the operating system needs to manage the process and that the processor needs to execute the process properly. 

The context includes the contents of the various processor registers, such as the program counter and data registers. It also includes information of use to the operating system, such as the priority of the process and whether the process is waiting for the completion of a particular I/O event and at all the interruption the contents of all the registers of process are recorded in execution context.

###6.List and briefly explain five storage management responsibilities of a typical OS?

- **Process isolation:** The operating system must isolate the independent processes in regards of each other’s memory interfering on basis of both data and instructions. 

- **Automatic allocation and management:** Programs should be dynamically allocated across the memory hierarchy as required. Allocation should be in sight to the programmer. Thus, the programmer will be no longer feel distressed of concerns relating to memory limitations, and the operating system can achieve efficiency by assigning memory to jobs only as needed. 

- **Support of modular programming:** This should help the programmers, be able to define dynamically program modules, and to create, destroy, and alter the size of modules. 

- **Protection and access control:** If a particular application needs sharing of memory then sharing of memory, at any level of the memory hierarchy is desirable. But, the operating systems needs to be careful in regards of sharing of memory, at any level of the memory hierarchy because it creates strength for one program to address the memory space of another. At other times, it threatens the integrity of programs and even of the operating system itself. The operating system must allow portions of memory to be accessible in various ways by various users. 

- **Long-term storage:** Many application programs require means for storing information for extended periods of time, after the computer has been powered down.

###7.Explain the distinction between a real address and a virtual address?

Real address is an address in main memory. Real addressing means that the program actually knows the real layout of RAM. A virtual address refers to a memory location in virtual memory; the location is on disk and sometimes in main memory. With virtual addressing, all application memory accesses go to a page table, which then maps from the virtual to the physical address. So every application has its own "private" address space, and no program can read or write to another program's memory. This is called segmentation.

###8.Describe the round-robin scheduling technique?

In the round robin scheduling, processes are dispatched in a FIFO manner but are given a limited amount of CPU time called a time-slice or a quantum. If a process does not complete before its CPU-time expires, the CPU is preempted and given to the next process waiting in a queue. The preempted process is then placed at the back of the ready list. 

Round Robin Scheduling is preemptive (at the end of time-slice) therefore it is effective in time-sharing environments in which the system needs to guarantee reasonable response times for interactive users. The only interesting issue with round robin scheme is the length of the quantum. Setting the quantum too short causes too many context switches and lowers the CPU efficiency. On the other hand, setting the quantum too long may cause poor response time and approximates FCFS.In any event, the average waiting time under round robin scheduling is often quite long.

###9.Explain the difference between a monolithic kernel and a microkernel?
**Monolithic kernel** is a single large process running entirely in a single address space. It is a single static binary file. All kernel services exist and execute in the kernel address space. The kernel can invoke functions directly **In microkernels** the kernel is broken down into separate processes, known as servers. Some of the servers run in kernel space and some run in user-space. All servers are kept separate and run in different address spaces. Servers invoke "services" from each other by sending messages via IPC (Inter process Communication). This separation has the advantage that if one server fails, other servers can still work efficiently.

###10.What is multithreading?

Multithreading is an execution model that allows a single process to have multiple code segments (i.e., threads) run concurrently within the “context” of that process. You can think of threads as child processes that share the parent process resources but execute independently. Multiple threads of a single process can share the CPU in a single CPU system or (purely) run in parallel in a multiprocessing system.

###11.List the key design issues for an SMP operating system?

 - **Simultaneous concurrent processes or threads**: Kernel routines need to be reentrant i.e.,(same copy can be shared by multiple users   )to allow several processors to execute the same kernel code simultaneously.
 
 - **Scheduling**: Any processor may perform scheduling, so conflicts must be avoided.
 
 - **Synchronization**: This point comes into act where multiple processes have to access to shared address spaces or shared I/O resources,  so care must be taken to provide effective synchronization among them. 
 
 - **Memory Management**:  Cache memory just brings a portion of main memory on its requirement; here we have a problem with cache memory.  Memory management on a multiprocessor must deal with all of the issues found on uniprocessor machines. If a processor changes the        contents of the main memory, these changes have to be recorded in the cache memories that contain a portion of main memory. This is      known as cache coherence problem and is typically solved in hardware.
 
- **Reliability and fault tolerance**: The operating system should provide low chances in the face of processor failure.




