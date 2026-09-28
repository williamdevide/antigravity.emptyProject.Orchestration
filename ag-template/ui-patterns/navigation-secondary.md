# Navigation Secondary — Tabs, Breadcrumbs, Pagination, Stepper

## Visão Geral

Este guia define os padrões de navegação secundária para projetos web mobile-first.

---

## Tabs

**Quando usar:**
- Alternar entre views relacionadas
- Organizar conteúdo em categorias
- Forms multi-step

**Estrutura:**

```tsx
// src/components/ui/Tabs.tsx
'use client'

import * as TabsPrimitive from '@radix-ui/react-tabs'
import { cn } from '@/lib/utils'

interface TabsProps {
  defaultValue: string
  value?: string
  onValueChange?: (value: string) => void
  children: React.ReactNode
  orientation?: 'horizontal' | 'vertical'
}

export function Tabs({ defaultValue, value, onValueChange, children, orientation = 'horizontal' }: TabsProps) {
  return (
    <TabsPrimitive.Root
      defaultValue={defaultValue}
      value={value}
      onValueChange={onValueChange}
      orientation={orientation}
    >
      {children}
    </TabsPrimitive.Root>
  )
}

export function TabsList({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <TabsPrimitive.List
      className={cn(
        'inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground',
        className
      )}
    >
      {children}
    </TabsPrimitive.List>
  )
}

export function TabsTrigger({ value, children, className }: { value: string; children: React.ReactNode; className?: string }) {
  return (
    <TabsPrimitive.Trigger
      value={value}
      className={cn(
        'inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium',
        'ring-offset-background transition-all',
        'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
        'disabled:pointer-events-none disabled:opacity-50',
        'data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm',
        className
      )}
    >
      {children}
    </TabsPrimitive.Trigger>
  )
}

export function TabsContent({ value, children, className }: { value: string; children: React.ReactNode; className?: string }) {
  return (
    <TabsPrimitive.Content
      value={value}
      className={cn(
        'mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
        className
      )}
    >
      {children}
    </TabsPrimitive.Content>
  )
}
```

**Uso:**

```tsx
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/Tabs'

<Tabs defaultValue="comics" className="w-full">
  <TabsList>
    <TabsTrigger value="comics">Quadrinhos</TabsTrigger>
    <TabsTrigger value="series">Séries</TabsTrigger>
    <TabsTrigger value="autores">Autores</TabsTrigger>
  </TabsList>
  <TabsContent value="comics">
    <ComicsList />
  </TabsContent>
  <TabsContent value="series">
    <SeriesList />
  </TabsContent>
  <TabsContent value="autores">
    <AuthorsList />
  </TabsContent>
</Tabs>
```

---

## Breadcrumb

**Quando usar:**
- Navegação hierárquica
- Mostrar localização atual
- Navegação rápida para níveis superiores

**Estrutura:**

```tsx
// src/components/ui/Breadcrumb.tsx
import { ChevronRight, Home } from 'lucide-react'
import Link from 'next/link'
import { cn } from '@/lib/utils'

interface BreadcrumbItem {
  label: string
  href?: string
}

interface BreadcrumbProps {
  items: BreadcrumbItem[]
  homeHref?: string
  className?: string
}

export function Breadcrumb({ items, homeHref = '/', className }: BreadcrumbProps) {
  return (
    <nav className={cn('flex items-center text-sm text-muted-foreground', className)} aria-label="Breadcrumb">
      {/* Home link */}
      <Link
        href={homeHref}
        className="flex items-center hover:text-foreground transition-colors"
      >
        <Home className="w-4 h-4" />
      </Link>
      
      {/* Items */}
      {items.map((item, index) => (
        <div key={index} className="flex items-center">
          <ChevronRight className="w-4 h-4 mx-1" />
          
          {item.href ? (
            <Link
              href={item.href}
              className="hover:text-foreground transition-colors"
            >
              {item.label}
            </Link>
          ) : (
            <span className="text-foreground font-medium">{item.label}</span>
          )}
        </div>
      ))}
    </nav>
  )
}
```

**Uso:**

```tsx
import { Breadcrumb } from '@/components/ui/Breadcrumb'

<Breadcrumb
  items={[
    { label: 'Explorar', href: '/explorar' },
    { label: 'Quadrinhos', href: '/explorar/quadrinhos' },
    { label: 'Batman #1' },
  ]}
/>
```

---

## Pagination

**Quando usar:**
- Navegar entre páginas de dados
- Listas longas
- Resultados de busca

**Estrutura:**

