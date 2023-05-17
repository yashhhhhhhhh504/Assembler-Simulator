instrnOpcode={"10000":"add" , "10001":"sub" , "10010":"movB" , "10011":"movC" , "10100":"ld" , "10101":"st" , "10110":"mul" , "10111":"div" , "11000":"rs" ,"11001":"ls" ,"11010":"xor" ,"11011":"or" , "11100":"and" , "11101":"not" ,"11110":"cmp" ,"11111":"jmp" ,"01100":"jlt" ,"01101":"jgt" ,"01111":"je" ,"01010":"hlt"}

instrnType = {"add":"A" , "sub":"A","movB":"B","movC":"C", "ld":"D" , "st":"D" , "mul":"A" , "div":"C" , "rs":"B" ,"ls":"B" ,"xor":"A" ,"or":"A","and":"A" , "not":"C" ,"cmp":"C" ,"jmp":"E" ,"jlt":"E" ,"jgt":"E" ,"je":"E" ,"hlt":"F"}

registers = {
    '000':"R0",
    '001':"R1",
    '010':"R2",
    '011':"R3",
    '100':"R4",
    '101':"R5",
    '110':"R6",
    '111':"flags"
}

mapping = {
    "PC":0,
    "R0":0,
    "R1":0,
    "R2":0,
    "R3":0,
    "R4":0,
    "R5":0,
    "R6":0,
    "flags":0,
    "cycle":0
}