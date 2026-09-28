# Real Sites Inspiration — Sites Reais para Inspiração

## Visão Geral

Este guia lista sites reais que servem como inspiração para projetos, com análise de features, UX e implementação.

---

## Categorias de Inspiração

1. **E-commerce de Quadrinhos** — Lojas de quadrinhos reais
2. **Streaming** — Plataformas de vídeo/música
3. **Landing Pages** — Páginas de produto impactantes
4. **Dashboards** — Interfaces administrativas
5. **Apps Mobile** — Padrões de navegação mobile

---

## E-commerce de Quadrinhos

### 1. Panini Books

**URL:** https://paninibooks.com.br/quadrinhos

**Features Notáveis:**
- Grid de produtos limpo
- Filtros laterais (editora, personagem, preço)
- Cards com hover effect
- Badge de lançamento
- Preço promocional destacado

**UX Highlights:**
- Navegação por categorias clara
- Busca com autocomplete
- Carrinho persistente
- Checkout em poucos passos

**Implementação:**
```tsx
// Grid de produtos
<div className="grid grid-cols-2 md:grid-cols-4 gap-4">
  {comics.map(comic => (
    <ComicCard key={comic.id} comic={comic} />
  ))}
</div>

// Filtros laterais
<aside className="w-64 space-y-4">
  <FilterSection title="Editora">
    <Checkbox label="Panini" />
    <Checkbox label="Mythos" />
  </FilterSection>
  <FilterSection title="Preço">
    <RangeSlider min={0} max={100} />
  </FilterSection>
</aside>
```

**Lições:**
- Cards simples e eficazes
- Filtros essenciais (não exagerar)
- Preços claros e destacados

---

### 2. Amazon Quadrinhos

**URL:** https://amazon.com.br/livros/quadrinhos

**Features Notáveis:**
- Recomendações personalizadas
- "Clientes também compraram"
- Reviews e ratings
- Múltiplas imagens por produto
- Opções de formato (físico, Kindle)

**UX Highlights:**
- Scroll infinito
- Carregamento lazy de imagens
- Filtros avançados
- Histórico de visualizados

**Implementação:**
```tsx
// Recomendações
<section>
  <h2>Clientes também compraram</h2>
  <InfiniteScroll>
    {recommendedComics.map(comic => (
      <ComicCard key={comic.id} comic={comic} />
    ))}
  </InfiniteScroll>
</section>

// Múltiplas imagens
<ImageGallery images={comic.images} />
```

**Lições:**
- Social proof (reviews, ratings)
- Recomendações aumentam conversão
- Múltiplas imagens reduzem dúvidas

---

### 3. ComicLink

**URL:** https://comiclink.com/

**Features Notáveis:**
- Marketplace de quadrinhos raros
- Busca avançada por grade (CGC)
- Preços de mercado
- Histórico de vendas
- Auction/bid system

**UX Highlights:**
- Filtros muito específicos (grade, ano, editora)
- Dados de mercado transparentes
- Sistema de confiança (seller rating)

**Implementação:**
```tsx
// Busca avançada
<AdvancedSearch>
  <Select label="Grade" options={gradeOptions} />
  <Select label="Editora" options={publisherOptions} />
  <Input label="Ano" type="number" />
  <Input label="Personagem" />
</AdvancedSearch>

// Preço de mercado
<MarketData>
  <Price current={comic.price} />
  <Price average={comic.avgPrice} />
  <Price trend={comic.priceTrend} />
</MarketData>
```

**Lições:**
- Nicho específico requer filtros específicos
- Transparência de preços gera confiança
- Dados de mercado são valiosos

---

## Streaming

### 4. Netflix

**URL:** https://netflix.com

**Features Notáveis:**
- Hero section com autoplay
- Carrosséis horizontais por categoria
- Thumbnails com hover preview
- Continue watching
- Minha lista

**UX Highlights:**
- Navegação por categorias visuais
- Personalização forte
- Progresso salvo entre devices
- Downloads offline

