"""
Defines the NetworkObject class.
This is the base class from which all network objects defined by the
user should descend.
"""

from ping.ping import Ping

class NetworkObject():
   
    def __init__(self, ip):
        # Constructor
        self._pingResponse = None
        self.ip = ip

    def ping(self):
        """
        Send a single ICMP echo request.

        Returns True if an ICMP response is recieved from the
        pinged host, and False otherwise.

        This function also sets/changes the value of self.pingResponse
        to include information about the ICMP response packet. This
        information can be accessed publicly in the form of a getter
        member function that returns a dictionary. See
        getPingResponse().

        NOTE: Pinging in Python will open a raw socket, and requires
        root/Administrator permissions. The Ping class will raise
        socket.error if you don't have the proper permissions.
        """
        ping = Ping(self.ip)
        self._pingResponse = ping.do()
        
        if self._pingResponse == None:
            return False
        else:
            return True

    def getPingResponse():
        """
        A 'getter' method that returns a dictionary of (possibly) useful
        information about the last ping response. Note that only
        information about the most recent response is stored. If
        self.ping() has not already been called, this function will
        return the default value of the object used to store ping
        response information, None.

        >>> myNetworkObject.getPingResponse()
        >>> myNetworkObject.ping()
        True
        >>> myNetworkObject.getPingResponse()
        {'delay': delay, 'ip': ip, 'packet_size': packet_size, 'ip_header': ip_header, 'icmp_header': icmp_header}
        >>> myNetworkObject.getPingResponse()['delay']
        delay
        """
        return _pingResponse
