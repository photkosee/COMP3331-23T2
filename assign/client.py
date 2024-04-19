import socket
import sys
import random
import struct
import io

# template from the demo code

class Header:
    def __init__(self, id, flags):
        self.id = id
        # from the demo code
        self.response_code = flags & 0b00001111
        self.is_authoritative = bool(flags & 0b00010000)
        self.is_truncated = bool(flags & 0b00100000)
        self.is_recursion_desired = bool(flags & 0b10000000)
        self.is_recursion_available = bool(flags & 0b01000000)

    def __repr__(self):
        return f'<Id:{self.id} Response Code:{self.response_code} Authoritative:{self.is_authoritative} Truncated:{self.is_truncated} Recursion Desired:{self.is_recursion_desired} Available:{self.is_recursion_available}>'

class Record:
    def __init__(self, name, type, ans):
        self.name = name
        if type == 1:
            self.type = 'A'
        elif type == 2:
            self.type = 'NS'
        elif type == 5:
            self.type = 'CNAME'
        # not supporting other types yet
        else:
            self.type = type
        self.ans = ans

    def __repr__(self):
        return f'<Name:{self.name} Type:{self.type} Answer:{self.ans}>'

def create_query(id, domain):
    # randomly generated id
    # header (1 question + no recursion desired)
    query = struct.pack('!HHHHHH', id, 0, 1, 0, 0, 0)
    # domain name to bytes
    for word in domain.encode('ascii').split(b'.'):
        query += bytes([len(word)]) + word
    # header (1 question + no recursion desired) + question (always type A (1) and class IN (1))
    return query + b'\x00' + struct.pack('!HH', 1, 1)

def get_domain(stream):
    # inspired from the demo code
    name = []
    while True:
        label_length = int.from_bytes(stream.read(1), byteorder='big')
        if label_length == 0:
            break
        # Check if it's compressed (first 2 bits are 1s) (ty google)
        if label_length & 0b11000000:
            # bottom 6 bits + 1 byte
            offset = int.from_bytes(bytes([label_length & 0b00111111]) + stream.read(1), byteorder='big')
            # keep track of the current position, seek to the offset then decode the name
            curr = stream.tell()
            stream.seek(offset)
            name.append(get_domain(stream))
            stream.seek(curr)
            break
        # normal situation
        else:
            name.append(stream.read(label_length))
    # forming
    return b'.'.join(name)

def get_record(stream):
    # get name, type, and length for ans
    name = get_domain(stream).decode()
    type = int.from_bytes(stream.read(2), byteorder='big')
    stream.read(6)
    label_length = int.from_bytes(stream.read(2), byteorder='big')
    # get ip address for A record
    if type == 1:
        ans = '.'.join([str(c) for c in stream.read(label_length)])
    # get domain name for NS and CNAME record
    elif type == 2 or type == 5:
        ans = get_domain(stream).decode('utf-8')
    # track offset for other types of record, not supporting other types yet
    else:
        ans = stream.read(label_length)
    
    return Record(name, type, ans)

def decode(dns_response):
    # inspired from the demo code
    # keep track of the response's offset
    stream = io.BytesIO(dns_response)
    # extract header
    header_id = int.from_bytes(stream.read(2), byteorder='big')
    header_flags = int.from_bytes(stream.read(2), byteorder='big')
    header_questions = int.from_bytes(stream.read(2), byteorder='big')
    header_answer_rrs = int.from_bytes(stream.read(2), byteorder='big')
    header_authority_rrs = int.from_bytes(stream.read(2), byteorder='big')
    header_additional_rrs = int.from_bytes(stream.read(2), byteorder='big')
    header = Header(header_id, header_flags)
    questions = []
    answers = []
    authorities = []
    additions = []

    # decode the question section
    for _ in range(header_questions):
        name = get_domain(stream)
        type = int.from_bytes(stream.read(2), byteorder='big')
        ans = int.from_bytes(stream.read(2), byteorder='big')
        questions.append(Record(name.decode('utf-8'), type, ans))

    if (header_answer_rrs != 0) :
        # decode the answer section
        for _ in range(header_answer_rrs):
            answers.append(get_record(stream))

    if (header_authority_rrs != 0) :
        # decode the authority section
        for _ in range(header_authority_rrs):
            authorities.append(get_record(stream))

    if (header_additional_rrs != 0) :
        # decode the additional section
        for _ in range(header_additional_rrs):
            additions.append(get_record(stream))

    return header, questions, answers, authorities, additions

def start_client(host, port, domain, timeout):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)
    client_socket.connect((host, port))

    # create a query with given domain name and send to the resolver
    id = random.randint(0, 65535)
    dns_query = create_query(id, domain)
    question = Record(domain, 1, 1)
    client_socket.send(dns_query)
    print('----------------------------------------------')
    # receiving a response
    response = client_socket.recv(1024)
    # name error
    if len(response) == 0:
        print("Error: server can't find ", domain)
    else:
        header, _, answers, authorities, additions = decode(response)
        header.id = id
        print('Header: ', header)
        print('Questions: ', question)
        print('Answers: ', answers)
        print('Authorities: ', authorities)
        print('Additions: ', additions)

    print('----------------------------------------------')
    client_socket.close()

if __name__ == '__main__':
    # check for invalid arguments
    if len(sys.argv) != 5:
        print('Error: invalid arguments')
        print('Usage: client resolver_ip resolver_port name timeoout')
        exit(1)

    host = sys.argv[1]
    server_port = int (sys.argv[2])
    domain = sys.argv[3]
    timeout = int (sys.argv[4])
    if server_port < 53 or server_port > 65535 or timeout <= 0:
        print('Error: invalid arguments')
        print('Usage: client resolver_ip resolver_port name timeoout')
        exit(1)

    # run client
    try:
        start_client(host, server_port, domain, timeout)
    except socket.timeout:
        print(f"Error: time out")
    except Exception as E:
        print(f"Error: resolver being shut down")