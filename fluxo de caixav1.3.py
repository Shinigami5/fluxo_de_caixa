import datetime 
import os.path

class valoresDia :
    def __init__ (self,v1=None,v2=None,v3=None,v4=None,v5=None,v6=None,v7=None,v8=None,v9=None,v10=None,v11=None):
        self.saldoNoDia = v1
        self.Salario = v2
        self.outros = v3
        self.mercado = v4
        self.ContaDeLuz = v5
        self.ContaDeAgua = v6
        self.OutrasContas = v7
        self.TelefoneInternet = v8
        self.aluguel = v9
        self.imposto = v10
        self.OutrasDespesas = v11

class fluxo :
    def __init__ (self,saldo,cod,data=None) :
        self.saldo = saldo
        self.cod = cod
        self.data = data
        self.valoresDia = valoresDia

    def depositoSaldo(self,saldo):
        self.saldo += saldo

    def saquerSaldo(self,saldo):
        self.saldo -= saldo

    def setValorDia(self,Vdia):
        self.valoresDia = Vdia

    def setData(self,data):
        self.data = data

class main:
    def __init__ (self):
        self.listF = []
        self.listB = []

    def inicia(self):
        m = SalvaArq()
        self.listF = m.getValues()
        del m
        print('Movimento de caixa')
        var = 1
        while(var):
            print('\n')
            print('1-inicial novo movimento de caixa')
            print('2-abir um movimento de caixa')
            print('3-sair')
            op=self.option()
            if (op == 1) :
                F=self.newF()
                self.dc(F)        
            if (op == 2):
                while(1):
                    print('\n')
                    print('1-abir movimento por codigo')
                    print('2-abir movimento por data')
                    print('3-ver todos os codigos de movimento cadastrado')
                    print('4-volta')
                    num=self.option()
                    if (num == 1):
                        dis=int(input('digite o codigo do movimento: '))
                        for i in range(len(self.listF)):
                            if (self.listF[i].cod == dis):
                                self.VisualizarFluxo(dis)
                    if (num == 2):
                        ano = int(input('digite o ano: '))
                        mes = int(input('digite o mes: '))
                        dia = int(input('digite o dia: '))
                        date = datetime.date(ano,mes,dia)
                        for i in range(len(self.listF)):
                            if (self.listF[i].data == date):
                                self.VisualizarFluxo(self.listF[i].cod)
                                                     
                    if (num == 3):
                        for i in range(len(self.listF)):
                            print('cod N.', i+1 ,' :', self.listF[i].cod )
                        if (len(self.listF) == 0):
                            print('nao existe nenhum movimento cadastrado')
                    if (num == 4):
                        break
            
            if (op == 3) :
                end = SalvaArq(self.listB)
                end.setValues()
                var = 0
                print('saindo')
            if (op == 4):
                print('valor invalido !')

    def option(self) :
        tr = 1
        while (tr):
            option = int(input('escolha uma opcao: '))
            if (option == 1) :
                return option
            if (option == 2) :
                return option
            if (option == 3 or option == 4):
                return option
            else :
                print('valor invalido !')

    def newF(self):
        sal = float(input('insira o saldo inicial do dia: '))
        cod = int(input('insira o codigo do fluxo do dia: '))
        dia = int(input('agora insira o dia do movimento: '))
        mes = int(input('insira o mes: '))
        ano = int(input('insira o ano: '))
        data = datetime.date(ano,mes,dia)
        Fluxo = fluxo(sal,cod,data)
        return Fluxo

    def dc(self,F) :
        self.Mcampos()
        saldoDoDia = F.saldo
        
        print('\n' * 5)
        print('digite os campos')
        print('     Saldo inicial     ')
        print('saldo atual %.2f' % saldoDoDia)
        ces = float(input('digite o/campo salario do mes: '))
        ceo = float(input('digite o/campo outros: '))
        print('     Despesas     ')
        csm =  float(input('digite o/campo mercado: '))
        csl =  float(input('digite o/campo conta de luz: '))
        csagua =  float(input('digite o/campo conta de agua: '))
        csc =  float(input('digite o/campo outras contas: '))
        csti = float(input('digite o/campo telefone e internet: '))
        csa =  float(input('digite o/campo aluguel: '))
        csi =  float(input('digite o/campo imposto: '))
        cso =  float(input('digite o/campo outras despesas: '))

        total_entrada = (ces + ceo)
        #print('total entrada: %.2f' % total_entrada)
        total_Saida = (csm + csl + csagua + csc + csti + csa + csi + cso)
        #print('total saida: %.2f' % total_Saida)
        saldo_final = total_entrada - total_Saida
        #print('total final: %.2f' % saldo_final)
        F.depositoSaldo(total_entrada)
        F.saquerSaldo(total_Saida)

        saldo_final += saldoDoDia
        #print('total final: %.2f' % saldo_final)
        x = valoresDia(saldoDoDia,ces,ceo,csm,csl,csagua,csc,csti,csa,csi,cso)
        F.setValorDia(x)
        self.listF.append(F)
        self.listB.append(F)

        print('o valor de saldo %.2f' % F.saldo)
        print('\n')

    def Mcampos(self):
        print('\n' * 20)
        print('digite os campos')
        print('     Saldo inicial     ')
        print('saldo atual --')
        print('salario do mes --')
        print('outros --')
        print('\n')
        print('     Despesas     ')
        print('mercado --')
        print('conta de luz --')
        print('conta de agua --')
        print('outras contas --')
        print('telefone e internet --')
        print('aluguel --')
        print('imposto --')
        print('outras despesas --')

    def VisualizarFluxo(self,num):
        for i in range(len(self.listF)):
            if (self.listF[i].cod == num):
                dataTexto = '{}/{}/{}' .format(self.listF[i].data.day, self.listF[i].data.month  ,self.listF[i].data.year)
                print('\n')
                print('--------dados do movimento-------')
                print('codigo do movimento: %d' % self.listF[i].cod)
                print('data do movimento: %s' % dataTexto)
                print('----------entradas-----------')
                print('saldo do dia: R$%.2f' % self.listF[i].valoresDia.saldoNoDia)
                print('salario: R$%.2f' % self.listF[i].valoresDia.Salario)
                print('outros: R$%.2f' % self.listF[i].valoresDia.outros)
                print('-----------Despesas----------')
                print('mercado: R$%.2f' % self.listF[i].valoresDia.mercado)
                print('Conta de luz: R$%.2f' % self.listF[i].valoresDia.ContaDeLuz)
                print('Conta de agua: R$%.2f' % self.listF[i].valoresDia.ContaDeAgua)
                print('Outras contas: R$%.2f' % self.listF[i].valoresDia.OutrasContas)
                print('Telefone e internet: R$%.2f' % self.listF[i].valoresDia.TelefoneInternet)
                print('Aluguel: R$%.2f' % self.listF[i].valoresDia.aluguel)
                print('Imposto: R$%.2f' % self.listF[i].valoresDia.imposto)
                print('Outras despesas: R$%.2f' % self.listF[i].valoresDia.OutrasDespesas)
                print('----saldo ao final do dia----')
                print('saldo ao final do dia: R$%.2f' % self.listF[i].saldo)

