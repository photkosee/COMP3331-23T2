<h3>
  Objectives:
 </h3>
 <ul>
  <li>
   Gain insights into the operation of the DNS protocol
  </li>
  <li>
   Dig deep into DNS server organisation
  </li>
  <li>
   Get familiar with the socket programming
  </li>
 </ul>
 <h3>
  Prerequisites &amp; Links:
 </h3>
 <ul>
  <li>
   Week 3 Lectures
  </li>
  <li>
   Relevant Parts of Chapter 2 of the textbook (Sections 2.4 on DNS and 2.7 on Socket programming)
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T1/resources/83638" target="_blank">
    Introduction to Tools of the Trade
   </a>
  </li>
  <li>
   Basic understanding of Linux. A good resource is
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/" target="_blank">
    here
   </a>
   but there are several other resources online.
  </li>
  <li>
   Several socket programming resources and sample code for all 3 programming languages are available
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87019" target="_blank">
    here
   </a>
   .
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86984" target="_blank">
    dns-wireshark-trace-2
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86993" target="_blank">
    index.html
   </a>
  </li>
 </ul>
 <h3>
  Marks:
  <strong>
   10 marks.
  </strong>
 </h3>
 <ul>
  <li>
   <span rel="font-size: 14px;" style="font-size: 14px;">
    This lab comprises a number of exercises. Pl, note that not all the exercises for this lab are marked. You have to submit a report containing answers to selected exercises only (Exercises 3 &amp; 4)
   </span>
  </li>
  <li>
   <span style="font-size: 14px;">
    Please attend the lab in your allocated lab time slot
   </span>
  </li>
  <li>
   <span style="font-size: 14px;">
    We expect the students to go through as much of the lab exercises as they can at home and come to the lab for clarifying any doubts in procedure/specifications
   </span>
  </li>
 </ul>
 <h3>
  Deadline:
 </h3>
 <p>
  <strong>
   <em>
    10:00 am 27/06/2023
   </em>
   .
  </strong>
  You can submit as many times as you wish before the deadline. A later submission will override the earlier submission, so make sure you submit the correct file. Do not leave until the last moment to submit, as there may be technical or communications errors and you will not have time to rectify it.
 </p>
 <h3>
  Late Report Submission Penalty:
 </h3>
 <p>
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
 <p>
  Note that the above penalty is applied to your final mark for your lab report. For example, if you submit your lab work report 2 days late and your score on the lab report is 8, then your final mark will be 8 - 0.8 (10% penalty) = 7.2.
 </p>
 <h3>
  Submission Instructions:
  <br/>
 </h3>
 <p>
  Create a PDF document
  <strong>
   Lab3.pdf
  </strong>
  with answers to Exercise 3. You also need to submit your source code file for Exercise 4. Your server should be named WebServer.c or WebServer.java or WebServer.py. Create a tar archive of all the files called
  <strong>
   Lab3.tar
  </strong>
  . Submit the archive using the give or use the WebCMS3 interface. You can submit from a lab machine or ssh into the CSE login server. Instructions to ssh into CSE login servers are
  <a href="https://taggi.cse.unsw.edu.au/FAQ/Logging_In_With_SSH/">
   here
  </a>
  .
 </p>
 <ol>
  <li>
   Put all your files (e.g., Lab3.pdf, WebServer source file) in a directory lab3.
  </li>
  <li>
   Type “tar -cvf Lab3.tar lab3”
  </li>
  <li>
   When you are ready to submit, at the bash prompt type 3331
  </li>
  <li>
   Next, type: give cs3331 Lab3 Lab3.tar
  </li>
 </ol>
 <ul>
  <li>
   You should make sure that the tar archive is not corrupted. You can untar (use tar –xvf Lab3.tar) the created archive to check that all the files are intact.
  </li>
  <li>
   Max file size for submission is
   <strong>
    3MB
   </strong>
   .
  </li>
  <li>
   COMP9331 students should also use 'give cs3331'
  </li>
 </ul>
 <p>
  If you are using Python, then please add a comment at the top of your code to indicate the correct version of Python to use for testing.
 </p>
 <h3>
  Original Work Only:
 </h3>
 <p>
  You are strongly encouraged to discuss the questions with other students in your lab. However, each student must submit his or her own work. You may need to refer to the material indicated above (particularly the Tools of the Trade document) and also conduct your own research to answer the questions.
 </p>
 <p>
  <b>
   <span style="font-size: 20px;">
    OS Compatibility:
   </span>
  </b>
 </p>
 <p>
  We will test your code on CSE machines via the command-line interface. Note that CSE machines support
  <b>
   gcc version 10.2, Java 11, Python 2.7 and 3.9. Thus, you must
  </b>
  test your code on CSE machines before submitting it. This is particularly important if you write your code on your own machine and use an IDE. Before submitting, you MUST test your code on CSE machines (via the command line). If we cannot get your code to work on CSE machines, then we can't mark it, and unfortunately, you won't receive any marks.
 </p>
 <h3>
  Exercise 1: Explore DNS records (Not marked, No need to submit)
  <br/>
 </h3>
 <p>
  DNS servers use different record types for different purposes. Each type of DNS record has an associated type of DNS query. Check the following page (
  <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">
   https://en.wikipedia.org/wiki/List_of_DNS_record_types
  </a>
  ) and find out what the following resource record types are used for:
 </p>
 <ul>
  <li>
   A
  </li>
  <li>
   CNAME
  </li>
  <li>
   MX
  </li>
  <li>
   NS
  </li>
  <li>
   PTR
  </li>
  <li>
   SOA
  </li>
 </ul>
 <h3>
  Exercise 2: Tracing DNS with Wireshark (Not marked, No need to submit)
 </h3>
 <p>
  For this particular experiment, download the DNS trace file:
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86984" target="_blank">
   dns-wireshark-trace-2
  </a>
  .
 </p>
 <p>
  Step 1: Start Wireshark natively on your machine or through VLAB.
 </p>
 <p>
  Step 2: Load the trace file
  <i>
   dns-wireshark-trace-2
  </i>
  by using the
  <i>
   File
  </i>
  pull-down menu, choosing
  <i>
   Open
  </i>
  and selecting the appropriate trace file. This file captures the sequence of messages exchanged between a host and its default DNS server while using the
  <i>
   nslookup
  </i>
  (similar to the dig tool we used earlier in the lab) utility for obtaining the canonical name (type A record) of
  <a href="http://www.mit.edu">
   www.mit.edu
  </a>
  . The IP address of the default DNS server for the host is 128.238.29.22. Now filter out all non-DNS packets by typing “dns” (without quotes) in the filter field. Also, click the right arrow for DNS in the packet-header detail window. Now focus on the
  <strong>
   last two DNS messages
  </strong>
  from the 6 listed and answer the following questions:
 </p>
 <p>
  Question 1: What transport layer protocol is being used by the DNS messages?
 </p>
 <p>
  Question 2: What are the source and destination port for the DNS query message and the corresponding response?
 </p>
 <p>
  Question 3: To what IP address is the DNS query message sent? Is this the same as the default local DNS server?
 </p>
 <p>
  Question 4: How many “questions” are contained in the DNS query message? What “Type” of DNS queries are they? Does the query message also contain any “answers”?
 </p>
 <p>
  Question 5: Examine the DNS response message. Provide details of the contents of the “Answers”, “Authority” and “Additional Information” fields. What can you infer from these?
 </p>
 <p>
  <strong>
   <span style="font-size: 20px;">
    Exercise 3: Digging into DNS (marked, include in the lab report)
   </span>
  </strong>
 </p>
 <p>
  To answer the following questions, you will make DNS queries using some of the query types you have encountered in the above exercise. Some questions may require you to send multiple DNS queries. Before you proceed, read the manpage of dig (type man dig in the terminal). Make sure you understand how you can explicitly specify the following:
 </p>
 <ul>
  <li>
   nameserver to query
  </li>
  <li>
   type of DNS query to make (the default query types are those you saw in exercise 1)
  </li>
  <li>
   performing reverse queries
  </li>
 </ul>
 <p>
  <strong>
   Note:
  </strong>
  Include the output of all the dig commands you have used in your answers.
 </p>
 <p>
  To send a query to a particular name server (say x.x.x.x) you should use the following command:
 </p>
 <pre>dig @x.x.x.x hostname</pre>
 <p>
  Question 1. What is the IP address of
  <a href="http://www.stanford.edu">
   www.stanford.edu
  </a>
  ? What type of DNS query is sent to get this answer?
  <br/>
 </p>
 <p>
  Question 2. What is the canonical name for the Stanford webserver (i.e.,
  <a href="http://www.stanford.edu">
   www.stanford.edu
  </a>
  )? Suggest a reason for having an alias for this server.
 </p>
 <p>
  Question 3. What can you make of the rest of the response (i.e. the details available in the Authority and Additional sections)?
  <br/>
 </p>
 <p>
  Question 4. What is the IP address of the local nameserver for your machine?
 </p>
 <p>
  Question 5. What are the DNS nameservers for the "stanford.edu.” domain (note: the domain name is stanford.edu and not
  <a href="http://www.stanford.edu">
   www.stanford.edu
  </a>
  . This is an example of what is referred to as the apex/naked domain)? Find their IP addresses. What type of DNS query is sent to obtain this information?
 </p>
 <p>
  Question 6. What is the DNS name associated with the IP address
  <span class="s1">
   129.25.60.56
  </span>
  ? What type of DNS query is sent to obtain this information?
 </p>
 <p>
  Question 7. Run, dig and query the CSE nameserver (129.94.242.33) for the mail servers for google.com (again, the domain name is google.com, not
  <a href="http://www.google.com">
   www.google.com
  </a>
  ). Did you get an authoritative answer? Why? (HINT: Just because a response contains information in the authoritative part of the DNS response message does not mean it came from an authoritative name server. You should examine the flags in the response message to determine the answer)
 </p>
 <p>
  Question 8. Repeat the above (i.e. Question 7) but use one of the nameservers obtained in Question 5. What is the result?
  <br/>
 </p>
 <p>
  Question 9. Obtain the authoritative answer for the mail servers for google.com. What type of DNS query is sent to obtain this information?
 </p>
 <p>
  Question 10. In this exercise, you simulate the iterative DNS query process to find the IP address of your machine (e.g. lyre00.cse.unsw.edu.au). If you are using VLAB Then find the IP address of one of the following: lyre00.cse.unsw.edu.au, lyre01.cse.unsw.edu.au, flute00.cse.unsw.edu.au or flute01.cse.unsw.edu.au. First, find the name server (query type NS) of the "." domain (root domain). Query this nameserver to find the authoritative name server for the "au." domain. Query this second server to find the authoritative nameserver for the "edu.au." domain. Now query this nameserver to find the authoritative nameserver for "unsw.edu.au". Next query the nameserver of unsw.edu.au to find the authoritative name server of cse.unsw.edu.au. Now query the nameserver of cse.unsw.edu.au to find the IP address of your host. How many DNS servers do you have to query to get the authoritative answer?
 </p>
 <p>
  Question 11. Can one physical machine have several names and/or IP addresses associated with it?
 </p>
 <p>
  <strong>
   <span style="font-size: 20px;">
    Exercise 4: A Simple Web Server (Marked, submit your code
   </span>
  </strong>
  <strong>
   <span style="font-size: 18px;">
    )
   </span>
  </strong>
 </p>
 <p>
  <strong>
   <span style="font-size: 18px;">
    Please submit the source code as a separate file. The tutor will run the code to check if the output is as expected.
   </span>
  </strong>
 </p>
 <p>
  In this exercise, you will learn the basics of TCP socket programming: how to create a socket, bind it to a specific address and port, and send and receive an HTTP packet. You will also learn some basics of HTTP header format. You will develop a web server that handles one HTTP request at a time. Your server should handle persistent connections (i.e.
  <strong>
   HTTP 1.1, the default version of HTTP used by all browsers)
  </strong>
  . Specifically, your web server should do the following:
 </p>
 <p>
  (i) create a connection socket when contacted by a client (browser).
 </p>
 <p>
  (ii) receive HTTP requests from this connection. Your server should only process GET requests. You may assume that only GET requests will be received.
 </p>
 <p>
  (iii) parse the request to determine the specific file being requested.
 </p>
 <p>
  (iv) get the requested file from the server's file system.
 </p>
 <p>
  (v) create an HTTP response message consisting of the requested file preceded by header lines.
 </p>
 <p>
  (vi) send the response over the TCP connection to the requesting browser.
 </p>
 <p>
  (vii) If the requested file is not present on the server, the server should send an HTTP “404 Not Found” message back to the client.
 </p>
 <p>
  (viii) the server should listen in a loop, waiting for the next request from the browser.
 </p>
 <p>
  You don't have to deal with any other error conditions.
 </p>
 <p>
  Your program should be called WebServer.c or WebServer.java or WebServer.py.
 </p>
 <p>
  You should write the server so that it executes with the following command:
 </p>
 <pre>$java WebServer port (for Java)</pre>
 <pre>$WebServer port (for C)</pre>
 <pre>$python WebServer.py port (for Python 2)</pre>
 <pre>$python3 WebServer.py port (for Python)</pre>
 <p>
  where the port is the port No your Web server will be listening on. Specify a non-standard port No (other than 80 and 8080, and &gt; 1024). We will use this port No in the URL while issuing requests from the web browser.
 </p>
 <p>
  1. Place a simple HTML file (index.html, without any hyperlinks) in the same directory as the server program. A sample index.html file is provided
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86993" target="_blank">
   here
  </a>
  . Run the server program as indicated above. Open a web browser on the same machine. Type the following URL:
 </p>
 <pre>http://127.0.0.1:port/index.html</pre>
 <p>
  where the
  <em>
   port
  </em>
  is the port number your server is listening on. Note that if you forget to include the port number, the browser will assume the default port of 80 while we are running our web server on a non-standard port. The browser should display the content of index.html.
 </p>
 <p>
  2. Place multiple image files (.png) in the same directory as the server program. Run the server program as indicated above. Open a web browser on the same machine. The type
 </p>
 <pre>http://127.0.0.1:port/myimage.png</pre>
 <p>
  where the
  <em>
   port
  </em>
  is the port number the server listens on and
  <em>
   myimage.png
  </em>
  is one of the image files present in the server's directory. The browser should display the image.
 </p>
 <p>
  3. Now try and request for an object that does not exist in the server directory, e.g.:
 </p>
 <pre>http://127.0.0.1:port/bio.html</pre>
 <p>
  The browser should display the 404 error message. Note that showing a specific error message depends on the browser. If you are sending the correct 404 error message and the browser is still not displaying it, you may consider sending a custom error message as text/html in the body of your response.
 </p>
 <p>
  Note that you cannot use any of the pre-made web servers available in different programming languages. Examples include http.server in Python.
 </p>
 <p>
  <strong>
   Note:
  </strong>
  Most browsers send a GET request for a "favicon.ico" object when accessing a website. This is the site-specific icon that you normally see in your browser's address bar. Your server is not required to handle this request. Your server can respond back with a 204 error (no content) for such requests. Further details about the favicon can be found
  <a href="https://en.wikipedia.org/wiki/Favicon">
   here
  </a>
  .
 </p>
 <p>
  <strong>
   EDIT:
  </strong>
  I have added a tag to the header field of the index.html file, which should prevent the browser from sending the favicon.ico request. Use the updated index.html page (linked at the top of this page)
 </p>