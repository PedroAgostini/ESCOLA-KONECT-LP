# Landing pages · Escola Konect Sorocaba

Domínio: https://lp.escolakonectsorocaba.com.br

| URL | Arquivo |
|---|---|
| /impressao-3d/ | impressao-3d/index.html |
| /ingles/ | ingles/index.html |
| (raiz) | redireciona para escolakonectsorocaba.com.br |

## Publicar
Envie para a raiz do subdomínio (public_html do subdomínio), mantendo a estrutura:
.htaccess, .well-known/, 404.html, favicon.ico, robots.txt, sitemap.xml, site.webmanifest, assets/, impressao-3d/, ingles/.
NÃO envie: _docs/, .impeccable/, PRODUCT.md.

Requisitos: Apache com mod_rewrite e mod_headers, e certificado SSL ativo no subdomínio (o .htaccess força HTTPS).

## Depois de publicar
- Google Search Console: adicionar a propriedade do subdomínio e enviar /sitemap.xml.
- Testar compartilhamento: https://developers.facebook.com/tools/debug/ (usa assets/img/og-*.jpg).
- Testar o "Ouvir em inglês" num celular real.

## Imagens e vídeos
- As duas LPs usam imagens locais em WebP, com tamanhos responsivos. As fotos de banco da LP de inglês foram substituídas por imagens geradas.
- Os registros reais da fachada, recepção, salas e impressoras foram extraídos de `assets/escola.mp4`.
- Tour da escola: `assets/video/escola-tour-24s.mp4`. Impressoras: `assets/video/impressoras-10s.mp4`. Os players só carregam o vídeo ao dar play.
- As cenas ilustrativas estão identificadas; não são apresentadas como alunos reais ou trabalhos da turma.
- Inventário, procedência, cortes e validação: [media/README.md](media/README.md). Prompts: [media/prompts.json](media/prompts.json).

## Anti-spam
- .htaccess: bloqueia POST/PUT/DELETE, sondagens de WordPress/PHP, query strings maliciosas, scanners e spam de referer.
- Formulário da LP de inglês: campo-isca invisível, tempo mínimo de 2,5 s, intervalo de 8 s entre envios e validação do nome (sem links/HTML). O formulário não envia dados a servidor: abre o WhatsApp.