class SalvaArq():
    def __init__(self,lista=None):
        self.listArq = lista
        self.varCod = ''
        self.varDia = ''
        self.varMes = ''
        self.varAno = ''
        self.varSaldo = ''
        self.varV1 = ''
        self.varV2 = ''
        self.varV3 = ''
        self.varV4 = ''
        self.varV5 = ''
        self.varV6 = ''
        self.varV7 = ''
        self.varV8 = ''
        self.varV9 = ''
        self.varV10 = ''
        self.varV11 = ''

    def setValues(self):
        x = open('mov.txt','a')
        for i in range(0,len(self.listArq)):
            fileString = ''
            self.varCod = str(self.listArq[i].cod)
            self.varDia = str(self.listArq[i].data.day)
            self.varMes = str(self.listArq[i].data.month)
            self.varAno = str(self.listArq[i].data.year)
            self.varV1 = str(self.listArq[i].valoresDia.saldoNoDia)
            self.varV2 = str(self.listArq[i].valoresDia.Salario)
            self.varV3 = str(self.listArq[i].valoresDia.outros)
            self.varV4 = str(self.listArq[i].valoresDia.mercado)
            self.varV5 = str(self.listArq[i].valoresDia.ContaDeLuz)
            self.varV6 = str(self.listArq[i].valoresDia.ContaDeAgua)
            self.varV7 = str(self.listArq[i].valoresDia.OutrasContas)
            self.varV8 = str(self.listArq[i].valoresDia.TelefoneInternet)
            self.varV9 = str(self.listArq[i].valoresDia.aluguel)
            self.varV10 = str(self.listArq[i].valoresDia.imposto)
            self.varV11= str(self.listArq[i].valoresDia.OutrasDespesas)
            self.varSaldo = str(self.listArq[i].saldo)

            fileString += self.varCod + ' ' + self.varDia + ' ' + self.varMes + ' ' + self.varAno + ' ' + self.varV1 + ' ' + self.varV2 + ' '
            fileString += self.varV3 + ' ' + self.varV4 + ' ' + self.varV5 + ' ' + self.varV6+ ' ' + self.varV7 + ' ' + self.varV8 + ' ' + self.varV9 + ' '
            fileString += self.varV10 + ' ' + self.varV11 + ' ' + self.varSaldo + ' \n'
            #print(fileString)
            x.write(fileString)
        x.close()

    def getValues(self):
        listR = []
        if (os.path.isfile('mov.txt') == False):
            return listR
        else:
            x = open('mov.txt','r')
            tem = x.readlines()
            ln = len(tem)
            tem.clear()
            x.seek(0)

            fileString = ''
            for i in range(0,ln):
                listTem = fluxo(0,0)
                diaA = valoresDia()
                line = x.readline()
                cot = 0
                var = ''
                ano = 0
                dia = 0
                mes = 0
                for g in range(0,len(line)):
                    if (line[g] == ' '):
                        cot += 1
                        if (cot == 1):
                            listTem.cod = int(var)
                            var = ''
                        elif (cot == 2):
                            dia = int(var)
                            var = ''
                        elif (cot == 3):
                            mes = int(var)
                            var = ''
                        elif (cot == 4):
                            ano = int(var)
                            var = ''
                        elif (cot == 5):
                            diaA.saldoNoDia = float(var)
                            var = ''
                        elif (cot == 6):
                            diaA.Salario = float(var)
                            var = ''
                        elif (cot == 7):
                            diaA.outros = float(var)
                            var = ''
                        elif (cot == 8):
                            diaA.mercado = float(var)
                            var = ''
                        elif (cot == 9):
                            diaA.ContaDeLuz = float(var)
                            var = ''
                        elif (cot == 10):
                            diaA.ContaDeAgua = float(var)
                            var = ''
                        elif (cot == 11):
                            diaA.OutrasContas = float(var)
                            var = ''
                        elif (cot == 12):
                            diaA.TelefoneInternet = float(var)
                            var = ''
                        elif (cot == 13):
                            diaA.aluguel = float(var)
                            var = ''
                        elif (cot == 14):
                            diaA.imposto = float(var)
                            var = ''
                        elif (cot == 15):
                            diaA.OutrasDespesas = float(var)
                            var = ''
                        elif (cot == 16):
                            listTem.saldo = float(var)
                            var = ''
                    else:
                        var = var + line[g]
                r=datetime.date(ano,mes,dia)
                listTem.setData(r)
                listTem.setValorDia(diaA)
                listR.append(listTem)
                del listTem
                del diaA
            
            x.close()
            return listR
            
m = main()
m.inicia()



