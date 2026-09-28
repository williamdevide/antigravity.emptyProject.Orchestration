# Loading States — Estados de Carregamento

## Visão Geral

Este guia define os padrões de loading states para projetos web mobile-first.

---

## Tipos de Loading

### 1. Loading Spinner

**Quando usar:**
- Carregamento indefinido
- Ações em andamento
- Feedback imediato

**Estrutura:**

```tsx
// src/components/ui/LoadingSpinner.tsx
import { cn } from '@/lib/utils'

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

export function LoadingSpinner({ size = 'md', className }: LoadingSpinnerProps) {
  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12',
  }
  
  return (
    <div
      className={cn(
        'animate-spin rounded-full border-2 border-muted border-t-foreground',
        sizeClasses[size],
        className
      )}
      role="status"
      aria-label="Carregando"
    />
  )
}
```

**Uso:**

```tsx
// Botão com loading
<Button disabled={isPending}>
  {isPending && <LoadingSpinner size="sm" className="mr-2" />}
  {isPending ? 'Salvando...' : 'Salvar'}
</Button>

// Overlay de loading
{isLoading && (
  <div className="fixed inset-0 bg-background/80 backdrop-blur-sm z-50 flex items-center justify-center">
    <LoadingSpinner size="lg" />
  </div>
)}
```

---

### 2. Skeleton

**Quando usar:**
- Carregamento de conteúdo
- Reduzir percepção de espera
- Layout conhecido

**Estrutura:**

```tsx
// src/components/ui/Skeleton.tsx
import { cn } from '@/lib/utils'

interface SkeletonProps {
  className?: string
}

export function Skeleton({ className }: SkeletonProps) {
  return (
    <div
      className={cn(
        'animate-pulse rounded-md bg-muted',
        className
      )}
    />
  )
}
```

**Exemplos de Uso:**

```tsx
// Card Skeleton
<div className="space-y-2">
  <Skeleton className="w-full h-40 rounded" />
  <Skeleton className="w-3/4 h-4" />
  <Skeleton className="w-1/2 h-4" />
</div>

// Lista Skeleton
<div className="space-y-4">
  {Array.from({ length: 5 }).map((_, i) => (
    <div key={i} className="flex items-center gap-4">
      <Skeleton className="w-12 h-12 rounded-full" />
      <div className="space-y-2 flex-1">
        <Skeleton className="w-3/4 h-4" />
        <Skeleton className="w-1/2 h-4" />
      </div>
    </div>
  ))}
</div>

// Tabela Skeleton
<div className="space-y-2">
  {Array.from({ length: 10 }).map((_, i) => (
    <div key={i} className="flex items-center gap-4">
      <Skeleton className="w-8 h-8 rounded" />
      <Skeleton className="flex-1 h-4" />
      <Skeleton className="w-20 h-4" />
    </div>
  ))}
</div>
```

---

### 3. Progress Bar

**Quando usar:**
- Carregamento com progresso conhecido
- Upload de arquivos
- Processos em etapas

**Estrutura:**

```tsx
// src/components/ui/ProgressBar.tsx
import { cn } from '@/lib/utils'

interface ProgressBarProps {
  value: number
  max?: number
  showLabel?: boolean
  className?: string
}

export function ProgressBar({ value, max = 100, showLabel, className }: ProgressBarProps) {
  const percentage = Math.min((value / max) * 100, 100)
  
  return (
    <div className={cn('w-full', className)}>
      <div className="bg-muted rounded-full h-2 overflow-hidden">
        <div
          className="bg-primary h-2 rounded-full transition-all duration-300"
          style={{ width: `${percentage}%` }}
          role="progressbar"
          aria-valuenow={value}
          aria-valuemin={0}
          aria-valuemax={max}
        />
      </div>
      
      {showLabel && (
        <p className="text-xs text-muted-foreground mt-1 text-right">
          {Math.round(percentage)}%
        </p>
      )}
    </div>
  )
}
```

