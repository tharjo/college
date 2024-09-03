# Problemas, soluções e suas particularidades
---
## Contexto:

É essencial para o analista desenvolver soluções para problemas, a capacidade de reconhecer padrões também é importante, pois uma arquitetura possui similaridades com projetos semelhantes e tudo é aproveitado para cortar tempo e custos. Alguns exemplos apresentados pelo professor para que os alunos solucionem problemas são:

- Gestão de serviços de uma biblioteca.
- Toda solicitação de empréstimo deve ser atendida.
- Processo de check-out de livros da biblioteca.
- Sistema de check-out de livros da biblioteca.

# Separação

- O problema mais óbvio pode não ser o problema que deve ser resolvido;
- Deve-se discutir o problema com os stakeholders para um melhor entendimento;

# Metodologias

O que é uma metodologia?

- Padrões
- Comunicação
- Objetivo comum
- Aproveitamento de recursos

## Desenvolvimento

*Tradicional:*
- PDI-SW (Processo de Desenvolvimento Iterativo de Software)

*Ágil:*
- SCRUM

*Simples:*
- KISS (Keep It Simple, Stupid)

---

> Métodos de desenvolvimento devem ser baseados em modelos *(e.g Cascata)*

    Comunicação |
                v
            Planejamento |
                         v
                        Modelagem |
                                  v
                                Construção |
                                           v
                                        Implementação

> Métodos de desenvolvimento usam de padronização (e.g UML)

---

# MDS com Scrum

## Visão Geral

A Metodologia de Desenvolvimento de Sistemas (MDS) integrada com o framework Scrum combina práticas de engenharia de software estruturadas com abordagens ágeis para o desenvolvimento de projetos.

## Principais Componentes

### 1. Fases do MDS

1. **Concepção**
   - Definição do escopo do projeto
   - Análise de viabilidade
   - Elaboração do documento de visão

2. **Elaboração**
   - Levantamento detalhado de requisitos
   - Definição da arquitetura do sistema
   - Criação do Product Backlog inicial

3. **Construção**
   - Implementação das funcionalidades
   - Testes unitários e de integração
   - Sprints de desenvolvimento

4. **Transição**
   - Testes de aceitação do usuário
   - Treinamento dos usuários finais
   - Implantação do sistema

### 2. Elementos do Scrum

- **Product Owner**: Responsável pela visão do produto e priorização do backlog
- **Scrum Master**: Facilitador do processo Scrum
- **Development Team**: Equipe multifuncional responsável pela entrega do incremento do produto

### 3. Artefatos do Scrum

- **Product Backlog**: Lista priorizada de funcionalidades do produto
- **Sprint Backlog**: Itens do Product Backlog selecionados para a Sprint atual
- **Incremento**: Soma de todos os itens do Product Backlog completados durante uma Sprint

### 4. Eventos do Scrum

- **Sprint**: Período de tempo fixo (geralmente 2-4 semanas) para desenvolvimento
- **Sprint Planning**: Reunião para planejar o trabalho da próxima Sprint
- **Daily Scrum**: Reunião diária de 15 minutos para sincronização da equipe
- **Sprint Review**: Apresentação do incremento ao final da Sprint
- **Sprint Retrospective**: Reflexão sobre o processo e melhorias

## Integração MDS e Scrum

1. **Alinhamento de Fases**
   - Concepção e Elaboração: Formação inicial do Product Backlog
   - Construção: Execução das Sprints
   - Transição: Sprints finais focadas em estabilização e implantação

2. **Documentação Adaptativa**
   - Documentos essenciais mantidos e atualizados ao longo do projeto
   - Foco em documentação que agrega valor direto ao desenvolvimento

3. **Prototipação Rápida**
   - Uso de protótipos desde as fases iniciais para validação com stakeholders

4. **Gestão de Riscos Contínua**
   - Identificação e mitigação de riscos em cada Sprint

5. **Métricas de Projeto**
   - Burndown charts
   - Velocidade da equipe
   - Débito técnico

## Benefícios

- Maior adaptabilidade a mudanças
- Entrega contínua de valor ao cliente
- Melhor visibilidade do progresso do projeto
- Aumento da produtividade e qualidade do produto final

---

Certamente. Aqui está uma descrição em Markdown sobre o Standish Group e sua relação com a recomendação de processos no contexto do MDS:

# Standish Group e MDS

## Standish Group

O Standish Group é uma organização de pesquisa internacional conhecida por seus estudos sobre projetos de tecnologia da informação, particularmente o relatório CHAOS.

### Relatório CHAOS

- Publicado anualmente desde 1994
- Analisa o sucesso, desafios e fracassos de projetos de software
- Fornece insights valiosos sobre fatores que influenciam o sucesso dos projetos

## Recomendações do Standish Group

Com base em suas pesquisas, o Standish Group identificou fatores críticos para o sucesso de projetos, incluindo:

1. Envolvimento do usuário
2. Apoio executivo
3. Objetivos de negócio claros
4. Otimização do escopo
5. Processos ágeis
6. Expertise em gerenciamento de projetos
7. Recursos qualificados

## Relação com MDS

A Metodologia de Desenvolvimento de Sistemas (MDS) recomenda o uso de processos estruturados, alinhando-se com as descobertas do Standish Group:

### 1. Importância do Processo

- **MDS**: Enfatiza a necessidade de um processo bem definido
- **Standish Group**: Identifica processos ágeis como fator de sucesso

### 2. Envolvimento do Usuário

- **MDS**: Promove a participação ativa dos stakeholders em todas as fases
- **Standish Group**: Classifica o envolvimento do usuário como crucial

### 3. Escopo Gerenciável

- **MDS**: Recomenda definição clara e gestão eficaz do escopo
- **Standish Group**: Destaca a otimização do escopo como fator de sucesso

### 4. Expertise em Gerenciamento

- **MDS**: Valoriza o papel do gerente de projetos e sua competência
- **Standish Group**: Enfatiza a importância da expertise em gerenciamento

## Adaptação de Processos

O MDS, considerando as recomendações do Standish Group, sugere:

1. **Flexibilidade**: Adaptar o processo às necessidades específicas do projeto
2. **Iterações**: Incorporar ciclos de feedback frequentes
3. **Priorização**: Focar em entregas de alto valor para o negócio
4. **Comunicação**: Manter canais de comunicação eficientes entre equipe e stakeholders

## Métricas de Sucesso

Alinhadas com as descobertas do Standish Group, o MDS recomenda avaliar:

- Satisfação do usuário
- Aderência ao cronograma e orçamento
- Qualidade do produto entregue
- Alinhamento com objetivos de negócio

## Conclusão

A recomendação do MDS para o uso de processos é fortemente respaldada pelas pesquisas do Standish Group. A adoção de práticas estruturadas, combinada com a flexibilidade para adaptação, contribui significativamente para o aumento das chances de sucesso em projetos de desenvolvimento de software.