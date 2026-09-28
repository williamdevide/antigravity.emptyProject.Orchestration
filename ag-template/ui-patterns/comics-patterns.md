# Comics Patterns — Padrões Específicos para E-commerce de Quadrinhos

## Visão Geral

Este guia define padrões específicos para e-commerce de quadrinhos, baseado no ComixFlix e projetos similares.

---

## Comic Card Avançado

**Quando usar:** Card de quadrinho completo para e-commerce.

**Features:**
- Capa com hover zoom
- Título, editora, personagem
- Preço normal e promocional
- Badge de lançamento
- Botão de coleção
- Rating stars

**Estrutura:**

```tsx
// src/components/features/comics/AdvancedComicCard.tsx
'use client'

import { useState } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { Bookmark, BookmarkCheck, Star } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/Card'
import { Badge } from '@/components/ui/Badge'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface Comic {
  id: string
  titulo: string
  editora: string
  personagem?: string
  preco: number
  precoPromocional?: number
  urlCapa: string
  isLancamento?: boolean
  isInCollection?: boolean
  rating?: number
}

interface AdvancedComicCardProps {
  comic: Comic
  onAddToCollection?: (comicId: string) => void
  variant?: 'default' | 'compact' | 'featured'
}

export function AdvancedComicCard({ comic, onAddToCollection, variant = 'default' }: AdvancedComicCardProps) {
  const [isHovered, setIsHovered] = useState(false)
  
  const isFeatured = variant === 'featured'
  
  return (
    <Card
      className={cn(
        'overflow-hidden group',
        isFeatured && 'md:col-span-2 md:row-span-2'
      )}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      {/* Capa */}
      <div className={cn('relative overflow-hidden', isFeatured ? 'aspect-[3/4]' : 'aspect-[2/3]')}>
        <Link href={`/quadrinhos/${comic.id}`}>
          <Image
            src={comic.urlCapa}
            alt={comic.titulo}
            fill
            className={cn(
              'object-cover transition-transform duration-300',
              isHovered && 'scale-110'
            )}
          />
        </Link>
        
        {/* Badges */}
        <div className="absolute top-2 left-2 flex flex-col gap-1">
          {comic.isLancamento && (
            <Badge variant="primary" size="sm">
              Lançamento
            </Badge>
          )}
          {comic.rating && comic.rating >= 4.5 && (
            <Badge variant="success" size="sm">
              <Star className="w-3 h-3 mr-1 fill-current" />
              {comic.rating.toFixed(1)}
            </Badge>
          )}
        </div>
        
        {/* Botão de coleção */}
        {onAddToCollection && (
          <Button
            variant="ghost"
            size="icon"
            className={cn(
              'absolute top-2 right-2 bg-background/80 hover:bg-background transition-opacity',
              isHovered ? 'opacity-100' : 'opacity-0'
            )}
            onClick={() => onAddToCollection(comic.id)}
          >
            {comic.isInCollection ? (
              <BookmarkCheck className="w-4 h-4 text-primary" />
            ) : (
              <Bookmark className="w-4 h-4" />
            )}
          </Button>
        )}
      </div>
      
      {/* Conteúdo */}
      <CardContent className="p-3">
        {/* Editora e personagem */}
        <div className="flex items-center gap-2 mb-1 text-xs text-muted-foreground">
          <span>{comic.editora}</span>
          {comic.personagem && (
            <>
              <span>•</span>
              <span>{comic.personagem}</span>
            </>
          )}
        </div>
        
        {/* Título */}
        <Link href={`/quadrinhos/${comic.id}`}>
          <h3 className="font-medium text-sm line-clamp-2 hover:underline transition-colors">
            {comic.titulo}
          </h3>
        </Link>
        
        {/* Preço */}
        <div className="mt-2">
          {comic.precoPromocional && (
            <p className="text-xs text-muted-foreground line-through">
              R$ {comic.preco.toFixed(2)}
            </p>
          )}
          <p className="text-base font-bold text-primary">
            R$ {(comic.precoPromocional || comic.preco).toFixed(2)}
          </p>
        </div>
      </CardContent>
    </Card>
  )
}
```

---

## Comic List com Toggle View

**Quando usar:** Alternar entre grid e lista.

**Estrutura:**