**Uso:**

```tsx
// Upload com progresso
function FileUpload() {
  const [progress, setProgress] = useState(0)
  
  const handleUpload = async (file: File) => {
    const formData = new FormData()
    formData.append('file', file)
    
    const xhr = new XMLHttpRequest()
    
    xhr.upload.addEventListener('progress', (e) => {
      if (e.lengthComputable) {
        const percentage = (e.loaded / e.total) * 100
        setProgress(percentage)
      }
    })
    
    xhr.addEventListener('load', () => {
      setProgress(100)
    })
    
    xhr.open('POST', '/api/upload')
    xhr.send(formData)
  }
  
  return (
    <div className="space-y-2">
      <input type="file" onChange={(e) => handleUpload(e.target.files[0])} />
      {progress > 0 && (
        <ProgressBar value={progress} showLabel />
      )}
    </div>
  )
}
```

---

### 4. Shimmer

**Quando usar:**
- Carregamento de imagens
- Conteúdo rico
- Efeito visual mais elaborado

**Estrutura:**

```tsx
// src/components/ui/Shimmer.tsx
import { cn } from '@/lib/utils'

interface ShimmerProps {
  className?: string
  children?: React.ReactNode
}

export function Shimmer({ className, children }: ShimmerProps) {
  return (
    <div
      className={cn(
        'relative overflow-hidden bg-muted',
        'before:absolute before:inset-0 before:-translate-x-full',
        'before:animate-[shimmer_1.5s_infinite]',
        'before:bg-gradient-to-r before:from-transparent before:via-white/10 before:to-transparent',
        className
      )}
    >
      {children}
    </div>
  )
}
```

**CSS Animation:**

```css
/* src/app/globals.css */
@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
```

**Uso:**

```tsx
// Image com shimmer
<div className="relative">
  <Shimmer className="w-full h-64 rounded" />
  <img
    src={comic.urlCapa}
    alt={comic.titulo}
    className="absolute inset-0 w-full h-64 object-cover rounded"
    onLoad={(e) => e.currentTarget.previousSibling.remove()}
  />
</div>
```

---

## Loading por Contexto

### Page Loading

```tsx
// src/components/layout/PageLoader.tsx
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'

export function PageLoader() {
  return (
    <div className="flex items-center justify-center min-h-[400px]">
      <LoadingSpinner size="lg" />
    </div>
  )
}

// Uso em páginas
export default function ComicsPage() {
  const { data, isLoading } = useComics()
  
  if (isLoading) {
    return <PageLoader />
  }
  
  return <ComicsList comics={data} />
}
```

---

### Card Loading

```tsx
// src/components/features/comics/ComicCardSkeleton.tsx
import { Skeleton } from '@/components/ui/Skeleton'

export function ComicCardSkeleton() {
  return (
    <div className="space-y-2">
      <Skeleton className="w-full h-64 rounded" />
      <Skeleton className="w-3/4 h-4" />
      <Skeleton className="w-1/2 h-4" />
    </div>
  )
}

// Uso em grid
export function ComicsGrid({ isLoading, comics }) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {isLoading
        ? Array.from({ length: 8 }).map((_, i) => (
            <ComicCardSkeleton key={i} />
          ))
        : comics.map((comic) => (
            <ComicCard key={comic.id} comic={comic} />
          ))
      }
    </div>
  )
}
```

---

### Button Loading

```tsx
// src/components/ui/Button.tsx (adicionar estado de loading)
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  isLoading?: boolean
}

export function Button({ children, isLoading, disabled, ...props }: ButtonProps) {
  return (
    <button
      disabled={disabled || isLoading}
      className={cn(
        'inline-flex items-center justify-center',
        'disabled:opacity-50 disabled:cursor-not-allowed',
        // ... outras classes
      )}
      {...props}
    >
      {isLoading && <LoadingSpinner size="sm" className="mr-2" />}
      {children}
    </button>
  )
}

// Uso
<Button isLoading={isSaving} onClick={handleSave}>
  {isSaving ? 'Salvando...' : 'Salvar'}
</Button>
```

