class TV:

    cor = "Preta"

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


minha_tv = TV(40)
maria_tv = TV(32)

minha_tv.volume = 20
print(minha_tv.volume)

print(minha_tv.canal)
minha_tv.mudar_canal("HBO")
print(minha_tv.canal)

print(minha_tv.cor)