# msiaLex
msiaLex consists of different types of modifiers from three languages (e.g. English, Bahasa Melayu, Chinese)
## Installation
pip install msiaLex

## Import package
from msiaLex import modifier

## Language code
Language code are required to serve as parameter for below functions in order to return modifiers for specific languages
- English : en
- Bahasa Melayu : zsm
- Chinese : zh

## Negation
> modifier.negation('en')

['no', 'not', 'none', 'nobody', 'nothing', 'neither', 'never', 'cannot']

## Intensifier
High and low intensifier are returned from English language 
>modifier.intensifier('en')

{'high': ['absolutely',
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

## Disjunction
>modifier.disjunction('en')

['but',
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
