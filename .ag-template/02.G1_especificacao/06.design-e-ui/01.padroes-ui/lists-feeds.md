# Lists & Feeds — Listas e Feeds

## Visão Geral

Este guia define os padrões de listas e feeds para projetos web mobile-first.

---

## Lista Simples

**Quando usar:** Listas de itens simples.

**Estrutura:**

```tsx
// src/components/ui/SimpleList.tsx
interface SimpleListItem {
  id: string
  title: string
  subtitle?: string
  icon?: React.ReactNode
  onClick?: () => void
}

interface SimpleListProps {
  items: SimpleListItem[]
}

export function SimpleList({ items }: SimpleListProps) {
  return (
    <div className="divide-y">
      {items.map((item) => (
        <div
          key={item.id}
          className="flex items-center gap-3 p-4 hover:bg-accent cursor-pointer"
          onClick={item.onClick}
        >
          {item.icon && (
            <div className="flex-shrink-0">
              {item.icon}
            </div>
          )}
          
          <div className="flex-1 min-w-0">
            <p className="font-medium truncate">{item.title}</p>
            {item.subtitle && (
              <p className="text-sm text-muted-foreground truncate">{item.subtitle}</p>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}
```

**Uso:**

```tsx
import { Settings, User, Bell, Lock } from 'lucide-react'
import { SimpleList } from '@/components/ui/SimpleList'

const menuItems = [
  { id: 'profile', title: 'Perfil', icon: <User className="w-5 h-5" /> },
  { id: 'notifications', title: 'Notificações', icon: <Bell className="w-5 h-5" /> },
  { id: 'security', title: 'Segurança', icon: <Lock className="w-5 h-5" /> },
  { id: 'settings', title: 'Configurações', icon: <Settings className="w-5 h-5" /> },
]

<SimpleList items={menuItems} />
```

---

## Lista com Ações

**Quando usar:** Listas com ações (editar, excluir).

**Estrutura:**

```tsx
// src/components/ui/ActionList.tsx
import { MoreVertical, Edit, Trash2 } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { DropdownMenu } from '@/components/ui/DropdownMenu'

interface ActionListItem {
  id: string
  title: string
  subtitle?: string
  metadata?: string
}

interface ActionListProps {
  items: ActionListItem[]
  onEdit?: (id: string) => void
  onDelete?: (id: string) => void
}

export function ActionList({ items, onEdit, onDelete }: ActionListProps) {
  return (
    <div className="divide-y">
      {items.map((item) => (
        <div key={item.id} className="flex items-center gap-3 p-4">
          <div className="flex-1 min-w-0">
            <p className="font-medium truncate">{item.title}</p>
            {item.subtitle && (
              <p className="text-sm text-muted-foreground truncate">{item.subtitle}</p>
            )}
          </div>
          
          {item.metadata && (
            <span className="text-sm text-muted-foreground">{item.metadata}</span>
          )}
          
          <DropdownMenu
            items={[
              { label: 'Editar', icon: <Edit className="w-4 h-4" />, onClick: () => onEdit?.(item.id) },
              { label: 'Excluir', icon: <Trash2 className="w-4 h-4" />, onClick: () => onDelete?.(item.id) },
            ]}
          >
            <Button variant="ghost" size="icon">
              <MoreVertical className="w-5 h-5" />
            </Button>
          </DropdownMenu>
        </div>
      ))}
    </div>
  )
}
```

---

## Feed Infinito

**Quando usar:** Feeds tipo Instagram, Twitter.

**Estrutura:**

