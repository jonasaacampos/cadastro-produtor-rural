import pytest
from propriedade_rural import PropriedadeRural

def test_criar_propriedade_rural_valida():
    fazenda = PropriedadeRural(
        nome='Fazenda Boa Vista',
        cidade='São Paulo',
        estado='SP',
        area_total=1000,
        area_agricultavel=600,
        area_vegetacao=300,
        culturas=['Soja', 'Milho']
    )
    assert fazenda.nome == 'Fazenda Boa Vista'
    assert fazenda.cidade == 'São Paulo'
    assert fazenda.estado == 'SP'
    assert fazenda.area_total == 1000
    assert fazenda.area_agricultavel == 600
    assert fazenda.area_vegetacao == 300
    assert fazenda.culturas == ['Soja', 'Milho']

def test_criar_propriedade_rural_area_invalida():
    with pytest.raises(ValueError) as excinfo:
        PropriedadeRural(
            nome='Fazenda Nova Esperança',
            cidade='Campinas',
            estado='SP',
            area_total=1000,
            area_agricultavel=700,
            area_vegetacao=400,
            culturas=['Café', 'Cana de Açucar']
        )
    assert str(excinfo.value) == "A soma da área agricultável e vegetação não pode ser maior que a área total da fazenda."

def test_criar_propriedade_rural_sem_culturas():
    fazenda = PropriedadeRural(
        nome='Fazenda Sem Culturas',
        cidade='Ribeirão Preto',
        estado='SP',
        area_total=500,
        area_agricultavel=300,
        area_vegetacao=200,
        culturas=[]
    )
    assert fazenda.culturas == []