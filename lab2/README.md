<strong>
  <span style="font-size: 20px;">
   Objectives:
  </span>
 </strong>
 <strong>
  <span style="font-size: 20px;">
  </span>
 </strong>
 <ul>
  <li>
   Gain insights into the operation of HTTP.
  </li>
  <li>
   Get familiar with basic socket programming.
  </li>
  <li>
   Preparation for programming assignment
  </li>
 </ul>
 <h3 style="">
  Prerequisites:
 </h3>
 <ul>
  <li>
   Week 2 Lectures
  </li>
  <li>
   Relevant Parts of Chapter 2 of the textbook (Sections 2.2 on HTTP and 2.7 on Socket Programming)
  </li>
  <li>
   Basic understanding of Linux. A good resource is
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/">
    here
   </a>
   , but there are several other resources online.
  </li>
  <li>
   Several socket programming resources and sample codes for all three programming languages are available on
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87019" target="_blank">
    this page
   </a>
   .
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87008" target="_blank">
    PingServer.java
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86988" target="_blank">
    http-wireshark-trace-1
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87003" target="_blank">
    http-wireshark-trace-2
   </a>
  </li>
 </ul>
 <h3 style="">
  Marks: 10 marks
 </h3>
 <ul>
  <li>
   This lab comprises several exercises. Pl, note that not all the exercises for this lab are marked. You have to submit a report containing answers to selected exercises only.
  </li>
  <li>
   Please attend the lab in your allocated lab time slot.
  </li>
  <li>
   We expect the students to go through as many of the lab exercises as they can at home and come to the lab to clarify any doubts about the procedure/specifications.
  </li>
 </ul>
 <h3 style="">
  Deadline:
 </h3>
 <p>
  <strong>
   10:00 am Tuesday
  </strong>
  <em>
   <strong>
    20/06/2023
   </strong>
   .
  </em>
  You can submit as many times as you wish before the deadline. A later submission will override the earlier submission, so make sure you submit the correct file. Do not leave until the last moment to submit, as there may be technical or communications errors, and you will not have time to rectify it.
 </p>
 <h3 style="">
  Late Report Submission Penalty:
 </h3>
 <p style="">
  A late penalty will be applied as follows:
 </p>
 <ul>
  <li>
   up to 24 hours after the deadline: 5% reduction
  </li>
  <li>
   more than 24 hours and less than 48 hours after the deadline: 10% reduction
  </li>
  <li>
   more than 48 hours after the deadline: NOT accepted
  </li>
 </ul>
 <p style="">
  Note that the above penalty is applied to your final mark in the report. For example, if you submit your lab report 2 days late and your score on the lab is 8, then your final mark will be 8 - 0.8 (10% penalty) = 7.2.
 </p>
 <h3 style="">
  Submission Instructions:
  <br/>
 </h3>
 <p style="">
  Submit a PDF document Lab2.pdf with answers to Exercises 3, 4 and 5. Your client should be named PingClient.c or PingClient.java, or PingClient.py. Create a tar archive of all the files (e.g. if you have additional header or helper files) called
  <strong>
   Lab2.tar.
  </strong>
  Submit the archive using give. You can submit from a lab machine or ssh into the CSE login server. Instructions to ssh into CSE login servers are
  <a href="https://taggi.cse.unsw.edu.au/FAQ/Logging_In_With_SSH/">
   here
  </a>
  . Max file size for submission is
  <strong>
   3MB
  </strong>
  .
 </p>
 <p style="">
  <strong>
   IMPORTANT: IF YOU ARE USING PYTHON, THEN PLEASE ADD A COMMENT AT THE TOP OF YOUR CODE TO INDICATE THE CORRECT VERSION OF PYTHON (VERSION 2 OR 3). THIS WILL ALLOW US TO USE THIS VERSION OF PYTHON FOR TESTING YOUR CODE.
  </strong>
 </p>
 <h3 style="">
  Original Work Only:
 </h3>
 <p style="">
  You are strongly encouraged to discuss the questions with other students in your lab. However, each student must submit his or her own work. You may need to refer to the material indicated above (particularly socket programming links) and conduct your own research to answer the questions.
 </p>
 <h3>
  System Compatibility (Very Important):
 </h3>
 <p>
  We will test your code on CSE machines via the command-line interface. Note that CSE machines support
  <strong>
   gcc version 10.2, Java 11, Python 2.7 and 3.9. Thus, you must
  </strong>
  test your code on CSE machines before submitting it. This is particularly important if you write your code on your own machine and use an IDE. Before submitting, you MUST test your code on CSE machines (via the command line). If we cannot get your code to work on CSE machines, then we can't mark it, and unfortunately, you won't receive any marks. This point is also relevant to the assignment.
 </p>
 <p>
  <span style="font-size: 24px;">
   <strong>
    Exercise 1:
   </strong>
  </span>
  <b>
   <span style="font-size: 24px;">
    <strong>
     Using Telnet to interact with a Web Server (Unmarked, not to be included in the report)
    </strong>
   </span>
  </b>
 </p>
 <p>
  Follow the steps described below.
 </p>
 <p>
  <b>
   Step 1:
  </b>
  Open an
  <i>
   xterm
  </i>
  window. Enlarge the size of your
  <i>
   xterm
  </i>
  window so that it is reasonably large and covers almost the entire screen.
 </p>
 <p>
  <b>
   Step 2:
  </b>
  Telnet to the vision.ucla.edu web server by typing:
 </p>
 <pre>$telnet vision.ucla.edu 80</pre>
 <p>
  Note that the port number for all web servers is “80”.
 </p>
 <p>
  <b>
   Step 3:
  </b>
  Retrieve the main webpage by typing:
 </p>
 <pre>GET / HTTP/1.1 
