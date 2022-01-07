import discord
import json
import requests
import os
from typing import Text
from discord.ext import commands

client = commands.Bot(command_prefix=".", case_insensitive=False, help_command=None)


@client.event
async def on_ready():
    activity = discord.Game(name='Digite .ajuda 👽', type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Conectando, por favor, aguarde...")


@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)


@client.command()
async def consulta(ctx):
    
    embed = discord.Embed(
        title='',
        description='',
        colour=16766976
    )

    embed.add_field(name="🕵🏻‍♂️ 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗡𝗢𝗠𝗘",
                    value="Use o comando ***a!nome*** {Nome Completo} para realizar a consulta.", inline=False)
    embed.add_field(name="👽 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗖𝗣𝗙",
                    value="Use o comando ***a!cpf*** {CPF da Pessoa} para a consultar os dados.", inline=False)
    embed.add_field(name="📵 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗧𝗘𝗟𝗘𝗙𝗢𝗡𝗘",
                    value="Use o comando ***a!telefone*** {Telefone} para realizar a consulta.", inline=False)
    embed.add_field(name="🏨 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗖𝗡𝗣𝗝",
                    value="Use o comando ***a!cnpj*** {CNPJ} para consultar os dados.", inline=False)
    embed.add_field(name="🚘 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗣𝗟𝗔𝗖𝗔",
                    value="Use o comando ***/placa*** {Placa do veículo} para realizar a consulta.", inline=False)
    embed.add_field(name="📌 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗜𝗣",
                    value="Use o comando ***a!ip*** {IP} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💳 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗕𝗜𝗡",
                    value="Use o comando ***a!bin*** {Número da BIN} para realizar a consulta.", inline=False)
    embed.add_field(name="📫 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗖𝗘𝗣",
                    value="Use o comando ***a!cep*** {CEP da Rua} para realizar a consulta.", inline=False)
    embed.add_field(name="🦠 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗖𝗢𝗩𝗜𝗗",
                    value="Use o comando ***a!covid*** {Sigla do Estado} para realizar a consulta.", inline=False)
    embed.add_field(name="🏦 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗕𝗔𝗡𝗖𝗢",
                    value="Use o comando ***a!banco*** {Código do Banco} para realizar a consulta.", inline=False)
    embed.add_field(name="💾 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗦𝗜𝗧𝗘",
                    value="Use o comando ***a!site*** {URL do site} para realizar a consulta.", inline=False)
    embed.add_field(name="💰 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗠𝗢𝗘𝗗𝗔",
                    value="Use o comando ***a!moeda*** ex:{USD/BRL} para realizar a consulta.", inline=False)
    embed.set_image(url='https://i.gifer.com/Cewn.gif')
    embed.set_author(name='ALIEN.py', icon_url='https://i.imgur.com/3GksSgz.png')
    embed.set_footer(text='ALIEN.py © All Rights Reserved', icon_url='https://i.imgur.com/Pn0zQ5S.jpg')

    await ctx.send(embed=embed)


#################################################################################################################################

@client.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title='',
        description='',
        colour=16766208
    )

    embed.add_field(name="🔐 Moderação", value='Use o comando `/admin` para ver os comandos administrativos. Comando de moderação existentes: `/kick`, `/ban`, `unban`, `/unmute`, `/role`, `/mute`, `/clear` ', inline=False)
    embed.add_field(name="🔍 Consultas", value='Use o comando `/consulta` para obter mais informações. Comandos de consultas disponíveis: `/nome`, `/cpf`, `/telefone`, `/cnpj`, `/placa`, `/ip` `/bin`, `/cep`, `/covid`, `/banco`, `/site`', inline=False)
    embed.add_field(name="🎵 Músicas", value='Use o comando `/musica` para vizualizar os comandos. Comandos acessíveis a classe: `/play`, `/stop`, `/pause`, `/resume`, `/back/`, `/skip`, `/disconnect`', inline=False)
    embed.add_field(name="🪐 Informações", value='Use o comando `/info` para ver os comandos disponíveis. Comandos existentes: `/ajuda`, `/ping`, `/git`, `/serverinfo`, `/userinfo`', inline=False)
    embed.add_field(name="🉐 Tradutor", value='Use o comando `/traduzir` "Texto" Língua (Exemplo: en, es, pt, ru)', inline=False)

    embed.set_author(name='🔮 Artic Helper', icon_url='')

    await ctx.author.send(embed=embed); 

@client.command()
async def nome(ctx):
    
    embed = discord.Embed(
        title='',
        description='USE O COMANDO /nome {nome da pessoa} para consultar',
        colour=3386077
    )

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


##CONSULTA DE CPF

