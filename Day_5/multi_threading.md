<h3>What is a Thread?</h3>

A thread is a unit of execution on concurrent programming. Multithreading is a technique which allows a CPU to execute many tasks of one process at the same time. These threads can execute individually while sharing their process resources.

<h3>What is a Process?</h3>

A process is basically the program in execution. When you start an application in your computer (like a browser or text editor), the operating system creates a process. 

<h3>What is Multithreading in Python?</h3>

Multithreading in Python programming is a well-known technique in which multiple threads in a process share their data space with the main thread which makes information sharing and communication within threads easy and efficient. Threads are lighter than processes. Multi threads may execute individually while sharing their process resources. The purpose of multithreading is to run multiple tasks and function cells at the same time.


<h3>What is Multiprocessing?</h3>

Multiprocessing allows you to run multiple unrelated processes simultaneously. These processes do not share their resources and communicate through IPC.
Python Multithreading vs Multiprocessing

To understand processes and threads, consider this scenario: An .exe file on your computer is a program. When you open it, the OS loads it into memory, and the CPU executes it. The instance of the program which is now running is called the process.

Every process will have 2 fundamental components:

    The Code
    The Data

Now, a process can contain one or more sub-parts called threads. This depends on the OS architecture,.You can think about a thread as a section of the process which can be executed separately by the operating system.

In other words, it is a stream of instructions which can be run independently by the OS. Threads within a single process share the data of that process and are designed to work together for facilitating parallelism.

<h3>Why use Multithreading?</h3>

Multithreading allows you to break down an application into multiple sub-tasks and run these tasks simultaneously. If you use multithreading properly, your application speed, performance, and rendering can all be improved.

<h3>Python MultiThreading</h3>

Python supports constructs for both multiprocessing as well as multithreading. In this tutorial, you will primarily be focusing on implementing multithreaded applications with python. There are two main modules which can be used to handle threads in Python:

    The thread module, and
    The threading module

However, in python, there is also something called a global interpreter lock (GIL). It doesn’t allow for much performance gain and may even reduce the performance of some multithreaded applications. You will learn all about it in the upcoming sections of this tutorial.

The Thread and Threading modules

The two modules that you will learn about in this tutorial are the thread module and the threading module.

However, the thread module has long been deprecated. Starting with Python 3, it has been designated as obsolete and is only accessible as __thread for backward compatibility.

You should use the higher-level threading module for applications which you intend to deploy. The thread module has only been covered here for educational purposes.
The Thread Module

The syntax to create a new thread using this module is as follows:

thread.start_new_thread(function_name, arguments)

<h3>The Threading Module</h3>

This module is the high-level implementation of threading in python and the de facto standard for managing multithreaded applications. It provides a wide range of features when compared to the thread module.
<img src="https://www.guru99.com/images/1/080219_0505_Multithread3.png" alt="" class="lazyloaded" data-ll-status="loaded" width="950" height="534">
<table class="table table-striped">
<tbody>
<tr>
<th>Function Name</th>
<th>Description</th>
</tr>
<tr>
<td><strong>activeCount()</strong></td>
<td>Returns the count of <strong>Thread</strong> objects which are still alive</td>
</tr>
<tr>
<td><strong>currentThread()</strong></td>
<td>Returns the current object of the Thread class.</td>
</tr>
<tr>
<td><strong>enumerate()</strong></td>
<td>Lists all active Thread objects.</td>
</tr>
<tr>
<td><strong>isDaemon()</strong></td>
<td>Returns true if the thread is a daemon.</td>
</tr>
<tr>
<td><strong>isAlive()</strong></td>
<td>Returns true if the thread is still alive.</td>
</tr>
<tr>
<td></td>
<td><strong>Thread Class methods</strong></td>
</tr>
<tr>
<td><strong>start()</strong></td>
<td>Starts the activity of a thread. It must be called only once for each thread because it will throw a runtime error if called multiple times.</td>
</tr>
<tr>
<td><strong>run()</strong></td>
<td>This method denotes the activity of a thread and can be overridden by a class that extends the Thread class.</td>
</tr>
<tr>
<td><strong>join()</strong></td>
<td>It blocks the execution of other code until the thread on which the join() method was called gets terminated.</td>
</tr>
</tbody>
</table>


<h3>Deadlocks and Race conditions</h3>

Before learning about deadlocks and race conditions, it’ll be helpful to understand a few basic definitions related to concurrent programming:

    Critical SectionIt is a fragment of code that accesses or modifies shared variables and must be performed as an atomic transaction.
    Context SwitchIt is the process that a CPU follows to store the state of a thread before changing from one task to another so that it can be resumed from the same point later.

<h3>Deadlocks</h3>

Deadlocks are the most feared issue that developers face when writing concurrent/multithreaded applications in python. The best way to understand deadlocks is by using the classic computer science example problem known as the Dining Philosophers Problem.

The problem statement for dining philosophers is as follows:

Five philosophers are seated on a round table with five plates of spaghetti (a type of pasta) and five forks, as shown in the diagram.
<img src="https://www.guru99.com/images/1/080219_0505_Multithread6.png" alt="" class="lazyloaded" data-ll-status="loaded" width="450" height="398">

At any given time, a philosopher must either be eating or thinking.

Moreover, a philosopher must take the two forks adjacent to him (i.e., the left and right forks) before he can eat the spaghetti. The problem of deadlock occurs when all five philosophers pick up their right forks simultaneously.

Since each of the philosophers has one fork, they will all wait for the others to put their fork down. As a result, none of them will be able to eat spaghetti.

Similarly, in a concurrent system, a deadlock occurs when different threads or processes (philosophers) try to acquire the shared system resources (forks) at the same time. As a result, none of the processes get a chance to execute as they are waiting for another resource held by some other process.
Race Conditions

A race condition is an unwanted state of a program which occurs when a system performs two or more operations simultaneously. For example, consider this simple for loop:

i=0; # a global variable
for x in range(100):
    print(i)
    i+=1;

If you create n number of threads which run this code at once, you cannot determine the value of i (which is shared by the threads) when the program finishes execution. This is because in a real multithreading environment, the threads can overlap, and the value of i which was retrieved and modified by a thread can change in between when some other thread accesses it.

These are the two main classes of problems that can occur in a multithreaded or distributed python application. In the next section, you will learn how to overcome this problem by synchronizing threads.
