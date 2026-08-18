#!/usr/bin/env python3
"""Gera o deck institucional da Deep Blue (v1) — dark #080C1A, identidade Blu.

Uso: python3 build_deck.py [output.pptx]
"""
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

# ---------- Design tokens (identidade Deep Blue / Blu) ----------
BG        = "080C1A"   # preto azulado
SURFACE   = "111827"   # cards
BORDER    = "1E293B"   # hairlines
TEXT      = "F1F5F9"
DIM       = "94A3B8"
ACCENT    = "3B82F6"
ACCENT_LT = "60A5FA"
DEEP      = "1D4ED8"
FONT_T    = "Plus Jakarta Sans"
FONT_B    = "Inter"

def C(hexstr):
    return RGBColor.from_string(hexstr)

def rgb(c):
    return C(c)

# ---------- Helpers ----------
def add_rect(slide, x, y, w, h, fill=None, line=None, line_w=0.75, shape=MSO_SHAPE.RECTANGLE, radius=None):
    sp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line)
        sp.line.width = Pt(line_w)
    else:
        sp.line.fill.background()
    sp.shadow.inherit = False
    return sp

def add_text(slide, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             space_after=0, line_spacing=None):
    """runs: list of paragraphs; each paragraph = list of (text, dict) run specs."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    first = True
    for para_specs in runs:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        if space_after:
            p.space_after = Pt(space_after)
        if line_spacing:
            p.line_spacing = line_spacing
        for text, style in para_specs:
            r = p.add_run()
            r.text = text
            f = r.font
            f.size = Pt(style.get("size", 14))
            f.bold = style.get("bold", False)
            f.italic = style.get("italic", False)
            f.name = style.get("font", FONT_B)
            f.color.rgb = rgb(style.get("color", TEXT))
    return tb

def kicker(slide, text, x=0.7, y=0.72):
    return add_text(slide, x, y, 11.9, 0.35, [[(text.upper(), {"size": 11, "bold": True,
            "color": ACCENT_LT, "font": FONT_B})]])

def title(slide, text, x=0.7, y=1.02, size=30, w=11.9, color=TEXT, line_spacing=1.04):
    return add_text(slide, x, y, w, 1.6, [[(text, {"size": size, "bold": True,
            "color": color, "font": FONT_T})]], line_spacing=line_spacing)

def sub(slide, text, x=0.7, y=2.5, size=14, w=11.9, color=DIM, line_spacing=1.3):
    return add_text(slide, x, y, w, 0.8, [[(text, {"size": size, "color": color})]],
                    line_spacing=line_spacing)

def card(slide, x, y, w, h, fill=SURFACE, line=BORDER, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    return add_rect(slide, x, y, w, h, fill=fill, line=line, shape=shape)

def footer(slide, page, total=12):
    add_rect(slide, 0.7, 7.08, 11.93, 0.012, fill=BORDER)
    add_text(slide, 0.7, 7.14, 6, 0.3, [[("Deep Blue · deepblue.company", {"size": 9, "color": DIM})]])
    add_text(slide, 11.5, 7.14, 1.13, 0.3, [[(f"{page:02d} / {total:02d}", {"size": 9, "color": DIM})]],
             align=PP_ALIGN.RIGHT)

def mini_logo(slide, x=0.7, y=0.5, scale=0.32, with_word=True):
    """Círculos concêntricos pequenos + wordmark (estilo nav do site)."""
    rings = [("0E1A3A", 1.00), ("162E63", 0.72), ("1D4ED8", 0.44), ("60A5FA", 0.16)]
    for color, rel in rings:
        d = 0.42 * rel * scale * 3
        add_rect(slide, x + (0.42*scale - d/2), y + (0.42*scale - d/2), d, d,
                 fill=color, shape=MSO_SHAPE.OVAL)
    if with_word:
        add_text(slide, x + 0.42*scale + 0.12, y + 0.03, 3.2, 0.35,
                 [[("Deep ", {"size": 15, "bold": True, "color": ACCENT, "font": FONT_T}),
                   ("Blue", {"size": 15, "bold": True, "color": TEXT, "font": FONT_T})]])

def big_rings(slide, cx, cy, base=3.0, max_color="60A5FA"):
    """Círculos concêntricos grandes e quietos (fundo)."""
    colors = ["0A1226", "0D1A38", "10244C", "14305F"]
    steps = [1.0, 0.74, 0.48, 0.22]
    for i, (color, rel) in enumerate(zip(colors, steps)):
        d = base * rel * 2
        add_rect(slide, cx - d/2, cy - d/2, d, d, fill=color, shape=MSO_SHAPE.OVAL)

def dots(slide, x, y, n=3, color=ACCENT, d=0.07, gap=0.12):
    for i in range(n):
        add_rect(slide, x + i*gap, y, d, d, fill=color, shape=MSO_SHAPE.OVAL)

# ---------- Build ----------
def build(path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank = prs.slide_layouts[6]

    # ===== Slide 1 — Capa =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    big_rings(s, 10.6, 4.1, base=3.1)
    mini_logo(s, x=0.7, y=0.62, scale=0.34)
    add_rect(s, 0.7, 2.6, 0.55, 0.045, fill=ACCENT)
    add_text(s, 0.7, 2.85, 7.6, 0.4, [[("INTELIGÊNCIA ARTIFICIAL COMO FERRAMENTA DE NEGÓCIO",
            {"size": 12, "bold": True, "color": ACCENT_LT})]])
    add_text(s, 0.7, 3.35, 8.4, 2.2,
             [[("Sua operação já funciona.", {"size": 42, "bold": True, "color": TEXT, "font": FONT_T})],
              [("A IA pode ser o que falta para ela render mais.", {"size": 42, "bold": True, "color": TEXT, "font": FONT_T})]],
             line_spacing=1.02, space_after=6)
    add_text(s, 0.7, 5.75, 7.8, 0.9,
             [[("Entregamos sistemas que agregam valor, com resultado mensurável. ", {"size": 15, "color": DIM}),
               ("Consultoria primeiro. Tecnologia depois.", {"size": 15, "color": TEXT, "bold": True})]],
             line_spacing=1.35)
    add_text(s, 0.7, 6.85, 8, 0.35, [[("deepblue.company", {"size": 12, "color": DIM})]])
    s.notes_slide.notes_text_frame.text = (
        "Abertura. Uma frase: a Deep Blue existe para PMEs que já rodam bem e querem render mais. "
        "Nosso ponto de partida é sempre o negócio; a IA entra depois, como ferramenta.")

    # ===== Slide 2 — Quem somos =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "A empresa")
    title(s, "A Deep Blue ajuda empresas a usar IA como ferramenta de negócio.", size=29)
    sub(s, "Fundada para um perfil específico: PMEs que já rodam bem e querem render mais. "
           "Duas frentes, uma lógica — entender o negócio antes de propor tecnologia.", y=2.62)
    card(s, 0.7, 3.5, 5.8, 2.6)
    add_text(s, 1.0, 3.85, 5.2, 0.4, [[("Deep Blue Labs", {"size": 18, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
    add_text(s, 1.0, 4.4, 5.2, 1.6,
             [[("Produtos em assinatura. ", {"size": 13.5, "bold": True, "color": TEXT})],
              [("Plataforma Blu, agentes de IA e assistentes que centralizam conhecimento e automatizam o dia a dia.", {"size": 13.5, "color": DIM})]],
             line_spacing=1.3, space_after=4)
    card(s, 6.83, 3.5, 5.8, 2.6)
    add_text(s, 7.13, 3.85, 5.2, 0.4, [[("Deep Blue Consulting", {"size": 18, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
    add_text(s, 7.13, 4.4, 5.2, 1.6,
             [[("Projetos de diagnóstico e estratégia. ", {"size": 13.5, "bold": True, "color": TEXT})],
              [("Mapeamos processos, identificamos onde a IA agrega valor e priorizamos casos de uso.", {"size": 13.5, "color": DIM})]],
             line_spacing=1.3, space_after=4)
    footer(s, 2)
    s.notes_slide.notes_text_frame.text = (
        "Apresentar as duas frentes como complementares: Labs é o produto contínuo, "
        "Consulting é a porta de entrada. Muitos clientes começam no diagnóstico e viram assinante depois.")

    # ===== Slide 3 — O ponto cego =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "O contexto")
    title(s, "PMEs rodam o país. E o dono decide sozinho.", size=30)
    sub(s, "Dados de mercado que explicam por que a IA vira ferramenta — e não brinquedo.", y=2.5)
    stats = [
        ("90%", "dos líderes de PMEs tomam decisões sozinhos em 5 áreas diferentes, sem apoio estruturado", "Itaú · Locomotiva"),
        ("30%", "do PIB brasileiro é movido por PMEs, que respondem por metade dos empregos ativos", "Sebrae"),
        ("9 em 10", "PMEs relatam dificuldade na gestão financeira do dia a dia", "Pesquisa Sebrae 2024"),
    ]
    for i, (num, txt, src) in enumerate(stats):
        x = 0.7 + i * 4.05
        card(s, x, 3.3, 3.75, 3.0)
        add_text(s, x + 0.3, 3.6, 3.15, 1.0, [[(num, {"size": 44, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
        add_text(s, x + 0.3, 4.55, 3.15, 1.4, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.3)
        add_text(s, x + 0.3, 5.85, 3.15, 0.3, [[(src, {"size": 10, "color": "64748B", "italic": True})]])
    footer(s, 3)
    s.notes_slide.notes_text_frame.text = (
        "Fonte: Itaú/Locomotiva, Sebrae (2024-2025). O dono de PME decide sozinho em 5 áreas; "
        "a Deep Blue existe pra tirar peso das costas dele. '90% dos líderes de PMEs tomam decisões "
        "sozinhos em 5 áreas diferentes enquanto tentam manter o negócio rodando.'")

    # ===== Slide 4 — Como trabalhamos =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Método")
    title(s, "Não começamos pela tecnologia. Começamos pelo negócio.", size=29)
    steps = [
        ("01", "Escutar", "Entrevistas com as pessoas, não só com os dados. As dores aparecem no dia a dia, não no relatório."),
        ("02", "Entender", "Processos, decisões, gargalos. Onde o tempo some e onde o conhecimento fica preso."),
        ("03", "Mapear", "Oportunidades priorizadas por impacto e viabilidade. O diagnóstico vira um mapa, não um laudo."),
    ]
    for i, (num, t, txt) in enumerate(steps):
        x = 0.7 + i * 4.05
        card(s, x, 3.3, 3.75, 3.0)
        add_text(s, x + 0.3, 3.6, 3.15, 0.6, [[(num, {"size": 15, "bold": True, "color": "64748B", "font": FONT_T})]])
        add_text(s, x + 0.3, 4.15, 3.15, 0.5, [[(t, {"size": 20, "bold": True, "color": TEXT, "font": FONT_T})]])
        add_text(s, x + 0.3, 4.75, 3.15, 1.4, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.3)
    add_text(s, 0.7, 6.55, 11.9, 0.4,
             [[("Todo projeto de IA começa com pessoas: escutamos as dores do cliente, entendemos o processo e mapeamos oportunidades.",
                {"size": 13, "color": TEXT, "italic": True})]])
    footer(s, 4)
    s.notes_slide.notes_text_frame.text = (
        "Frase do fundador (padrão ouro). Consultoria primeiro, tecnologia depois. "
        "Isso diferencia a Deep Blue de quem vende ferramenta pronta sem entender o negócio.")

    # ===== Slide 5 — O diagnóstico =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "O que encontramos")
    title(s, "As dores se repetem. Conhecimento preso, decisão solitária, processo manual.", size=27)
    pains = [
        ("Conhecimento espalhado", "Documentos, planilhas e SOPs em lugares diferentes. O que a equipe sabe não vira ativo da empresa."),
        ("Decisão solitária", "O dono decide sozinho, sem ter os números na mão no momento da decisão. Tudo depende da cabeça dele."),
        ("Trabalho manual", "O tempo que poderia gerar negócio é gasto repetindo o mesmo processo. Cada proposta, cada relatório, do zero."),
    ]
    for i, (t, txt) in enumerate(pains):
        x = 0.7 + i * 4.05
        card(s, x, 3.3, 3.75, 2.9)
        dots(s, x + 0.3, 3.62, n=3, d=0.075, gap=0.13)
        add_text(s, x + 0.3, 3.95, 3.15, 0.5, [[(t, {"size": 17, "bold": True, "color": TEXT, "font": FONT_T})]])
        add_text(s, x + 0.3, 4.55, 3.15, 1.5, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.3)
    footer(s, 5)
    s.notes_slide.notes_text_frame.text = (
        "Essas três dores aparecem em quase todo diagnóstico. Use exemplos do cliente real "
        "que você está apresentando: troque os genéricos pelas dores específicas dele.")

    # ===== Slide 6 — O que entregamos =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Capabilities")
    title(s, "Ferramentas de IA a serviço do seu negócio.", size=30)
    sub(s, "Três frentes. Todas inseridas nos pontos de impacto que o diagnóstico revelou.", y=2.5)
    caps = [
        ("Plataforma", "Sistemas completos: documentos, conhecimento e agentes de IA num ambiente só. A operação centralizada."),
        ("Fluxos de agentes", "Processos automatizados com agentes integrados aos sistemas que o cliente já usa. Cada um na sua função."),
        ("Assistente diário", "Um agente que entende o negócio e responde em linguagem natural. Perguntou, resolveu — com contexto."),
    ]
    for i, (t, txt) in enumerate(caps):
        x = 0.7 + i * 4.05
        card(s, x, 3.3, 3.75, 3.0)
        add_text(s, x + 0.3, 3.6, 3.15, 0.5, [[(t, {"size": 19, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
        add_text(s, x + 0.3, 4.25, 3.15, 1.7, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.3)
        add_rect(s, x + 0.3, 5.95, 0.5, 0.045, fill=ACCENT)
    footer(s, 6)
    s.notes_slide.notes_text_frame.text = (
        "Visão geral antes de aprofundar. As três frentes respondem a três perguntas do cliente: "
        "'onde fica minha operação?', 'quem executa meu processo?', 'quem responde minhas perguntas?'")

    # ===== Slide 7 — Plataforma Blu =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Capability · Plataforma")
    title(s, "Plataforma Blu. O escritório virtual da sua empresa.", size=29)
    sub(s, "Um ambiente só para o que hoje está espalhado: documentos, conhecimento e agentes.", y=2.5)
    feats = [
        ("Agentes de IA", "Trabalham nos seus processos: atendimento, documentos, relatórios, rotinas."),
        ("Pipeline de documentos", "Do lead ao contrato, tudo num fluxo único e rastreável."),
        ("Sala de estratégia", "Busca semântica no conhecimento da empresa. Pergunta em linguagem natural, resposta com contexto."),
        ("Gestão de conhecimento", "O que a equipe sabe vira ativo da empresa — acessível, não preso na cabeça de ninguém."),
    ]
    for i, (t, txt) in enumerate(feats):
        col, row = i % 2, i // 2
        x = 0.7 + col * 6.03
        y = 3.3 + row * 1.85
        card(s, x, y, 5.8, 1.62)
        add_text(s, x + 0.3, y + 0.22, 5.2, 0.4, [[(t, {"size": 16, "bold": True, "color": TEXT, "font": FONT_T})]])
        add_text(s, x + 0.3, y + 0.68, 5.2, 0.85, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.25)
    footer(s, 7)
    s.notes_slide.notes_text_frame.text = (
        "Blu é o carro-chefe do Labs. Se o cliente tem a operação espalhada em planilha, e-mail e Drive, "
        "o Blu centraliza. Demo ao vivo se possível: mostrar busca semântica na sala de estratégia.")

    # ===== Slide 8 — Fluxos de agentes =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Capability · Agentes")
    title(s, "Agentes que trabalham dentro do seu processo.", size=29)
    sub(s, "Implantados nos sistemas que o cliente já usa. Cada um com uma função clara.", y=2.5)
    agents = [
        ("TalentFlow", "RH — triagem de currículos, agendamento, onboarding, análise de turnover."),
        ("KnowledgeBase", "Conhecimento — respostas com o contexto da empresa, não texto genérico."),
        ("ProjectPilot", "Projetos — prazos, riscos, status. O PM que não dorme."),
        ("OpsFlow", "Operações — rotinas e fluxos internos automatizados."),
    ]
    for i, (t, txt) in enumerate(agents):
        col, row = i % 2, i // 2
        x = 0.7 + col * 6.03
        y = 3.3 + row * 1.85
        card(s, x, y, 5.8, 1.62)
        add_text(s, x + 0.3, y + 0.22, 5.2, 0.4, [[(t, {"size": 16, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
        add_text(s, x + 0.3, y + 0.68, 5.2, 0.85, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.25)
    add_text(s, 0.7, 6.55, 11.9, 0.4,
             [[("Nossa operação roda com 6 agentes assim. A mesma tecnologia que entregamos para clientes.",
                {"size": 13, "color": TEXT, "italic": True})]])
    footer(s, 8)
    s.notes_slide.notes_text_frame.text = (
        "Agentes sob medida são o ticket mais alto (implantação + mensalidade). "
        "Contar que a Deep Blue usa os próprios agentes para rodar a operação: é vitrine, não teoria.")

    # ===== Slide 9 — Assistente diário =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Capability · Assistente")
    title(s, "Pergunte em linguagem natural. Ele entende o seu negócio.", size=29)
    sub(s, "Um assistente diário — um Hermes trabalhando para você, com o contexto da empresa.", y=2.5)
    card(s, 0.7, 3.3, 7.4, 3.1)
    flow = [
        ("1 · Entende o contexto", "Processo, gargalos e histórico da empresa. Não responde no vácuo."),
        ("2 · Consulta as ferramentas por você", "Busca nos documentos, puxa os números, executa rotinas."),
        ("3 · Responde com contexto", "Resposta com a cara do seu negócio — não texto genérico de IA."),
    ]
    for i, (t, txt) in enumerate(flow):
        y = 3.55 + i * 0.95
        add_text(s, 1.05, y, 6.8, 0.8,
                 [[(t + "  ", {"size": 14, "bold": True, "color": TEXT, "font": FONT_T}),
                   (txt, {"size": 13, "color": DIM})]], line_spacing=1.25)
    card(s, 8.4, 3.3, 4.23, 3.1, fill="0C1024", line=DEEP)
    add_text(s, 8.75, 3.62, 3.6, 0.4, [[("Exemplo", {"size": 11, "bold": True, "color": ACCENT_LT})]])
    add_text(s, 8.75, 4.1, 3.6, 2.2,
             [[("\u201cQuantas propostas foram enviadas este mês e quais estão paradas há mais de uma semana?\u201d",
                {"size": 13, "color": TEXT, "italic": True})],
              [("→ Busca, cruza e responde com os números da casa.", {"size": 12.5, "color": DIM})]],
             line_spacing=1.35, space_after=10)
    footer(s, 9)
    s.notes_slide.notes_text_frame.text = (
        "O assistente diário é o 'Hermes do cliente': consulta em linguagem natural, entende o negócio, "
        "usa as ferramentas. Demo ideal: fazer a pergunta ao vivo e mostrar a resposta com contexto.")

    # ===== Slide 10 — O método =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Como entra a tecnologia")
    title(s, "Diagnóstico primeiro. Ferramentas nos pontos de impacto.", size=29)
    sub(s, "Entendemos as dores do cliente e inserimos as ferramentas exatamente onde elas mudam o dia a dia.", y=2.5)
    card(s, 0.7, 3.5, 5.8, 2.7)
    add_text(s, 1.0, 3.85, 5.2, 0.5, [[("1 · Diagnóstico", {"size": 18, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
    add_text(s, 1.0, 4.45, 5.2, 1.6,
             [[("Gargalos e dores mapeados com o cliente: onde o tempo some, onde a decisão trava, onde o conhecimento fica preso.",
                {"size": 13.5, "color": DIM})]], line_spacing=1.3)
    add_text(s, 6.9, 4.3, 0.9, 0.9, [[("→", {"size": 40, "bold": True, "color": ACCENT, "font": FONT_T})]])
    card(s, 7.83, 3.5, 4.8, 2.7)
    add_text(s, 8.13, 3.85, 4.2, 0.5, [[("2 · Inserção", {"size": 18, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
    add_text(s, 8.13, 4.45, 4.2, 1.6,
             [[("Ferramentas de IA nos pontos de impacto do diagnóstico. Cada uma responde a uma dor mapeada.",
                {"size": 13.5, "color": DIM})]], line_spacing=1.3)
    add_text(s, 0.7, 6.55, 11.9, 0.4,
             [[("A IA é uma poderosa ferramenta que usamos para impactar o diagnóstico que fizemos.",
                {"size": 13, "color": TEXT, "italic": True})]])
    footer(s, 10)
    s.notes_slide.notes_text_frame.text = (
        "O coração da proposta: nada de ferramenta sem diagnóstico. Esse é o slide que separa "
        "a Deep Blue de quem vende IA pronta. Feche com a frase do fundador.")

    # ===== Slide 11 — Vitrine =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Prova viva")
    title(s, "Usamos o que vendemos.", size=30)
    sub(s, "Nossa operação roda com agentes de IA. A mesma tecnologia que entregamos para clientes.", y=2.5)
    team = [
        ("Writer", "Propostas, documentação, conteúdo"),
        ("PM", "Cronogramas, riscos, status"),
        ("Sales", "Leads, follow-ups, pipeline"),
        ("Dev", "Código, code review, testes"),
        ("Legal", "Contratos e compliance"),
        ("Finance", "Fluxo de caixa e margem por projeto"),
    ]
    for i, (t, txt) in enumerate(team):
        col, row = i % 3, i // 3
        x = 0.7 + col * 4.05
        y = 3.4 + row * 1.7
        card(s, x, y, 3.75, 1.5)
        add_text(s, x + 0.3, y + 0.2, 3.15, 0.4, [[("Hermes " + t, {"size": 15, "bold": True, "color": ACCENT_LT, "font": FONT_T})]])
        add_text(s, x + 0.3, y + 0.68, 3.15, 0.7, [[(txt, {"size": 12, "color": DIM})]], line_spacing=1.2)
    footer(s, 11)
    s.notes_slide.notes_text_frame.text = (
        "Os 6 agentes Hermes internos. Quando o cliente perguntar 'isso funciona?', "
        "a resposta é: a gente opera assim. Cada proposta que vocês estão vendo foi escrita por um agente.")

    # ===== Slide 12 — Próximos passos =====
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, 13.333, 7.5, fill=BG)
    big_rings(s, 11.2, 1.9, base=2.2)
    mini_logo(s, 0.7, 0.5, scale=0.3)
    kicker(s, "Próximos passos")
    title(s, "Conta o seu desafio. A gente mapeia onde a IA agrega.", size=29)
    steps = [
        ("1", "Diagnóstico gratuito", "Entendemos seu processo e suas dores. Sem compromisso, sem fórmula pronta."),
        ("2", "Mapa de impacto", "Onde a IA agrega valor no seu negócio, com priorização por impacto e viabilidade."),
        ("3", "Proposta", "Ferramentas nos pontos de impacto, com resultado mensurável e cronograma."),
    ]
    for i, (num, t, txt) in enumerate(steps):
        x = 0.7 + i * 4.05
        card(s, x, 3.4, 3.75, 2.7)
        add_text(s, x + 0.3, 3.7, 1, 0.6, [[(num, {"size": 28, "bold": True, "color": "64748B", "font": FONT_T})]])
        add_text(s, x + 0.3, 4.35, 3.15, 0.5, [[(t, {"size": 17, "bold": True, "color": TEXT, "font": FONT_T})]])
        add_text(s, x + 0.3, 4.95, 3.15, 1.0, [[(txt, {"size": 12.5, "color": DIM})]], line_spacing=1.25)
    add_text(s, 0.7, 6.45, 11.9, 0.5,
             [[("deepblue.company  ·  ", {"size": 13, "color": DIM}),
               ("formly.ink", {"size": 13, "color": ACCENT_LT, "bold": True}),
               ("  ·  ", {"size": 13, "color": DIM}),
               ("app.mcp-brain.com", {"size": 13, "color": ACCENT_LT, "bold": True})]])
    footer(s, 12)
    s.notes_slide.notes_text_frame.text = (
        "Fechamento com ação: agendar o diagnóstico gratuito. O CTA real é a reunião de "
        "descoberta. Levar contatos: site, Formly, MCP Brain.")

    prs.save(path)
    print(f"OK -> {path} ({len(prs.slides._sldIdLst)} slides)")

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "deck-empresa-v1.pptx")
