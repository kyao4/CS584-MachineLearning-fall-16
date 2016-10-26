'''
Created on 2016年9月19日

@author: kyao4
'''
import csv

def main():
    with open('Pokemon.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        myList = []
        for each in spamreader:
            num = each[0]
            Name = each[1]
            Type1 = each[2]
            Type2 = each[3]
            Total = each[4]
            HP = each[5]
            Attack = each[6]
            ATTSP = each[7]
            DEFSP = each[8]
            Speed = each[9]
            Generation = each[10]
            Lengendary = each[11]
            num = "'?'" if num == "" else num
            Name = "'?'" if Name == "" else Name
            Type1 = "'?'" if Type1 == "" else Type1
            Type2 = "'?'" if Type2 == "" else Type2
            Total = "'?'" if Total == "" else Total
            HP = "'?'" if HP == "" else HP
            Attack = "'?'" if Attack == "" else Attack
            ATTSP = "'?'" if ATTSP == "" else ATTSP
            DEFSP = "'?'" if DEFSP == "" else DEFSP
            Speed = "'?'" if Speed == "" else Speed
            Generation = "'?'" if Generation == "" else Generation
            Lengendary = "'?'" if Lengendary == "" else Lengendary
#             if num == "" or Name == "" or Type1 == "" or Type2 == "" or Total == "" or HP == "" or Attack == "" or ATTSP == "" or DEFSP == "" or Speed == "" or Generation == "" or Lengendary == "":
#                     continue
            pokemon = [num, Name, Type1, Type2 , Total, HP, Attack, ATTSP, DEFSP, Speed, Generation, Lengendary]
            myList.append(pokemon) 
        with open('output.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for item in myList:
                spamwriter.writerow(item)
if __name__ == '__main__':
    main()