from empleado import Empleado
from cliente import Cliente


#emp = Empleado('Lucas','Moy','123123','234234423',1900)
#cli = Cliente('Lucas','Moy','123123','234234423','vip')


###########################################################################################
#creando la funcion para que carge los datos y poderlo mostrar por mensaje 
def cargar():
    respuesta = input ('va a  agregar un empleado')
    nombre = input ('ingrese el nombre')
    apellido = input ('ingrese el apellido')
    dni = input ('ingrese el dni')
    telefono = input ('ingrese el telefono')
    
    if (respuesta == 'si'):
        salario = input('ingrese el salario')
        emp = Empleado(nombre , apellido , dni , telefono , int (salario))
        personas.append(emp)
    else:
        tipo = input('ingrese el tipo de cliente')
        cli = Cliente(nombre , apellido , dni , telefono , tipo)

personas = []
cargar()

for persona in personas:
    print(persona)