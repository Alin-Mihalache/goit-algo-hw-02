Homework description
Task 1
You are to develop a program that simulates the acceptance and processing of requests: the program should automatically generate new requests (identified by a unique number or other data), 
add them to the queue, and then sequentially remove them from the queue for "processing", thus simulating the work of a service center.
Here is the pseudo-code for a task using a queue (Queue from the queue module in Python) for a request processing system:

import Queue

Create a queue of applications
queue = Queue()

The generate_request() function:
    Create a new request
    Add a request to the queue

Function process_request():
    If the queue is not empty:
        Remove a request from the queue
        Process the request
    Otherwise:
        Display a message that the queue is empty

The main cycle of the program:
    Until the user exits the application:
        Execute generate_request() to create new requests
        Execute process_request() to process requests

Task 2
Your task is to develop a function that takes a string as input, adds all its characters to a two-way queue (deque from the collections module in Python), 
and then compares the characters at both ends of the queue to determine if the string is a palindrome. 
The program should correctly handle both even and odd-numbered strings and be case and space-insensitive.
