



#inheretence - just place the class functions you want to inheret in parentheses

class new:
    def __init__(self, name, size, age, is_dead):
        self.name = name 
        self.size = size
        self.age = age
        self.is_dead = is_dead 
    def old_person(self):
        if self.age >= 60:
            return True
        else:
            return False


class Question(new):
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

