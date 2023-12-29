#!/usr/bin/env python3

sentence_extractors = ['. ', '? ', '! ']
mark_replacer = '||||'

class MyString:
  pass
  def __init__(self, value=""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    return self._value[-1] == '.'
  
  def is_question(self):
    return self._value[-1] == '?'
  
  def is_exclamation(self):
    return self._value[-1] == '!'
  
  def count_sentences(self):
    
    # If empty string, return 0
    if (len(self._value) == 0):
      return 0
    
    # If not an empty string, count sentences and return count
    sentences = self._value
    print(sentences)
    for extractor in sentence_extractors:
      sentences = sentences.replace(extractor, mark_replacer)
      while (str(mark_replacer + mark_replacer) in sentences):
        sentences = sentences.replace(str(mark_replacer + mark_replacer), mark_replacer)
      print(sentences)
    sentences = sentences.split(mark_replacer)
    print(sentences)
    print(len(sentences))
    return len(sentences)
  
  