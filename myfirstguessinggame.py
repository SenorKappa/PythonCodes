secret_word = "Johan"
guess_limit = 3
guess = ""
guess_count = 0

while guess != secret_word and guess_count < guess_limit:
     guess = input("enter your guess: ")
     if guess == secret_word:
          print("you win!")


     elif guess_count < guess_limit:
          print("wrong! ")
          guess_count += 1
          if guess_count == 3:
               print("you're out of guesses, you lose")


