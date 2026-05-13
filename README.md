# 🎨 JGAN Designer - Portfólio Esportivo Premium

Portfólio profissional em tempo real para **Gabriel Alves (JGAN)**, especialista em Design Esportivo.

> Desenvolvido com **Python + Streamlit** | Design Premium | 100% Responsivo | Pronto para Deploy

---

## 🌐 Acesse Agora

**[🚀 Clique aqui para ver o site em ação](https://jgan-designer-gb.streamlit.app)**

---

## ✨ Características

- ✅ **Design Moderno & Premium** - Estilo europeu de portfólio profissional
- ✅ **Responsivo** - Funciona perfeitamente em mobile, tablet e desktop
- ✅ **Cores Neon** - Azul ciano (#00d9ff) + Rosa neon (#ff006e)
- ✅ **Efeitos Glow** - Animações e transições suaves
- ✅ **Glassmorphism** - Efeito de vidro fosco moderno
- ✅ **Performance** - Carrega em menos de 2 segundos
- ✅ **Pronto para Deploy** - Um clique no Streamlit Cloud

---

## 📋 Seções do Site

### 1. **HERO SECTION** 🎯
- Logo e nome centralizado
- Subtítulo profissional
- Descrição breve
- Botões para Instagram e WhatsApp

### 2. **SOBRE MIM** 👋
- Foto profissional
- Biografia e especialidades
- Experiência e diferencial

### 3. **SERVIÇOS** 💼
Cards interativos com:
- Matchday
- Poster Esportivo
- Social Media
- Thumbs
- Wallpapers
- Identidade Visual

### 4. **PORTFÓLIO** 🖼️
- Grid responsivo de trabalhos
- 6 imagens de artes esportivas
- Efeitos hover premium

### 5. **CONTATO** 📞
- Botão WhatsApp
- Link Instagram
- Email profissional

### 6. **FOOTER** 📄
- Copyright e informações

---

## 🚀 Como Rodar Localmente

### 1. **Clonar o Repositório**
```bash
git clone https://github.com/JGAN-DESIGNER/GB.git
cd GB
```

### 2. **Criar Ambiente Virtual** (Opcional mas recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. **Instalar Dependências**
```bash
pip install -r requirements.txt
```

### 4. **Rodar a Aplicação**
```bash
streamlit run streamlit_app.py
```

A aplicação abrirá em `http://localhost:8501`

---

## 📸 Adicionar Suas Imagens

### Arquivos Necessários

1. **`minhafoto.png`** - Sua foto profissional (recomendado: 400x500px)
2. **`arte1.png`** até **`arte6.png`** - Seus trabalhos de design (recomendado: 400x300px)

### Como Adicionar

#### Opção 1: Via GitHub (Recomendado)
1. Acesse: https://github.com/JGAN-DESIGNER/GB
2. Clique em **"Add file"** → **"Upload files"**
3. Selecione todas as 7 imagens
4. Clique em **"Commit changes"**
5. ⏳ Aguarde 2-5 minutos para o site atualizar

#### Opção 2: Localmente
1. Coloque os arquivos PNG na raiz do projeto
2. Execute `git add .`
3. Execute `git commit -m "Adicionar imagens do portfólio"`
4. Execute `git push origin develop`

#### Opção 3: Se a imagem não existir
O site cria automaticamente um **placeholder** com gradiente e texto, mantendo a aplicação 100% funcional mesmo sem as imagens!

---

## 🌐 Fazer Deploy no Streamlit Cloud

### Pré-requisitos
- ✅ Conta no GitHub
- ✅ Conta no Streamlit Cloud (gratuita)
- ✅ Repositório público

### Passo a Passo

1. **Acesse Streamlit Cloud**
   - Vá para: https://share.streamlit.io/

2. **Faça Login com GitHub**
   - Clique em "Sign up"
   - Autorize o Streamlit a acessar seus repositórios

3. **Criar Novo App**
   - Clique em **"New app"**
   - Preencha os campos:
     - **Repository:** `JGAN-DESIGNER/GB`
     - **Branch:** `develop`
     - **Main file path:** `streamlit_app.py`

4. **Deploy**
   - Clique em **"Deploy"**
   - ⏳ Aguarde 3-5 minutos

5. **Seu site estará em**
   ```
   https://jgan-designer-gb-[seu-hash].streamlit.app
   ```

---

## 🎨 Personalizar o Site

### Editar Informações

Abra o arquivo `streamlit_app.py` e procure por:

**Seu nome e títulos:**
```python
"JGAN DESIGNER"  # Linha ~XX
"SPORTS GRAPHIC DESIGNER"  # Linha ~XX
```

**Seu WhatsApp:**
```python
"https://wa.me/558396851338"  # Procure por este link
```

**Seu Instagram:**
```python
"https://www.instagram.com/jgan.designer/"  # Procure por este link
```

**Seu Email:**
```python
"gabriel@jgandesigner.com"  # Procure por este link
```

**Sua biografia:**
```python
# Procure pela seção "ABOUT SECTION"
"Me chamo Gabriel Alves..."
```

### Mudar Cores

Edite as cores no CSS (no arquivo `streamlit_app.py`):

```css
/* Cor Principal */
#00d9ff  /* Azul Neon - Altere para sua cor */

/* Cor Secundária */
#ff006e  /* Rosa Neon - Altere para sua cor */

/* Cor de Fundo */
#0a0a0a  /* Preto Escuro - Altere para sua cor */
```

---

## 📱 Responsividade

O site funciona perfeitamente em:
- ✅ Smartphones (320px+)
- ✅ Tablets (768px+)
- ✅ Desktops (1024px+)
- ✅ Ultra-wide (2560px+)

---

## 🔧 Troubleshooting

### "O site não carrega"
- Verifique se o `streamlit_app.py` está na raiz do projeto
- Confirme que tem `requirements.txt`

### "Imagens não aparecem"
- O site cria automaticamente placeholders
- Envie as imagens PNG na raiz do projeto
- Aguarde 5 minutos para o site atualizar

### "Botões não funcionam"
- Verifique sua conexão de internet
- Teste em outro navegador
- Limpe o cache (Ctrl+Shift+Del)

### "Site muito lento"
- Redimensione as imagens para ~400x300px
- Use formato PNG otimizado
- Limite o tamanho das imagens a 500KB cada

---

## 📦 Estrutura do Projeto

```
GB/
├── streamlit_app.py          # Aplicação principal
├── requirements.txt          # Dependências
├── README.md                 # Este arquivo
├── .streamlit/
│   └── config.toml          # Configuração do Streamlit
├── .gitignore               # Arquivos para ignorar
├── minhafoto.png            # Sua foto (adicionar)
├── arte1.png até arte6.png  # Seus trabalhos (adicionar)
└── pyproject.toml           # Configuração do projeto
```

---

## 💡 Dicas Profissionais

1. **Fotos de Alta Qualidade** - Use imagens em alta resolução (mínimo 1024px)
2. **Formato PNG** - Melhor para design (suporta transparência)
3. **Consistência Visual** - Mantenha um padrão de cor e estilo
4. **Descrições Claras** - Escreva descrições profissionais dos serviços
5. **Links Ativos** - Garanta que WhatsApp e Instagram funcionam
6. **Mobile First** - Teste sempre em celular antes de publicar

---

## 🚀 Próximos Passos

- [ ] Adicionar suas 7 imagens
- [ ] Personalizar informações de contato
- [ ] Fazer deploy no Streamlit Cloud
- [ ] Compartilhar o link nas redes sociais
- [ ] Monitorar acessos (Streamlit fornece analytics)

---

## 📞 Suporte

Se tiver dúvidas:
1. Verifique este README
2. Consulte a [documentação do Streamlit](https://docs.streamlit.io/)
3. Abra uma issue no GitHub

---

## 📝 Licença

Projeto pessoal - Todos os direitos reservados © 2026 JGAN Designer

---

## ✨ Desenvolvido com ❤️ e 🎨

**Criado para transformar sua visão em arte visual profissional!**

---

**Última atualização:** 13 de Maio de 2026
**Versão:** 1.0.0
**Status:** ✅ Pronto para Produção
