#takes the contents of the file name.txt and assigns it to the variable full_text
with open('name.txt') as f:
	my_name = f.read()

#creates a new file named hello.txt, which prints 'Hello, my name is' and a string of the characters contained within full text.
with open('hello.txt', 'w') as f:
	f.write('Hello, my name is ' + str(my_name))


#David and Ancito