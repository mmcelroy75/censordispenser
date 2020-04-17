# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)

#def censor_text(text, phrase):
#  new_text = text.replace(phrase, "******")
#  return new_text

#print(censor_text(email_one, "learning algorithms"))

#print(email_two)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

proprietary_terms += [term.capitalize() for term in proprietary_terms]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

negative_words += [word.capitalize() for word in negative_words]

def censor_two(input_text, censored_list): 
  for word in censored_list:
    censored_word = ""
    for x in range(0,len(word)):
      if word[x] == " ":
        censored_word = censored_word + " "
      else:
        censored_word = censored_word + "X"
    input_text = input_text.replace(word, censored_word)
  return input_text

#print(censor_two(email_two, proprietary_terms))

def censor_three(input_text1, censored_list1, censored_list2)

#print(email_three)