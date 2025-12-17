# 🔍 User Checker 2025

Um verificador avançado de disponibilidade de usernames para múltiplas plataformas sociais.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Descrição

User Checker é uma ferramenta assíncrona e de alta performance que verifica a disponibilidade de nomes de usuário em diversas plataformas de redes sociais. Suporta verificação em lote e geração aleatória de usernames.

## ✨ Funcionalidades

- ⚡ Verificação assíncrona ultra-rápida
- 🎯 Suporte para 7 plataformas principais:
  - Instagram
  - Twitter/X
  - TikTok
  - YouTube
  - Twitch
  - GitHub
  - Discord
- 📝 Dois modos de operação:
  - Verificação de lista personalizada (`users.txt`)
  - Geração e verificação aleatória
- 💾 Salvamento automático de usernames disponíveis
- 🎨 Interface colorida e amigável no terminal

## 🚀 Instalação

### Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/Garotinha666/User-Checker
cd user-checker
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📖 Como Usar

### Execução Básica

```bash
python checker.py
```

### Modo 1: Verificar Lista de Usernames

1. Crie um arquivo `users.txt` na mesma pasta do script
2. Adicione os usernames que deseja verificar (um por linha)
3. Execute o script e selecione a opção `[1]`
4. Escolha a plataforma desejada

Exemplo de `users.txt`:
```
username1
username2
username3
```

### Modo 2: Geração Aleatória

1. Execute o script e selecione a opção `[2]`
2. Escolha a plataforma
3. Defina o tamanho dos usernames (4-15 caracteres)
4. Defina a quantidade a gerar

## 📊 Resultados

Os usernames disponíveis são salvos automaticamente no arquivo `available.txt` no formato:
```
Instagram: @username1
Twitter/X: @username2
GitHub: @username3
```

## 🎨 Exemplo de Uso

```
╦ ╦╔═╗╔═╗╦═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
║ ║╚═╗║╣ ╠╦╝  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╚═╝╚═╝╚═╝╩╚═  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═

Advanced Username Availability Checker
                made by ice.o1

[1] Instagram
[2] Twitter/X
[3] TikTok
[4] YouTube
[5] Twitch
[6] GitHub
[7] Discord

Select platform (1-7): 1
[1] Check from users.txt   [2] Generate random
Choose: 2

Username length (4-15) → 6: 
Amount to generate → 1000: 

[AVAILABLE] @xyz123 → Instagram
[TAKEN] @abc456
[AVAILABLE] @qwe789 → Instagram
```

## ⚙️ Configuração Avançada

### Ajuste de Rate Limiting

O script inclui delays entre requisições para evitar bloqueios:
- Modo lista: 0.18s entre cada verificação
- Modo aleatório: 0.16s entre cada verificação

Você pode ajustar esses valores nas linhas:
```python
await asyncio.sleep(0.18)  # Modo lista
await asyncio.sleep(0.16)  # Modo aleatório
```

### Limite de Conexões

Por padrão, o script usa até 500 conexões simultâneas:
```python
connector = aiohttp.TCPConnector(limit=500, ssl=False)
```

## ⚠️ Avisos Importantes

- **Uso Responsável**: Use esta ferramenta de forma ética e responsável
- **Rate Limits**: Respeite os limites de taxa das APIs das plataformas
- **Tokens**: Alguns tokens de API podem expirar e precisar ser atualizados
- **Fins Educacionais**: Este projeto é para fins educacionais

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**VaiXourar**

- Feito com ❤️ e Python

## 🙏 Agradecimentos

- Comunidade Python pela excelente documentação
- Desenvolvedores das bibliotecas utilizadas

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!
