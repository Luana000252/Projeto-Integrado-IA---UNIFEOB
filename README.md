# 🔍 Analisador de Texto com IA

Sistema de análise de texto com inteligência artificial para detecção de informações pessoais (PII) e avaliação de riscos, desenvolvido com tema cyberpunk/neon.

## ✨ Características

- **Interface Cyberpunk**: Design dark com paleta neon vibrante
- **Glassmorphism**: Painéis translúcidos com efeito blur
- **Análise de PII**: Detecção automática de informações pessoais
- **Avaliação de Riscos**: Classificação por níveis com indicadores visuais
- **Efeitos Interativos**: Animações de glow e placeholder dinâmico

## 🎨 Design

- **Cores**: Fundo roxo profundo (#140726, #1A0633)
- **Paleta Neon**: Ciano, verde-limão, roxo, magenta, amarelo
- **Tipografia**: Inter (sans-serif moderna)
- **Efeitos**: Bordas neon, glassmorphism, animações suaves

## 🚀 Como Usar

1. Abra o arquivo `index.html` no navegador
2. Escolha o modo de análise (Local ou Servidor)
3. Cole o texto na área de análise
4. Clique em "Analisar" para processar
5. Visualize os resultados com métricas de risco e PII detectado

## 🔄 Modos de Funcionamento

### 💻 Modo Local (Padrão)
- **Funciona offline** sem necessidade de servidor
- **Detecção rápida** de PII usando regex
- **Identifica**: E-mails, telefones, CPF, nomes próprios
- **Ideal para**: Testes rápidos e demonstrações

### 🌐 Modo Servidor
- **Requer API backend** em `http://127.0.0.1:5000/analyze`
- **Análise avançada** com IA/ML
- **Maior precisão** na detecção de PII
- **Ideal para**: Produção e análises complexas

## 📋 Requisitos

- Navegador moderno com suporte a CSS3
- **Modo Local**: Nenhum requisito adicional
- **Modo Servidor**: API backend rodando na porta 5000

## 🔧 Estrutura

```
├── index.html          # Interface principal
├── foto.png           # Logo da aplicação
└── README.md          # Documentação
```

## 🎯 Funcionalidades

- ✅ **Duplo modo**: Local (offline) e Servidor (online)
- ✅ **Análise de texto** em tempo real
- ✅ **Detecção de PII**: E-mails, telefones, CPF, nomes
- ✅ **Classificação de riscos** (Alto/Médio/Baixo)
- ✅ **Interface responsiva** com tema cyberpunk
- ✅ **Validação de entrada** e estados de loading
- ✅ **Tratamento de erros** com fallback automático

---

**Desenvolvido para UNIFEOB - Projeto Integrado IA**