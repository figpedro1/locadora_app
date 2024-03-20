class Cliente:
    """
    Classe que representa um único cliente.

    :param cpf: CPF do cliente, formatado como XXX.XXX.XXX-XX
    :type cpf: str
    :param nome: Nome do cliente
    :type nome: str
    :param idade: Idade do cliente
    :type idade: int
    :param endereco: Endereco do cliente
    :type endereco: str
    :param cidade: Cidade do cliente
    :type cidade: str
    :param estado: Estado do cliente
    :type estado: str
    """
    __cpf: str | None = None
    __nome: str | None = None
    __idade: int | None = None
    __endereco: str | None = None
    __cidade: str | None = None
    __estado: str | None = None

    def set_cpf(self, novo_cpf: str) -> None:
        """
        Define um CPF, desde que o mesmo seja válido
        :param novo_cpf: CPF para o qual se deseja mudar
        :return: None
        :rtype: None
        """
        self.__cpf = self.formatar_cpf(novo_cpf)

    @staticmethod
    def formatar_cpf(cpf: str | int) -> str:
        """
        Formata um CPF no formato XXX.XXX.XXX-XX, garantindo que ele seja válido
        :param cpf: CPF que se deseja formatar/checar validade
        :type cpf: str | int
        :return: CPF formatado no formato XXX.XXX.XXX-XX
        :rtype: str
        """
        cpf = str(cpf).replace(".", "").replace("-", "")
        if len(cpf) != 11 or (not cpf.isnumeric()):
            raise ValueError("CPF inválido.")
        if not cpf.isnumeric():
            raise ValueError("CPF inválido")
        resto_primeira = (
                (
                        int(cpf[0]) * 10 +
                        int(cpf[1]) * 9 +
                        int(cpf[2]) * 8 +
                        int(cpf[3]) * 7 +
                        int(cpf[4]) * 6 +
                        int(cpf[5]) * 5 +
                        int(cpf[6]) * 4 +
                        int(cpf[7]) * 3 +
                        int(cpf[8]) * 2
                ) % 11
        )
        resto_segunda = (
                (
                        int(cpf[0]) * 11 +
                        int(cpf[1]) * 10 +
                        int(cpf[2]) * 9 +
                        int(cpf[3]) * 8 +
                        int(cpf[4]) * 7 +
                        int(cpf[5]) * 6 +
                        int(cpf[6]) * 5 +
                        int(cpf[7]) * 4 +
                        int(cpf[8]) * 3 +
                        int(cpf[9]) * 2
                ) % 11
        )
        if (
                (resto_primeira <= 1 and int(cpf[9]) != 0) or
                (resto_segunda <= 1 and int(cpf[10]) != 0)
        ):
            raise ValueError("CPF inválido")
        if (
                (resto_primeira > 1 and 11 - resto_primeira != int(cpf[9])) or
                (resto_segunda > 1 and 11 - resto_segunda != (cpf[10]))
        ):
            raise ValueError("CPF inválido")
        cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        return cpf

    def get_cpf(self) -> str:
        """
        Retorna o CPF
        :return: CPF
        :rtype: str
        """
        return self.__cpf

    def set_nome(self, novo_nome: str) -> None:
        """
        Define o nome do cliente
        :param novo_nome: Nome para o qual deseja ser definido
        :type novo_nome:  str
        :return: None
        :rtype: None
        """
        self.__nome = str(novo_nome)

    def get_nome(self) -> str:
        """
        Retorna o nome do cliente
        :return: Nome do cliente
        :rtype: str
        """
        return self.__nome

    def set_idade(self, nova_idade: int) -> None:
        """
        Define o idade do cliente
        :param nova_idade: Idade para a qual deve ser definida
        :return: None
        :rtype: None
        """
        nova_idade = int(nova_idade)
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self.__idade = nova_idade

    def get_idade(self) -> int:
        """
        Retorna o idade do cliente
        :return: Idade do cliente
        :rtype
        """
        return self.__idade

    def set_endereco(self, novo_endereco: str) -> None:
        self.__endereco = str(novo_endereco)

    def get_endereco(self) -> str:
        return self.__endereco

    def set_cidade(self, nova_cidade: str) -> None:
        self.__cidade = str(nova_cidade)

    def get_cidade(self) -> str:
        return self.__cidade

    def set_estado(self, novo_estado: str) -> None:
        self.__estado = str(novo_estado)

    def get_estado(self) -> str:
        return self.__estado

    def __init__(
        self,
        cpf: str,
        nome: str,
        idade: int,
        endereco: str,
        cidade: str,
        estado: str,
        vazio: bool = False
    ) -> None:
        if not vazio:
            self.set_cpf(cpf)
            self.set_nome(nome)
            self.set_idade(idade)
            self.set_endereco(endereco)
            self.set_cidade(cidade)
            self.set_estado(estado)

    def get_linha(self) -> tuple:
        return (
            self.get_cpf(),
            self.get_nome(),
            self.get_idade(),
            self.get_endereco(),
            self.get_cidade(),
            self.get_estado()
        )

    def is_valido(self) -> bool:
        if (
            self.get_cpf() is None or
            self.get_nome() is None or
            self.get_idade() is None or
            self.get_endereco() is None or
            self.get_cidade() is None or
            self.get_estado() is None
        ):
            return False
        return True
