import pandas as pd
import requests as r
import re

urls_dict = {'rxlist': 'https://www.rxlist.com/drugs/alpha_{letter}.htm',
             'drugs': 'https://www.drugs.com/alpha/{letter}{second_letter}.html'}


def make_drugs_dataframe(drugs_list, letter, second_letter=None):
    """ Spits out drugs dataframe from provided list. """
    column_order = ['letter', 'second_letter', 'drug']
    drugs_df = pd.DataFrame(drugs_list, columns=['drug'])
    drugs_df['letter'] = letter
    if second_letter is not None:
        drugs_df['second_letter'] = second_letter
    else:
        column_order.remove('second_letter')
    return drugs_df[column_order]


def split_drugs_out(drug):
    """ Splits parentheses drugs and non-parantheses drugs from each other.
    May use at some point down the road. """
    if ')' in drug:
        return [e.rstrip() for e in drug.strip(')').split('(')]
    else:
        return [drug, '']


# function for rxlist
def grab_drugs_by_letter(url, letter):
    """ Grabs drugs from rxlist.com by letter provided. """
    letter_url = url.format(letter=letter)
    letter_grab = r.get(letter_url)
    letter_regex = re.compile('\-drug.htm">(.*)</a>')
    drugs_pull = letter_regex.findall(letter_grab.text)
    return make_drugs_dataframe(drugs_pull, letter)


# function for drugs.com
def grab_drugs_by_letters(url, letter, second_letter):
    """ Grabs drugs from drugs.com by letters provided and spits out into a dataframe. """
    letters_url = url.format(letter=letter, second_letter=second_letter)
    letters_grab = r.get(letters_url)
    letters_regex = re.compile("a href=(.*).html'>(.*)</a></li")
    drugs_pull_base = letters_regex.findall(letters_grab.text)[9:-4]
    drugs_pull = [e[1] for e in drugs_pull_base] 
    return make_drugs_dataframe(drugs_pull, letter, second_letter)