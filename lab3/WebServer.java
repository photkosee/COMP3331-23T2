import java.io.*;
import java.net.*;
import java.util.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

// from provided TCPServer
public class WebServer {

	public static void main(String[] args)throws Exception {
    if (args.length != 1) {
			System.out.println("Required argument: port");
			return;
		}
		int port = Integer.parseInt(args[0]);
		String currentDirectory = System.getProperty("user.dir");
		File directoryPath = new File(currentDirectory);
		File[] files = directoryPath.listFiles();
		
		/*create server socket that is assigned the port
        We will listen on this port for connection request from clients */
		ServerSocket welcomeSocket = new ServerSocket(port);
    System.out.println("Server is ready :");

		while (true){

		    // accept connection from connection queue
		    Socket connectionSocket = welcomeSocket.accept();
            /*When a client knocks on this door, the program invokes the accept( ) method for welcomeSocket, which creates a new socket in the server, called connectionSocket, dedicated to this particular client. The client and server then complete the handshaking, creating a TCP connection between the client’s clientSocket and the server’s connectionSocket. With the TCP connection established, the client and server can now send bytes to each other over the connection. With TCP, all bytes sent from one side not are not only guaranteed to arrive at the other side but also guaranteed to arrive in order*/
            

		    // create read stream to get input
		    BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
		    String clientSentence;
		    clientSentence = inFromClient.readLine();
            //data from client is stored in clientSentence

		    // process input, get requested file
		    String file = clientSentence.split(" ")[1].split("/")[1];
				DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
				File requestedFile = null;
				for (File f : files) {
					if (f.getName().equals(file)) {
						requestedFile = f;
						break;
					}
				}
				if (requestedFile != null) {
					outToClient.writeBytes("HTTP/1.1 200 OK\r\n");
					if (file.endsWith(".html")) {
						outToClient.writeBytes("Content-type: text/html\r\n\r\n");
						Scanner scan = new Scanner(requestedFile);
						while (scan.hasNextLine()) {
							outToClient.writeBytes(scan.nextLine());
						}
					} else {
						// get file extension
						String extension = requestedFile.getName().substring(requestedFile.getName().lastIndexOf(".") + 1);
						outToClient.writeBytes("Content-type: image/" + extension + "\r\n\r\n");
						// convert the file to bytes
						BufferedImage bufIm = ImageIO.read(requestedFile);
						ByteArrayOutputStream bo = new ByteArrayOutputStream();
						ImageIO.write(bufIm, extension, bo);
						outToClient.write(bo.toByteArray());
					}
					System.out.println("200 OK");
				} else {
					outToClient.writeBytes("HTTP/1.1 404 Not Found\r\n");
					outToClient.writeBytes("Content-type: text/html\r\n\r\n");
					System.out.println("404 Not Found");
				}

            
        connectionSocket.close();
            /*In this program, after sending the capitalized sentence to the client, we close the connection socket. But since welcomeSocket remains open, another client can now knock on the door and send the server a sentence to modify.
             */
		} // end of while (true)

	} // end of main()

} // end of class TCPServer