**Implementação:**
```tsx
// Hero com autoplay
<section className="hero">
  <VideoAutoplay src={featuredVideo.trailer} />
  <div className="hero-content">
    <h1>{featuredVideo.title}</h1>
    <p>{featuredVideo.description}</p>
    <Button>Assistir</Button>
    <Button variant="secondary">Mais Informações</Button>
  </div>
</section>

// Carrossel horizontal
<Carousel title="Tendências">
  {trendingVideos.map(video => (
    <VideoCard key={video.id} video={video} />
  ))}
</Carousel>
```

**Lições:**
- Hero impactante prende atenção
- Carrosséis facilitam descoberta
- Hover preview reduz cliques

---

### 5. Spotify

**URL:** https://spotify.com

**Features Notáveis:**
- Sidebar de navegação fixa
- Bottom nav em mobile
- Playlists personalizadas
- Search com resultados em tempo real
- Lyrics sincronizadas

**UX Highlights:**
- Navegação consistente
- Descoberta musical forte
- Integração social (compartilhar, collaborative playlists)

**Implementação:**
```tsx
// Sidebar fixa
<aside className="sidebar w-64 fixed h-full">
  <nav>
    <NavItem icon={<Home />} label="Início" />
    <NavItem icon={<Search />} label="Buscar" />
    <NavItem icon={<Library />} label="Sua Biblioteca" />
  </nav>
</aside>

// Bottom nav mobile
<nav className="bottom-nav md:hidden">
  <NavItem icon={<Home />} label="Início" />
  <NavItem icon={<Search />} label="Buscar" />
  <NavItem icon={<Library />} label="Biblioteca" />
</nav>
```

**Lições:**
- Navegação consistente entre plataformas
- Personalização é chave
- Search rápido e relevante

---

### 6. YouTube

**URL:** https://youtube.com

**Features Notáveis:**
- Feed infinito
- Sidebar com recomendações
- Mini player persistente
- Chapters em vídeos
- Shorts (TikTok-like)

**UX Highlights:**
- Algoritmo de recomendação forte
- Engajamento (likes, comments, shares)
- Criador de conteúdo integrado

**Implementação:**
```tsx
// Feed infinito
<InfiniteFeed>
  {videos.map(video => (
    <VideoCard key={video.id} video={video} />
  ))}
</InfiniteFeed>

// Mini player
{currentVideo && (
  <MiniPlayer video={currentVideo} />
)}
```

**Lições:**
- Feed infinito mantém engajamento
- Mini player permite multitarefa
- Recomendações são cruciais

---

## Landing Pages

### 7. Linear

**URL:** https://linear.app

**Features Notáveis:**
- Hero com ilustração 3D
- Scroll animations suaves
- Features em grid
- Social proof (logos de clientes)
- CTA claro

**UX Highlights:**
- Copy concisa e clara
- Visual impactante
- Navegação mínima (foco em conversão)

**Implementação:**
```tsx
// Hero com 3D
<section className="hero">
  <Canvas3D>
    <AnimatedModel />
  </Canvas3D>
  <div className="hero-content">
    <h1>Issue tracking reimaginado</h1>
    <p>Linear é a maneira mais rápida de construir produtos.</p>
    <Button>Começar</Button>
  </div>
</section>

// Social proof
<section>
  <p>Usado por times na</p>
  <LogoGrid logos={customerLogos} />
</section>
```

**Lições:**
- Hero impactante converte
- Social proof gera confiança
- Copy clara e direta

---

### 8. Vercel

**URL:** https://vercel.com

**Features Notáveis:**
- Design minimalista
- Code snippets em destaque
- Performance como feature
- Integration showcase
- Customer stories

**UX Highlights:**
- Developer-first messaging
- Documentação acessível
- Deploy em um clique (demo)

