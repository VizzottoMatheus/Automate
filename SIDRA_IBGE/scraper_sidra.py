
import pandas as pd
import dicionario_api as da

dicionarios = da.dicionarios()
culturas = da.culturas()
estados = da.estados()
variaveis = da.variaveis()



class sidra:
	""" TABELA 5457 DA API SIDRA """
	
	def show_menu(self):
		print("Argumentos: ")
		for dicionario in dicionarios:
			print("    -" + dicionario)
		print("Modelo: extrai_dados(codigo_variavel, codigo_estado, codigo_cultura)")
	def show_cultures(self):
		print("Culturas disponíveis:")
		for cultura in culturas.items():
			print(f"    ({cultura[0]}) " + cultura[1]) 

	def show_states(self):
		print("Estados:")
		for estado in estados.items():
			print(f"    ({estado[0]}) " + estado[1])

	def show_variables(self):
		print("Variáveis:")
		for variavel in variaveis.items():
			print(f"    ({variavel[0]}) " + variavel[1])

	def extrai_dados(self, variavel, estado, cultura, cod_tab = 5457):
		root = "http://api.sidra.ibge.gov.br/values/"
		link = root + "t/" + str(cod_tab) + "/p/all/v/" + str(variavel) + "/c782/" + str(cultura) + "/n6/in%20n3%20" + str(estado)
		print(link)
		df = pd.read_json(link)
		return df


agricultura = sidra()
agricultura.show_menu()
agricultura.show_cultures()
agricultura.show_states()
agricultura.show_variables()
#df = agricultura.extrai_dados(8331, 43, 40124)
#print(df.head(10))
