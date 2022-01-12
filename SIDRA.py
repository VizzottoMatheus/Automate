import pandas as pd

class sidra:
	def culturas(self):
		c = {
			0: 'Total',
			40129: 'Abacate',
			40092: 'Abacaxi*',
			45982: 'Açaí',
			40329: 'Alfafa fenada',
			40130: 'Algodão arbóreo (em caroço)',
			40099: 'Algodão herbáceo (em caroço)',
			40100: 'Alho',
			40101: 'Amendoim (em casca)',
			40102: 'Arroz (em casca)',
			40103: 'Aveia (em grão)',
			40131: 'Azeitona',
			40136: 'Banana (cacho)',
			40104: 'Batata-doce',
			40105: 'Batata-inglesa',
			40137: 'Borracha (látex coagulado)',
			40468: 'Borracha (látex líquido)',
			40138: 'Cacau (em amêndoa)',
			40139: 'Café (em grão) Total',
			40140: 'Café (em grão) Arábica',
			40141: 'Café (em grão) Canephora',
			40330: 'Caju',
			40106: 'Cana-de-açúcar',
			40331: 'Cana para forragem',
			40142: 'Caqui',
			40143: 'Castanha de caju',
			40107: 'Cebola',
			40108: 'Centeio (em grão)',
			40109: 'Cevada (em grão)',
			40144: 'Chá-da-índia (folha verde)',
			40145: 'Coco-da-baía*',
			40146: 'Dendê (cacho de coco)',
			40147: 'Erva-mate (folha verde)',
			40110: 'Ervilha (em grão)',
			40111: 'Fava (em grão)',
			40112: 'Feijão (em grão)',
			40148: 'Figo',
			40113: 'Fumo (em folha)',
			40114: 'Girassol (em grão)',
			40149: 'Goiaba',
			40150: 'Guaraná (semente)',
			40115: 'Juta (fibra)',
			40151: 'Laranja',
			40152: 'Limão',
			40116: 'Linho (semente)',
			40260: 'Maçã',
			40117: 'Malva (fibra)',
			40261: 'Mamão',
			40118: 'Mamona (baga)',
			40119: 'Mandioca',
			40262: 'Manga',
			40263: 'Maracujá',
			40264: 'Marmelo',
			40120: 'Melancia',
			40121: 'Melão',
			40122: 'Milho (em grão)',
			40265: 'Noz (fruto seco)',
			40266: 'Palmito',
			40267: 'Pera',
			40268: 'Pêssego',
			40269: 'Pimenta-do-reino',
			40123: 'Rami (fibra)',
			40270: 'Sisal ou agave (fibra)',
			40124: 'Soja (em grão)',
			40125: 'Sorgo (em grão)',
			40271: 'Tangerina',
			40126: 'Tomate',
			40127: 'Trigo (em grão)',
			40128: 'Triticale (em grão)',
			40272: 'Tungue (fruto seco)',
			40273: 'Urucum (semente)',
			40274: 'Uva'
			}
		print(c)

	def estados(self):
		e = {
			12: 'Acre',
			27: 'Alagoas',
			16: 'Amapá',
			13: 'Amazonas',
			29: 'Bahia',
			23: 'Ceará',
			53: 'Distrito Federal',
			32: 'Espírito Santo',
			52: 'Goiás',
			21: 'Maranhão',
			51: 'Mato Grosso',
			50: 'Mato Grosso do Sul',
			31: 'Minas Gerais',
			15: 'Pará',
			25: 'Paraíba',
			41: 'Paraná',
			26: 'Pernambuco',
			22: 'Piauí',
			33: 'Rio de Janeiro',
			24: 'Rio Grande do Norte',
			43: 'Rio Grande do Sul',
			11: 'Rondônia',
			14: 'Roraima'
			}

		print(e)

	def variaveis(self):
		v = {
			8331: 'Área plantada ou destinada à colheita',
			1008331: 'Área plantada ou destinada à colheita - percentual do total geral (%)',
			216: 'Área colhida (Hectares)',
			1000216: 'Área colhida - percentual do total geral (%)',
			214: 'Quantidade produzida (Toneladas)',
			112: 'Rendimento médio da produção',
			215: 'Valor da produção (mil reais)',
			1000215: 'Valor da produção - percentual do total geral (%)'
			}

		print(v)

	def extrai_sidra(self, cod_tab, variavel, estado, cultura):
		root = "http://api.sidra.ibge.gov.br/values/"
		link = root + "t/" + str(cod_tab) + "/p/all/v/" + str(variavel) + "/c782/" + str(cultura) + "/n6/in%20n3%20" + str(estado)
		print(link)
		df = pd.read_json(link)
		print(df.head())


agricultura = sidra()
agricultura.culturas()
agricultura.estados()
agricultura.variaveis()
agricultura.extrai_sidra(5457, 8331, 43, 40124)