host: www.vision.ucla.edu</pre>
 <p>
  <b>
   Important Note
  </b>
  : After typing the last line, you must press the carriage return twice.
 </p>
 <p>
  Question 1: What is the content type of the response? What is the size of the response? When was the webpage last modified? Do you see an "Accept-Ranges" header field? What may this be used for?
 </p>
 <p>
  <b>
   Step 4:
  </b>
  Now execute the HEAD method. When a server receives a request with the HEAD method, it responds with only the message header lines (i.e. the response to the GET method minus the actual requested object).
 </p>
 <pre>HEAD / HTTP/1.1
host: www.vision.ucla.edu</pre>
 <p>
  Question 2: What is the content type of the response? What is the size of the response?
 </p>
 <p>
  Question 3:
  <i>
  </i>
  Using telnet, find a way to get the people.html webpage from vision.ucla.edu
 </p>
 <p>
  Question 4: Why must the host be included in the GET (and HEAD) HTTP 1.1 request messages?
 </p>
 <p>
  <b>
   <span style="font-size: 24px;">
    Exercise 2: Understanding Internet Cookies (unmarked, not to be included in the report)
   </span>
  </b>
 </p>
 <p>
  Question 1. Repeat steps 1-3 in the previous experiment for
  <a href="http://www.google.com.au">
   www.google.com.au
  </a>
  . Does the site set a cookie in your browser? How can you tell by purely examining the HTTP response message received using telnet? How about www.vision.ucla.edu? Do you think this site will set a cookie in your browser?
  <b>
  </b>
 </p>
 <p>
  Question 2. Open a web browser (Firefox/IceWeasel/Mozilla preferred). Go to the browser preferences and remove all existing cookies. Open the google webpage and then view the cookies. How many cookies are stored on your machine? Which sites installed the cookies?
 </p>
 <p>
  Question 3. Repeat the above steps for the vision.ucla.edu website. How many cookies are stored on your machine? Which sites installed the cookies? Is the answer inconsistent with the answer for Question 1? Explain why.
 </p>
 <p>
  <b>
   <span style="font-size: 24px;">
    Exercise 3: Using Wireshark to understand basic HTTP request/response messages (marked, include in your report)
   </span>
  </b>
 </p>
 <p>
  <b>
   <span style="font-size: 24px;">
   </span>
  </b>
  We will not be running Wireshark on a live network connection (You are strongly encouraged to try this on your own machine. Pointers are provided at the end of this exercise). The CSE network administrators do not permit live traffic monitoring for security reasons. Instead, for all our lab exercises, we will use several trace files collected by running Wireshark by one of the textbook’s authors. For this particular experiment, download the following trace file:
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86988" target="_blank">
   http-wireshark-trace-1
  </a>
 </p>
 <table class="table">
  <tbody>
   <tr>
    <td>
     <strong>
      NOTE: IT IS NOT POSSIBLE TO RUN WIRESHARK VIA SSH. IT IS A RESOURCE-INTENSIVE PROGRAM, AND IT WOULD SLOW DOWN THE CSE LOGIN SERVERS. IF YOU WANT TO WORK REMOTELY, THEN MAKE SURE YOU ARE USING VLAB.
     </strong>
     <strong>
      WIRESHARK IS AVAILABLE ON ALL LAB MACHINES AND IN VLAB. HOWEVER, IT CANNOT BE INVOKED FROM THE COMMAND LINE. INSTEAD, GO TO THE APPLICATION MENU, AND SELECT "INTERNET" AND "WIRESHARK".
     </strong>
     <strong>
      YOU CAN ALSO DOWNLOAD AND INSTALL
     </strong>
     <a href="https://www.wireshark.org/download.html" target="_blank">
      <b>
       WIRESHARK
      </b>
     </a>
     <strong>
      ON YOUR PERSONAL MACHINE.
     </strong>
    </td>
   </tr>
  </tbody>
 </table>
 <p>
  The following indicates the steps involved:
 </p>
 <p>
  <strong>
   Step 1:
  </strong>
  Start Wireshark natively on your machine or through VLAB, as noted above.
 </p>
 <p>
  <strong>
   Step 2:
  </strong>
  Load the trace file
  <em>
   http-wireshark-trace-1
  </em>
  by using the
  <em>
   File
  </em>
  pull-down menu, choosing
  <em>
   Open
  </em>
  and selecting the appropriate trace file. This trace file captures a simple request/response interaction between a browser and a web server.
 </p>
 <p>
  <strong>
   Step 3:
  </strong>
  You will see many packets in the packet listing window. Since we are currently only interested in HTTP, we will filter out all the other packets by typing “http” in lowercase in the
  <em>
   Filter
  </em>
  field and pressing Enter. You should now see only HTTP packets in the packet-listing window.
 </p>
 <p>
  <strong>
   Step 4:
  </strong>
  Select the first HTTP message in the packet-listing window and observe the data in the packet-header detail window. Recall that since each HTTP message is encapsulated inside a TCP segment, which is encapsulated inside an IP datagram, which is encapsulated within an Ethernet frame, Wireshark displays the Frame, Ethernet, IP, and TCP packet information as well. We want to minimize the amount of non-HTTP data displayed (we’re interested in HTTP here and will be investigating these other protocols in later labs), so make sure the boxes at the far left of the Frame, Ethernet, IP and TCP information have a right-pointing arrowhead (which means there is hidden, undisplayed information), and the HTTP line has a down-pointing arrowhead (which means that all information about the HTTP message is displayed).
 </p>
 <p>
  <strong>
   NOTE:
  </strong>
  Please neglect the HTTP GET and response for favicon.ico, (the third and fourth HTTP messages in the trace file. Most browsers automatically ask the server if the server has a small icon file that should be displayed next to the displayed URL in the browser. We will ignore references to this pesky file in this lab.)
 </p>
 <p>
  By looking at the information in the HTTP GET and response messages (the first two messages), answer the following questions:
 </p>
 <p>
  Question 1: What is the status code and phrase returned from the server to the client browser?
 </p>
 <p>
  Question 2: When was the HTML file the browser retrieves last modified at the server? Does the response also contain a DATE header? How are these two fields different?
 </p>
 <p>
  Question 3: Is the connection established between the browser and the server persistent or non-persistent? How can you infer this?
 </p>
 <p>
  Question 4: How many bytes of content are being returned to the browser?
 </p>
 <p>
  Question 5: What is the data contained inside the HTTP response packet?
 </p>
 <p>
  <img/>
  <strong>
   Note:
  </strong>
  Students are strongly encouraged to use Wireshark to capture real network traffic on their own machines. Check
  <a href="https://www.wireshark.org/download.html" target="_top">
   https://www.wireshark.org/download.html
  </a>
  for details. Once you have Wireshark installed, do the following. Clear your web browser's cache (Firefox-&gt;Tools-&gt;Clear Recent History). Launch the Wireshark tool by typing Wireshark in the command line. Start Wireshark capture by clicking on: capture -&gt; interfaces -&gt; click Start on the interface eth0. Run the Web browser and enter an URL for a website (e.g.
  <a href="http://www.bbc.co.uk">
   www.bbc.co.uk
  </a>
  ). Stop capturing packets when the web page is fully loaded. Examine the captured trace and answer the questions above. This is just for you to try in your own time. You do not have to include this in your report.
 </p>
 <p>
  <b>
   <span style="font-size: 24px;">
    Exercise 4: Using Wireshark to understand the HTTP CONDITIONAL GET/response interaction (marked, include in your report)
   </span>
  </b>
 </p>
 <p>
  <b>
   <span style="font-size: 24px;">
   </span>
  </b>
  For this particular experiment, download the second trace file:
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87003" target="_blank">
   http-wireshark-trace-2
  </a>
 </p>
 <p>
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/18s2/resources/17311">
  </a>
  The following indicates the steps for this experiment:
 </p>
 <p>
  <strong>
   Step 1:
  </strong>
  Start Wireshark natively on your machine or through VLAB, as noted above.
 </p>
 <p>
  <strong>
   Step 2:
  </strong>
  Load the trace file
  <em>
   http-wireshark-trace-2
  </em>
  by using the
  <em>
   File
  </em>
  pull-down menu, choosing
  <em>
   Open
  </em>
  and selecting the appropriate trace file. This trace file captures a request-response between a client browser and a web server where the client requests the same file from the server within a span of a few seconds.
 </p>
 <p>
  <strong>
   Step 3:
  </strong>
  Filter out all the non-HTTP packets and focus on the HTTP header information in the packet-header detail window.
 </p>
 <p>
  We will focus on the first two GET requests and the corresponding responses (so the first 4 HTTP messages).
 </p>
 <p>
  Question 1: Inspect the contents of the first HTTP GET request from the browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
 </p>
 <p>
  Question 2: Does the HTTP response from the server indicate the last time that the requested file was modified?
 </p>
 <p>
  Question 3: Now inspect the contents of the second HTTP GET request from the browser to the server. Do you see the “IF-MODIFIED-SINCE:” and “IF-NONE-MATCH” lines in the HTTP GET? If so, what information is contained in these header lines?
 </p>
 <p>
  Question 4: What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the file's contents? Explain.
 </p>
 <p>
  <img/>
  Question 5: What is the value of the Etag field in the 2nd response message, and how is it used? Is the Etag value the same as in  the 1
  <sup>
   st
  </sup>
  response?
 </p>
 <p>
  <span style="font-size: 24px;">
   <strong>
    Exercise 5: Ping Client (marked, submit source code as a separate file, include sample output in the report)
   </strong>
  </span>
 </p>
 <p style="text-align: justify;">
  In this exercise, you will study a simple Internet ping server (written in Java), and implement a corresponding client. The functionality provided by these programs is similar to the standard ping programs available in modern operating systems, except that they use UDP rather than Internet Control Message Protocol (ICMP) to communicate with each other. Note that we will study ICMP later in the course. (Most programming languages do not provide a straightforward means to interact with ICMP)
 </p>
 <p style="text-align: justify;">
  The ping protocol allows a client machine to send a packet of data to a remote machine and have the remote machine return the data back to the client unchanged (an action referred to as echoing). Among other uses, the ping protocol allows hosts to determine round-trip times to other machines.
 </p>
 <p>
  <b>
   Ping Server (provided)
  </b>
 </p>
 <p>
  You are given the complete code for the Ping server:
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87008" target="_blank">
   PingServer.java.
  </a>
  The server sits in an infinite loop listening for incoming UDP packets. When a packet arrives at the server, it returns the encapsulated data to the client.
 </p>
 <p>
  Your task is to write the corresponding Ping client. You can use either C, Java or Python to write your client. You should read through the server code thoroughly, as it will help you develop your client program.
 </p>
 <p>
  <b>
   Packet Loss &amp; Delay
  </b>
 </p>
 <p style="text-align: justify;">
  UDP provides applications with an unreliable transport service because messages may get lost in the network due to router queue overflows or other reasons. In contrast, TCP provides applications with a reliable transport service and takes care of any lost packets by retransmitting them until they are successfully received. Therefore, applications using UDP for communication must implement any reliability they need separately at the application level (each application can implement a different policy according to its specific needs). Because packet loss is rare or even non-existent in typical campus networks, the server in this lab injects artificial loss to simulate the effects of network packet loss. The server has a parameter LOSS_RATE that specifies the percentage of lost packets (i.e. dropped). The server also has another parameter AVERAGE_DELAY that simulates the delay incurred by packets on the Internet. You should set AVERAGE_DELAY to a positive value when testing your client and server on the same machine or when machines are nearby on the network. You can set AVERAGE_DELAY to 0 to determine the actual round-trip time between the client and server.
 </p>
 <p>
  <b>
   Compiling and Running Server
  </b>
  <b>
  </b>
  <b>
  </b>
 </p>
 <p>
  To compile the server, type the following at the command prompt:
 </p>
 <pre> $javac PingServer.java
