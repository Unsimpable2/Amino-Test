import re

class Amino():

    def __init__(self):
        self.filename = 'codon.tsv'
        
        self.amino = []
        self.resultoffind = []
        self.result = {}

        self.Open_file()

    def Open_file(self):
        with open(self.filename) as f:
            for line in f:
                self.amino.append(line.split())
        f.close()

        self.run()

    def run(self):
        print("----")
        self.Find_amino("AAACCCAATTTTTTACACAGCTGCTGGGCCCAGT")
        self.check_amino("Proline")

        print("----")
        self.Find_amino("AAACCCAATTTTTT")
        self.check_amino("Opal")

        print("----")
        self.Find_amino("CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG")
        self.check_amino("Alanine")
        self.check_amino("Glycine")

        print("----")
        self.Find_amino("CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG")
        self.count_many()

        print("----")
        self.Find_amino("CTAGATC")
        self.count_many()

    def Find_amino(self, data):
        self.data = data
            
        y = 0
        for j in range(len(self.data)):
            self.subdata = self.data[y:y +3]
            y +=3

            if len(self.subdata) <= 2:
                y = 0
                break

            if [x for x in self.amino if re.search(self.subdata, str(x))]:
                for i in range(len(self.amino)): 
                    if self.subdata == self.amino[i][0]: 
                        self.resultoffind.append(self.amino[i][1]) 
                        break 

        self.result = {i:self.resultoffind.count(i) for i in self.resultoffind}

    def check_amino(self, check):
        self.check = check
        print(f'Find {self.check}:')
        if self.check in self.result:
            print(f'Yes, {self.check} {self.result[self.check]}\n')
        else:
            print(f"No {self.check}\n")
        
        self.resultoffind = []

    def count_many(self):
        print(f"Amount of Amino Acids: {len(self.result)}\n")
        self.resultoffind = []

run = Amino()