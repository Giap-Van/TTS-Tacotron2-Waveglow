""" from https://github.com/keithito/tacotron """
import re
from text import cleaners
from text.symbols import symbols

import os, json
from collections import defaultdict

# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

# Regular expression matching text enclosed in curly braces:
_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')


def text_to_sequence(text, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.

    The text can optionally have ARPAbet sequences enclosed in curly braces embedded
    in it. For example, "Turn left on {HH AW1 S S T AH0 N} Street."

    Args:
      text: string to convert to a sequence
      cleaner_nmes: names of the cleaner functions to run the text through

    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []
  
  phonemes = g2p_sentence_function(text)
  for phoneme in phonemes:
      sequence.append(_symbol_to_id[phoneme])

  print(text)
  print(sequence)

  return sequence

def load_vowels():
    vowels_dict = defaultdict(list)
    with open('/storage/vangt/TTS/tacotron2/text/g2p_vowels.json','r') as f:
        vowels_dict = json.load(f)
    return vowels_dict

def load_consonants():
    consonants_dict = defaultdict(list)
    with open('/storage/vangt/TTS/tacotron2/text/g2p_consonants.json','r') as f:
        consonants_dict = json.load(f)
    return consonants_dict

def g2p_word_function(word, vowels, consonants, vowels_dict, consonants_dict):

    p_word = []
    index = 0
    
    for initial in consonants:
        if word.startswith(initial):
            index += len(initial)
            phoneme = consonants_dict[initial]
            p_word.append(phoneme[0])
            break

    flat1 = 1
    while flat1 == 1:
        flat2 = -1
        for vowel in vowels:
            if word.find(vowel, index) == index:
                flat2 = 1
                index += len(vowel)
                phoneme = vowels_dict[vowel]
                p_word.append(phoneme[0])
                break
        if flat2 == -1:
            flat1 = -1
    
    for final in consonants:
        if word.endswith(final):
            phoneme = consonants_dict[final]
            p_word.append(phoneme[0])
            break

    # pword = '_'.join(p_word)
    return p_word
        

def g2p_sentence_function(sentence):
    vowels_dict = load_vowels()
    consonants_dict = load_consonants()

    vowels = []
    consonants = []
    for key, value in vowels_dict.items():
        vowels.append(key)
    for key, value in consonants_dict.items():
        consonants.append(key)

    text = sentence.split(' ')
    ptext = []
    for word in text:
        if word == "," or word == ".":
            ptext.append(word)
        else:
            # print(g2p_word_function(word, vowels, consonants, vowels_dict, consonants_dict))
            # ptext.append(g2p_word_function(word, vowels, consonants, vowels_dict, consonants_dict))
            ptext += g2p_word_function(word, vowels, consonants, vowels_dict, consonants_dict)
    # ptext = ' '.join(ptext)
    return ptext


def sequence_to_text(sequence):
  '''Converts a sequence of IDs back to a string'''
  result = ''
  for symbol_id in sequence:
    if symbol_id in _id_to_symbol:
      s = _id_to_symbol[symbol_id]
      # Enclose ARPAbet back in curly braces:
      if len(s) > 1 and s[0] == '@':
        s = '{%s}' % s[1:]
      result += s
  return result.replace('}{', ' ')


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text


def _symbols_to_sequence(symbols):
  return [_symbol_to_id[s] for s in symbols if _should_keep_symbol(s)]


def _arpabet_to_sequence(text):
  return _symbols_to_sequence(['@' + s for s in text.split()])


def _should_keep_symbol(s):
  return s in _symbol_to_id and s is not '_' and s is not '~'
