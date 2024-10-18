from propriedade_rural import PropriedadeRural

class ProdutorRural:
    def __init__(self, cpf_cnpj, nome):
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.fazendas = []

    def cadastrar_fazenda(self, fazenda):
        if not isinstance(fazenda, PropriedadeRural):
            raise TypeError('A fazenda deve ser uma instância da classe PropriedadeRural.')
        fazenda.validar_areas()
        self.fazendas.append(fazenda)

    def excluir_fazenda(self, fazenda):
        self.fazendas.remove(fazenda)

    def listar_fazendas(self):
        return self.fazendas