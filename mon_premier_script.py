import unittest

"""
Ce code compte le nombre de prenoms ayant plus de 7 lettres 

prenoms : liste de prenoms 
Returns : le nombre de prenoms de plus de 7 lettres 

"""
def count_long_names(prenoms):
    nb_prenoms_more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            nb_prenoms_more_than_seven += 1
            print("Prenom avec plus de 7 lettres : " + prenom)
        else:
            print("Prenom avec moins de 7 lettres : " + prenom)
    return nb_prenoms_more_than_seven 

## **Tests unitaires**

class TestNamesMethod(unittest.TestCase):
     def test_count_long_names(self):
        prenoms_1 = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        nb_prenoms_more_than_seven_1 = count_long_names(prenoms=prenoms_1)
        self.assertEqual(nb_prenoms_more_than_seven_1, 4)

        prenoms_2 = [] # test avec une liste vide 
        nb_prenoms_more_than_seven_2 = count_long_names(prenoms=prenoms_2)
        self.assertEqual(nb_prenoms_more_than_seven_2, 0)

if __name__ == '__main__':
    unittest.main()