@client.command()
async def cpf(ctx):
    
    embed = discord.Embed(
        title='',
        description='A Consulta por ***CPF*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***CPF!***',
        colour=13874766
    )

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPF', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


##TELEFONE

@client.command()
async def telefone(ctx):
    
    embed = discord.Embed(
        title='',
        description='A Consulta por ***TELEFONE*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***telefone!***',
        colour=6084221
    )

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONE', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


##PLACA

@client.command()
async def placa(ctx):
    
    embed = discord.Embed(
        title='',
        description='A Consulta por ***PLACA*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***placa!***',
        colour=3556561
    )

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACA', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##CONSULTA DE CNPJ

@client.command()
async def cnpj(ctx, cnpj):
    
    data = requests.get(f"https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}").json()
    print()
    try:
        embed = discord.Embed(
            title='',
            colour=16766976
        )
        
        embed.add_field(name="➢ CNPJ", value=data['CNPJ'], inline=False)
        embed.add_field(name="➢ Nome Fantasia", value=data['NOME FANTASIA'], inline=False)
        embed.add_field(name="➢ Razão Social", value=data['RAZAO SOCIAL'], inline=False)
        embed.add_field(name="➢ Status", value=data['STATUS'], inline=False)
        embed.add_field(name="➢ UF", value=data['UF'], inline=False)
        embed.add_field(name="➢ Bairro", value=data['BAIRRO'], inline=False)
        embed.add_field(name="➢ Número", value=data['NUMERO'], inline=False)
        embed.add_field(name="➢ Município", value=data['MUNICIPIO'], inline=False)
        embed.add_field(name="➢ Abertura", value=data['DATA ABERTURA'], inline=False)
        embed.add_field(name="➢ DDD", value=data['DDD'], inline=False)
        embed.add_field(name="➢ Telefone", value=data['TELEFONE'], inline=False)
        embed.add_field(name="➢ CNAE", value=data['CNAE PRINCIPAL DESCRICAO'], inline=False)
        embed.add_field(name="➢ CNAE Código", value=data['CNAE PRINCIPAL CODIGO'], inline=False)
        embed.add_field(name="➢ CNAE Código", value=data['COMPLEMENTO'], inline=False)
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJ ', icon_url='https://cdn-icons.flaticon.com/png/512/4151/premium/4151858.png?token=exp=1641266909~hmac=2cddb88d70dc89e429a8175901424a57')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=16766976
    )

    embed.add_field(name="COM DIFICULDADES?", value='TESTANDO', inline=False)

    await ctx.send(embed=embed)

##CONSULTA DE IP

@client.command()
async def ip(ctx, ip):
    
    data = requests.get(f"http://ipwhois.app/json/{ip}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ IP NÃO ENCONTRADO ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=10441
    )

    embed.add_field(name="➢ IP", value=data['ip'], inline=False)
    embed.add_field(name="➢ Cidade", value=data['city'], inline=False)
    embed.add_field(name="➢ Estado", value=data['region'], inline=False)
    embed.add_field(name="➢ País", value=data['country'], inline=False)
    embed.add_field(name="➢ Latitude", value=data['latitude'], inline=False)
    embed.add_field(name="➢ Longitude", value=data['longitude'], inline=False)
    embed.add_field(name="➢ Provedor", value=data['isp'], inline=False)
    embed.add_field(name="➢ Empresa Responsável", value=data['org'], inline=False)
    embed.add_field(name="➢ Tipo de Conexão", value=data['type'], inline=False)
    embed.set_author(name='ㅤﾠㅤ   CONSULTA DE IP', icon_url='https://cdn-icons-png.flaticon.com/512/6434/6434897.png')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=data['country_flag'])

    await ctx.send(embed=embed)

##CONSULTA DE COVID19

@client.command()
async def covid(ctx, covid):
    
    data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

    try:
        error = data["error"]
        embed = discord.Embed(
            title='⚠️ ESTADO NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=13841202
    )

    embed.add_field(name="➢ Estado", value=data['state'], inline=False)
    embed.add_field(name="➢ Casos", value=data['cases'], inline=False)
    embed.add_field(name="➢ Mortes", value=data['deaths'], inline=False)
    embed.add_field(name="➢ Suspeitos", value=data['suspects'], inline=False)
    embed.add_field(name="➢ Descartados", value=data['refuses'], inline=False)
    embed.add_field(name="➢ Atualização", value=data['datetime'], inline=False)
    embed.set_author(name='ㅤCONSULTA DE COVID19ㅤㅤㅤ', icon_url='https://cdn-icons.flaticon.com/png/512/5428/premium/5428573.png?token=exp=1641268025~hmac=fb2ee7ad00ddbf8a5a1cf67a15f04945')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##CONSULTA DE CEP

