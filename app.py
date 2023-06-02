class App:
    def __init__(self):
        # Initializes the App class
        App.title("The shape of us!")
        print()
        print("=> Informe alguns dados para começar: ")
        print()
        App.generate_header()

    @classmethod
    def padding(cls):
        # Adds padding between sections in the output
        print()
        print()

    @classmethod
    def generate_header(cls):
        # Generates the header for user input
        print("OBS: O Nivel de atividade varia de 1 (Sedentário) a 4 (Muito Ativo) !")
        print("Ex: {:^8s} {:^22s} {:^14s} {:^20s} {:^10s} ".format("1.70", "70.0", "M", "3", "20"))
        print()

    @classmethod
    def print_row(cls):
        # Prints a row of asterisks as a separator
        print('*' * 81)

    @classmethod
    def print_row_table(cls):
        # Prints a row of dashes for table formatting
        print(f"+{'-' * 25}++{'-' * 25}++{'-' * 25}+")

    @classmethod
    def title(cls, title):
        # Prints a title surrounded by asterisks
        App.print_row()
        print('*{:^79s}*'.format(title))
        App.print_row()

    @classmethod
    def collect_user_data(cls):
        # Collects user input for height, weight, sex, activity level, and age
        print("{:^16s}".format("Altura (m):"), end="")
        print("{:^18s}".format("Peso (Kg):"), end="")
        print("{:^18s}".format("Sexo (M/F):"), end="")
        print("{:^18s}".format("Nvl de Ativ:"), end="")
        print("{:^16s}".format("Idade :"))

        user_data = input("")
        user_data = user_data.split(" ")
        print()
        App.print_row()

        return user_data

    @classmethod
    def list_user_data(cls, values):
        # Creates a list of user data, excluding empty values
        data_list = []
        for i in values:
            if i != "":
                if i in "Mm" or i in "Ff":
                    data_list.append(i)
                else:
                    data_list.append(float(i))
        return data_list

    @classmethod
    def validate_data(cls, values):
        # Validates user input and handles exceptions
        while True:
            try:
                data_list = App.list_user_data(values)
                user_data = App.generate_dict(data_list)

            except IndexError:
                print()
                print('Preencha todos os dados para prosseguir!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()

            except ValueError:
                print()
                print('Valor inválido!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()

            else:
                data_list = App.list_user_data(values)
                break

        return data_list

    @classmethod
    def generate_dict(cls, data_list):
        # Generates a dictionary from the user data
        data_dict = {'altura': None, 'peso': None, 'sexo': None, 'nvlAtiv': None, 'idade': None}
        cont = 0
        for k, v in data_dict.items():
            data_dict[k] = data_list[cont]
            cont += 1

        return data_dict

    @classmethod
    def print_result(cls, data_list):
        # Prints the result row with user data
        print()
        App.print_row()
        print('|{:^25s}||{:^25s}||{:^25s}|'.format(str(data_list[0][0]), str(data_list[0][1]), str(data_list[0][2])))
        App.print_row()

    @classmethod
    def create_table_imc(cls, imc, status):
        # Creates a table with content about the Body Mass Index (IMC) and prints it
        content = [['Tabela de IMC', 'Intervalo', ' Status'],
                   ['Menos do que: ', '18,5', 'Abaixo do Peso !'],
                   ['Entre: ', '18,5 e 24,9', 'Peso Normal!'],
                   ['Entre: ', '25,0 e 29,9', 'Sobrepeso!'],
                   ['Entre: ', '30,0 e 34,9', 'Obesidade Grau 1!'],
                   ['Entre: ', '35,0 e 39,9', 'Obesidade Grau 2!'],
                   ['Mais do que: ', '40,0', 'Obesidade Grau 3!']]

        result = [['SEU IMC: ', str(imc), status]]
        print()
        for print_row in range(0, len(content)):
            App.print_row_table()
            print('|{:^25s}||{:^25s}||{:^25s}|'.format(content[print_row][0], content[print_row][1],
                                                       content[print_row][2]))
            if print_row == 6:
                App.print_row_table()
                App.print_result(result)

    @classmethod
    def create_table_qtd_cal(cls, data_dict):
        # Creates a table with content about the quantity of calories for macronutrients and prints it
        content = [
            ["Carboidratos: ", data_dict["carboidratos"], round(float((data_dict["carboidratos"])) / 4.0, 2)],
            ["Proteínas: ", data_dict["proteinas"], round(float((data_dict["proteinas"])) / 4.0, 2)],
            ["Gorduras", data_dict["gorduras"], round(float((data_dict["gorduras"])) / 9.0, 2)]
        ]

        for print_row in range(0, len(content)):
            App.print_row_table()
            print('|{:^25}||{:^25}||{:^25}|'.format(str(content[print_row][0]), str(content[print_row][1]) + " kcal",
                                                    str(content[print_row][2]) + " g"))
            App.print_row_table()

    @classmethod
    def menu(cls, response):
        # Main menu for the application
        while True:
            App.padding()
            print("=> Selecione uma opção: ")
            print()
            print('{:^16s}{:^18s}{:^18s}{:^18s}{:2s}'.format("1 - IMC", "2 - TMB", "3 -  QTD KCAL", "4 - SAIR", ""),
                  end="\t")
            opt = input()
            App.padding()

            if opt == "1":
                # Option 1: IMC calculation
                App.title("IMC")
                print()
                print("{:^81s}".format("O Indice de Massa Corporal (IMC) é um parâmetro"))
                print("{:^81s}".format("utilizado para saber se o peso está de acordo com a altura de um"))
                print(
                    "{:^81s}".format("indivíduo, o que pode interferir diretamente na sua saúde e qualidade de vida!"))
                App.create_table_imc(response["imc"], response["statusImc"])

            elif opt == "2":
                # Option 2: TMB calculation
                App.title("Taxa Metabólica Basal: ")
                print()
                print("{:^81s}".format("A Taxa de Metabolismo Basal (TMB) é a quantidade"))
                print("{:^81s}".format("mínima de energia (calorias) necessária para manter as"))
                print("{:^81s}".format("funções vitais do organismo em repouso. Essa taxa pode variar"))
                print("{:^81s}".format("de acordo com o sexo, peso, altura, idade e nível de atividade física."))

                result = [['RESULTADO :', 'SUA TMB:', str(response['tmb']) + " kcal"]]
                App.print_result(result)

            elif opt == "3":
                # Option 3: Quantity of calories calculation
                nut = response["nutrientes"]
                App.title("Quantidade de Calorias: ")
                print()
                print("{:^81s}".format("Calorias são a quantidade de energia que um determinado alimento"))
                print("{:^81s}".format("fornece após ser consumido, contribuindo para as funções essenciais do"))
                print(
                    "{:^81s}".format("organismo, como respiração, produção de hormônios, e funcionamento do cérebro."))

                print()
                print("{:^81s}".format("Você deve consumir aproximadamente: "))
                print()
                App.create_table_qtd_cal(nut)

                result = [['RESULTADO :', 'SUA QTD DE KCAL:', str(response['cal']) + " kcal"]]
                App.print_result(result)

            elif opt == "4":
                # Option 4: Exit the application
                print('{:^79s}'.format("Obrigado por usar nosso App !"))
                App.padding()
                App.print_row()
                break

            else:
                print("Erro: Opção Inválida!")
