# Empty States — Estados Vazios

## Visão Geral

Este guia define os padrões de empty states para projetos web mobile-first.

---

## Quando Usar

**Use empty states quando:**
- Lista ou coleção está vazia
- Nenhum resultado de busca
- Primeira vez do usuário
- Filtros não retornam resultados
- Erro que resulta em dados vazios

**Não use quando:**
- Loading state é mais apropriado
- Error state deve ser mostrado
- Dados estão sendo carregados

---

## Tipos de Empty State

### 1. Empty State de Lista

**Quando usar:**
- Lista de itens vazia
- Coleção pessoal vazia
- Histórico vazio

**Estrutura:**

```tsx
// src/components/ui/EmptyState.tsx
import { cn } from '@/lib/utils'

interface EmptyStateProps {
  icon?: React.ReactNode
  title: string
  description?: string
  action?: React.ReactNode
  className?: string
}

export function EmptyState({ icon, title, description, action, className }: EmptyStateProps) {
  return (
    <div
      className={cn(
        'flex flex-col items-center justify-center text-center p-8',
        className
      )}
    >
      {icon && (
        <div className="mb-4 text-muted-foreground">
          {icon}
        </div>
      )}
      
      <h3 className="text-lg font-medium mb-2">{title}</h3>
      
      {description && (
        <p className="text-muted-foreground text-sm max-w-sm mb-4">
          {description}
        </p>
      )}
      
      {action && (
        <div className="mt-2">
          {action}
        </div>
      )}
    </div>
  )
}
```

**Exemplos de Uso:**

```tsx
// Lista de quadrinhos vazia
import { BookOpen } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from '@/components/ui/EmptyState'
import Link from 'next/link'

function ComicsList({ comics }) {
  if (comics.length === 0) {
    return (
      <EmptyState
        icon={<BookOpen className="w-16 h-16" />}
        title="Nenhum quadrinho encontrado"
        description="Comece explorando nossa coleção de quadrinhos."
        action={
          <Button asChild>
            <Link href="/explorar">Explorar Quadrinhos</Link>
          </Button>
        }
      />
    )
  }
  
  return <ComicsGrid comics={comics} />
}
```

```tsx
// Coleção pessoal vazia
import { Bookmark } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from '@/components/ui/EmptyState'
import Link from 'next/link'

function MyCollection({ comics }) {
  if (comics.length === 0) {
    return (
      <EmptyState
        icon={<Bookmark className="w-16 h-16" />}
        title="Sua coleção está vazia"
        description="Adicione quadrinhos à sua coleção para acompanhá-los."
        action={
          <Button asChild>
            <Link href="/explorar">Explorar Quadrinhos</Link>
          </Button>
        }
      />
    )
  }
  
  return <ComicsGrid comics={comics} />
}
```

---

### 2. Empty State de Busca

**Quando usar:**
- Busca sem resultados
- Filtros muito restritivos

**Estrutura:**

```tsx
// src/components/ui/EmptySearch.tsx
import { Search, X } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from './EmptyState'

interface EmptySearchProps {
  query: string
  onClear: () => void
}

export function EmptySearch({ query, onClear }: EmptySearchProps) {
  return (
    <EmptyState
      icon={<Search className="w-16 h-16" />}
      title="Nenhum resultado encontrado"
      description={
        query
          ? `Não encontramos resultados para "${query}". Tente outros termos.`
          : 'Tente ajustar os filtros para encontrar o que procura.'
      }
      action={
        query && (
          <Button variant="outline" onClick={onClear}>
            <X className="w-4 h-4 mr-2" />
            Limpar busca
          </Button>
        )
      }
    />
  )
}

// Uso
function SearchResults({ results, query, onClearFilters }) {
  if (results.length === 0) {
    return <EmptySearch query={query} onClear={onClearFilters} />
  }
  
  return <ComicsGrid comics={results} />
}
```

---

### 3. Empty State Onboarding

**Quando usar:**
- Primeira vez do usuário
- Feature não utilizada
- Guiar usuário para ação

**Estrutura:**

