class Dashboard:
    def __init__(self, produtores):
        self.produtores = produtores

    def total_fazendas(self):
        return sum(len(produtor.fazendas) for produtor in self.produtores)

    def area_total(self):
        return sum(fazenda.area_total for produtor in self.produtores for fazenda in produtor.fazendas)

    def grafico_por_estado(self):
        estado_count = {}
        for produtor in self.produtores:
            for fazenda in produtor.fazendas:
                if fazenda.estado in estado_count:
                    estado_count[fazenda.estado] += 1
                else:
                    estado_count[fazenda.estado] = 1
        return estado_count

    def grafico_por_cultura(self):
        cultura_count = {}
        for produtor in self.produtores:
            for fazenda in produtor.fazendas:
                for cultura in fazenda.culturas:
                    if cultura in cultura_count:
                        cultura_count[cultura] += 1
                    else:
                        cultura_count[cultura] = 1
        return cultura_count

    def grafico_por_uso_solo(self):
        uso_solo = {"Agricultável": 0, "Vegetação": 0}
        for produtor in self.produtores:
            for fazenda in produtor.fazendas:
                uso_solo["Agricultável"] += fazenda.area_agricultavel
                uso_solo["Vegetação"] += fazenda.area_vegetacao
        return uso_solo

