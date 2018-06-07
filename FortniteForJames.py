import PIL
from PIL import ImageGrab
import pytesseract
from ctypes import windll



def get_accuracy(results):
    accuracy_index = results.find("Accuracy")
    results_from_accuracy = results[accuracy_index + 9:]
    end_of_stat_index = results_from_accuracy.find(" ")
    accuracy = results_from_accuracy[:end_of_stat_index]
    return accuracy

    

picture = PIL.ImageGrab.grabclipboard()#"C:/Code/Python/Test Screenshots/3840x2160.jpeg"
print(picture)
results = pytesseract.image_to_string(PIL.Image.open(picture))
print(get_accuracy(results))

