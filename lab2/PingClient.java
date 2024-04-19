/*
 *
 *  PingClient
 *  * Compile: java PingClient.java
 *  * Run: java PingClient
 */
import java.io.*;
import java.net.*;

public class PingClient {

	public static void main(String[] args) throws Exception {

        // Get command line argument.
        if (args.length != 2) {
            System.out.println("Required arguments: host port");
            return;
        }
        InetAddress host = InetAddress.getByName(args[0]);
        int port = Integer.parseInt(args[1]);
		// create socket which connects to server
		DatagramSocket clientSocket = new DatagramSocket();

/*This line creates the client’s socket, called clientSocket. DatagramSocket indicates that we are using UDP*/

        clientSocket.setSoTimeout(600);
        long start, gap, avg;
        long min = 601;
        long max = 0;
        long sum = 0;
        int count = 0;
        String rtt, sentence;
        byte[] sendData;
        for (int i = 3331; i <= 3345; i++) {
            start = System.currentTimeMillis();
            sentence = "PING " + i + " " + start + " \r\n"; 
            sendData = sentence.getBytes();
            // write to server, need to create DatagramPAcket with server address and port No
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, host, port);
            //actual send call
            clientSocket.send(sendPacket);
            
            //prepare buffer to receive reply
            byte[] receiveData = new byte[1024];
            // receive from server
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

            try {
                clientSocket.receive(receivePacket);
                gap = System.currentTimeMillis() - start;
                rtt = "rtt = " + String.valueOf(gap) + " ms";
                min = Math.min(min, gap);
                max = Math.max(max, gap);
                sum += gap;
                count++;
            } catch (Exception e) {
                rtt = "time out";
            }
            
            System.out.println("ping to " + sendPacket.getAddress().getHostAddress() + ", seq = " + i + ", " + rtt);
        }
        //close the scoket
        clientSocket.close();
        System.out.println("The minimum RTTs of all packets received successfully is " + min);
        System.out.println("The maximum RTTs of all packets received successfully is " + max);
        System.out.println("The average RTTs of all packets received successfully is " + (sum / count));

	} // end of main

} // end of class Ping Client