---

### Form Loading

```tsx
// src/components/ui/FormLoader.tsx
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'

interface FormLoaderProps {
  message?: string
}

export function FormLoader({ message = 'Carregando...' }: FormLoaderProps) {
  return (
    <div className="flex flex-col items-center justify-center py-8">
      <LoadingSpinner size="md" />
      {message && (
        <p className="text-sm text-muted-foreground mt-2">{message}</p>
      )}
    </div>
  )
}

// Uso em forms
function SettingsForm() {
  const { data, isLoading } = useSettings()
  
  if (isLoading) {
    return <FormLoader message="Carregando configurações..." />
  }
  
  return <SettingsContent settings={data} />
}
```

---

### Infinite Scroll Loading

```tsx
// src/components/ui/InfiniteLoader.tsx
import { useEffect, useRef } from 'react'
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'

interface InfiniteLoaderProps {
  onLoadMore: () => void
  hasMore: boolean
  isLoading: boolean
}

export function InfiniteLoader({ onLoadMore, hasMore, isLoading }: InfiniteLoaderProps) {
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
  
  if (!hasMore) return null
  
  return (
    <div ref={loadMoreRef} className="flex items-center justify-center py-8">
      {isLoading && <LoadingSpinner size="md" />}
    </div>
  )
}

// Uso
export function ComicsInfiniteList() {
  const { data, isLoading, fetchNextPage, hasNextPage } = useComicsInfinite()
  
  const comics = data?.pages.flatMap(page => page.comics) ?? []
  
  return (
    <div>
      <ComicsGrid comics={comics} />
      <InfiniteLoader
        onLoadMore={fetchNextPage}
        hasMore={hasNextPage}
        isLoading={isLoading}
      />
    </div>
  )
}
```

---

## Acessibilidade

### Checklist

- [ ] `role="status"` em spinners
- [ ] `aria-label` descritivo
- [ ] `aria-busy="true"` em regiões carregando
- [ ] Contraste adequado
- [ ] Não depender apenas de cor
- [ ] Screen reader announcements

### Exemplo: ARIA

```tsx
// Spinner acessível
<div
  className="animate-spin rounded-full"
  role="status"
  aria-label="Carregando"
>
  <span className="sr-only">Carregando</span>
</div>

// Região com loading
<div aria-busy="true" aria-live="polite">
  {isLoading && <LoadingSpinner />}
  {content}
</div>

// Progress bar acessível
<div
  className="progress-bar"
  role="progressbar"
  aria-valuenow={progress}
  aria-valuemin={0}
  aria-valuemax={100}
  aria-label="Progresso do upload"
>
  <div style={{ width: `${progress}%` }} />
</div>
```

---

## Performance

### Otimizações

- **Lazy load** loaders pesados
- **Debounce** loading states
- **Skeleton** ao invés de spinner quando possível
- **Prefetch** dados antecipadamente

### Exemplo: Debounce Loading

```tsx
// Evitar flash de loading para cargas rápidas
function useDelayedLoading(isLoading: boolean, delay = 300) {
  const [showLoading, setShowLoading] = useState(false)
  
  useEffect(() => {
    if (isLoading) {
      const timer = setTimeout(() => setShowLoading(true), delay)
      return () => clearTimeout(timer)
    } else {
      setShowLoading(false)
    }
  }, [isLoading, delay])
  
  return showLoading
}

// Uso
function DataComponent() {
  const { data, isLoading } = useData()
  const showLoading = useDelayedLoading(isLoading)
  
  if (showLoading) {
    return <PageLoader />
  }
  
  return <DataContent data={data} />
}
```

---

## Referências

- [splash.md](./splash.md)
- [error.md](./error.md)
- [empty.md](./empty.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)