@client.command()
async def cep(ctx, cep):
    
    data = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ CEP NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=4236377
    )

    embed.add_field(name="➢ CEP", value=data['cep'], inline=False)
    embed.add_field(name="➢ Rua", value=data['address'], inline=False)
    embed.add_field(name="➢ Bairro", value=data['district'], inline=False)
    embed.add_field(name="➢ Cidade", value=data['city'], inline=False)
    embed.add_field(name="➢ Estado", value=data['state'], inline=False)
    embed.add_field(name="➢ Logradouro", value=data['address_name'], inline=False)
    embed.add_field(name="➢ Latitude", value=data['lat'], inline=False)
    embed.add_field(name="➢ Longitude", value=data['lng'], inline=False)
    embed.add_field(name="➢ IBGE", value=data['city_ibge'], inline=False)
    embed.add_field(name="➢ DDD", value=data['ddd'], inline=False)
    embed.set_author(name='ㅤㅤCONSULTA DE CEPㅤㅤㅤㅤ', icon_url='https://cdn-icons-png.flaticon.com/512/2642/2642502.png')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##CONSULTA CÓDIGO BANCÁRIO

@client.command()
async def banco(ctx, banco):
    
    data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ CÓDIGO BANCÁRIO NÃO ENCONTRADO ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=7667888
    )

    embed.add_field(name="➢ ISPB", value=data['ispb'], inline=False)
    embed.add_field(name="➢ Nome do Banco", value=data['name'], inline=False)
    embed.add_field(name="➢ Código Bancário", value=data['code'], inline=False)
    embed.add_field(name="➢ Informações Adicionais", value=data['fullName'], inline=False)
    embed.set_author(name='ㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤ', icon_url='https://cdn-icons.flaticon.com/png/512/1041/premium/1041584.png?token=exp=1641266545~hmac=506f329c4c0c70a61d42fe5f4abea701')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##CONSULTA DE BIN

