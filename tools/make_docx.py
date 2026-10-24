"""Генератор отчётов по образцу inbox/LR1-2_KucherUD_31ISIP.docx.

Берёт образец как шаблон (рамка и штамп лежат в колонтитулах, стили и списки в
styles.xml / numbering.xml) и заменяет только тело документа.

Блоки: ("title", текст), ("h1", текст), ("h2", текст), ("p", текст),
("bullets", [текст, ...]), ("table", [ширины], [[ячейки]...]),
("code", текст), ("image", путь, ширина_см, подпись), ("caption", текст),
("pagebreak",).
"""
import re
import struct
import zipfile
from xml.sax.saxutils import escape

TEMPLATE = "/root/labs/inbox/LR1-2_KucherUD_31ISIP.docx"
SZ = '<w:sz w:val="28"/><w:szCs w:val="28"/>'
SZ_TABLE = '<w:sz w:val="24"/><w:szCs w:val="24"/>'


def run(text, bold=False, italic=False, size=SZ, font=None):
    rpr = ""
    if font:
        rpr += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
    if bold:
        rpr += "<w:b/><w:bCs/>"
    if italic:
        rpr += "<w:i/><w:iCs/>"
    return f'<w:r><w:rPr>{rpr}{size}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def runs(text, **kw):
    """**жирный** фрагмент внутри строки."""
    out = []
    for i, part in enumerate(re.split(r"\*\*", text)):
        if part:
            out.append(run(part, bold=kw.get("bold", False) or i % 2 == 1,
                           size=kw.get("size", SZ), font=kw.get("font")))
    return "".join(out)


def para(text, jc="both", first=709, bold=False, keep=False, size=SZ, before=0, after=0):
    ind = f'<w:ind w:firstLine="{first}"/>' if first else ""
    kn = "<w:keepNext/>" if keep else ""
    return (f'<w:p><w:pPr>{kn}<w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/>{ind}'
            f'<w:jc w:val="{jc}"/></w:pPr>{runs(text, bold=bold, size=size)}</w:p>')


def heading(level, text):
    spacing = ('<w:spacing w:after="120" w:line="360" w:lineRule="auto"/>' if level == 1 else
               '<w:spacing w:before="120" w:after="120" w:line="360" w:lineRule="auto"/>')
    rpr = (f'<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
           f'{SZ if level == 1 else ""}')
    return (f'<w:p><w:pPr><w:pStyle w:val="{level}"/><w:keepNext/>{spacing}</w:pPr>'
            f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>')


def bullet(text):
    return ('<w:p><w:pPr><w:pStyle w:val="afa"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="4"/></w:numPr>'
            '<w:suppressAutoHyphens w:val="0"/><w:spacing w:after="0" w:line="360" w:lineRule="auto"/>'
            f'<w:contextualSpacing w:val="0"/><w:jc w:val="both"/></w:pPr>{runs(text)}</w:p>')


def code(text):
    lines = text.rstrip("\n").split("\n")
    out = []
    for ln in lines:
        out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>'
                   f'<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>'
                   f'<w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t xml:space="preserve">{escape(ln) or " "}</w:t></w:r></w:p>')
    return "".join(out)


def table(widths, rows):
    borders = "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                      for s in ("top", "left", "bottom", "right"))
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    xml = (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/><w:tblLayout w:type="fixed"/>'
           f'<w:tblBorders>{borders}<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
           f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/></w:tblBorders></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid>')
    for ri, row in enumerate(rows):
        hdr = ri == 0
        xml += "<w:tr><w:trPr><w:cantSplit/>" + ("<w:tblHeader/>" if hdr else "") + "</w:trPr>"
        for w, cell in zip(widths, row):
            shd = '<w:shd w:val="clear" w:color="auto" w:fill="E7E6E6"/>' if hdr else ""
            xml += (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{shd}'
                    '<w:tcMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
                    '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar></w:tcPr>')
            for line in str(cell).split("\n"):
                xml += ('<w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>'
                        f'{runs(line, bold=hdr, size=SZ_TABLE)}</w:p>')
            xml += "</w:tc>"
        xml += "</w:tr>"
    return xml + "</w:tbl>" + '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr></w:p>'


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def build(blocks, out_path):
    zin = zipfile.ZipFile(TEMPLATE)
    doc = zin.read("word/document.xml").decode("utf8")
    rels = zin.read("word/_rels/document.xml.rels").decode("utf8")
    ctypes = zin.read("[Content_Types].xml").decode("utf8")
    head = doc[:doc.index("<w:body>") + 8]
    sect = re.findall(r"<w:sectPr.*?</w:sectPr>", doc, re.S)[-1]
    sect = sect.replace('<w:pgNumType w:start="3"/>', '<w:pgNumType w:start="1"/>')
    sect = sect.replace('<w:type w:val="continuous"/>', "")

    media, body, n = {}, [], 0
    for b in blocks:
        k = b[0]
        if k == "title":
            body.append(para(b[1], jc="center", first=0, bold=True))
        elif k == "h1":
            body.append(heading(1, b[1]))
        elif k == "h2":
            body.append(heading(2, b[1]))
        elif k == "p":
            body.append(para(b[1]))
        elif k == "bullets":
            body += [bullet(t) for t in b[1]]
        elif k == "table":
            body.append(table(b[1], b[2]))
        elif k == "code":
            body.append(code(b[1]))
        elif k == "caption":
            body.append(para(b[1], jc="center", first=0, after=120))
        elif k == "pagebreak":
            body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
        elif k == "image":
            n += 1
            path, width_cm = b[1], b[2]
            w, h = png_size(path)
            cx = int(width_cm * 360000)
            cy = int(cx * h / w)
            name = f"lab_img{n}.png"
            media[f"word/media/{name}"] = open(path, "rb").read()
            rid = f"rIdLab{n}"
            rels = rels.replace("</Relationships>",
                                f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{name}"/></Relationships>')
            body.append(
                '<w:p><w:pPr><w:keepNext/><w:spacing w:before="120" w:after="60"/><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
                f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
                f'<wp:docPr id="{100 + n}" name="img{n}"/><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                f'<pic:nvPicPr><pic:cNvPr id="{n}" name="{name}"/><pic:cNvPicPr/></pic:nvPicPr>'
                f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
                f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
                '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
                '</wp:inline></w:drawing></w:r></w:p>')
            if len(b) > 3 and b[3]:
                body.append(para(b[3], jc="center", first=0, after=120))
    if "png" not in ctypes:
        ctypes = ctypes.replace("<Default ", '<Default Extension="png" ContentType="image/png"/><Default ', 1)

    new_doc = head + "".join(body) + sect + "</w:body></w:document>"
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = new_doc.encode("utf8")
            elif item.filename == "word/_rels/document.xml.rels":
                data = rels.encode("utf8")
            elif item.filename == "[Content_Types].xml":
                data = ctypes.encode("utf8")
            zout.writestr(item, data)
        for name, data in media.items():
            zout.writestr(name, data)