</pre>
 <p>
  To run the server, type the following:
 </p>
 <pre>$java PingServer port
</pre>
 <p>
  where the
  <i>
   port
  </i>
  is the port number the server listens on. Remember to pick a port number greater than 1024 because only processes running with root (administrator) privilege can bind to ports less than 1024. If you get a message that the port is in use, try a different port number, as the one you chose may be in use.
 </p>
 <p>
  <b>
   Note:
  </b>
  if you get a class not found error when running the above command, then you may need to tell Java to look in the current directory to resolve class references. In this case, the commands will be as follows:
 </p>
 <pre>$java -classpath . PingServer port
</pre>
 <h4>
  Your Task: Implementing Ping Client
 </h4>
 <p style="text-align: justify;">
  You should write the client (called PingClient.java or PingClient.c or PingClient.py)  such that it sends 15 ping requests to the server. Each message contains a payload of data with the keyword PING, a sequence number starting from 3,331, and a timestamp. After sending each packet, the client waits up to 600 ms to receive a response. If 600 ms goes by without a response from the server, then the client assumes that its packet or the server's reply packet has been lost in the network.
 </p>
 <p style="text-align: justify;">
  You should write the client so that it executes with the following command:
 </p>
 <pre>$javac PingClient.java
$java PingClient host port (for Java)
</pre>
 <p style="text-align: justify;">
  or
 </p>
 <pre>$ gcc -o PingClient PingClient.c