```tsx
// src/components/features/comics/ComicListView.tsx
'use client'

import { useState } from 'react'
import { Grid, List } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { AdvancedComicCard } from './AdvancedComicCard'
import { ComicListItem } from './ComicListItem'

interface ComicListViewProps {
  comics: Comic[]
  onAddToCollection?: (comicId: string) => void
}

export function ComicListView({ comics, onAddToCollection }: ComicListViewProps) {
  const [view, setView] = useState<'grid' | 'list'>('grid')
  
  return (
    <div>
      {/* View toggle */}
      <div className="flex items-center justify-end gap-2 mb-4">
        <span className="text-sm text-muted-foreground">Visualizar:</span>
        <Button
          variant={view === 'grid' ? 'default' : 'outline'}
          size="icon"
          onClick={() => setView('grid')}
        >
          <Grid className="w-4 h-4" />
        </Button>
        <Button
          variant={view === 'list' ? 'default' : 'outline'}
          size="icon"
          onClick={() => setView('list')}
        >
          <List className="w-4 h-4" />
        </Button>
      </div>
      
      {/* Content */}
      {view === 'grid' ? (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {comics.map((comic) => (
            <AdvancedComicCard
              key={comic.id}
              comic={comic}
              onAddToCollection={onAddToCollection}
            />
          ))}
        </div>
      ) : (
        <div className="space-y-2">
          {comics.map((comic) => (
            <ComicListItem
              key={comic.id}
              comic={comic}
              onAddToCollection={onAddToCollection}
            />
          ))}
        </div>
      )}
    </div>
  )
}
```

---

## Comic List Item

**Quando usar:** View de lista para quadrinhos.

**Estrutura:**

```tsx
// src/components/features/comics/ComicListItem.tsx
import Image from 'next/image'
import Link from 'next/link'
import { Bookmark, BookmarkCheck } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/Card'
import { Badge } from '@/components/ui/Badge'
import { Button } from '@/components/ui/Button'

interface ComicListItemProps {
  comic: Comic
  onAddToCollection?: (comicId: string) => void
}

export function ComicListItem({ comic, onAddToCollection }: ComicListItemProps) {
  return (
    <Card>
      <CardContent className="p-4 flex gap-4">
        {/* Capa */}
        <div className="relative w-20 h-28 flex-shrink-0">
          <Link href={`/quadrinhos/${comic.id}`}>
            <Image
              src={comic.urlCapa}
              alt={comic.titulo}
              fill
              className="object-cover rounded"
            />
          </Link>
        </div>
        
        {/* Conteúdo */}
        <div className="flex-1 flex items-center justify-between">
          <div className="flex-1">
            {/* Editora e personagem */}
            <div className="flex items-center gap-2 text-xs text-muted-foreground mb-1">
              <span>{comic.editora}</span>
              {comic.personagem && (
                <>
                  <span>•</span>
                  <span>{comic.personagem}</span>
                </>
              )}
            </div>
            
            {/* Título */}
            <Link href={`/quadrinhos/${comic.id}`}>
              <h3 className="font-medium hover:underline">
                {comic.titulo}
              </h3>
            </Link>
            
            {/* Preço */}
            <div className="mt-2">
              {comic.precoPromocional && (
                <span className="text-sm text-muted-foreground line-through mr-2">
                  R$ {comic.preco.toFixed(2)}
                </span>
              )}
              <span className="text-lg font-bold text-primary">
                R$ {(comic.precoPromocional || comic.preco).toFixed(2)}
              </span>
            </div>
          </div>
          
          {/* Ações */}
          <div className="flex items-center gap-2">
            {onAddToCollection && (
              <Button
                variant="ghost"
                size="icon"
                onClick={() => onAddToCollection(comic.id)}
              >
                {comic.isInCollection ? (
                  <BookmarkCheck className="w-5 h-5 text-primary" />
                ) : (
                  <Bookmark className="w-5 h-5" />
                )}
              </Button>
            )}
            <Button asChild>
              <Link href={`/quadrinhos/${comic.id}`}>
                Ver Detalhes
              </Link>
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
```

---

## Collection Tracker

**Quando usar:** Mostrar progresso de leitura de série.

**Estrutura:**