@client.command()
async def bin(ctx, bin):
    
    data = requests.get(
        f"https://api.bincodes.com/bin/?format=json&api_key=c0107d14acda7e1831dfe26ee8e8b3a5&bin={bin}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ BIN NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

    embed = discord.Embed(
        title='',
        colour=16711701
    )

    embed.add_field(name="➢ BIN", value=data['bin'], inline=False)
    embed.add_field(name="➢ Modelo", value=data['type'], inline=False)
    embed.add_field(name="➢ Nível", value=data['level'], inline=False)
    embed.add_field(name="➢ Bandeira", value=data['card'], inline=False)
    embed.add_field(name="➢ País", value=data['country'], inline=False)
    embed.add_field(name="➢ Sigla do País", value=data['countrycode'], inline=False)
    embed.add_field(name="➢ Banco", value=data['bank'], inline=False)
    embed.set_author(name='ㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤ', icon_url='https://i.imgur.com/U18eyhV.png')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##CONSULTA DE SITE

@client.command()
async def site(ctx, site):
    
    embed = discord.Embed(
        title='',
        colour=58879
    )

    embed.add_field(name="➢ IP", value=data['ip'], inline=False)
    embed.add_field(name="➢ Cidade", value=data['city'], inline=False)
    embed.add_field(name="➢ Estado", value=data['region'], inline=False)
    embed.add_field(name="➢ País", value=data['country'], inline=False)
    embed.add_field(name="➢ Latitude", value=data['latitude'], inline=False)
    embed.add_field(name="➢ Longitude", value=data['longitude'], inline=False)
    embed.add_field(name="➢ Organização", value=data['isp'], inline=False)
    embed.add_field(name="➢ Empresa", value=data['org'], inline=False)
    embed.add_field(name="➢ Fuso Horário", value=data['timezone'], inline=False)
    embed.set_author(name='USE ')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##GERADORES
    
@client.command()
async def gerador(ctx):
    
    embed = discord.Embed(
        title='',
        description='',
        colour=6356774
    )

    embed.add_field(name="👥 GERADOR DE PESSOA", value="Use o comando ***a!gerarpessoa*** para gerar uma pessoa.",
                    inline=False)
    embed.add_field(name="💳 GERADOR DE CARTÃO",
                    value="Use o comando ***a!gerarcartao*** para gerar um cartão Debito/Crédito.", inline=False)
    embed.add_field(name="📁 GERADOR DE E-MAIL",
                    value="Use o comando ***a!geraremail*** para gerar um e-mail aleatório.", inline=False)
    embed.add_field(name="🔆 GERADOR DE CPF", value="Use o comando ***a!gerarcpf*** para gerar e validar um CPF.",
                    inline=False)
    embed.add_field(name="🎮 GERADOR DE USERNAME", value="Use o comando ***a!gerarusr*** para gerar um username.",
                    inline=False)
    embed.add_field(name="🔐 GERADOR DE SENHA", value="Use o comando ***a!gerarsenha*** para gerar uma senha.",
                    inline=False)
    embed.add_field(name="🚙 GERADOR DE VEÍCULO", value="Use o comando ***a!gerarveiculo*** para gerar um veículo.",
                    inline=False)
    embed.add_field(name="📞 GERADOR DE NÚMERO TELEFONE",
                    value="Use o comando ***a!gerartel*** para gerar um telefone.", inline=False)
    embed.add_field(name="📲 GERADOR DE IMEI", value="Use o comando ***a!gerarimei*** para gerar um IMEI.",
                    inline=False)
    embed.set_image(url='')
    embed.set_author(name='ALIEN.py', icon_url='https://cdn-icons-png.flaticon.com/512/6498/6498012.png')
    embed.set_footer(text='ALIEN.py © All Rights Reserved', icon_url='https://i.imgur.com/Pn0zQ5S.jpg')

    await ctx.send(embed=embed)

##INFOBOT    
    
@client.command()
async def infobot(ctx):
    
    embed = discord.Embed(
        title='SOBRE O ALIEN.py',
        description='O BOT **ALIEN.py** é um robô multifuncional equipado com comandos de moderação, consultas, checkers etc. Atualmente, encontra-se em versão beta!',
        colour=13107455
    )

    embed.set_author(name='ALIEN.py', icon_url='https://thumbs.gfycat.com/PlayfulCandidCalf-max-1mb.gif')
    embed.set_image(url='https://media.giphy.com/media/XTFDgzeOD0lzD449d8/giphy.gif')
    embed.add_field(name="🐍 𝐋𝐈𝐍𝐆𝐔𝐀𝐆𝐄𝐌",
                    value="O ***ALIEN.py*** foi criado inteiramente na linguagem ***[𝐏𝐘𝐓𝐇𝐎𝐍]***", inline=False)
    embed.add_field(name="🤖 𝐒𝐔𝐆𝐄𝐒𝐓𝐎𝐄𝐒",
                    value="Quer reportar um Bug ou fazer alguma indicação de melhoria? Digite ***a!sugestao*** para ver os meios de contato.",
                    inline=False)
    embed.set_footer(text='ALIEN.py © All Rights Reserved', icon_url='https://i.imgur.com/Pn0zQ5S.jpg')

    await ctx.send(embed=embed)

##FERRAMENTE PARA TESTAR PING    
    
@client.command()
async def ping(ctx):
    
    embed = discord.Embed(
        title='',
        colour=29695
    )

    embed.add_field(name='➢ Ping do usuário', value=f"{round(client.latency * 500)} ms", inline=False)
    embed.add_field(name='➢ Ping do servidor', value=f"{round(client.latency * 1000)} ms", inline=False)
    embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='https://cdn-icons-png.flaticon.com/512/2695/2695903.png')
    embed.set_image(url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

##SUGESTÕES DE MELHORIAS    
    
@client.command()
async def sugestao(ctx):
    
    embed = discord.Embed(
        title='DÚVIDAS / SUGESTÕES', url="",
        description='Ficou com alguma dúvida? gostaria de dar sugestões ou até mesmo fazer críticas ***construtivas***? Ficaremos extremamente feliz em poder ouvi-los! Estamos sempre trabalhando em atualizações futuras para poder trazer as melhores experiências para os usuários.\n',
        colour=6646071
    )

    embed.set_author(name='ALIEN.py', icon_url='')
    embed.set_image(url='https://i.imgur.com/Pn0zQ5S.jpg')
    embed.add_field(name="INSTAGRAM", value="@alien.pipy", inline=False)
    embed.add_field(name="E-MAIL", value="alien.py@protonmail.com", inline=False)
    embed.add_field(name="APOIE MEU TRABALHO  💚", value="Chave PIX: d1651eb8-4c84-4b2b-b60a-9e3884cea92d",
                    inline=False)
    
    await ctx.send(embed=embed)

#--------------------------------------------------------[TRADUÇÃO]-------------------------------------------------------------#

@client.command() #TRADUÇÃO
async def traduzir(ctx):
    
    embed = discord.Embed(
        title='',
        colour=29695
    )

    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/languages-1891105-1598018.png")
    embed.add_field(name="Use o comando", value='/traduzir "Texto" LÍNGUA (Exemplo: en, es, pt)', inline=False)
    embed.set_author(name='COMANDO PARA TRADUÇÃO', icon_url='https://cdn-icons-png.flaticon.com/512/484/484531.png')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

client.run('ODk0MDE0Nzk2Nzc1NjkwMjcw.YVj2KQ.pAi2T-enFcthkZ-NIMSTglHZ2hI')
