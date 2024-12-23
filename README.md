# Calculadora com Interface Gráfica em Python

Este é um projeto de uma **calculadora simples** com interface gráfica desenvolvida em **Tkinter**, a biblioteca padrão do Python para criação de GUIs. O objetivo é ajudar iniciantes em Python a praticar contribuições open source enquanto aprendem a criar aplicações desktop.

## Recursos

- Interface gráfica intuitiva com **Tkinter**.
- Operações matemáticas básicas: adição, subtração, multiplicação e divisão.
- Estilo simples e organizado, ideal para quem está começando.

## Pré-requisitos

- **Python 3.x** instalado. Você pode baixá-lo em [python.org](https://www.python.org/).
- Este projeto utiliza apenas bibliotecas padrão, então nenhuma instalação adicional é necessária.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-tkinter.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd calculadora-tkinter
   ```

3. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

## Captura de Tela

![Imagem da Calculadora](https://via.placeholder.com/500x300?text=Adicione+uma+captura+de+tela+aqui)

> **Nota**: Atualize esta seção com uma captura de tela do seu projeto para torná-lo mais atrativo.

## Como Contribuir

Quer contribuir para este projeto? Aqui está como você pode começar:

1. **Faça um fork** deste repositório.
2. **Crie uma branch** para suas alterações:
   ```bash
   git checkout -b minha-contribuicao
   ```

3. **Faça suas alterações** e um commit com uma descrição clara:
   ```bash
   git commit -m "Descrição das alterações"
   ```

4. **Envie as alterações** para o seu fork:
   ```bash
   git push origin minha-contribuicao
   ```

5. **Abra um Pull Request** neste repositório.

### O que você pode fazer?

- Melhorar o design da interface gráfica.
- Corrigir bugs ou adicionar novas funcionalidades.
- Escrever testes automatizados.
- Melhorar esta documentação.

## Oportunidades de Aprendizado

Este projeto é uma ótima oportunidade para aprender:

- **Tkinter**: Criação de interfaces gráficas no Python.
- **Git e GitHub**: Fluxo de trabalho open source, incluindo forks, branches e pull requests.
- **Colaboração**: Trabalhar em equipe em um projeto open source.

## Possíveis Melhorias no Código e Atualizações Futuras

### **Erros e Melhorias no Código**

1. **Segurança no uso de `eval()`**  
   O uso da função `eval()` para calcular expressões pode ser perigoso, pois permite a execução de código arbitrário. Recomenda-se substituir `eval()` por uma solução mais segura, como bibliotecas especializadas em matemática.

2. **Botões Incompletos**  
   Alguns botões necessários para uma calculadora funcional estão ausentes no código. Certifique-se de que todos os botões estejam implementados e devidamente posicionados.

3. **Interface Gráfica não Responsiva**  
   A interface atual utiliza tamanhos fixos para os botões e outros componentes, o que dificulta a adaptação a diferentes tamanhos de tela. A interface pode ser melhorada para ser responsiva.

4. **Validação de Entrada**  
   O código não valida as entradas do usuário, o que pode resultar em erros ao processar cálculos inválidos. É importante implementar validações para entradas incorretas, como `5//` ou `10**`.

5. **Internacionalização**  
   Os textos da interface estão fixos em inglês. Implementar suporte a múltiplos idiomas tornará o projeto mais acessível para usuários de diferentes locais.

---

### **Possíveis Atualizações Futuras**

1. **Estilo e Temas Personalizados**  
   - Adicionar temas (claro, escuro, etc.) para personalizar a interface.  
   - Usar bibliotecas como `ttkthemes` para criar uma aparência mais moderna.

2. **Histórico de Cálculos**  
   - Incluir uma seção para exibir o histórico de cálculos realizados.  
   - Adicionar a opção de limpar o histórico ou salvá-lo em um arquivo.

3. **Suporte a Operações Avançadas**  
   - Implementar funções como seno, cosseno, tangente e cálculo de raiz quadrada.  
   - Adicionar suporte a cálculos científicos e estatísticos.

4. **Atalhos de Teclado**  
   - Permitir que o usuário insira números e operações diretamente pelo teclado, vinculando eventos de tecla aos botões correspondentes.

5. **Exportação de Resultados**  
   - Adicionar funcionalidades para salvar o resultado em arquivos, como PDF ou imagem, para uso futuro.

6. **Salvar e Carregar Histórico**  
   - Permitir salvar o histórico de cálculos em arquivos `.txt` ou `.csv` e reabri-los no aplicativo.

7. **Testes Automatizados**  
   - Adicionar testes automatizados para garantir que o programa funcione corretamente em diferentes cenários.

8. **Adaptação a Dispositivos Móveis**  
   - Tornar a interface gráfica adaptável a telas menores, como as de smartphones e tablets.

9. **Interface Mais Atrativa**  
   - Melhorar o layout e adicionar animações para tornar a experiência do usuário mais agradável.

10. **Documentação do Código**  
    - Adicionar mais comentários ao código para facilitar a compreensão por outros desenvolvedores.

---

### **Para Iniciantes**

Se você é iniciante, aqui estão algumas ideias para começar a trabalhar neste projeto:

- Substituir o uso de `eval()` por alternativas mais seguras.
- Validar as entradas para evitar cálculos inválidos.
- Aprender a estilizar interfaces com melhores layouts e temas.
- Implementar um histórico simples de cálculos para praticar manipulação de listas.
- Explorar bibliotecas como `unittest` para criar testes automatizados.

Essas melhorias irão aprimorar o projeto e proporcionar aprendizado valioso para futuros desenvolvimentos.


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Você pode usá-lo livremente para fins educacionais e comerciais.

---

💡 **Gostou?** Dê uma estrela no repositório e ajude a divulgar o projeto para outros iniciantes em Python! 😊
