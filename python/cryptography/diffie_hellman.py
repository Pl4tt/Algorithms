import random


class Network:
    def __init__(self) -> None:
        self.users = []
        self.base = 13
        self.mod = random.getrandbits(4000)

    def _rotate_users(self):
        self.users = self.users[1:] + [self.users[0]]
    
    def key_exchange(self) -> None:
        for _ in range(len(self.users)):
            curr_base = self.base

            for user in self.users:
                store_key = user is self.users[-1]
                
                key = user.sign_key(curr_base, store_key)
                curr_base = key
            
            self._rotate_users()


class User:
    def __init__(self, network: Network) -> None:
        self.network = network
        self.network.users.append(self)

        self.network_key = None
        self.private_key = random.randint(self.network.mod//2, self.network.mod-1)
    
    def sign_key(self, key: int, store_key: bool) -> int:
        network_key = pow(key, self.private_key, self.network.mod)
        
        if store_key:
            self.network_key = network_key

        return network_key




if __name__ == "__main__":
    # TEST
    network1 = Network()

    user1 = User(network1)
    user2 = User(network1)
    user3 = User(network1)
    user4 = User(network1)
    user5 = User(network1)
    user6 = User(network1)
    user7 = User(network1)

    network1.key_exchange()

    check_key = pow(
        network1.base,
        user1.private_key*
        user2.private_key*
        user3.private_key*
        user4.private_key*
        user5.private_key*
        user6.private_key*
        user7.private_key,
        network1.mod
    )

    for user in network1.users:
        assert user.network_key == check_key
    
    print(check_key)