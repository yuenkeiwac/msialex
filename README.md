# msiaLex
msiaLex consists of different types of modifiers from three languages (e.g. English, Bahasa Melayu, Chinese)
# Installation
pip install msiaLex

# Description on how to use modifier
from msiaLex import modifier

# Language code
Language code are required to serve as parameter for below functions in order to return modifiers for specific language
English : en
Bahasa Melayu : zsm
Chinese : zh

# Negation
This function return negations of English language
>>modifier.negation('en')
>>['no', 'not', 'none', 'nobody', 'nothing', 'neither', 'never', 'cannot']

# Intensifier
This function return intensifiers of English language
>>modifier.intensifier('en')
>>{'high': ['absolutely',
  'completely',
  'extremely',
  'highly',
  'rather',
  'really',
  'so',
  'too',
  'totally',
  'utterly',
  'very',
  'much',
  'more',
  'quite',
  'most',
  'super'],
 'low': ['little', 'less']}

# Disjunction
This function return disjunctions of English language
>>modifier.disjunction('en')
>>['but',
 'however',
 'in contrast',
 'instead',
 'whereas',
 'except that',
 'on the contrary',
 'conversely',
 'nevertheless',
 'although',
 'alternatively']
