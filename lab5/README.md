<h3>
  Objectives:
 </h3>
 <ul>
  <li>
   gain insights into the operation of TCP.
  </li>
  <li>
   study how competing flows share network resources.
  </li>
  <li>
   get familiar with the ns-2 simulator
  </li>
 </ul>
 <h3>
  Prerequisites and Links:
 </h3>
 <ul>
  <li>
   Week 6 Lectures
  </li>
  <li>
   Relevant Parts of Chapter 3 of the textbook
  </li>
  <li>
   Introduction to ns-2 as part of Lab Exercise 4
  </li>
  <li>
   Basic understanding of Linux. A good resource is
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/">
    here
   </a>
   , but there are several other resources online:
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86995" target="_blank">
    tpWindow.tcl
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87004" target="_blank">
    Window.plot
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87007" target="_blank">
    WindowTPut.plot
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87000" target="_blank">
    tp_fainess.tcl
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86981" target="_blank">
    fairness_pkt.plot
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86990" target="_blank">
    tp_TCPUDP.tcl
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86987" target="_blank">
    TCPUDP_pps.plot
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
   This lab comprises several exercises. Pl, note that not all the exercises for this lab are marked. However, you must submit a report containing answers for all the lab exercises.
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
  <em>
   <strong>
    Tuesday 25/07/2023
   </strong>
  </em>
  . You can submit as many times as you wish before the deadline. A later submission will override the earlier submission, so make sure you submit the correct file. Do not leave until the last moment to submit, as there may be technical or communications errors, and you will not have time to rectify it.
 </p>
 <h3>
  Late Submission Penalty:
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
  Note that the above penalty is applied to your final mark. For example, if you submit your lab work 2 days late and your score on the lab is 8, then your final mark will be 8 - 0.8 (10% penalty) = 7.2.
 </p>
 <h3>
  Submission Instructions:
  <br/>
 </h3>
 <p>
  Submit a PDF document
  <strong>
   Lab5.pdf
  </strong>
  with answers to all questions for Exercises 1, 2 &amp; 3. To include all supporting documents, create a tar archive of all files called
  <b>
   Lab5.tar.
  </b>
  Submit the archive using the give or WebCMS3 interface. You can submit from a lab machine or ssh into the CSE login server.
 </p>
 <h3>
  Original Work Only:
 </h3>
 <p>
  You are strongly encouraged to discuss the questions with other students in your lab. However, each student must submit his or her own work. You may need to refer to the material indicated above (particularly the Tools of the Trade document) and conduct your own research to answer the questions.
 </p>
 <h3>
  Important Note:
 </h3>
 <p>
  The provided scripts (for ns-2 and gnuplot) have been tested on CSE Linux machines. They may not work on your personal machine even if you have installed ns-2 and gnuplot. As such, we suggest that you work on a CSE lav machine or in the VLAB environment to complete these lab exercises.
 </p>
 <h3>
  Revision of TCP Congestion Control (NO SUBMISSION REQUIRED)
 </h3>
 <p>
  The following question is included so that you can revise the TCP congestion control algorithm. It is recommended that students have a short discussion with their tutors at the start of the lab to go over this question and TCP congestion control in general. Students are strongly encouraged to participate and ask questions. You are not required to submit the answer to this question in your lab report. I suggest you use the lab's first 15-20 minutes to go over this.
 </p>
 <p>
  The graph in the figure below shows how the congestion window of a TCP Reno connection changes over time. It is drawn roughly to scale. Certain parts of the graph that are of extra interest have been marked with numbers. With the help of the graph, answer the following questions:
 </p>
 <p>
  <img src="/static/uploads/pic/z3116703/96166c1c32eddf0bf560416e0e14b308125320a857e1b7bd33533df74257b78f/tcp_cc.jpg" style="width: 488px; height: 303.961px;"/>
 </p>
 <p>
  Question 1. Name the loss events that occur at 1 and 2. Explain why the congestion window is changed differently in those two cases.
 </p>
 <p>
  Question 2. What phase of the TCP congestion control algorithm coincides with the circled segment marked by 3?
 </p>
 <p>
  Question 3. What phase of the TCP congestion control algorithm coincides with the circled segment marked by 4?
 </p>
 <p>
  Question 4: Why is the congestion window increased more rapidly at 3 than at  4?
 </p>
 <p>
  Question 5: Can you precisely explain what happens to the window after 2?
 </p>
 <h3>
  Exercise 1: Understanding TCP Congestion Control using ns-2
 </h3>
 <p>
  We have studied the TCP congestion control algorithm in detail in the lecture (and Section 3.6 of the text). You may wish to review this before continuing with this exercise. Recall that each TCP sender limits the rate at which it sends traffic as a function of perceived network congestion.  We studied three variants of the congestion control algorithm: TCP Tahoe, TCP Reno and TCP new Reno.
 </p>
 <p>
  We will first consider TCP Tahoe (this is the default version of TCP in ns-2). Recall that TCP Tahoe uses two mechanisms:
 </p>
 <ul>
  <li>
   A varying congestion window determines how many packets can be sent before the acknowledgement for the first packet arrives.
  </li>
  <li>
   A slow-start mechanism increases the congestion window exponentially in the initial phase before it stabilises when it reaches a threshold value. A TCP sender re-enters the slow-start state whenever it detects congestion in the network.
  </li>
 </ul>
 <p>
  The provided script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86995" target="_blank">
   tpWindow.tcl
  </a>
  implements a simple network that is illustrated in the figure below.
 </p>
 <p>
  <img src="/static/uploads/pic/z3116703/de47848eecd49bade6b9cba410be91cb80b1a82b79c53c8508fd71d93ed148fc/tcp.jpg"/>
 </p>
 <pre>proc finish {} {
     global ns file1 file2
     $ns flush-trace
     close $file1
     close $file2
     #exec nam out.nam &amp;
     exit 0
}
</pre>
 <p>
  We strongly recommend reading through the script file to understand the simulation setting. The simulation is run for 60 seconds. The MSS for TCP segments is 500 bytes. Node 0 is configured as an FTP sender, transmitting packets every 0.01 seconds. Node 1 is a receiver (TCP sink). It does not transmit data and only acknowledges the TCP segments received from Node 0.
 </p>
 <p>
  The script will run the simulation and generate two trace files: (i)
  <em>
   Window.tr,
  </em>
  which keeps track of the size of the congestion window and (ii)
  <em>
   WindowMon.tr
  </em>
  , which shows several parameters of the TCP flow.
 </p>
 <p>
  The
  <em>
   Window.tr
  </em>
  file has two columns:
 </p>
 <pre>time congestion_window_size</pre>
 <p>
  A new entry is created in this file every 0.02 seconds of simulation time and records the congestion window size at that time.
 </p>
 <p>
  The
  <em>
   WindowMon.tr
  </em>
  file has six columns:
 </p>
 <pre>time number_of_packets_dropped drop_rate throughput queue_size avg_tput</pre>
 <p>
  A new entry is created in this file every second of simulation time. The
  <em>
   number_of_packets_dropped
  </em>
  ,
  <em>
   drop_rate
  </em>
  and
  <em>
   throughput
  </em>
  represent the corresponding measured values over each second. The
  <em>
   queue_size
  </em>
  indicates the queue size at each second, whereas
  <em>
   avg_tput
  </em>
  is the average throughput measured since the start of the simulation.
 </p>
 <p>
  Question 1: Run the script with the max initial window size set to 150 packets and the delay set to 100ms (be sure to type "ms" after 100). In other words, type the following:
  <br/>
 </p>
 <pre>$ns tpWindow.tcl 150 100ms
