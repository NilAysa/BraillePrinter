'''
Dati kod je dizajniran da formatira tekst na način koji je kompatibilan sa specifičnim zahtjevima Braille štampača. 
Sastoji se od tri glavne funkcije: `fillToBrailleFormat`, `parseText` i `toMachineBraille`. 
Funkcija `fillToBrailleFormat` obrađuje ulazni tekst pretvarajući velika slova u mala i dodajući im donju crtu, 
te zamjenjujući cifre sa simbolom hash, čime se osigurava da tekst odgovara Brailleovim kodiranim konvencijama. 
Funkcija `parseText` zatim dijeli formatirani tekst na riječi i raspoređuje ih u linije određene dužine (`lineLength`), 
osiguravajući da svaka linija bude pravilno popunjena prazninama kako bi se održala konzistentna dužina. 
Na kraju, funkcija `toMachineBraille` kombinuje ove korake tako što prvo konvertuje tekst pomoću `fillToBrailleFormat`, 
zatim ga organizuje u linije sa `parseText` i preokreće svaku liniju kako bi odgovarala orijentaciji kucanja štampača. 
Rezultat je lista formatiranih tekstualnih linija, spremnih za štampanje u Brailleovom pismu.
Konstante lineLength i numOfLines predstavljaju koliko braille slova može stati u jednom redu te koliko redova
jedna strana papira može da ima.
'''

lineLength = 32 
numOfLines = 25

def fillToBrailleFormat(text):
    brailleText = ""
    for c in text:
        if c.isupper():
            brailleText += '_' + c.lower()
        elif c.isdigit():
            brailleText += '#' + c
        else:
            brailleText += c
    return brailleText

def parseText(text):
    words = text.split()
    lines = []
    currentLine = ""

    for word in words:
        if len(word) > lineLength:
            raise ValueError("Word {} exceeds line length.".format(word))
        
        if len(currentLine) + len(word) + 1 <= lineLength:
            if currentLine:
                currentLine += " "
            currentLine += word
        else:
            currentLine += " " * (lineLength - len(currentLine))
            lines.append(currentLine)
            currentLine = word

    if currentLine:
        currentLine += " " * (lineLength - len(currentLine))
        lines.append(currentLine)

    return lines
  
def toMachineBraille(text):
    text = fillToBrailleFormat(text)
    lines = parseText(text)
    return [line[::-1] for line in lines]