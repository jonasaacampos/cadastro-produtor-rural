import pytest
from produtor_rural import ProdutorRural
from propriedade_rural import PropriedadeRural

#######################
# DEFAULT VALUES TEST #
#######################

@pytest.fixture
def produtor():
    return ProdutorRural("12345678901", "João Silva")

@pytest.fixture
def fazenda1():
    return PropriedadeRural(
        nome='Fazenda Boa Vista',
        cidade='São Paulo',
        estado='SP',
        area_total=1000,
        area_agricultavel=600,
        area_vegetacao=300,
        culturas=['Soja', 'Milho']
    )

@pytest.fixture
def fazenda2():
    return PropriedadeRural(
        nome='Fazenda Nova Esperança',
        cidade='Campinas',
        estado='SP',
        area_total=1200,
        area_agricultavel=700,
        area_vegetacao=400,
        culturas=['Café', 'Cana de Açucar']
    )

########
# Test #
########

def test_cadastrar_fazenda(produtor, fazenda1):
    produtor.cadastrar_fazenda(fazenda1)
    assert fazenda1 in produtor.listar_fazendas()

def test_excluir_fazenda(produtor, fazenda1):
    produtor.cadastrar_fazenda(fazenda1)
    produtor.excluir_fazenda(fazenda1)
    assert fazenda1 not in produtor.listar_fazendas()

def test_listar_fazendas(produtor, fazenda1, fazenda2):
    produtor.cadastrar_fazenda(fazenda1)
    produtor.cadastrar_fazenda(fazenda2)
    fazendas = produtor.listar_fazendas()
    assert len(fazendas) == 2
    assert fazenda1 in fazendas
    assert fazenda2 in fazendas

def test_cadastrar_fazenda_invalida(produtor):
    with pytest.raises(TypeError):
        produtor.cadastrar_fazenda("Fazenda Inválida")