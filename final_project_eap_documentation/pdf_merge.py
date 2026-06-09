#Εισάγεις την κλάση PdfMerger από τη βιβλιοθήκη PyPDF2.
#Η PdfMerger σου επιτρέπει να ενώσεις πολλά PDF σε ένα.
from PyPDF2 import PdfMerger

#Εισάγεις το module os.
import os #Το os χρησιμοποιείται για να αλληλεπιδράς με το λειτουργικό σύστημα, π.χ. να δεις ποια αρχεία υπάρχουν σε έναν φάκελο.

merger = PdfMerger() #Δημιουργείς ένα αντικείμενο merger. Είναι το εργαλείο που θα κρατήσει όλα τα PDF μέχρι να τα γράψεις σε ένα ενιαίο αρχείο.

#os.listdir() → επιστρέφει όλα τα αρχεία του τρέχοντος φακέλου. f for f (για καθε αρχειο)
#if f.endswith(".pdf") → κράτα μόνο όσα τελειώνουν σε .pdf. εκτος απο merged.pdf
#Το αποτέλεσμα είναι μια λίστα με όλα τα PDF αρχεία εκτός από το merged.pdf.
pdf_files = [
    f for f in os.listdir()
    if f.endswith(".pdf") and f != "merged.pdf"
]

#Το key λέει στη sort: "Με βάση ΠΟΙΟ πράγμα θέλω να ταξινομήσεις;"
#lambda είναι μια ανώνυμη συνάρτηση (function χωρίς όνομα).
pdf_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0])) # η ταξινόμηση γίνεται βάσει του αριθμού μετά το _.

for pdf in pdf_files:     #Για κάθε PDF στη λίστα: το προσθέτεις μέσα στο merger.
    merger.append(pdf)

merger.write("merged.pdf") # Γράφει όλα τα ενωμένα PDF σε νέο αρχείο merged.pdf.
merger.close() # Κλείνει το merger (καλή πρακτική για απελευθέρωση πόρων).

print("GGOP")