```tsx
// src/components/ui/OnboardingEmpty.tsx
import { EmptyState } from './EmptyState'

interface OnboardingStep {
  icon: React.ReactNode
  title: string
  description: string
  action?: React.ReactNode
}

interface OnboardingEmptyProps {
  steps: OnboardingStep[]
  className?: string
}

export function OnboardingEmpty({ steps, className }: OnboardingEmptyProps) {
  return (
    <div className={cn('grid gap-6 md:grid-cols-2 lg:grid-cols-3', className)}>
      {steps.map((step, index) => (
        <EmptyState
          key={index}
          icon={step.icon}
          title={step.title}
          description={step.description}
          action={step.action}
          className="border rounded-lg bg-card"
        />
      ))}
    </div>
  )
}

// Uso
function DashboardOnboarding() {
  const steps = [
    {
      icon: <Search className="w-16 h-16" />,
      title: 'Explore quadrinhos',
      description: 'Descubra milhares de quadrinhos de diversas editoras.',
      action: (
        <Button asChild>
          <Link href="/explorar">Começar a explorar</Link>
        </Button>
      ),
    },
    {
      icon: <Bookmark className="w-16 h-16" />,
      title: 'Crie sua coleção',
      description: 'Adicione quadrinhos à sua coleção pessoal.',
      action: null,
    },
    {
      icon: <Bell className="w-16 h-16" />,
      title: 'Receba notificações',
      description: 'Seja avisado sobre novos lançamentos.',
      action: null,
    },
  ]
  
  return <OnboardingEmpty steps={steps} />
}
```

---

### 4. Empty State de Filtros

**Quando usar:**
- Filtros aplicados sem resultados
- Combinar múltiplos filtros

**Estrutura:**

```tsx
// src/components/ui/EmptyFilters.tsx
import { SlidersHorizontal, X } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from './EmptyState'

interface EmptyFiltersProps {
  filters: Record<string, any>
  onClear: () => void
}

export function EmptyFilters({ filters, onClear }: EmptyFiltersProps) {
  const filterCount = Object.keys(filters).filter(key => filters[key]).length
  
  return (
    <EmptyState
      icon={<SlidersHorizontal className="w-16 h-16" />}
      title="Nenhum resultado com esses filtros"
      description={
        filterCount > 0
          ? `Você aplicou ${filterCount} filtro(s). Tente remover alguns filtros.`
          : 'Tente ajustar os filtros para encontrar o que procura.'
      }
      action={
        <Button variant="outline" onClick={onClear}>
          <X className="w-4 h-4 mr-2" />
          Limpar filtros
        </Button>
      }
    />
  )
}

// Uso
function FilteredComics({ comics, filters, onClearFilters }) {
  if (comics.length === 0) {
    return <EmptyFilters filters={filters} onClear={onClearFilters} />
  }
  
  return <ComicsGrid comics={comics} />
}
```

---

## Exemplos por Contexto

### Coleção Pessoal

```tsx
// src/components/features/comics/EmptyCollection.tsx
import { Bookmark, Search, Heart } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from '@/components/ui/EmptyState'
import Link from 'next/link'

export function EmptyCollection() {
  return (
    <EmptyState
      icon={<Bookmark className="w-16 h-16" />}
      title="Sua coleção está vazia"
      description="Adicione quadrinhos à sua coleção para acompanhá-los e acessá-los rapidamente."
      action={
        <div className="flex gap-4">
          <Button asChild>
            <Link href="/explorar">
              <Search className="w-4 h-4 mr-2" />
              Explorar
            </Link>
          </Button>
          <Button variant="outline" asChild>
            <Link href="/favoritos">
              <Heart className="w-4 h-4 mr-2" />
              Ver Favoritos
            </Link>
          </Button>
        </div>
      }
    />
  )
}
```

---

### Histórico

```tsx
// src/components/features/history/EmptyHistory.tsx
import { Clock } from 'lucide-react'
import { EmptyState } from '@/components/ui/EmptyState'

export function EmptyHistory() {
  return (
    <EmptyState
      icon={<Clock className="w-16 h-16" />}
      title="Nenhum histórico"
      description="Os quadrinhos que você visualizar aparecerão aqui."
    />
  )
}
```

