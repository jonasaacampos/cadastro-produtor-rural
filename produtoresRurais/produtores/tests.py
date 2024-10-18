from django.test import TestCase
from .models import ProdutorRural, PropriedadeRural

class ProdutorRuralTestCase(TestCase):
    def setUp(self):
        self.fazenda = PropriedadeRural.objects.create(
            nome='Fazenda Boa Vista',
            cidade='São Paulo',
            estado='SP',
            area_total=1000,
            area_agricultavel=600,
            area_vegetacao=300,
            culturas='Soja, Milho'
        )
        self.produtor = ProdutorRural.objects.create(
            cpf_cnpj='12345678901',
            nome='João Silva'
        )
        self.produtor.fazendas.add(self.fazenda)

    def test_produtor_rural_creation(self):
        self.assertEqual(self.produtor.nome, 'João Silva')
        self.assertEqual(self.produtor.cpf_cnpj, '12345678901')
        self.assertIn(self.fazenda, self.produtor.fazendas.all())

    def test_propriedade_rural_creation(self):
        self.assertEqual(self.fazenda.nome, 'Fazenda Boa Vista')
        self.assertEqual(self.fazenda.cidade, 'São Paulo')
        self.assertEqual(self.fazenda.estado, 'SP')
        self.assertEqual(self.fazenda.area_total, 1000)
        self.assertEqual(self.fazenda.area_agricultavel, 600)
        self.assertEqual(self.fazenda.area_vegetacao, 300)
        self.assertEqual(self.fazenda.culturas, 'Soja, Milho')