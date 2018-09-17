
invoker=None

def f1():
	for i in range(1,10):
		hola = f2()

	return 'cloudbook: done' 

def f2():
	invoker("du_0.cloudbook_print('dir1.file2.f2: hello world')")
	
	return 'cloudbook: done' 

