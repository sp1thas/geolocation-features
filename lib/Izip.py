'''
me ayto to script diamorfwnw ti lista me ta data poy gia to arxeio arff
'''
from itertools import izip

def CreateObj(BasicFeatures, LetterFreq, SymbolFreq, MostUsedWords, SlanFreq, textClass, PunctuationsFreq):
    return izip(
                    BasicFeatures['SymbolsPerChar'],
                    BasicFeatures['PuncuationsPerChar'],
                    BasicFeatures['SpacesPerChar'],
                    BasicFeatures['UpperPerChar'],
                    BasicFeatures['LettersPerChar'],
                    BasicFeatures['DigitsPerChar'],
                    BasicFeatures['ShortWords'],
                    BasicFeatures['TotalCharsInWords'],
                    BasicFeatures['AvgWordLen'],
                    BasicFeatures['AvgSentencesWords'],
                    BasicFeatures['AvgSentencesChars'],
                    BasicFeatures['TotalDiffWords'],
                    BasicFeatures['HapaxLegomena'],
                    BasicFeatures['HapaxDislegomena'],
                    LetterFreq['a'],
                    LetterFreq['b'],
                    LetterFreq['c'],
                    LetterFreq['d'],
                    LetterFreq['e'],
                    LetterFreq['f'],
                    LetterFreq['g'],
                    LetterFreq['h'],
                    LetterFreq['i'],
                    LetterFreq['j'],
                    LetterFreq['k'],
                    LetterFreq['l'],
                    LetterFreq['m'],
                    LetterFreq['n'],
                    LetterFreq['o'],
                    LetterFreq['p'],
                    LetterFreq['q'],
                    LetterFreq['r'],
                    LetterFreq['s'],
                    LetterFreq['t'],
                    LetterFreq['u'],
                    LetterFreq['v'],
                    LetterFreq['w'],
                    LetterFreq['x'],
                    LetterFreq['y'],
                    LetterFreq['z'],
                    SymbolFreq['1'],
                    SymbolFreq['2'],
                    SymbolFreq['3'],
                    SymbolFreq['4'],
                    SymbolFreq['5'],
                    SymbolFreq['6'],
                    SymbolFreq['7'],
                    SymbolFreq['8'],
                    SymbolFreq['9'],
                    SymbolFreq['10'],
                    SymbolFreq['11'],
                    SymbolFreq['12'],
                    SymbolFreq['13'],
                    SymbolFreq['14'],
                    SymbolFreq['15'],
                    SymbolFreq['16'],
                    SymbolFreq['17'],
                    SymbolFreq['18'],
                    SymbolFreq['19'],
                    SymbolFreq['20'],
                    SymbolFreq['21'],
                    PunctuationsFreq['1'],
                    PunctuationsFreq['2'],
                    PunctuationsFreq['3'],
                    PunctuationsFreq['4'],
                    PunctuationsFreq['5'],
                    PunctuationsFreq['6'],
                    PunctuationsFreq['7'],
                    PunctuationsFreq['8'],
                    MostUsedWords['US'],
                    MostUsedWords['UK'],
                    MostUsedWords['AUS'],
                    MostUsedWords['CAN'],
                    MostUsedWords['NNS'],
                    SlanFreq['US'],
                    SlanFreq['UK'],
                    SlanFreq['AUS'],
                    SlanFreq['AUS'] ,
                    textClass
                )