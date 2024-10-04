class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "realizou um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}.")

heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Zane", 25, "ninja")
heroi3 = Heroi("Lana", 22, "mago")
heroi4 = Heroi("Kai", 28, "monge")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar() 
