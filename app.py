import socket

def reverse(ip):
    return socket.gethostbyaddr(ip)

def ip2bin(ip) :
    b = ""
    for n in ip.split(".") :
        b += bin(int(n))[2:].zfill(8)
    return b

def snMask2bin(snMask) :
   return "1" * snMask + "0" * (32-snMask)

def bin2ip(b) :
    r = []
    for i in range(0, 32, 8) :
        r.append(str(int(b[i:i+8], 2)))
    return ".".join(r)

def calcDomainRange(domain) :
    snMask = snMask2bin(int(domain.split("/")[1]))
    domain = ip2bin(domain.split("/")[0])

    b = ""
    for i in range(0, 32) :
        b += domain[i] if snMask[i] == "1" else ""
    n = snMask.count("0")

    res = []
    for i in range(0, 2 ** n) :
        res.append(bin2ip(b + bin(i)[2:].zfill(n)))

    return res

def main() :
    f = open("domains.txt", "r")
    domains_ = f.read().split("\n")
    f.close()
    domains = []

    for domain in domains_ :
        if not domain :
            continue
        if "/" in domain :
            snDomain = calcDomainRange(domain)
            domains.extend(snDomain)
        else :
            domains.append(domain)
    
    result = {}
    for domain in domains :
        try :
            res = reverse(domain)
            result[domain] = res
            print(res)
        except socket.herror as e:
            continue
    
    print(result)

if __name__ == "__main__" :
    main()