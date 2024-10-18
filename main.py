from propriedade_rural import PropriedadeRural
from produtor_rural import ProdutorRural
from dashboards import Dashboard

from faker import Faker
import random

fake = Faker('pt_BR')

def gerar_produtor():
    cpf = fake.cpf()
    nome = fake.name()
    return ProdutorRural(cpf, nome)

def gerar_fazenda():
    nome = fake.company()
    cidade = fake.city()
    estado = fake.state_abbr()
    area_total = random.uniform(50, 500)
    area_agricultavel = random.uniform(20, area_total - 10)
    area_vegetacao = random.uniform(10, area_total - area_agricultavel)
    culturas = random.sample(["Soja", "Milho", "Algodão", "Café", "Cana de Açucar"], random.randint(1, 3))
    return PropriedadeRural(nome, cidade, estado, area_total, area_agricultavel, area_vegetacao, culturas)

def gerar_dados_aleatorios(num_produtores):
    produtores = []
    for _ in range(num_produtores):
        produtor = gerar_produtor()
        num_fazendas = random.randint(1, 5)
        for _ in range(num_fazendas):
            fazenda = gerar_fazenda()
            produtor.cadastrar_fazenda(fazenda)
        produtores.append(produtor)
    return produtores

# Gerando dados aleatórios
produtores = gerar_dados_aleatorios(10)

# Criando o dashboard
dashboard = Dashboard(produtores)

# Exemplo de uso do dashboard
print(dashboard.total_fazendas())
print(dashboard.area_total())
print(dashboard.grafico_por_estado()) # pie chart
print(dashboard.grafico_por_cultura()) # pie chart
print(dashboard.grafico_por_uso_solo()) # pie chart
