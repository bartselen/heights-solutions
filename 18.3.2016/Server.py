# Question 2 - Calculator server - Solution
#
# Written by Bar Tselenchuk

import socket


# Main method
def main():
    try:
        HOST, PORT = '', 8001

        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)
        print 'Serving on port %s ...' % PORT
#       Loop for accepting connections.
        while True:
            client_connection, client_address = listen_socket.accept()
            print "<INFO> Client at " + str(client_address) + " has connected."
#           Handle connection
            while True:
                try:
                    request = client_connection.recv(1024)
                    if not request:
                        raise socket.error
                    print "<RECV from:" + str(client_address) + "> " + request
                    response = ""
                    request_valid = True
                    split_req = request.split(' ')
                    if len(split_req) == 3:
                        first_number = split_req[0]
                        math_operand = split_req[1]
                        second_number = split_req[2]
                        if ("." not in first_number and
                                "." not in second_number):
                            if (first_number.isdigit() and
                                    second_number.isdigit()):
                                first_number = int(first_number)
                                second_number = int(second_number)
                                if first_number < 65536 and first_number > 0:
                                    if (second_number < 65536 and
                                            second_number > 0):
                                        if math_operand == "+":
                                            response = str(
                                                            first_number +
                                                            second_number)
                                        elif math_operand == "-":
                                            response = str(
                                                            first_number - second_number)
                                        elif math_operand == "*":
                                            response = str(
                                                           first_number * second_number)
                                        elif math_operand == "/":
                                            response = str(first_number / second_number)
                                        else:
                                            request_valid = False
                                    else:
                                        request_valid = False
                                else:
                                    request_valid = False
                            else:
                                request_valid = False
                        else:
                            request_valid = False
                    else:
                        request_valid = False
                    if not request_valid:
                        response = "Invalid request."
                    print "<RSPD> " + response
                    client_connection.sendall(response)
                except Exception as e:
                    if type(e) is socket.error:
                        print "<INFO> Client at " + \
                            str(client_address) + " has disconnected."
                    else:
                        print "<EXCP> An exception of type " + str(type(e)) + \
                              "has occurred.\nMessage: " + str(e) + \
                              "| Args: " + str(e.args) + ".\n"
                    break
            client_connection.close()
        try:
            listen_socket.close()
        except Exception:
            print "Could not close listener socket."
    except Exception as e:
        print "An exception of type " + str(type(e))
        print " has occurred, before the script exists,\n"
        print "here are some details:\n=+=+=+=+=+=+=+=+=+=+=+=+\n"
        print str(e) + "\n=+=+=+=+=+=+=+=+=+=+=+=+"


if __name__ == "__main__":
    main()
