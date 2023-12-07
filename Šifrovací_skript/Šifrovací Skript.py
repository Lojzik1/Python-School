class Cypher:
    
    def __init__(self, amount = 2):
        self.__number_of_rails = amount
    
    def __transcript(self, open_text):
        return open_text.replace(" ","")
    
    def encrypt(self, open_text):
        self.__open_text = self.__transcript(open_text)
        array = ['' for _ in range(self.__number_of_rails)]

        row, direction = 0, 1
        for character in self.__open_text:
            array[row] += character
            if row == 0:
                direction = 1
            elif row == self.__number_of_rails - 1:
                direction = -1
            row += direction

        encrypted_text = ''.join(array)
        return encrypted_text

    def decrypt(self, cypher_text):
        self.__cypher_text = cypher_text
        
    def get_open_text(self):
        pass
    
    def get_cypher_text(self):
        pass
    
    def __str__(self):
        pass

print(Cypher(4).encrypt("GEEKS FOR GEEKS"))
print(Cypher(4).decrypt("GESOGESEKFREK"))