class Todo:
    def __init__(self):
        self.code_id: int
        self.title: str 
        self.description: str 
        self.completed: bool  = False
        self.tags: list = []

    def mark_completed(self):
        self.completed =  True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

        def __str__(self):
            return "{} - {}".format(self.code_id self.title)
        

class TodoBook:
    def __init__(self):
        self.todos = dict= {}
    def add_todo(self,title:str, descrition: str)-> int:
        id = len(self.todos)+1
        todo = Todo (id, title, description)
        self.todos[id] = todo
        return id
    def pendings_todo(self):
        lista_tareas_pendientes = [item for item in self.todos.values() if not todo.completed]
        return lista_tareas_pendientes
    def completed_todos(self)-> list [Todo]:
        lista_tareas_completadas = [todo for todo in self.todos.values() if todo.completed]
        return lista_tareas_completadas
    
    def tags_todo_count(self)-> dict:
        todo_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in todo.count.keys():
                    todo_count[tag] = todo_count[tag]
                else:
                    todo_count[tag] = 1
"""
listas
numeros = [1,2,3,4,5]
print (numeros[0])el numero indica la posicion de la lista que se desea imprimir

tuplas 
nombres = ("juan","pedro", "maria")
print nombres[0] el nombre es un elemento en una tupla y no puede ser modificado

strings
cadena ="hola mundo"
print cadena[::-1] reversa del string

diccionarios
personas = {"nombre":"Juan", "apellido": "Perez"}
print personas["nombre"] muestra los valores dentro del diccionario

sets
frutas = set(["manzana","pera"])
frutas.add("naranja") agrega elementos al conjunto, los elementos son tratados como uno solo 
"""