```tsx
// src/components/features/comics/CollectionTracker.tsx
import { Book, CheckCircle } from 'lucide-react'
import { Progress } from '@/components/ui/Progress'
import { Badge } from '@/components/ui/Badge'

interface CollectionTrackerProps {
  totalIssues: number
  readIssues: number
  seriesTitle: string
}

export function CollectionTracker({ totalIssues, readIssues, seriesTitle }: CollectionTrackerProps) {
  const percentage = (readIssues / totalIssues) * 100
  const isComplete = readIssues >= totalIssues
  
  return (
    <div className="p-4 border rounded-lg">
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          {isComplete ? (
            <CheckCircle className="w-5 h-5 text-green-600" />
          ) : (
            <Book className="w-5 h-5 text-muted-foreground" />
          )}
          <span className="font-medium">{seriesTitle}</span>
        </div>
        
        <Badge variant={isComplete ? 'success' : 'default'}>
          {isComplete ? 'Completo' : `${readIssues}/${totalIssues}`}
        </Badge>
      </div>
      
      <Progress value={percentage} className="h-2" />
      
      <p className="text-xs text-muted-foreground mt-2">
        {percentage.toFixed(0)}% concluído
        {isComplete && ' - Parabéns!'}
      </p>
    </div>
  )
}
```

---

## Reading List

**Quando usar:** Lista de leitura/coleção pessoal.

**Estrutura:**

```tsx
// src/components/features/collection/ReadingList.tsx
import { CollectionTracker } from './CollectionTracker'
import { AdvancedComicCard } from './AdvancedComicCard'

interface ReadingListProps {
  series: Series[]
  comics: Comic[]
}

export function ReadingList({ series, comics }: ReadingListProps) {
  return (
    <div className="space-y-6">
      {/* Progresso das séries */}
      <section>
        <h2 className="text-lg font-bold mb-4">Minhas Séries</h2>
        <div className="grid gap-4 md:grid-cols-2">
          {series.map((s) => (
            <CollectionTracker
              key={s.id}
              totalIssues={s.totalIssues}
              readIssues={s.readIssues}
              seriesTitle={s.titulo}
            />
          ))}
        </div>
      </section>
      
      {/* Quadrinhos na coleção */}
      <section>
        <h2 className="text-lg font-bold mb-4">Quadrinhos na Coleção</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {comics.map((comic) => (
            <AdvancedComicCard
              key={comic.id}
              comic={comic}
              variant="compact"
            />
          ))}
        </div>
      </section>
    </div>
  )
}
```

---

## Publisher Filter

**Quando usar:** Filtro específico para editoras.

**Estrutura:**

```tsx
// src/components/features/comics/PublisherFilter.tsx
import Image from 'next/image'
import { Badge } from '@/components/ui/Badge'
import { cn } from '@/lib/utils'

interface Publisher {
  id: string
  nome: string
  logo?: string
  count: number
}

interface PublisherFilterProps {
  publishers: Publisher[]
  selectedPublisher?: string
  onSelect: (publisherId: string) => void
  onClear: () => void
}

export function PublisherFilter({ publishers, selectedPublisher, onSelect, onClear }: PublisherFilterProps) {
  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between">
        <h3 className="font-medium">Editoras</h3>
        {selectedPublisher && (
          <button
            onClick={onClear}
            className="text-xs text-muted-foreground hover:text-foreground"
          >
            Limpar
          </button>
        )}
      </div>
      
      <div className="grid grid-cols-3 gap-2">
        {publishers.map((publisher) => (
          <button
            key={publisher.id}
            onClick={() => onSelect(publisher.id)}
            className={cn(
              'p-2 border rounded-lg text-center transition-colors',
              selectedPublisher === publisher.id
                ? 'border-primary bg-primary/10'
                : 'hover:bg-muted'
            )}
          >
            {publisher.logo ? (
              <div className="relative w-12 h-12 mx-auto mb-1">
                <Image
                  src={publisher.logo}
                  alt={publisher.nome}
                  fill
                  className="object-contain"
                />
              </div>
            ) : (
              <p className="text-sm font-medium">{publisher.nome}</p>
            )}
            <Badge variant="default" size="sm" className="mt-1">
              {publisher.count}
            </Badge>
          </button>
        ))}
      </div>
    </div>
  )
}
```

---

## Referências

- [cards.md](./cards.md)
- [lists-feeds.md](./lists-feeds.md)
- [search-filter.md](./search-filter.md)
- [real-sites-inspiration.md](../guides/real-sites-inspiration.md)