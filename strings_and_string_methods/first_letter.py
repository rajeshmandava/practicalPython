# Challenge: Pick Apart your User's Input
# from asyncio.windows_events import NULL


password = input("Tell me your password:")
upper_case_password = password.upper()
if upper_case_password != "":
  print(upper_case_password[0])