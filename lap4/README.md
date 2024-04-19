<h3>
  Objectives:
 </h3>
 <ul>
  <li>
   Gain insights into the operation of TCP.
  </li>
  <li>
   get familiar with the ns-2 simulator (as preparation for the next two labs)
  </li>
 </ul>
 <h3>
  Prerequisites and Links:
 </h3>
 <ul>
  <li>
   Week 5 Lectures
  </li>
  <li>
   Relevant Parts of Chapter 3 of the textbook
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86895" target="_blank">
    Introduction to Tools of the Trade
   </a>
  </li>
  <li>
   Basic understanding of Linux. A good resource is
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/" target="_blank">
    here
   </a>
   , but there are several other resources online:
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86991" target="_blank">
    tcp-wireshark-trace-1
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86997" target="_blank">
    NS2 overview slides
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86998" target="_blank">
    simpleSim.tcl
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86996" target="_blank">
    Explanation of script simpleSim.tcl
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
   This lab comprises several exercises. Pl, note that not all the exercises for this lab are marked. You must submit a report containing answers to all questions in
   <strong>
    <em>
     Exercises 1 and 2 only.
    </em>
   </strong>
  </li>
  <li>
   Please attend the lab in your allocated lab time slot.
  </li>
  <li>
   We expect the students to go through as many of the lab exercises as they can at home and come to the lab to clarify any doubts about the procedure/specifications.
  </li>
 </ul>
 <h3>
  Deadline:
 </h3>
 <p>
  <strong>
   10:00 am
  </strong>
  <strong>
   Tuesday 18/07/2023.
  </strong>
  You can submit as many times as you wish before the deadline. A later submission will override the earlier submission, so make sure you submit the correct file. Do not leave until the last moment to submit, as there may be technical or communications errors, and you will not have time to rectify it.
 </p>
 <h3>
  Late Submission Penalty:
 </h3>
 <p>
  A late penalty will be applied as follows:
 </p>
 <ul>
  <li>
   1 day after deadline: 5% reduction
  </li>
  <li>
   2 days after deadline: 10% reduction
  </li>
  <li>
   3 or more days late: NOT accepted
  </li>
 </ul>
 <p>
  Note that the above penalty is applied to your final mark. For example, if you submit your lab work 2 days late and your score on the lab is 8, then your final mark will be 8 - 0.8 (10% penalty) = 7.2.
 </p>
 <h3>
  Submission Instructions:
  <br/>
 </h3>
 <p>
  Submit a PDF document
  <strong>
   Lab4.pdf
  </strong>
  with answers to all questions for Exercises 1 &amp; 2 only.
  <b>
   There is no need to create an archive.
  </b>
  Submit the PDF directly.
 </p>
 <ol>
  <li>
   When you are ready to submit, at the bash prompt type 3331
  </li>
  <li>
   Next, type: give cs3331 Lab4 Lab4.pdf
  </li>
 </ol>
 <p>
  Alternatively, submit the PDF file through WebCMS.
 </p>
 <h3>
  Original Work Only:
 </h3>
 <p>
  You are strongly encouraged to discuss the questions with other students in your lab. However, each student must submit his or her own work. You may need to refer to the material indicated above (particularly the Tools of the Trade document) and conduct your own research to answer the questions.
 </p>
 <h3>
  Exercise 1: Understanding TCP using Wireshark
 </h3>
 <p>
  For this particular experiment, download the trace file:
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86991" target="_blank">
   tcp-wireshark-trace-1
  </a>
  <i>
   .
  </i>
 </p>
 <p>
  The following indicates the steps for this experiment:
 </p>
 <p>
  Step 1: Launch Wireshark by searching for it in the application finder. NOTE: If wireshark does not launch then type the following at a terminal while you are in the VLAB environment - "3331 wireshark".
 </p>
 <p>
  Step 2: Load the trace file
  <i>
   tcp-ethereal-trace-1
  </i>
  by using the
  <i>
   File
  </i>
  pull-down menu, choosing
  <i>
   Open
  </i>
  and selecting the appropriate trace file. This file captures the sequence of messages exchanged between a host and a remote server (gaia.cs.umass.edu). The host transfers a 150 KB text file containing the text of Lewis Carrol’s
  <i>
   Alice’s Adventure in Wonderland
  </i>
  to the server. Note that the file is being transferred from the host to the server using an HTTP POST message.
 </p>
 <p>
  Step 3: Now filter out all non-TCP packets by typing “tcp” (without quotes) in the filter field towards the top of the Wireshark window. You should see a series of TCP segments between the host in MIT and gaia.cs.umass.edu. The first three segments of the trace consist of the initial three-way handshake containing the SYN, SYN ACK and ACK messages. You should see an HTTP POST message in the 4
  <sup>
   th
  </sup>
  segment of the trace being sent from the host in MIT to gaia.cs.umass.edu (check the contents of the payload of this segment). You should observe that the text file is transmitted as multiple TCP segments (i.e. a single POST message has been split into several TCP segments) from the client to the server (gaia.cs.umass.edu). You should also see several TCP ACK segments being returned reversely.
 </p>
 <p>
  <b>
   IMPORTANT NOTE:
  </b>
  Do the sequence numbers for the sender and receiver start from zero? This is because Wireshark, by default, scales down all real sequence numbers such that the first segment in the trace file always starts from 0. To turn off this feature, you have to click Edit-&gt;Preferences&gt;Protocols-&gt;TCP (or Wireshark-&gt;Preferences-&gt;Protocols-&gt;TCP) and then disable the “Relative Sequence Numbers” option. Note that the answers in the solution set will reflect this change. If you conduct the experiment without this change, the sequence numbers you observe will differ from those in the answers. Also, set the time shown in the 2nd column as the "Seconds since first captured packet" or "Seconds since begining of capture" under view-&gt;Time display format.
 </p>
 <p>
  <a name="OLE_LINK6">
  </a>
  <i>
   Question 1
  </i>
  . What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection? What are the IP address and TCP port numbers used by the client computer (source) that is transferring the file to gaia.cs.umass.edu?
 </p>
 <p>
  <i>
   Question 2.
  </i>
  What is the sequence number of the TCP segment containing the HTTP POST command? Note that to find the POST command, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with a “POST” within its DATA field.
  <br/>
 </p>
 <p>
  <i>
   Question 3.
  </i>
  Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection.
 </p>
 <p>
  (a) What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST) sent from the client to the webserver (Do not consider the ACKs received from the server as part of these six segments)?
 </p>
 <p>
  (b) At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent and when its acknowledgement was received, what is the RTT value for each of the six segments?
 </p>
 <p>
  (c) What is the
  <i>
   EstimatedRTT
  </i>
  value (see relevant parts of Section 3.5 or lecture slides) after receiving each ACK? Assume that the initial value of
  <i>
   EstimatedRTT
  </i>
  is equal to the measured RTT (
  <i>
   SampleRTT
  </i>
  ) for the first segment and then is computed using the
  <i>
   EstimatedRTT
  </i>
  equation for all subsequent segments. Set alpha to 0.125.
 </p>
 <p>
  <b>
   Note:
  </b>
  Wireshark has a nice feature that allows you to plot the RTT for each TCP segment sent. Select a TCP segment in the “listing of captured packets” window that is being sent from the client to the gaia.cs.umass.edu server. Then select:
  <i>
   Statistics-&gt;TCP Stream Graph&gt;Round Trip Time Graph
  </i>
  . However, do not use this graph to answer the above question.
 </p>
 <p>
  <a name="OLE_LINK10">
  </a>
  <i>
   Question 4.
  </i>
  What is the length of each of the first six TCP segments? (same six segments as Question 3)
 </p>
 <p>
  <i>
   Question 5.
  </i>
  What is the minimum amount of available buffer space advertised at the receiver for the entire trace? Does the lack of receiver buffer space ever throttle the sender?
 </p>
 <p>
  Question 6. Are there any retransmitted segments in the trace file? To answer this question, what did you check for (in the trace)?
 </p>
 <p>
  <i>
   Question 7.
  </i>
  How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (recall the discussion about delayed acks from the lecture notes or Section 3.5 of the text)?
 </p>
 <p>
  <i>
   Question 8.
  </i>
  What is the TCP connection's throughput (bytes transferred per unit of time)? Explain how you calculated this value.
 </p>
 <h3>
  Exercise 2: TCP Connection Management
 </h3>
 <p>
  Consider the following TCP transaction between a client (10.9.16.201) and a server (10.99.6.175).
 </p>
 <p>
  <img src="/static/uploads/pic/z3003139/9cd551d541d7250901a394ee82b69c6b17b3642ca8b1e970b06a9dbe7490a13f/Screen_Shot_2018-08-28_at_8.06.30_pm.png"/>
 </p>
 <p>
  Answer the following questions:
  <br/>
 </p>
 <p>
  <i>
   Question 1
  </i>
  . What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and server?
 </p>
 <p>
  <i>
   Question 2.
  </i>
  What is the sequence number of the SYNACK segment sent by the server to the client computer in reply to the SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did the server determine that value?
 </p>
 <p>
  <em>
   Question 3
  </em>
  . What is the sequence number of the ACK segment sent by the client computer in response to the SYNACK? What is the value of the Acknowledgment field in this ACK segment? Does this segment contain any data?
 </p>
 <p>
  <em>
   Question 4
  </em>
  . Who has done the active close? Is it the client or the server? How you have determined this? What type of closure has been performed? 3 Segment (FIN/FINACK/ACK), 4 Segment (FIN/ACK/FIN/ACK) or Simultaneous close?
 </p>
 <p>
  <em>
   Question 5
  </em>
  . How many data bytes have been transferred from the client to the server and from the server to the client during the whole duration of the connection? What relationship does this have with the Initial Sequence Number and the final ACK received from the other side?
 </p>
 <h3>
  Exercise 3: Getting familiarised with ns-2 simulator (not marked, do not include in your report)
 </h3>
 <p>
  <strong>
   IMPORTANT NOTE:
  </strong>
  ns-2 and Nam are installed on all CSE lab machines.
  <strong>
   We do not recommend that you install ns-2 on your personal machines. This is not as straightforward as installing Wireshark
  </strong>
  . Moreover, the provided scripts have ONLY been tested on CSE machines and may not work on other operating systems. We cannot offer support for running ns-2 natively on your local machines. It is possible to run ns-2 remotely via ssh.
  <br/>
 </p>
 <p>
  <a href="http://www.isi.edu/nsnam/ns/" target="_blank">
   ns-2
  </a>
  is a powerful simulator that provides substantial support for simulating TCP, routing and multicast protocols, among other things. It can simulate the conditions that occur in wired or wireless networks. It is widely used in the research community and also in industry.
 </p>
 <p>
  <span class="s2">
   The simulator is written in C++. However, it uses OTcl as its command and configuration interface. In our lab exercises, we will use scripts written in OTcl. You will not be required to write any C++ code for any of the lab exercises. You will also not be required to write OTcl scripts from scratch. All scripts will be provided and, at most, ask you to change a line or two in the scripts with proper instructions. You can safely assume ns-2 is a black box to complete the lab exercises. However, for those interested in learning more about ns-2, please refer to the following
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86997" target="_blank">
    overview slides
   </a>
   , which offer a good introduction.
  </span>
 </p>
 <p>
  We will also use a network animator tool:
  <a href="http://www.isi.edu/nsnam/nam/" target="_blank">
   <span class="s3">
    Nam
   </span>
  </a>
  . This allows us to visualise the topology and the transmission of packets during the experiments.
  <br/>
 </p>
 <p>
  <b>
   Illustrative Example: 2 nodes communicating directly over UDP
  </b>
 </p>
 <p>
  We will use this example to get acquainted with ns-2. The OTcl script for the first experiment is
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86998" target="_blank">
   simpleSim.tcl
  </a>
  .  It creates two nodes and simulates sending data packets from one node to the other over UDP. The full explanation of the script can be found
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86996" target="_blank">
   here.
  </a>
  <strong>
   We strongly recommend
  </strong>
  you read through it as it will be helpful for you for future exercises. It doesn't go over all details but rather gives you an overview of how to set up a topology, creates traffic and run an experiment.
 </p>
 <p>
  You can run the script by typing the following command:
 </p>
 <pre>$ ns simpleSim.tcl</pre>
 <p>
  This will start the nam tool, and you will see the
  <a href="http://www.isi.edu/nsnam/ns/tutorial/nsbasic.html#nam" target="_blank">
   nam window
  </a>
  . When you click on the 'play' button in the window, you will see that after 0.5 seconds of simulated time, node 0 starts sending data packets to node 1. The transmission stops at t = 1.5 seconds, and the simulation stops at time t = 2 seconds. You might want to slow nam down by using the 'Step' slider at the top right.
 </p>
 <p>
  Once the experiment has concluded, close nam. You will find an output trace file named 'out.tr' in your current directory. The format is as follows:
 </p>
 <pre>event time src dest PktType PktSize Flags Fid SrcSddr DestAddr SeqNum PktId</pre>
 <p>
  where:
 </p>
 <ul>
  <li>
   event:
   <ul>
    <li>
     <span class="s3">
      r:
     </span>
     receive at dest
    </li>
    <li>
     <span class="s3">
      +:
     </span>
     enqueue
    </li>
    <li>
     <span class="s3">
      -:
     </span>
     dequeue
    </li>
    <li>
     <span class="s3">
      d:
     </span>
     drop
    </li>
   </ul>
  </li>
 </ul>
 <ul>
  <li>
   ScrAddr and DestAddr
   <span class="s4">
    :
   </span>
   <ul>
    <li>
     <span class="s3">
      node.port
     </span>
     (e.g.,
     <span class="s3">
      0.1
     </span>
     means node
     <span class="s3">
      0
     </span>
     , port
     <span class="s3">
      1
     </span>
     )
    </li>
   </ul>
  </li>
 </ul>
 <p>
  Example trace:
 </p>
 <pre>r 0.519 0 1 cbr 500 ------- 0 0.0 1.0 1 1
+ 0.52  0 1 cbr 500 ------- 0 0.0 1.0 4 4
- 0.52  0 1 cbr 500 ------- 0 0.0 1.0 4 4
</pre>
 <p>
  You may wish to examine out.tr to understand better what happens in the experiment.
 </p>
 <p>
  We will use ns-2 in the next lab to run some experiments with TCP flows.
 </p>
