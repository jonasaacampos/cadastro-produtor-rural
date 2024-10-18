class PropriedadeRural:
    def __init__(self, nome, cidade, estado, area_total, area_agricultavel, area_vegetacao, culturas):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.area_total = area_total
        self.area_agricultavel = area_agricultavel
        self.area_vegetacao = area_vegetacao
        self.culturas = culturas

        self.validar_areas()

    def validar_areas(self):
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValueError("A soma da área agricultável e vegetação não pode ser maior que a área total da fazenda.")