---

### Favoritos

```tsx
// src/components/features/favorites/EmptyFavorites.tsx
import { Heart } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from '@/components/ui/EmptyState'
import Link from 'next/link'

export function EmptyFavorites() {
  return (
    <EmptyState
      icon={<Heart className="w-16 h-16" />}
      title="Nenhum favorito"
      description="Marque quadrinhos como favoritos para acessá-los rapidamente."
      action={
        <Button asChild>
          <Link href="/explorar">Explorar Quadrinhos</Link>
        </Button>
      }
    />
  )
}
```

---

### Notificações

```tsx
// src/components/features/notifications/EmptyNotifications.tsx
import { Bell } from 'lucide-react'
import { EmptyState } from '@/components/ui/EmptyState'

export function EmptyNotifications() {
  return (
    <EmptyState
      icon={<Bell className="w-16 h-16" />}
      title="Nenhuma notificação"
      description="Você não tem notificações no momento."
    />
  )
}
```

---

### Mensagens

```tsx
// src/components/features/messages/EmptyMessages.tsx
import { MessageSquare } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { EmptyState } from '@/components/ui/EmptyState'

export function EmptyMessages() {
  return (
    <EmptyState
      icon={<MessageSquare className="w-16 h-16" />}
      title="Nenhuma mensagem"
      description="Comece uma conversa com outros usuários."
      action={
        <Button>
          Nova Mensagem
        </Button>
      }
    />
  )
}
```

---

## Ilustrações

### Quando Usar Ilustrações

**Use ilustrações quando:**
- Branding permite
- Quer criar conexão emocional
- Onboarding ou primeira experiência

**Não use quando:**
- Performance crítica
- Design minimalista
- Contexto sério (erros críticos)

### Exemplo com Ilustração

```tsx
// src/components/ui/EmptyStateWithIllustration.tsx
import Image from 'next/image'
import { EmptyState } from './EmptyState'

interface EmptyStateWithIllustrationProps {
  illustration: string
  title: string
  description?: string
  action?: React.ReactNode
}

export function EmptyStateWithIllustration({ illustration, title, description, action }: EmptyStateWithIllustrationProps) {
  return (
    <EmptyState
      icon={
        <div className="relative w-32 h-32 mb-4">
          <Image
            src={illustration}
            alt=""
            fill
            className="object-contain"
          />
        </div>
      }
      title={title}
      description={description}
      action={action}
    />
  )
}

// Uso
<EmptyStateWithIllustration
  illustration="/illustrations/empty-collection.svg"
  title="Sua coleção está vazia"
  description="Adicione quadrinhos para começar."
  action={<Button>Começar</Button>}
/>
```

---

## Acessibilidade

### Checklist

- [ ] Texto alternativo em ilustrações
- [ ] Contraste adequado
- [ ] Focus em botões de ação
- [ ] Screen reader friendly
- [ ] Não depender apenas de ícones

### Exemplo: ARIA

```tsx
<EmptyState
  icon={
    <div role="img" aria-label="Coleção vazia">
      <Bookmark className="w-16 h-16" />
    </div>
  }
  title="Sua coleção está vazia"
  description="Adicione quadrinhos para começar."
  action={
    <Button aria-label="Explorar quadrinhos e adicionar à coleção">
      Explorar
    </Button>
  }
/>
```

---

## Performance

### Otimizações

- **SVG inline** para ícones
- **Lazy load** ilustrações
- **Static import** assets críticos
- **WebP** para imagens

### Exemplo: SVG Inline

```tsx
// Ao invés de importar imagem
<img src="/illustrations/empty.svg" />

// Use SVG inline
<svg viewBox="0 0 200 200" className="w-32 h-32">
  {/* SVG content */}
</svg>
```

---

## Referências

- [loading.md](./loading.md)
- [error.md](./error.md)
- [menus.md](./menus.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)