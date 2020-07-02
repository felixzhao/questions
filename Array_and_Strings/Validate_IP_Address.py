from ipaddress import ip_address, IPv6Address


class Solution:
    def validIPv4(self, IP: str) -> str:
        terms = IP.split('.')
        for t in terms:
            print(t)
            if len(t) == 0 or len(t) > 3:
                return "Neither"
            if t[0] == '0' and len(t) != 1 or not t.isnumeric() or int(t) > 255:
                return "Neither"
        return "IPv4"

    def validIPv6(self, IP: str) -> str:
        terms = IP.split(':')
        Hexs = ['a', 'b', 'c', 'd', 'e', 'f']
        for t in terms:
            if len(t) == 0 or len(t) > 4:
                print(t)
                return "Neither"
            for c in t:
                if not c.isnumeric() and c.lower() not in Hexs:
                    return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        """
        Divide and Conquer

        boring question, lots of rules

        Time  O(N)
        space O(1)
        """
        if len(IP.split('.')) == 4:
            return self.validIPv4(IP)
        elif len(IP.split(':')) == 8:
            return self.validIPv6(IP)
        return "Neither"

    def validIPAddress_v2(self, IP: str) -> str:
        """
        useful way
        :param IP:
        :return:
        """
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"