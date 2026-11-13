# Mídias das duas LPs

Implementadas em 12/11/2026 no projeto local. Geração com a ferramenta integrada `image_gen`; prompts completos em [prompts.json](prompts.json).

## Imagens geradas

Diretório final: `assets/img/generated/`.

| Nome | Uso | Larguras |
|---|---|---|
| ingles-hero | Abertura e fundo da chamada final | 640, 1024, 1536 |
| ingles-trabalho | Benefício profissional e situação de trabalho | 400, 800 |
| ingles-viagem | Benefício de viajar e situação de viagem | 400, 800 |
| ingles-estudo | Benefício de estudar e situação de estudo | 400, 800 |
| ingles-conexoes | Confiança e conexões | 400, 800 |
| ingles-aula | Banner da apresentação do curso | 640, 1024, 1536 |
| impressao-pecas | Exemplos ilustrativos de impressão 3D | 480, 960 |

Arquivos nomeados `nome-largura.webp`. As sete imagens foram revisadas visualmente e convertidas em 16 arquivos WebP. Os originais gerados permanecem no diretório padrão de geração; todos os arquivos usados pelas LPs estão dentro do projeto. Não há dependência desses originais para publicar.

## Material real

Fonte: vídeo `assets/escola.mp4` enviado pelo usuário, 221,5 segundos, 1024 × 576, sem faixa de áudio. A foto anexada serviu de referência visual da fachada; a imagem implementada da fachada é um quadro do próprio vídeo.

Diretório final: `assets/img/escola/`. Cinco imagens em 512 e 1024 pixels de largura:

- `fachada`: 5,5 s.
- `recepcao`: 40 s.
- `sala-tecnica`: 114 s.
- `sala-aula`: 203 s.
- `impressoras`: 171 s.

Os registros reais não foram reconstruídos com IA. A qualidade está limitada ao vídeo de origem.

## Edição dos vídeos

- `assets/video/escola-tour-24s.mp4`: seis tomadas de quatro segundos, começando em 3, 38, 64, 112, 170 e 203 segundos. Fachada, recepção, laboratório, sala técnica, impressoras e sala de aula. Aproximadamente 3,44 MiB.
- `assets/video/impressoras-10s.mp4`: trecho de 170 a 180 segundos. Aproximadamente 1,40 MiB.
- MP4/H.264, 24 fps, yuv420p, faststart, fade de entrada e saída. Sem áudio, como o original. Sem autoplay. Controles nativos, reprodução inline e `preload="none"`.
- Fonte original preservada. `prepare.py` documenta conversão e edição; depende de Pillow, FFmpeg e dos PNGs originais no caminho registrado no script. Não é necessário executá-lo para publicar.

## Verificação

- Duas páginas e todas as referências locais responderam HTTP 200 em servidor de teste.
- Imagens WebP decodificadas e verificadas, IDs e descrições dos players conferidos.
- Vídeos decodificados integralmente pelo FFmpeg; duração, codec, formato de pixel e posição do bloco faststart confirmados.
- Nenhum placeholder de galeria nem URL de imagem Unsplash permanece nas páginas.
- A prévia visual das páginas no navegador não pôde ser feita: o serviço de acesso ao navegador estava indisponível. Não houve publicação externa.