**Implementação:**
```tsx
// Code snippet
<section>
  <pre>
    <code>{`$ vercel deploy`}</code>
  </pre>
  <p>Deploy em segundos</p>
</section>

// Integration grid
<Grid>
  {integrations.map(integration => (
    <IntegrationCard key={integration.id} integration={integration} />
  ))}
</Grid>
```

**Lições:**
- Mostrar, não apenas falar
- Developer experience é feature
- Integrações ampliam valor

---

### 9. Raycast

**URL:** https://raycast.com

**Features Notáveis:**
- Product demo interativa
- Store de extensions
- Keyboard-first navigation
- Performance destacada

**UX Highlights:**
- Demo do produto na landing
- Extensions como diferencial
- Comunidade ativa

**Implementação:**
```tsx
// Demo interativa
<section>
  <InteractiveDemo>
    <CommandK />
    <Search results={demoResults} />
  </InteractiveDemo>
</section>

// Extensions store
<StoreGrid>
  {extensions.map(ext => (
    <ExtensionCard key={ext.id} extension={ext} />
  ))}
</StoreGrid>
```

**Lições:**
- Demo > descrição
- Extensions criam ecossistema
- Keyboard-first para power users

---

## Dashboards

### 10. Notion

**URL:** https://notion.so

**Features Notáveis:**
- Sidebar com pages
- Block-based editor
- Templates
- Collaboration features
- Database views (table, board, calendar)

**UX Highlights:**
- Flexibilidade (pode ser tudo)
- Templates reduzem atrito inicial
- Collaboration transparente

**Implementação:**
```tsx
// Sidebar com pages
<aside className="sidebar">
  <PageTree pages={pages} />
  <Button>Add Page</Button>
</aside>

// Block editor
<Editor>
  {blocks.map(block => (
    <Block key={block.id} block={block} />
  ))}
</Editor>
```

**Lições:**
- Flexibilidade atrai usuários
- Templates aceleram onboarding
- Collaboration é essencial

---

### 11. Figma

**URL:** https://figma.com

**Features Notáveis:**
- Canvas infinito
- Multiplayer collaboration
- Components e variants
- Auto layout
- Plugins

**UX Highlights:**
- Colaboração em tempo real
- Component system poderoso
- Plugins estendem funcionalidades

**Implementação:**
```tsx
// Canvas infinito
<Canvas infinite>
  {layers.map(layer => (
    <Layer key={layer.id} layer={layer} />
  ))}
</Canvas>

// Multiplayer
<MultiplayerCursor users={activeUsers} />
```

**Lições:**
- Colaboração em tempo real é mágico
- Components reduzem trabalho repetitivo
- Plugins criam ecossistema

---

### 12. Airtable

**URL:** https://airtable.com

**Features Notáveis:**
- Spreadsheet + database
- Views (grid, kanban, calendar, gallery)
- Automations
- Integrations
- Forms

**UX Highlights:**
- Familiar (parece spreadsheet)
- Poderoso (é um database)
- Visual (multiple views)

**Implementação:**
```tsx
// Multi-view
<Tabs>
  <Tab label="Grid">
    <GridView data={records} />
  </Tab>
  <Tab label="Kanban">
    <KanbanView data={records} />
  </Tab>
  <Tab label="Calendar">
    <CalendarView data={records} />
  </Tab>
</Tabs>
```

**Lições:**
- Familiar + poderoso = win
- Multiple views atendem diferentes needs
- Automations aumentam valor

---

## Apps Mobile

### 13. Instagram

**Features Notáveis:**
- Bottom nav (5 items)
- Stories no topo
- Feed infinito
- Stories highlights no profile
- Reels (TikTok competitor)

**UX Highlights:**
- Navegação com uma mão
- Stories criam FOMO
- Algorithm feed maximiza engajamento

