import pytest
from dashboards import Dashboard
from produtor_rural import ProdutorRural
from propriedade_rural import PropriedadeRural

@pytest.fixture
def setup_dashboard():
    # Criando produtores e fazendas para o teste
    produtor1 = ProdutorRural("12345678901", "João Silva")
    fazenda1 = PropriedadeRural(
        nome='Fazenda Boa Vista',
        cidade='São Paulo',
        estado='SP',
        area_total=1000,
        area_agricultavel=600,
        area_vegetacao=300,
        culturas=['Soja', 'Milho']
    )
    fazenda2 = PropriedadeRural(
        nome='Fazenda Nova Esperança',
        cidade='Campinas',
        estado='SP',
        area_total=1200,
        area_agricultavel=700,
        area_vegetacao=400,
        culturas=['Café', 'Soja']
    )
    produtor1.cadastrar_fazenda(fazenda1)
    produtor1.cadastrar_fazenda(fazenda2)

    produtor2 = ProdutorRural("98765432100", "Maria Oliveira")
    fazenda3 = PropriedadeRural(
        nome='Fazenda Alegre',
        cidade='Rio de Janeiro',
        estado='RJ',
        area_total=800,
        area_agricultavel=500,
        area_vegetacao=200,
        culturas=['Milho', 'Café']
    )
    produtor2.cadastrar_fazenda(fazenda3)

    dashboard = Dashboard([produtor1, produtor2])
    return dashboard

def test_grafico_por_cultura(setup_dashboard):
    dashboard = setup_dashboard
    cultura_count = dashboard.grafico_por_cultura()
    assert cultura_count == {'Soja': 2, 'Milho': 2, 'Café': 2}

def test_grafico_por_uso_solo(setup_dashboard):
    dashboard = setup_dashboard
    uso_solo = dashboard.grafico_por_uso_solo()
    assert uso_solo == {'Agricultável': 1800, 'Vegetação': 900}