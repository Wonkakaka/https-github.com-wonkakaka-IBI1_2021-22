from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
# import these functions
DOMTree = xml.dom.minidom.parse("C:/Users/lenovo/Desktop/go_obo.xml")
# Use this step to reach the location of the file.
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
# Define a new dictionary whose keys are parentnodes and the values are childnodes.
D1 = {}
total_list =[]
translation_list = []
number_of_terms = 0
for term in terms:
    number_of_terms+=1
a = "the total number of terms currently recorded in the Gene Ontology is: "
# Perform calculations
print(a+str(number_of_terms))
def counter(list):
 for n in list:
  if n not in list_:
   list_.append(n)
   if n in D1:
    counter(D1[n])
 return len(list_)
for term in terms:
 is_a_list=[]
 for n in term.getElementsByTagName("is_a"):
  is_a_list.append(n.childNodes[0].data)
 id_all= term.getElementsByTagName("id")[0].childNodes[0].data
 for is_a in is_a_list:
  if is_a in D1:
   D1[is_a].append(id_all)
  else:
   D1[is_a]=[id_all]
for term in terms:
 childnodes_number=0
 list_=[]
 id_all=term.getElementsByTagName('id')[0].childNodes[0].data
 if id_all in D1:
  childnodes_number=counter(D1[id_all])
 total_list.append(childnodes_number)
 if 'translation' in term.getElementsByTagName("defstr")[0].childNodes[0].data:
  translation_list.append(childnodes_number)
# The codes are used to calculate the total number of childnodes.
plt.boxplot(total_list,labels = ["Gene Ontology"])
plt.title("The distribution of childnodes across terms in the Gene Ontology")
plt.xlabel("terms")
plt.ylabel("the number of childnodes")
plt.show()
# Output a boxplot describing the distribution of childnodes and give it a title.
plt.boxplot(translation_list,labels = ["translation Gene Ontology"])
plt.title("The distribution of childnodes across terms associated with translation")
plt.xlabel("terms with translation")
plt.ylabel("the number of childnodes")
plt.show()
# Output a boxplot with the distribution of the childnodes associated with the translation described and named.
total_average = sum(total_list)/len(total_list)
translation_average = sum(translation_list)/len(translation_list)
X = "The translation terms contain, on average, a smaller number of childnodes than the overall Gene Ontology."
Y = "The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology."
if total_average>translation_average:
    print(X)
if total_average<translation_average:
    print(Y)
# Calculate and compare the average childnodes of the two.
# The final result is:The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology.