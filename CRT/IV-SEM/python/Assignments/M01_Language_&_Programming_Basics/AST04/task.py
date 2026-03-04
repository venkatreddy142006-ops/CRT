def Reverse_String(s: str) -> str:
   new_str = ""
   for i in range(len(s)-1, -1, -1):
       new_str += s[i]
   return new_str 



if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
