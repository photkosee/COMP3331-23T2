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

def load_root():
    # get ip address of each root in A record only
    root_ip = []
    try:
        # look into named.root file in the directory
        with open('named.root', 'r') as file:
            for line in file:
                line = line.strip()
                # ignore a line starting with ;
                if line and not line.startswith(';'):
                    parts = line.split()
                    if parts[2] == 'A':
                        # get ip address of root domain
                        root_ip.append(parts[3])
    except FileNotFoundError:
        print('Error: no named.root files')
        exit(1)
    
    # return a list of roots' ip
    print('Successfully downloaded all roots ip')
    return root_ip

def create_query(domain):
    # randomly generated id
    # header (1 question + no recursion desired)
    query = struct.pack('!HHHHHH', random.randint(0, 65535), 0, 1, 0, 0, 0)
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
            pointer = int.from_bytes(bytes([label_length & 0b00111111]) + stream.read(1), byteorder='big')
            # Remember the current position, seek to the pointer position, and decode the name
            curr = stream.tell()
            stream.seek(pointer)
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
        name = get_domain(stream).decode('utf-8')
        type = int.from_bytes(stream.read(2), byteorder='big')
        ans = int.from_bytes(stream.read(2), byteorder='big')
        questions.append(Record(name, type, ans))

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

def get_answer(ip, domain, root):
    # send a new A type query of given domain to given address
    query = create_query(domain)
    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tmp_socket.sendto(query, (ip, 53))
    response, _ = tmp_socket.recvfrom(512)
    tmp_socket.close()
    # get all records in each section from the response
    header, questions, answers, authorities, additions = decode(response)
    # print('Header: ', header)
    # print('Questions: ', questions)
    # print('Answers: ', answers)
    # print('Authorities: ', authorities)
    # print('Additions: ', additions)
    # print('----------------------------------------------')

    # error response
    if (header.response_code != 0):
        return response, '', 're'

    ip_a = ''
    name_ns = ''
    ip_ns = ''
    name_cn = ''

    # get the ip address of an A record in the answer section if there's any
    for record in answers:
        if record.type == 'A':
            ip_a = record.ans
    # get the name of cn record from the answer section if there's any
    for record in answers:
        if record.type == 'CNAME':
            name_cn = record.ans
    # get ns record from the authority section if there's any
    for record in authorities:
        if record.type == 'NS':
            name_ns = record.ans
    # get the ip address from the additional section if there's any
    for record in additions:
        if record.type == 'A':
            ip_ns = record.ans

    # return the ip address of an A type answer if exists
    if len(ip_a) != 0:
        return response, ip_a, ''
    # send query to one of the auth if ip provided
    elif len(ip_ns) != 0:
        return get_answer(ip_ns, domain, root)
    # look for the ip address of ns
    elif len(name_ns) != 0:
        _, ip_ns, re = get_answer(ip, name_ns, root)
        if len(re) != 0:
            return response, '', 're'
        return get_answer(ip_ns, domain, root)
    # start looking from the root for cn name
    elif len(name_cn) != 0:
        return get_answer(root, name_cn, root)
    # no answers
    else:
        return response, '', 're'

def start_server(port):

    root_ip = load_root()
    host = '127.0.0.1'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print('Server is listening on port', port)

    # continue receiving queries from clients
    while True:
        conn, address = server_socket.accept()
        print('Connection from', address)
        query = conn.recv(1024)
        if len(query) == 0:
            print("Error: invalid query")
            conn.close()
            continue

        # decode question
        _, questions, _, _, _ = decode(query)
        question_name = ''
        for record in questions:
            if record.type == 'A':
                question_name = record.name
        if len(question_name) == 0:
            print("Error: invalid query")
            conn.close()
            continue

        try:
            # start by asking from the roots
            # if one isn't getting back the answer, try the next one until the answer is returned or never
            ip_a = ''
            for ip in root_ip:
                response, ip_a, re = get_answer(ip, question_name, ip)
                if len(re) != 0:
                    continue
                if (len(ip_a) != 0):
                    conn.send(response)
                    break
            if (len(ip_a) == 0):
                print("Error: server can't find ", question_name)
        except KeyboardInterrupt:
            print('stop searching')
            conn.close()
            break
        # print('----------------------------------------------')
        conn.close()

if __name__ == '__main__':
    # check for invalid arguments
    if len(sys.argv) != 2:
        print('Error: invalid arguments')
        print('Usage: resolver port')
        exit(1)

    server_port = int (sys.argv[1])
    if server_port < 1024 or server_port > 65535:
        print('Error: invalid arguments')
        print('Usage: resolver port')
        exit(1)

    # start the server
    try:
        start_server(server_port)
    except KeyboardInterrupt:
        print("stop the server")
    except Exception as E:
        print(f"Error: {E}:{E.args}")