```tsx
// src/components/ui/InfiniteFeed.tsx
'use client'

import { useEffect, useRef } from 'react'
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'
import { ErrorState } from '@/components/ui/ErrorState'

interface InfiniteFeedProps<T> {
  items: T[]
  isLoading: boolean
  isLoadingMore: boolean
  hasMore: boolean
  error?: Error
  onLoadMore: () => void
  renderItem: (item: T, index: number) => React.ReactNode
  emptyComponent?: React.ReactNode
}

export function InfiniteFeed<T>({
  items,
  isLoading,
  isLoadingMore,
  hasMore,
  error,
  onLoadMore,
  renderItem,
  emptyComponent,
}: InfiniteFeedProps<T>) {
  const observerRef = useRef<IntersectionObserver | null>(null)
  const loadMoreRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    if (isLoading || !hasMore) return
    
    observerRef.current = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        onLoadMore()
      }
    })
    
    if (loadMoreRef.current) {
      observerRef.current.observe(loadMoreRef.current)
    }
    
    return () => observerRef.current?.disconnect()
  }, [isLoading, hasMore, onLoadMore])
  
  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-8">
        <LoadingSpinner />
      </div>
    )
  }
  
  if (error) {
    return <ErrorState error={error.message} onRetry={onLoadMore} />
  }
  
  if (items.length === 0) {
    return emptyComponent || <p className="text-center text-muted-foreground py-8">Nenhum item</p>
  }
  
  return (
    <div>
      {items.map((item, index) => renderItem(item, index))}
      
      {hasMore && (
        <div ref={loadMoreRef} className="flex items-center justify-center py-8">
          {isLoadingMore ? <LoadingSpinner /> : <p className="text-sm text-muted-foreground">Carregando mais...</p>}
        </div>
      )}
    </div>
  )
}
```

**Uso:**

```tsx
import { InfiniteFeed } from '@/components/ui/InfiniteFeed'
import { ComicCard } from '@/components/features/comics/ComicCard'

function ComicsFeed() {
  const { data, isLoading, isLoadingMore, hasNextPage, fetchNextPage, error } = useComicsInfinite()
  
  const comics = data?.pages.flatMap(page => page.comics) ?? []
  
  return (
    <InfiniteFeed
      items={comics}
      isLoading={isLoading}
      isLoadingMore={isLoadingMore}
      hasMore={hasNextPage}
      error={error}
      onLoadMore={fetchNextPage}
      renderItem={(comic) => (
        <div key={comic.id} className="p-4">
          <ComicCard comic={comic} />
        </div>
      )}
      emptyComponent={<EmptyComics />}
    />
  )
}
```

---

## Pull to Refresh

**Quando usar:** Mobile, atualizar feed.

**Estrutura:**

```tsx
// src/components/ui/PullToRefresh.tsx
'use client'

import { useState, useRef, useEffect } from 'react'
import { cn } from '@/lib/utils'

interface PullToRefreshProps {
  onRefresh: () => Promise<void>
  children: React.ReactNode
  threshold?: number
}

export function PullToRefresh({ onRefresh, children, threshold = 100 }: PullToRefreshProps) {
  const [isPulling, setIsPulling] = useState(false)
  const [pullDistance, setPullDistance] = useState(0)
  const startY = useRef<number | null>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    const container = containerRef.current
    if (!container) return
    
    const handleTouchStart = (e: TouchEvent) => {
      if (container.scrollTop === 0) {
        startY.current = e.touches[0].clientY
      }
    }
    
    const handleTouchMove = (e: TouchEvent) => {
      if (startY.current === null || container.scrollTop > 0) return
      
      const currentY = e.touches[0].clientY
      const distance = currentY - startY.current
      
      if (distance > 0) {
        e.preventDefault()
        setPullDistance(distance)
        setIsPulling(distance < threshold)
      }
    }
    
    const handleTouchEnd = async () => {
      if (pullDistance >= threshold) {
        await onRefresh()
      }
      setIsPulling(false)
      setPullDistance(0)
      startY.current = null
    }
    
    container.addEventListener('touchstart', handleTouchStart)
    container.addEventListener('touchmove', handleTouchMove)
    container.addEventListener('touchend', handleTouchEnd)
    
    return () => {
      container.removeEventListener('touchstart', handleTouchStart)
      container.removeEventListener('touchmove', handleTouchMove)
      container.removeEventListener('touchend', handleTouchEnd)
    }
  }, [onRefresh, threshold, pullDistance])
  
  return (
    <div ref={containerRef} className="relative h-full overflow-y-auto">
      {/* Pull indicator */}
      {isPulling && (
        <div
          className="absolute top-0 left-0 right-0 flex items-center justify-center py-2 bg-muted z-10"
          style={{ height: pullDistance }}
        >
          <span className="text-sm text-muted-foreground">
            {pullDistance >= threshold ? 'Libere para atualizar' : 'Puxe para atualizar'}
          </span>
        </div>
      )}
      
      {children}
    </div>
  )
}
```