**Padrões:**
```tsx
// Bottom nav
<nav className="bottom-nav">
  <NavItem icon={<Home />} label="Início" />
  <NavItem icon={<Search />} label="Buscar" />
  <NavItem icon={<Plus />} label="Criar" />
  <NavItem icon={<Reels />} label="Reels" />
  <NavItem icon={<Profile />} label="Perfil" />
</nav>

// Stories
<StoriesBar>
  {stories.map(story => (
    <StoryCircle key={story.id} story={story} />
  ))}
</StoriesBar>
```

**Lições:**
- Bottom nav para 5+ items
- Stories no topo (padrão da indústria)
- Criar no centro (fácil acesso)

---

### 14. TikTok

**Features Notáveis:**
- Full-screen video feed
- Swipe vertical para próximo
- Swipe horizontal para profile/effects
- Double tap para like
- Comments overlay

**UX Highlights:**
- Zero friction (abre e já tem conteúdo)
- Algorithm extremamente personalizado
- Criação facilitada

**Padrões:**
```tsx
// Full-screen feed
<Feed>
  {videos.map(video => (
    <VideoSection key={video.id} className="h-screen">
      <Video src={video.url} />
      <Overlay>
        <LikeButton />
        <CommentButton />
        <ShareButton />
      </Overlay>
    </VideoSection>
  ))}
</Feed>
```

**Lições:**
- Full-screen imersivo
- Gestos naturais (swipe)
- Algorithm > social graph

---

### 15. Duolingo

**Features Notáveis:**
- Gamificação (streaks, XP, leagues)
- Progress tracking claro
- Daily goals
- Notifications push
- Social features (friends, leagues)

**UX Highlights:**
- Gamificação funciona
- Progresso visível motiva
- Notifications eficazes (não irritantes)

**Padrões:**
```tsx
// Progress tracking
<ProgressBar current={xp} max={dailyGoal} />
<Streak days={streak} />

// Gamification
<Badge earned={badges} />
<League rank={leagueRank} />
```

**Lições:**
- Gamificação aumenta retenção
- Progresso visível motiva
- Notifications com propósito

---

## Matriz de Features

| Feature | Panini | Netflix | Linear | Notion | Instagram |
|---|---|---|---|---|---|
| Grid de Cards | ✅ | ✅ | ✅ | ✅ | ✅ |
| Filtros | ✅ | ✅ | ❌ | ✅ | ❌ |
| Carrossel | ❌ | ✅ | ✅ | ❌ | ✅ |
| Feed Infinito | ❌ | ✅ | ❌ | ✅ | ✅ |
| Bottom Nav | ❌ | ❌ | ❌ | ❌ | ✅ |
| Sidebar | ❌ | ❌ | ✅ | ✅ | ❌ |
| Hero 3D | ❌ | ❌ | ✅ | ❌ | ❌ |
| Gamification | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Checklist de Implementação

### E-commerce

- [ ] Grid de produtos responsivo
- [ ] Filtros laterais (mobile: drawer)
- [ ] Card de produto com hover
- [ ] Badge de lançamento/promoção
- [ ] Carrinho persistente
- [ ] Checkout simplificado

### Streaming

- [ ] Hero com autoplay
- [ ] Carrosséis horizontais
- [ ] Feed infinito
- [ ] Mini player
- [ ] Bottom nav (mobile)
- [ ] Sidebar (desktop)

### Landing Page

- [ ] Hero impactante
- [ ] Social proof (logos, testimonials)
- [ ] Features em grid
- [ ] CTAs claros
- [ ] Scroll animations sutis

### Dashboard

- [ ] Sidebar de navegação
- [ ] Multi-view (table, board, etc.)
- [ ] Block-based editor (se aplicável)
- [ ] Collaboration features
- [ ] Templates

### Mobile App

- [ ] Bottom nav (3-5 items)
- [ ] Gestos (swipe, tap)
- [ ] Feed infinito
- [ ] Progress tracking
- [ ] Gamification (se aplicável)

---

## Referências

- [3d-web-guidelines.md](./3d-web-guidelines.md)
- [frontend-libraries.md](./frontend-libraries.md)
- [ui-patterns/menus.md](../ui-patterns/menus.md)