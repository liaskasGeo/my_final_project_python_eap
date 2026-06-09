A = {1,2,3,4}
B = {4,5}
print("A = ",A)
print("B = ",B)
print("===============================")
print("union:" + str(A|B)) #ενωση Α ή του Β.
print("intersect:" + str(A&B)) # Επιστρεφει την τομη στοιχεια του Α και του Β
print("diff A-B:" + str(A-B)) #Επιστρεφει στοιχεια του Α που δεν ανηκουν στο Β
print("diff B-A:" + str(B-A)) #Επιστρεφει στοιχεια του Β που δεν ανηκουν στο Α
print("symm.dif.:" + str(A^B)) # Eπιστρεφει μη κοινα σημεια του Α και Β (Δλδ φευγει το 4 στην συγκεκριμενη)
print("A subset B:" + str(A.issubset(B))) # ειναι το Α υποσυνολο του Β ;; False
print("A,B disjoint: "+ str(A.isdisjoint(B)))# ειναι ξενα μεταξύ τους ;; False

A.update(B) # αντι να γραψω A = A | B , κανει την ενωση
print("A=A|B: "+ str(A))
A.intersection_update(B)
print("A=A&B:"+ str(A))

print("================================")

#Functions build-in
print("Length of set A: ",len(A))
print("Maximum of set A: ",max(A))
print("Min of set A: ",min(A))
print("Sum of set A: ",sum(A))