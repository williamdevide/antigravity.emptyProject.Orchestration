# Cards — Componentes de Card

## Visão Geral

Este guia define os padrões de cards para projetos web mobile-first.

---

## Card Básico

**Quando usar:** Container de conteúdo genérico.

**Estrutura:**

```tsx
// src/components/ui/Card.tsx
import { cn } from '@/lib/utils'

interface CardProps {
  children: React.ReactNode
  className?: string
  hover?: boolean
  onClick?: () => void
}

export function Card({ children, className, hover, onClick }: CardProps) {
  return (
    <div
      className={cn(
        'rounded-lg border bg-card text-card-foreground shadow-sm',
        hover && 'cursor-pointer transition-shadow hover:shadow-md',
        className
      )}
      onClick={onClick}
    >
      {children}
    </div>
  )
}

export function CardHeader({ children, className }: { children: React.ReactNode; className?: string }) {
  return <div className={cn('p-4 border-b', className)}>{children}</div>
}

export function CardTitle({ children, className }: { children: React.ReactNode; className?: string }) {
  return <h3 className={cn('font-semibold text-lg', className)}>{children}</h3>
}

export function CardDescription({ children, className }: { children: React.ReactNode; className?: string }) {
  return <p className={cn('text-sm text-muted-foreground mt-1', className)}>{children}</p>
}

export function CardContent({ children, className }: { children: React.ReactNode; className?: string }) {
  return <div className={cn('p-4', className)}>{children}</div>
}

export function CardFooter({ children, className }: { children: React.ReactNode; className?: string }) {
  return <div className={cn('p-4 border-t bg-muted', className)}>{children}</div>
}
```

**Uso:**

```tsx
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'

<Card>
  <CardHeader>
    <CardTitle>Título do Card</CardTitle>
    <CardDescription>Descrição do card</CardDescription>
  </CardHeader>
  <CardContent>
    Conteúdo do card
  </CardContent>
  <CardFooter>
    <Button>Ação</Button>
  </CardFooter>
</Card>
```

---

## Comic Card (Produto)

**Quando usar:** E-commerce de quadrinhos.

**Estrutura:**

```tsx
// src/components/features/comics/ComicCard.tsx
import Image from 'next/image'
import Link from 'next/link'
import { Bookmark, BookmarkCheck } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/Card'
import { Badge } from '@/components/ui/Badge'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface Comic {
  id: string
  titulo: string
  editora: string
  preco: number
  precoPromocional?: number
  urlCapa: string
  isLancamento?: boolean
  isInCollection?: boolean
}

interface ComicCardProps {
  comic: Comic
  onAddToCollection?: (comicId: string) => void
  variant?: 'default' | 'compact' | 'horizontal'
}

export function ComicCard({ comic, onAddToCollection, variant = 'default' }: ComicCardProps) {
  const isHorizontal = variant === 'horizontal'
  
  return (
    <Card className={cn('overflow-hidden group', isHorizontal && 'flex')}>
      {/* Capa */}
      <div className={cn('relative', isHorizontal ? 'w-32 flex-shrink-0' : 'aspect-[2/3]')}>
        <Link href={`/quadrinhos/${comic.id}`}>
          <Image
            src={comic.urlCapa}
            alt={comic.titulo}
            fill
            className="object-cover transition-transform group-hover:scale-105"
          />
        </Link>
        
        {/* Badge de lançamento */}
        {comic.isLancamento && (
          <Badge className="absolute top-2 left-2" variant="primary">
            Lançamento
          </Badge>
        )}
        
        {/* Botão de coleção */}
        {onAddToCollection && (
          <Button
            variant="ghost"
            size="icon"
            className="absolute top-2 right-2 bg-background/80 hover:bg-background"
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
      <CardContent className={cn('p-4', isHorizontal && 'flex-1 flex flex-col justify-between')}>
        <div>
          {/* Editora */}
          <p className="text-xs text-muted-foreground mb-1">{comic.editora}</p>
          
          {/* Título */}
          <Link href={`/quadrinhos/${comic.id}`}>
            <h3 className="font-medium line-clamp-2 hover:underline">
              {comic.titulo}
            </h3>
          </Link>
        </div>
        
        {/* Preço */}
        <div className="mt-2">
          {comic.precoPromocional && (
            <p className="text-sm text-muted-foreground line-through">
              R$ {comic.preco.toFixed(2)}
            </p>
          )}
          <p className="text-lg font-bold">
            R$ {(comic.precoPromocional || comic.preco).toFixed(2)}
          </p>
        </div>
      </CardContent>
    </Card>
  )
}
```

