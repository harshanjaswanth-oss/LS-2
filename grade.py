marks_english=int(input("marks of english"))
marks_maths=int(input("marks of maths"))
marks_social=int(input("marks of social"))
marks_science=int(input("marks of science"))
marks_hindi=int(input("marks of hindi"))

average=( marks_english+marks_maths+marks_social+marks_hindi+marks_science)/5

if average>75:
    print("grade a")
elif average>60:
     print("grade b")
elif average>35:
     print("grade c")
else:
      print("fail")