import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

np.random.seed(1)
synaptic_weights = 2 * np.random.random((3,1)) - 1
print("Случайные инициализирующие веса успешно созданы")

#Метод обратного распространения
print("Процесс обучения весов начат...")
for i in range(20000):
	input_layer = training_inputs
	outputs = sigmoid(np.dot(input_layer, synaptic_weights))

	err = training_outputs - outputs
	adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

	synaptic_weights += adjustments
else:
	print("Успешно")

#Процесс обработки
def main():
	def checking(what):
		assert what == 0 or what == 1, "Нужно вводить число от 0 до 1"

	f_el = int(input("Введите первое значение(от 0 до 1): "))
	checking(f_el)
	s_el = int(input("Введите второе значение(от 0 до 1): "))
	checking(s_el)
	t_el = int(input("Введите третье значение(от 0 до 1): "))
	checking(t_el)
	check = np.array([f_el,s_el,t_el])
	print("Был создан массив: {0}".format(check))

	output = sigmoid(np.dot(check, synaptic_weights))
	print(np.around(output))

#Переменная работы
isWorking = True

#Цикл для постоянной проверки до выхода(т.е пока не выйдешь он работает)
while isWorking:
	print('')
	main()
	x = input("Выйти?: ")
	if x.lower() == 'да':
		isWorking = False
else:
	print("Конец работы")