**Uso:**

```tsx
// Grid de comics
<div className="grid grid-cols-2 md:grid-cols-4 gap-4">
  {comics.map(comic => (
    <ComicCard
      key={comic.id}
      comic={comic}
      onAddToCollection={handleAddToCollection}
    />
  ))}
</div>
```

---

## Content Card

**Quando usar:** Posts, artigos, conteúdo.

**Estrutura:**

```tsx
// src/components/ui/ContentCard.tsx
import Image from 'next/image'
import Link from 'next/link'
import { Calendar, Clock, User } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card'
import { Badge } from '@/components/ui/Badge'

interface ContentCardProps {
  title: string
  excerpt: string
  image?: string
  author?: string
  date?: string
  readTime?: string
  tags?: string[]
  href: string
}

export function ContentCard({ title, excerpt, image, author, date, readTime, tags, href }: ContentCardProps) {
  return (
    <Card className="overflow-hidden">
      {/* Imagem */}
      {image && (
        <Link href={href} className="block aspect-video relative">
          <Image
            src={image}
            alt={title}
            fill
            className="object-cover"
          />
        </Link>
      )}
      
      {/* Conteúdo */}
      <CardContent className="p-4">
        {/* Tags */}
        {tags && tags.length > 0 && (
          <div className="flex gap-2 mb-2">
            {tags.map(tag => (
              <Badge key={tag} variant="default" size="sm">
                {tag}
              </Badge>
            ))}
          </div>
        )}
        
        {/* Título */}
        <Link href={href}>
          <h3 className="font-semibold text-lg mb-2 hover:underline line-clamp-2">
            {title}
          </h3>
        </Link>
        
        {/* Excerpt */}
        <p className="text-sm text-muted-foreground mb-4 line-clamp-3">
          {excerpt}
        </p>
        
        {/* Meta */}
        {(author || date || readTime) && (
          <div className="flex items-center gap-4 text-xs text-muted-foreground">
            {author && (
              <div className="flex items-center gap-1">
                <User className="w-3 h-3" />
                <span>{author}</span>
              </div>
            )}
            {date && (
              <div className="flex items-center gap-1">
                <Calendar className="w-3 h-3" />
                <span>{date}</span>
              </div>
            )}
            {readTime && (
              <div className="flex items-center gap-1">
                <Clock className="w-3 h-3" />
                <span>{readTime}</span>
              </div>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  )
}
```

---

## Profile Card

**Quando usar:** Perfis de usuário.

**Estrutura:**