**Uso:**

```tsx
import { PullToRefresh } from '@/components/ui/PullToRefresh'
import { ComicsFeed } from '@/components/features/comics/ComicsFeed'

function ComicsPage() {
  const { refetch } = useComics()
  
  return (
    <PullToRefresh onRefresh={refetch}>
      <ComicsFeed />
    </PullToRefresh>
  )
}
```

---

## Load More Button

**Quando usar:** Alternativa ao infinite scroll.

**Estrutura:**

```tsx
// src/components/ui/LoadMoreButton.tsx
import { Button } from '@/components/ui/Button'
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'

interface LoadMoreButtonProps {
  onLoadMore: () => void
  isLoading: boolean
  hasMore: boolean
}

export function LoadMoreButton({ onLoadMore, isLoading, hasMore }: LoadMoreButtonProps) {
  if (!hasMore) return null
  
  return (
    <div className="flex items-center justify-center py-8">
      <Button
        variant="outline"
        onClick={onLoadMore}
        disabled={isLoading}
      >
        {isLoading ? (
          <>
            <LoadingSpinner size="sm" className="mr-2" />
            Carregando...
          </>
        ) : (
          'Carregar mais'
        )}
      </Button>
    </div>
  )
}
```

**Uso:**

```tsx
import { LoadMoreButton } from '@/components/ui/LoadMoreButton'

function ComicsList() {
  const { data, isLoadingMore, hasNextPage, fetchNextPage } = useComics()
  
  return (
    <div>
      <ComicsGrid comics={data.comics} />
      <LoadMoreButton
        onLoadMore={fetchNextPage}
        isLoading={isLoadingMore}
        hasMore={hasNextPage}
      />
    </div>
  )
}
```

---

## Grid Responsivo

**Quando usar:** Cards em grid.

**Estrutura:**

```tsx
// src/components/ui/ResponsiveGrid.tsx
import { cn } from '@/lib/utils'

interface ResponsiveGridProps {
  children: React.ReactNode
  columns?: 2 | 3 | 4
  gap?: 'sm' | 'md' | 'lg'
  className?: string
}

const columnsClasses = {
  2: 'grid-cols-2',
  3: 'grid-cols-2 md:grid-cols-3',
  4: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-4',
}

const gapClasses = {
  sm: 'gap-2',
  md: 'gap-4',
  lg: 'gap-6',
}

export function ResponsiveGrid({ children, columns = 4, gap = 'md', className }: ResponsiveGridProps) {
  return (
    <div className={cn('grid', columnsClasses[columns], gapClasses[gap], className)}>
      {children}
    </div>
  )
}
```

**Uso:**

```tsx
import { ResponsiveGrid } from '@/components/ui/ResponsiveGrid'
import { ComicCard } from '@/components/features/comics/ComicCard'

<ResponsiveGrid columns={4} gap="md">
  {comics.map(comic => (
    <ComicCard key={comic.id} comic={comic} />
  ))}
</ResponsiveGrid>
```

---

## Referências

- [cards.md](./cards.md)
- [tables-data.md](./tables-data.md)
- [loading.md](./loading.md)