```tsx
// src/components/ui/Pagination.tsx
import { ChevronLeft, ChevronRight, ChevronsLeft, ChevronsRight } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface PaginationProps {
  currentPage: number
  totalPages: number
  onPageChange: (page: number) => void
  siblingCount?: number
  className?: string
}

export function Pagination({ currentPage, totalPages, onPageChange, siblingCount = 1, className }: PaginationProps) {
  const pages = []
  
  // Always show first page
  pages.push(1)
  
  // Calculate range around current page
  const startPage = Math.max(2, currentPage - siblingCount)
  const endPage = Math.min(totalPages - 1, currentPage + siblingCount)
  
  // Add ellipsis if needed
  if (startPage > 2) {
    pages.push('...')
  }
  
  // Add pages around current
  for (let i = startPage; i <= endPage; i++) {
    pages.push(i)
  }
  
  // Add ellipsis if needed
  if (endPage < totalPages - 1) {
    pages.push('...')
  }
  
  // Always show last page
  if (totalPages > 1) {
    pages.push(totalPages)
  }
  
  return (
    <div className={cn('flex items-center gap-1', className)}>
      {/* First page */}
      <Button
        variant="outline"
        size="icon"
        onClick={() => onPageChange(1)}
        disabled={currentPage === 1}
      >
        <ChevronsLeft className="w-4 h-4" />
      </Button>
      
      {/* Previous page */}
      <Button
        variant="outline"
        size="icon"
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
      >
        <ChevronLeft className="w-4 h-4" />
      </Button>
      
      {/* Page numbers */}
      {pages.map((page, index) => (
        <Button
          key={index}
          variant={page === currentPage ? 'default' : 'outline'}
          size="sm"
          onClick={() => typeof page === 'number' && onPageChange(page)}
          disabled={page === '...'}
        >
          {page}
        </Button>
      ))}
      
      {/* Next page */}
      <Button
        variant="outline"
        size="icon"
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage === totalPages}
      >
        <ChevronRight className="w-4 h-4" />
      </Button>
      
      {/* Last page */}
      <Button
        variant="outline"
        size="icon"
        onClick={() => onPageChange(totalPages)}
        disabled={currentPage === totalPages}
      >
        <ChevronsRight className="w-4 h-4" />
      </Button>
    </div>
  )
}
```

**Uso:**

```tsx
import { Pagination } from '@/components/ui/Pagination'

<Pagination
  currentPage={currentPage}
  totalPages={totalPages}
  onPageChange={handlePageChange}
/>
```

---

## Stepper (Multi-step Form)

**Quando usar:**
- Forms longos divididos em etapas
- Onboarding
- Wizards

**Estrutura:**

```tsx
// src/components/ui/Stepper.tsx
import { Check } from 'lucide-react'
import { cn } from '@/lib/utils'

interface Step {
  id: string
  title: string
  description?: string
}

interface StepperProps {
  steps: Step[]
  currentStep: number
  onStepClick?: (stepIndex: number) => void
}

export function Stepper({ steps, currentStep, onStepClick }: StepperProps) {
  return (
    <nav aria-label="Progress">
      <ol className="flex items-center">
        {steps.map((step, index) => {
          const isComplete = index < currentStep
          const isCurrent = index === currentStep
          
          return (
            <li key={step.id} className="relative">
              {/* Step */}
              <div className="flex items-center">
                <button
                  type="button"
                  onClick={() => onStepClick?.(index)}
                  className={cn(
                    'relative flex items-center justify-center w-8 h-8 rounded-full',
                    'transition-colors',
                    isComplete && 'bg-primary text-primary-foreground',
                    isCurrent && 'border-2 border-primary bg-background',
                    !isComplete && !isCurrent && 'border-2 border-muted bg-background'
                  )}
                >
                  {isComplete ? (
                    <Check className="w-4 h-4" />
                  ) : (
                    <span className="text-sm font-medium">{index + 1}</span>
                  )}
                </button>
                
                {/* Step label */}
                <div className="ml-3">
                  <p className={cn('text-sm font-medium', isCurrent && 'text-foreground', !isCurrent && 'text-muted-foreground')}>
                    {step.title}
                  </p>
                  {step.description && (
                    <p className="text-xs text-muted-foreground">{step.description}</p>
                  )}
                </div>
              </div>
              
              {/* Connector line */}
              {index < steps.length - 1 && (
                <div
                  className={cn(
                    'absolute top-4 left-8 w-full h-0.5',
                    index < currentStep ? 'bg-primary' : 'bg-muted'
                  )}
                  style={{ width: 'calc(100% + 2rem)' }}
                />
              )}
            </li>
          )
        })}
      </ol>
    </nav>
  )
}
```

**Uso:**

```tsx
import { Stepper } from '@/components/ui/Stepper'

const steps = [
  { id: 'account', title: 'Conta', description: 'Informações básicas' },
  { id: 'profile', title: 'Perfil', description: 'Dados pessoais' },
  { id: 'preferences', title: 'Preferências', description: 'Configurações' },
  { id: 'confirm', title: 'Confirmação', description: 'Revisar dados' },
]

<Stepper
  steps={steps}
  currentStep={currentStep}
  onStepClick={handleStepClick}
/>
```

---

## Scroll-based Navigation

**Quando usar:**
- Navegação em páginas longas
- Table of contents
- Documentação

**Estrutura:**

```tsx
// src/components/ui/ScrollNav.tsx
'use client'

import { useEffect, useState } from 'react'
import { cn } from '@/lib/utils'

interface ScrollNavItem {
  id: string
  label: string
}

interface ScrollNavProps {
  items: ScrollNavItem[]
}

export function ScrollNav({ items }: ScrollNavProps) {
  const [activeId, setActiveId] = useState<string>('')
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id)
          }
        })
      },
      { rootMargin: '-20% 0% -80% 0%' }
    )
    
    items.forEach((item) => {
      const element = document.getElementById(item.id)
      if (element) {
        observer.observe(element)
      }
    })
    
    return () => observer.disconnect()
  }, [items])
  
  return (
    <nav className="space-y-2">
      {items.map((item) => (
        <a
          key={item.id}
          href={`#${item.id}`}
          className={cn(
            'block text-sm transition-colors',
            activeId === item.id
              ? 'text-foreground font-medium'
              : 'text-muted-foreground hover:text-foreground'
          )}
        >
          {item.label}
        </a>
      ))}
    </nav>
  )
}
```

---

## Referências

- [menus.md](./menus.md)
- [tables-data.md](./tables-data.md)
- [forms.md](./forms.md)