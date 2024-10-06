class AddressIPv4:
    def __init__(self, address: str):
        self.address = address
        self.octets = self.address.split('.')

    def isValid(self) -> bool:
        if len(self.octets) != 4:
            return False
        try:
            return all(0 <= int(octet) <= 255 for octet in self.octets)
        except ValueError:
            return False

    def set(self, address: str) -> 'AddressIPv4':
        self.address = address
        self.octets = self.address.split('.')
        return self

    def getAsString(self) -> str:
        return self.address

    def getAsInt(self) -> int:
        if not self.isValid():
            raise ValueError("Invalid IP Address")
        return sum(int(self.octets[i]) << (8 * (3 - i)) for i in range(4))

    def getAsBinaryString(self) -> str:
        return ''.join(f'{int(octet):08b}' for octet in self.octets)

    def getOctet(self, number: int) -> int:
        if not self.isValid():
            raise ValueError("Invalid IP Address")
        if not 1 <= number <= 4:
            raise ValueError("Octet number must be between 1 and 4")
        return int(self.octets[number - 1])

    def getClass(self) -> str:
        if not self.isValid():
            raise ValueError("Invalid IP Address")
        first_octet = int(self.octets[0])
        if first_octet < 128:
            return 'A'
        elif first_octet < 192:
            return 'B'
        elif first_octet < 224:
            return 'C'
        elif first_octet < 240:
            return 'D'
        else:
            return 'E'

    def isPrivate(self) -> bool:
        if not self.isValid():
            raise ValueError("Invalid IP Address")
        first_octet = int(self.octets[0])
        second_octet = int(self.octets[1])
        if (first_octet == 10 or
           (first_octet == 172 and 16 <= second_octet <= 31) or
           (first_octet == 192 and second_octet == 168)):
            return True
        return False

ip1 = AddressIPv4("192.168.1.1")
ip2 = AddressIPv4("10.0.0.1")
ip3 = AddressIPv4("300.168.1.1")

print(f"IP1 validní: {ip1.isValid()}")
print(f"IP1 třída: {ip1.getClass()}")
print(f"IP1 soukromá: {ip1.isPrivate()}")
print(f"IP1 binárně: {ip1.getAsBinaryString()}")
print(f"IP1 druhý oktet: {ip1.getOctet(2)}")

print(f"IP2 validní: {ip2.isValid()}")
print(f"IP2 třída: {ip2.getClass()}")
print(f"IP2 soukromá: {ip2.isPrivate()}")

print(f"IP3 validní: {ip3.isValid()}")