$./PingClient host port  (for C)
</pre>
 <p style="text-align: justify;">
  or
 </p>
 <pre>$python PingClient.py host port (for Python 2)
$python3 PingClient.py host port (for Python 3)
</pre>
 <p style="text-align: justify;">
  The host is the computer's IP address, the server is running on, and the
  <i>
   port
  </i>
  is the port number it is listening to. In this lab, you will run the client and server on the same machine. So use 127.0.0.1 (i.e., localhost) for the
  <i>
   host
  </i>
  when running your client. In practice, you can run the client and server on different machines.
  <br/>
 </p>
 <p style="text-align: justify;">
  The client should send 15 pings to the server. Because UDP is an unreliable protocol, packets sent to the server may be lost, or packets sent from the server to the client may be lost. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should have the client wait up to 600 ms for a response; if no response is received, then the client should assume that the packet was lost during transmission across the network. It would help if you chose a reasonably significant value that is greater than the expected RTT (Note that the server artificially delays the response using the AVERAGE_DELAY parameter). To achieve this, your socket will need to be non-blocking (i.e. it must not just wait indefinitely for a response from the server). If you use Java, you must research the API for DatagramSocket to determine how to set the timeout value on a datagram socket (Check:
  <a href="http://java.sun.com/javase/6/docs/api/java/net/Socket.html">
   http://java.sun.com/javase/6/docs/api/java/net/Socket.html
  </a>
  ). If you are using C, you can find information here:
  <a href="http://www.beej.us/guide/bgnet/html/multi/index.html" target="_blank">
   http://www.beej.us
  </a>
  . Note that the
  <i>
   fcntl()
  </i>
  function is the simplest way to achieve this.
  <br/>
 </p>
 <p>
  Note that your client should not send all 15 ping messages back-to-back but rather sequentially. The client should send one ping and then wait for either the reply from the server or a timeout before transmitting the next ping. Upon receiving a response from the server, your client should compute the RTT, i.e. the difference between when the packet was sent and the response was received. There exist functions in Java, Python and C that will allow you to read the system time in milliseconds. The RTT value should be printed to the standard output (similar to the output printed by ping; have a look at the output of ping for yourself). An example output could be:
 </p>
 <pre>ping to 127.0.0.1, seq = 1, rtt = 120 ms