</pre>
 <p>
  To plot the size of the TCP window and the number of queued packets, we use the provided gnuplot script
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87004" target="_blank">
   Window.plot
  </a>
  as follows:
  <br/>
 </p>
 <pre>$gnuplot Window.plot</pre>
 <p>
  (a) In this case, what is the maximum size of the congestion window that the TCP flow reaches?
 </p>
 <p>
  (b) What does the TCP flow do when the congestion window reaches this value? Why?
 </p>
 <p>
  (c) What happens next?
 </p>
 <p>
  Include the graph in your submission report.
 </p>
 <p>
  Question 2: From the simulation script we used, we know that the packet's payload is 500 Bytes. Keep in mind that the size of the IP and TCP headers is 20 Bytes each. Neglect any other headers. What is the average throughput of TCP in this case? (both in number of packets per second and bps)
 </p>
 <p>
  You can plot the throughput using the provided gnuplot script
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87007" target="_blank">
   WindowTPut.plot
  </a>
  as follows:
 </p>
 <pre>$gnuplot WindowTPut.plot</pre>
 <p>
  This will create a graph that plots the instantaneous and average throughput in packets/sec. Include the graph in your submission report.
 </p>
 <p style="text-align: justify;">
  Question 3: Rerun the above script, each time with different values for the max congestion window size but the same RTT (i.e. 100ms). How does TCP respond to the variation of this parameter? Find the value of the maximum congestion window at which TCP stops oscillating (i.e., does not move up and down again) to reach a stable behaviour. What is the average throughput (in packets and bps) at this point? How does the actual average throughput compare to the link capacity (1Mbps)?
 </p>
 <p style="text-align: justify;">
  <strong>
   TCP Tahoe vs TCP Reno
  </strong>
 </p>
 <p>
  Recall that, so far; we have observed the behaviour of TCP Tahoe. Let us now observe the difference with TCP Reno. As you may recall, in TCP Reno, the sender will cut the window size to 1/2 its current size if it receives three duplicate ACKs. The default version of TCP in ns-2 is TCP Tahoe. To change to TCP  Reno, modify the Window.tcl OTcl script. Look for the following line:
 </p>
 <pre>set tcp0 [new Agent/TCP]</pre>
 <p>
  and replace it with:
 </p>
 <pre>set tcp0 [new Agent/TCP/Reno]</pre>
 <p>
  Question 4: Repeat the steps outlined in Questions 1 and 2 (NOT Question 3) but for TCP Reno. Compare the graphs for the two implementations and explain the differences. (Hint: compare the number of times the congestion window returns to zero in each case). How does the average throughput differ in both implementations?
 </p>
 <p>
  <strong>
   Note:
  </strong>
  Remember to include all graphs in your report.
 </p>
 <h3>
  Exercise 2: Flow Fairness with TCP
 </h3>
 <p>
  In this exercise, we will study how competing TCP flows with similar characteristics behave when they share a single bottleneck link.
 </p>
 <p>
  The provided script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/87000" target="_blank">
   tp_fairness.tcl
  </a>
  generates 5 source-destination pairs which all share a common network link. Each source uses a single TCP flow that transfers FTP traffic to the respective destination. The flows are created one after the other at 5-second intervals (i.e., flow
  <i>
   i+1
  </i>
  starts 5 seconds after flow
  <i>
   i
  </i>
  for
  <i>
   i
  </i>
  in
  <i>
   [1,4]
  </i>
  ). You can invoke the script as follows:
 </p>
 <pre>$ns tp_fairness.tcl   </pre>
 <p>
  The figure below shows the resulting topology; there are 5 sources (2,4,6,8,10), 5 destinations (3,5,7,9,11), and each source sends a large file to a single destination. Node 2 sends a file to Node 3; Node 4 sends a file to Node 5, and so on.
  <br/>
 </p>
 <p>
  <img src="/static/uploads/pic/z3116703/830028bcd800f4d398d6570cf785a8c81968e6a823c57f8a9d1e5443bb866277/tptransnet_ex1_1.jpg"/>
  i.tr for each
  <i>
   i
  </i>
  in
  <i>
   [1,5]
  </i>
  . Each of these files contains three columns:
  <br/>
 </p>
 <p>
  time | number of packets delivered so far | throughput (packets per second)
 </p>
 <p>
  You can plot the throughput as a function of time using the provided gnuplot script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86981" target="_blank">
   fairness_pkt.plot
  </a>
  , as follows:
 </p>
 <pre>$gnuplot fairness_pkt.plot</pre>
 <p>
  <strong>
   NOTE:
  </strong>
  The NAM visualiser is disabled in the script. If you want to display the NAM window (graphical interface), modify tp_fairness.tcl and uncomment the fifth line of the 'finish' procedure:
 </p>
 <pre>proc finish {} {
    global ns file1 file2
    $ns flush-trace
    close $file1
    close $file2
    #exec nam out.nam &amp; 
    exit 0
}
</pre>
 <p>
  Run the above script and plot the throughput as a function of the time graph and answer the following questions:
 </p>
 <p>
  Question 1: Does each flow get an equal share of the capacity of the common link (i.e., is TCP fair)? Explain which observations lead you to this conclusion.
 </p>
 <p>
  Question 2. What happens to the throughput of the pre-existing TCP flows when a new flow is created? Explain the mechanisms of TCP which contribute to this behaviour. Argue whether you consider this behaviour to be fair or unfair.
 </p>
 <p>
  <strong>
   Note:
  </strong>
  Remember to include all graphs in your report.
  <br/>
 </p>
 <h3>
  Exercise 3: TCP competing with UDP
 </h3>
 <p>
  In this exercise, we will observe how a TCP flow reacts when it has to share a bottleneck link that is also used by a UDP flow.
 </p>
 <p>
  The provided script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86990" target="_blank">
   tp_TCPUDP.tcl
  </a>
  , takes a link capacity value as a command line argument. It creates a link with the given capacity, and two flows traverse that link, one UDP flow and one TCP flow. A traffic generator creates new data for each flow at a rate of 4Mbps. You can execute the simulation as follows,
  <br/>
 </p>
 <pre>$ns tp_TCPUDP &lt;link_capacity&gt;</pre>
 <p>
  After the simulation completes, you can plot the throughput using the provided gnuplot script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86987" target="_blank">
   TCPUDP_pps.plot
  </a>
  , as follows,
 </p>
 <pre>$gnuplot TCPUDP_pps.plot</pre>
 <p>
  Question 1: How do you expect the TCP flow and the UDP flow to behave if the link's capacity is 5 Mbps?
 </p>
 <p>
  Now, you can use the simulation to test your hypothesis. Run the above script as follows,
 </p>
 <pre>$ns tp_TCPUDP.tcl 5Mb
</pre>
 <p>
  The script will open the NAM window. Play the simulation. You can speed up the simulation by increasing the step size in the right corner. You will observe packets with two different colours depicting the UDP and TCP flow. Can you guess which colour represents the UDP flow and the TCP flow, respectively?
 </p>
 <p>
  You may disable the NAM visualiser by commenting the "exec 3331 nam out.nam &amp;' line in the 'finish' procedure.
 </p>
 <p>
  Plot the throughput of the two flows using the above script (TCPUDP_pps.plot) and answer the following questions:
 </p>
 <p>
  Question 2: Why does one flow achieve higher throughput than the other? Try to explain what mechanisms force the two flows to stabilise to the observed throughput.
 </p>
 <p>
  Question 3: List the advantages and the disadvantages of using UDP instead of TCP for a file transfer, when our connection has to compete with other flows for the same link. What would happen if everybody started using UDP instead of TCP for that same reason?
 </p>
 <p>
  <strong>
   Note:
  </strong>
  Remember to include all graphs in your report.
 </p>