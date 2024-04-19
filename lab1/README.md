<h3>
  Objectives:
  <br/>
 </h3>
 <ul>
  <li>
   Get familiar with the basic networking tools: ping, traceroute, ifconfig, netstat, nslookup
  </li>
  <li>
   Gain insights into evaluating network performance and understanding network topology
  </li>
 </ul>
 <h3>
  Prerequisites:
 </h3>
 <ul>
  <li>
   Week 1 Lectures
  </li>
  <li>
   Relevant Parts of Chapter 1 of the textbook
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86895" target="_blank">
    Introduction to Tools of the Trade
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86980" target="_blank">
    runping.sh
   </a>
  </li>
  <li>
   <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86986">
    plot.sh
   </a>
  </li>
  <li>
   Basic understanding of Linux. A good resource is
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/">
   </a>
   <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/">
    here,
   </a>
   but several other resources are available online.
  </li>
 </ul>
 <h3>
  Marks: 10 marks
 </h3>
 <ul>
  <li>
   This lab comprises several exercises. Pl, note that not all the exercises for this lab are marked. However, you must submit a report containing answers for all lab exercises.
  </li>
  <li>
   Please attend only in your allocated lab slot.
  </li>
  <li>
   We expect the students to go through as many of the lab exercises as they can at home and come to the lab to clarify any doubts about the procedure/specifications.
  </li>
 </ul>
 <h3>
  Deadline:
 </h3>
 <p>
  <em>
   <strong>
    10:00 am Tuesday 13/06/2023
   </strong>
  </em>
  . You can submit as many times as you wish before the deadline. A later submission will override the earlier submission, so make sure you submit the correct file. Do not leave until the last moment to submit, as there may be technical or communications errors, and you will not have time to rectify it.
 </p>
 <p>
  <em>
   Note: For all the lab exercises, you are asked to put a screenshot of your outputs (e.g., graphs, traceroute, dig comments) in your report.
  </em>
  <br/>
 </p>
 <h3>
  Late Penalty:
 </h3>
 <p>
  The late penalty will be applied as follows:
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
  Prepare a PDF document
  <strong>
   Lab1.pdf
  </strong>
  with answers to all questions for all exercises. To include other supporting documents, create a tar archive of all the files called
  <strong>
   Lab1.tar.
  </strong>
  Submit the archive using the give or WebCMS3 interface. You can submit from a lab machine or ssh into the CSE login server. Instructions to ssh into CSE login servers are
  <a href="https://taggi.cse.unsw.edu.au/FAQ/Logging_In_With_SSH/">
   here
  </a>
  .
 </p>
 <ol>
  <li>
   Put all your files (e.g., Lab1.pdf, output.txt) in a directory lab1.
  </li>
  <li>
   Type “tar -cvf Lab1.tar lab1”
  </li>
  <li>
   When you are ready to submit, at the bash prompt type 3331
  </li>
  <li>
   Next, type: give cs3331 Lab1 Lab1.tar
  </li>
 </ol>
 <ul>
  <li>
   Please make sure that the tar archive is not corrupted. You can untar (use tar -xvf Lab1.tar) the created archive to check that all the files are intact.
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
 <h3>
  Original Work Only:
 </h3>
 <p>
  You are strongly encouraged to discuss the questions with other students in your lab. However, each student must submit his or her work. You may need to refer to the material indicated above (particularly the Tools of the Trade document) and conduct your research to answer the questions.
  <br/>
 </p>
 <h3>
  OS Compatibility:
 </h3>
 <p>
  Please note that the instructions provided herein assume that you are running the exercises on a Linux machine (similar to the CSE lab machines). These commands (and the scripts provided) may not work as prescribed on other OSes (Windows, Mac OS X, etc.). We strongly recommend that you run these experiments on CSE machines. If you are running from off-campus, you can use VNC to connect to
  <a href="https://taggi.cse.unsw.edu.au/Vlab/">
   VLAB.
  </a>
  We cannot help you diagnose any issues that may arise with OSes other than Linux.
 </p>
 <p>
  <b>
   Exercise 1: nslookup (Not Marked)
  </b>
 </p>
 <p>
  Use the nslookup command from the "Tools of the Trade" and answer the following questions:
 </p>
 <ol>
  <li>
   Which is the IP address of the website www.koala.com.au? In your opinion, what is the reason for having several IP addresses as an output? You can ignore any IPv6 addresses.
  </li>
  <li>
   Find out the name of the IP address 127.0.0.1. What is special about this IP address?
  </li>
 </ol>
 <p>
  <b>
   Exercise 2: Use ping to test host reachability (2 marks)
  </b>
 </p>
 <p>
  Are the following hosts reachable from your machine by using ping:
 </p>
 <ul>
  <li>
   <a href="http://www.google.com.au/">
    www.google.com.au
   </a>
  </li>
  <li>
   <a href="http://www.stanford.edu/">
    www.stanford.edu
   </a>
  </li>
  <li>
   <a href="http://www.wikipedia.org/">
    www.wikipedia.org
   </a>
  </li>
  <li>
   <a href="http://ec.ho/">
    ec.ho
   </a>
  </li>
  <li>
   <a href="http://pin.gs/">
    pin.gs
   </a>
  </li>
  <li>
   <a href="http://nasa.gov/">
    nasa.gov
   </a>
  </li>
  <li>
   <a href="http://yes.no/">
    yes.no
   </a>
  </li>
  <li>
   <a href="http://one.one.one.one/">
    one.one.one.one
   </a>
  </li>
  <li>
   <a href="http://theguardian.com/">
    theguardian.com
   </a>
  </li>
  <li>
   <a href="http://xn--i-7iq.ws/">
    xn--i-7iq.ws
   </a>
  </li>
 </ul>
 <p>
  If you observe that some hosts are unreachable, can you explain why? Check if the addresses unreachable by the ping command are reachable from the Web browser.
 </p>
 <p>
  <b>
   Exercise 3: Use traceroute to understand the network topology (4 marks)
  </b>
 </p>
 <p>
  <i>
   Note: Include all traceroute outputs in your report.
  </i>
 </p>
 <ol>
  <li>
   Run traceroute on your machine to
   <a href="http://www.tu-berlin.de/">
    www.tu-berlin.de
   </a>
   . How many routers are there between your workstation and
   <a href="http://www.tu-berlin.de/">
    www.tu-berlin.de
   </a>
   ? How many routers along the path are part of the UNSW network? Which router is the first router outside of Australia? Which router is the first router in Europe? HINT: compare the round trip times from your machine to the routers. You might also find some router names informative and/or looking at network maps (e.g. for AARNet).
  </li>
  <li>
   Run a traceroute from your machine to the following destinations: (i)
   <a href="http://canterbury.ac.nz/">
    canterbury.ac.nz
   </a>
   (ii)
   <a href="http://stanford.edu/">
    stanford.edu
   </a>
   , and (iii)
   <a href="http://reading.ac.uk/">
    reading.ac.uk
   </a>
   . At which router do the paths from your machine to these three destinations diverge (i.e. which is the last router they have in common)? Find out further details about this router. HINT: You can learn more about a router by running the Whois command: whois router-IP-address. Is the number of hops on each path proportional to the physical distance? HINT: You may be able to find out the geographical location of a server using the following tool -
   <a href="http://www.yougetsignal.com/tools/network-location/">
    http://www.yougetsignal.com/tools/network-location/
   </a>
   .
  </li>
  <li>
   Several servers are distributed worldwide to provide a web interface from which you can perform a traceroute to any other host on the Internet. Here are two examples: (i)
   <a href="http://www.speedtest.com.sg/tr.php">
    www.speedtest.com.sg/tr.php
   </a>
   and (ii)
   <a href="http://www.as13030.net/traceroute.php">
    www.as13030.net/traceroute.php
   </a>
   . Run a traceroute from both these servers towards your machine and in the reverse direction (i.e.from your machine to these servers - do not include the full URL while doing this, e.g. just "
   <a href="http://www.speedtest.com.sg">
    www.speedtest.com.sg
   </a>
   ". You may also try other traceroute servers from the list at
   <a href="http://www.traceroute.org/">
    www.traceroute.org
   </a>
   . What are the IP addresses of the two servers that you have chosen? Does the reverse path go through the same routers as the forward path? If you observe standard routers between the forward and the reverse path, do you also observe the same IP addresses? Why or why not?
  </li>
 </ol>
 <p>
  <b>
   IMPORTANT
  </b>
  : (1) When running this test on your machine connected to UniWide, the reverse traceroute fails because of the 10.x.x.x IP address assigned to your machine is a private IP address (i.e. it is behind a NAT) and thus not publicly routable. So make sure you conduct the above experiment through VLAB. (2) Feel free to terminate the traceroute if you start receiving output with multiple " * * * " responses or if you can confirm that the traceroute messages have reached the destination network.
 </p>
 <p>
  <b>
   Exercise 4: Use ping to gain insights into network performance (4 marks)
  </b>
 </p>
 <p>
  <i>
   Note: Include all graphs in your report.
  </i>
  <i>
   You need to run the scripts (runping.sh and plot.sh) when you are physically using a lab machine or connected to a CSE server/lab machine using VLAB / VNC client. You need to ensure gnuplot and ps2pdf are available on your system if you plan to do this exercise on your machine.
  </i>
 </p>
 <p>
  We now use the ping utility to investigate network delay and its implications on network performance. In particular, we will analyze the dependency of packet size and delay.
 </p>
 <p>
  There is a shell script
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86980">
   runping.sh
  </a>
  , provided that you can use it instead of running many pings with different packet sizes by hand. After downloading this script on your machine, make sure you can execute it. If not, you must execute the following command in the command line:
  <i>
   chmod u+x runping.sh
  </i>
  . To run the ping traces, you may use the runping.sh script as follows: ./runping.sh
  <a href="http://www.abc.net/">
   www.abc.net
  </a>
  (or whatever other destination you want to ping). It will automatically run ping for different packet sizes, with 50 ping packets per size (-c 50). Note since ping is sent once per second (-i 1), this script will take a few minutes to finish. Additional options are enabled to use IPv4 only (-4) and not lookup symbolic names for host addresses (-n). Basically, this script only executes the commands:
 </p>
 <p>
  $ ping -4 -n -c 50 -i 1 -s 22
  <a href="http://www.abc.net">
   www.abc.net
  </a>
  &gt;
  <a href="http://www.abc.net">
   www.abc.net
  </a>
  -p50
 </p>
 <p>
  ...
 </p>
 <p>
  $ ping -4 -n -c 50 -i 1 -s 1472
  <a href="http://www.abc.net">
   www.abc.net
  </a>
  &gt;
  <a href="http://www.abc.net">
   www.abc.net
  </a>
  -p1500
 </p>
 <p>
  and writes the output of the pings to the corresponding files.
 </p>
 <p>
  Use this script for the following destinations:
 </p>
 <ol>
  <li>
   <a href="http://flinders.edu.au/">
    flinders.edu.au
   </a>
   (Flinders University - Adelaide, Australia)
  </li>
  <li>
   <a href="http://upd.edu.ph/">
    upd.edu.ph
   </a>
   (University of the Philippines Diliman - Quezon City, Philippines)
  </li>
  <li>
   <a href="http://uio.no/">
    uio.no
   </a>
   (University of Oslo - Oslo, Norway)
  </li>
 </ol>
 <p>
  In other words, execute the following commands
 </p>
 <p>
  $ ./runping.sh flinders.edu.au
 </p>
 <p>
  $ ./runping.sh upd.edu.ph
 </p>
 <p>
  $ ./runping.sh uio.no
 </p>
 <p>
  <b>
   Note that all delay values reported are in milliseconds (ms) and reflect the round trip time (RTT) between your host and the destinations.
  </b>
 </p>
 <p>
  If you cannot execute runping.sh, then fix the permissions by running the following command in the command line:
 </p>
 <p>
  $ chmod u+x runping.sh
 </p>
 <p>
  When the runping.sh script is finished for all destinations, you can plot the results using another provided script,
  <a href="https://webcms3.cse.unsw.edu.au/COMP3331/23T2/resources/86986">
   plot.sh
  </a>
  , as follows:
 </p>
 <p>
  $ ./plot.sh flinders.edu.au-p*
 </p>
 <p>
  $ ./plot.sh upd.edu.ph-p*
 </p>
 <p>
  $ ./plot.sh uio.no-p*
 </p>
 <p>
  If you cannot execute plot.sh, then fix the permissions by running the following command in the command line:
 </p>
 <p>
  $ chmod u+x plot.sh
 </p>
 <p>
  The script plot.sh will produce the following files: destination_delay.pdf, destination_scatter.pdf, and destination_avg.txt for each destination (e.g., for
  <a href="http://flinders.edu.au/">
   flinders.edu.au
  </a>
  we have
  <i>
   flinders.edu.au_delay.pdf
  </i>
  and
  <em>
   flinders.edu.au_scatter.pdf
  </em>
  and
  <em>
   flinders.edu.au_avg.txt
  </em>
  ).
 </p>
 <p>
  The graph
  <i>
   destination_delay.pdf
  </i>
  shows how delay varies over time (different colours correspond to different packet sizes), and
  <i>
   destination_scatter.pdf
  </i>
  shows delay vs. packet size as a scatter plot.
  <i>
   destination_avg.txt
  </i>
  contains the average (2nd column) and minimum (3rd column) delay values corresponding to each packet size (1st column).
 </p>
 <ol>
  <li>
   For each location, ﬁnd the (approximate) physical distance from UNSW. You can use a site like
   <a href="https://www.distancecalculator.net/">
    Distance Calculator
   </a>
   ,
   <a href="https://www.google.com/maps">
    Google Maps
   </a>
   , or whatever you prefer to take this measurement. Then compute the shortest possible time T for a packet to reach that location from UNSW. You should assume that the packet moves (i.e. propagates) at the speed of light, 3 x 10^8 m/s. Note that the shortest possible time will be the distance divided by the propagation speed. Plot a graph where the x-axis represents the distance to each city (i.e. Adelaide, Quezon City and Oslo). The y-axis represents the ratio between the minimum delay (i.e. RTT) as measured by the ping program (select the values for 50-byte packets) and the shortest possible time T to reach that city from UNSW. (Note that the y-values are no smaller than 2 since it takes at least 2*T time for any packet to reach the destination from UNSW and return). Can you think of at least two reasons why the y-axis values that you plot are greater than 2?
  </li>
  <li>
   Is the delay to the destinations constant, or does it vary over time? Explain why.
  </li>
  <li>
   The measured delay (i.e., the delay you can see in the graphs) is composed of propagation delay, transmission delay, processing delay and queuing delay. Which of these delays depend on the packet size and which do not?
  </li>
 </ol>