</pre>
 <p>
  We prefer that you show the timeout requests in the output. Only replace the 'rtt=120ms' in the above example with 'time out'. You will also need to report the minimum, maximum and average RTTs of all packets received successfully at the end of your program's output.
 </p>
 <p>
  <b>
   Message Format
  </b>
  <b>
  </b>
 </p>
 <p>
  The ping messages in this lab are formatted in a simple way. Each message contains a sequence of characters terminated by a carriage return (CR) character (\r) and a line feed (LF) character (\n). The message contains the following string:
 </p>
 <p>
  <i>
   PING  sequence_number  time  CRLF
  </i>
 </p>
 <p>
  where
  <i>
   sequence_number
  </i>
  starts at 3,331 and progresses to 3,345 for each successive ping message sent by the client,
  <i>
   time
  </i>
  is the time when the client sent the message, and CRLF represents the carriage return and line feed characters that terminate the line.
 </p>
 <p>
  <i>
   Hint: Cut and paste PingServer, rename the code PingClient, and then modify the code if you use Java.
  </i>
 </p>
 <p>
  <span style="font-size: 24px;">
   <b>
    Optional Extensions (For students keen to take up a challenge.  THESE ARE NOT MARKED)
   </b>
   <b>
   </b>
  </span>
 </p>
 <p style="text-align: justify;">
  When you are finished writing the client, you may wish to try one of the following exercises:
 </p>
 <p style="text-align: justify;">
  1) The basic program sends a new ping immediately when it receives a reply. Modify the program to send precisely 1 ping per second, similar to how the standard ping program works (difficult).
  <br/>
 </p>
 <p style="text-align: justify;">
  2) Develop two new classes
  <i>
   ReliableUdpSender
  </i>
  <i>
   and ReliableUdpReceiver
  </i>
  , which are used to send and receive data reliably over UDP. To do this, you must devise a protocol (such as TCP) in which the data recipient returns acknowledgements to the sender to indicate that the data has arrived. You can simplify the problem by only providing one-way transport of application data from sender to recipient. Because your experiments may be in a network environment with little or no loss of IP packets, you should simulate packet loss (difficult).
