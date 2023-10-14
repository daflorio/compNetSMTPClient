from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #  testServer = 'smtp.nyu.edu'
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start

    # create the socket named 'clientSocket'
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # establishing the TCP connection
    clientSocket.connect((mailserver, port))

    # Fill in end 

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
#    if recv[:3] != '220':
#        print('220 reply not received from server.')
#    else:
#        print('GOOD')

    # Send HELO command and print server response.
    # helo command : initiates the smtp convo
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # LOCAL TESTING:
    #print(recv1) 
 #   if recv1[:3] != '250':
 #       print('250 reply not received from server.')
 #   else:
 #       print('GOOD2')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # mail from command : specifies the sender & initiates the mail transfer
    mailfromCommand = 'MAIL FROM: <daf491@nyu.edu> \r\n'
    clientSocket.send(mailfromCommand.encode())     # send(and encode) the command to the server
    recv2 = clientSocket.recv(1024).decode()    # receives/reads the data from the server and decodes it
    # LOCAL TESTING:
 #   if recv2[:3] != '250':
 #       print('250 reply not received from server.-MAIL')
 #   else:
 #       print('GOOD2')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    # rcpt to command : specifies the recipient of the email
    rcpttoCommand = 'RCPT TO: <daf491@nyu.edu> \r\n'
    clientSocket.send(rcpttoCommand.encode())   # send/encode rcptto command to the server
    recv3 = clientSocket.recv(1024).decode()    # receives/reads the data from the server and decodes it
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    # data command : tells server that the body of the email is being sent
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())      # send/encode data command to the server
    recv4 = clientSocket.recv(1024) # receives/reads the data from the server and decodes it
    # Fill in end

    # Send message data.
    # Fill in start
    # send/encode the 'msg' variable to the server
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # send/encode the 'endmsg' variable to the server (the '.')
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024) 
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # quit command : ends the smtp session
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())    # send/encode quit command to the server
    # Fill in end

    # close the socket
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')