from util.Stack import Stack                # import Stack Class

# Update Function To Update The Count Of Particular Vowel


def update(data):
    lista = []                          # declare 2 empty list
    listb = []

    for i in range(5):
        lista.append(stack1.pop())      # pop all element from stack1 in lista
        listb.append(stack2.pop())      # pop all element from stack1 in listb

    index = lista.index(data)             # read index from lista
    listb[index] = listb[index] + 1         # update the value by 1 in listb

    for i in range(len(lista)):         # push all element of lista in stack1
        stack1.push(lista[i])           # push all element of lista in stack1
        stack2.push(listb[i])


if __name__ == '__main__':

    stack1 = Stack()                    # Create stack1 Object For Stack A
    stack2 = Stack()                    # Create stack2 Object For Stack B

    v = 'aeiou'                         # Vowels In string
    for i in v:
        stack1.push(i)                  # Push Vowels In Stack A
        stack2.push(0)                  # Push 0 In Stack B

    para = input("Enter Paragraph : ")  # Reading Paragraph From User

    for i in para:                      # Loop Through Paragraph
        if (i is 'a' or i is 'A') or (i is 'e' or i is 'E') or (i is 'i' or i is 'I') or (i is 'o' or i is 'O') \
                or (i is 'u' or i is 'U'):         # Check If There is Vowel If True
                update(str(i).lower())             # Calling update Function by Passing Vowel as Parameter

    print("\nStack A : ", end=' ')
    for i in range(5):                             # Print Stack A
        print(stack1.pop(), end='  ')
    print("\nStack B : ", end=' ')
    for i in range(5):                             # Print Stack B
        print(stack2.pop(), end='  ')