```tsx
// src/components/ui/ProfileCard.tsx
import Image from 'next/image'
import Link from 'next/link'
import { MapPin, Link as LinkIcon } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { Badge } from '@/components/ui/Badge'

interface ProfileCardProps {
  avatar: string
  name: string
  username: string
  bio?: string
  location?: string
  website?: string
  followers?: number
  following?: number
  isFollowing?: boolean
  onFollow?: () => void
}

export function ProfileCard({ avatar, name, username, bio, location, website, followers, following, isFollowing, onFollow }: ProfileCardProps) {
  return (
    <Card>
      {/* Header com background */}
      <div className="h-24 bg-gradient-to-r from-primary/20 to-primary/40" />
      
      <CardContent className="relative px-4 pb-4">
        {/* Avatar */}
        <div className="relative -mt-12 mb-3">
          <div className="relative w-24 h-24 rounded-full border-4 border-background overflow-hidden">
            <Image src={avatar} alt={name} fill className="object-cover" />
          </div>
        </div>
        
        {/* Nome e username */}
        <div className="mb-2">
          <h3 className="font-bold text-lg">{name}</h3>
          <p className="text-sm text-muted-foreground">@{username}</p>
        </div>
        
        {/* Bio */}
        {bio && (
          <p className="text-sm mb-3">{bio}</p>
        )}
        
        {/* Meta info */}
        <div className="flex items-center gap-4 text-sm text-muted-foreground mb-4">
          {location && (
            <div className="flex items-center gap-1">
              <MapPin className="w-4 h-4" />
              <span>{location}</span>
            </div>
          )}
          {website && (
            <Link href={website} className="flex items-center gap-1 hover:text-foreground">
              <LinkIcon className="w-4 h-4" />
              <span>Website</span>
            </Link>
          )}
        </div>
        
        {/* Followers/Following */}
        {(followers || following) && (
          <div className="flex gap-4 mb-4">
            {followers !== undefined && (
              <div>
                <span className="font-bold">{followers}</span>{' '}
                <span className="text-sm text-muted-foreground">seguidores</span>
              </div>
            )}
            {following !== undefined && (
              <div>
                <span className="font-bold">{following}</span>{' '}
                <span className="text-sm text-muted-foreground">seguindo</span>
              </div>
            )}
          </div>
        )}
        
        {/* Follow button */}
        {onFollow && (
          <Button
            variant={isFollowing ? 'outline' : 'default'}
            className="w-full"
            onClick={onFollow}
          >
            {isFollowing ? 'Seguindo' : 'Seguir'}
          </Button>
        )}
      </CardContent>
    </Card>
  )
}
```

---

## Stat Card

**Quando usar:** Dashboards, métricas.

**Estrutura:**

```tsx
// src/components/ui/StatCard.tsx
import { cn } from '@/lib/utils'

interface StatCardProps {
  title: string
  value: string | number
  change?: number
  changeLabel?: string
  icon?: React.ReactNode
  trend?: 'up' | 'down' | 'neutral'
}

export function StatCard({ title, value, change, changeLabel, icon, trend = 'neutral' }: StatCardProps) {
  const isUp = trend === 'up'
  const isDown = trend === 'down'
  
  return (
    <div className="rounded-lg border bg-card p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-muted-foreground mb-1">{title}</p>
          <p className="text-2xl font-bold">{value}</p>
          
          {change !== undefined && (
            <div className="flex items-center gap-1 mt-2">
              <span className={cn('text-sm font-medium', isUp && 'text-green-600', isDown && 'text-red-600')}>
                {isUp && '↑'}{isDown && '↓'}{Math.abs(change)}%
              </span>
              {changeLabel && (
                <span className="text-xs text-muted-foreground">{changeLabel}</span>
              )}
            </div>
          )}
        </div>
        
        {icon && (
          <div className="p-3 rounded-full bg-muted">
            {icon}
          </div>
        )}
      </div>
    </div>
  )
}
```

**Uso:**

```tsx
import { DollarSign, Users, ShoppingCart } from 'lucide-react'
import { StatCard } from '@/components/ui/StatCard'

<div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
  <StatCard
    title="Receita Total"
    value="R$ 45.231,89"
    change={20.1}
    changeLabel="vs mês passado"
    icon={<DollarSign className="w-6 h-6" />}
    trend="up"
  />
  <StatCard
    title="Usuários Ativos"
    value="2.350"
    change={15.3}
    changeLabel="vs mês passado"
    icon={<Users className="w-6 h-6" />}
    trend="up"
  />
  <StatCard
    title="Vendas"
    value="12.234"
    change={-5.4}
    changeLabel="vs mês passado"
    icon={<ShoppingCart className="w-6 h-6" />}
    trend="down"
  />
</div>
```

---

## Referências

- [lists-feeds.md](./lists-feeds.md)
- [tables-data.md](./tables-data.md)
- [forms.md](./forms.md)