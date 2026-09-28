# Menus — Padrões de Navegação e Menus

## Visão Geral

Este guia define os padrões de navegação e menus para projetos web mobile-first.

---

## Tipos de Menu

### 1. Bottom Navigation (Mobile)

**Quando usar:**
- Apps mobile-first
- 3-5 seções principais
- Navegação frequente entre seções

**Estrutura:**

```tsx
// src/components/layout/BottomNav.tsx
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Home, Search, Plus, Bookmark, User } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
  { href: '/', label: 'Início', icon: Home },
  { href: '/explorar', label: 'Explorar', icon: Search },
  { href: '/criar', label: 'Criar', icon: Plus },
  { href: '/colecao', label: 'Coleção', icon: Bookmark },
  { href: '/perfil', label: 'Perfil', icon: User },
]

export function BottomNav() {
  const pathname = usePathname()

  return (
    <nav className="bottom-nav fixed bottom-0 left-0 right-0 z-50">
      <div className="grid grid-cols-5 h-16 bg-background border-t">
        {navItems.map((item) => {
          const Icon = item.icon
          const isActive = pathname === item.href

          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                'flex flex-col items-center justify-center gap-1',
                'text-muted-foreground hover:text-foreground transition-colors',
                isActive && 'text-foreground'
              )}
            >
              <Icon className="w-5 h-5" />
              <span className="text-xs">{item.label}</span>
            </Link>
          )
        })}
      </div>
    </nav>
  )
}
```

**Estilos Tailwind:**

```css
/* src/app/globals.css */
.bottom-nav {
  @apply safe-area-bottom;
  @apply bg-background/80 backdrop-blur-sm;
}

/* Padding para conteúdo não ficar atrás do menu */
.main-content {
  @apply pb-20 md:pb-0;
}
```

**Acessibilidade:**
- Labels claros em cada item
- Estado ativo visível
- Navegação por teclado
- ARIA role="navigation"

---

### 2. Top Navigation (Desktop)

**Quando usar:**
- Sites desktop
- Landing pages
- Sites de conteúdo

**Estrutura:**

```tsx
// src/components/layout/Header.tsx
import Link from 'next/link'
import { Button } from '@/components/ui/Button'

const navItems = [
  { href: '/', label: 'Início' },
  { href: '/explorar', label: 'Explorar' },
  { href: '/sobre', label: 'Sobre' },
  { href: '/contato', label: 'Contato' },
]

export function Header() {
  return (
    <header className="header sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="logo">
            <span className="text-xl font-bold">ComixFlix</span>
          </Link>

          {/* Nav Items */}
          <nav className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="text-muted-foreground hover:text-foreground transition-colors"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          {/* Actions */}
          <div className="flex items-center gap-4">
            <Button variant="ghost" asChild>
              <Link href="/login">Entrar</Link>
            </Button>
            <Button asChild>
              <Link href="/registro">Criar Conta</Link>
            </Button>
          </div>
        </div>
      </div>
    </header>
  )
}
```

**Estilos Tailwind:**

```css
.header {
  @apply bg-background/80 backdrop-blur-sm border-b;
}
```

---

### 3. Hamburger Menu (Mobile)

**Quando usar:**
- Mobile com muitas seções
- Quando bottom nav não cabe todos os itens
- Menus secundários

**Estrutura:**

```tsx
// src/components/layout/MobileMenu.tsx
'use client'

import { useState } from 'react'
import Link from 'next/link'
import { Menu, X } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

const navItems = [
  { href: '/', label: 'Início' },
  { href: '/explorar', label: 'Explorar' },
  { href: '/colecao', label: 'Minha Coleção' },
  { href: '/favoritos', label: 'Favoritos' },
  { href: '/historico', label: 'Histórico' },
  { href: '/configuracoes', label: 'Configurações' },
]

export function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      {/* Toggle Button */}
      <Button
        variant="ghost"
        size="icon"
        onClick={() => setIsOpen(!isOpen)}
        className="md:hidden"
        aria-label="Menu"
      >
        {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
      </Button>

      {/* Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 md:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Menu Panel */}
      <div
        className={cn(
          'fixed top-0 right-0 h-full w-64 bg-background z-50',
          'transform transition-transform duration-300 md:hidden',
          isOpen ? 'translate-x-0' : 'translate-x-full'
        )}
      >
        <div className="p-4">
          {/* Close Button */}
          <Button
            variant="ghost"
            size="icon"
            onClick={() => setIsOpen(false)}
            className="absolute top-4 right-4"
          >
            <X className="w-5 h-5" />
          </Button>

          {/* Nav Items */}
          <nav className="mt-12 space-y-2">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2 text-foreground hover:bg-accent rounded-md"
                onClick={() => setIsOpen(false)}
              >
                {item.label}
              </Link>
            ))}
          </nav>
        </div>
      </div>
    </>
  )
}
```

---

### 4. Dropdown Menu

**Quando usar:**
- Ações contextuais
- Menu de usuário
- Opções de configuração

**Estrutura (com Radix UI):**

```tsx
// src/components/ui/DropdownMenu.tsx
'use client'

import * as DropdownMenu from '@radix-ui/react-dropdown-menu'
import { MoreVertical, Settings, LogOut } from 'lucide-react'
import { cn } from '@/lib/utils'

interface DropdownMenuItem {
  label: string
  icon?: React.ReactNode
  onClick?: () => void
  href?: string
  separator?: boolean
}

interface DropdownMenuProps {
  items: DropdownMenuItem[]
  trigger?: React.ReactNode
}

export function DropdownMenu({ items, trigger }: DropdownMenuProps) {
  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        {trigger || (
          <button className="p-2 hover:bg-accent rounded-full">
            <MoreVertical className="w-5 h-5" />
          </button>
        )}
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content
          className="min-w-[180px] bg-background border rounded-md shadow-lg p-1 z-50"
          sideOffset={5}
        >
          {items.map((item, index) => {
            if (item.separator) {
              return <DropdownMenu.Separator key={index} className="h-[1px] bg-border my-1" />
            }

            return (
              <DropdownMenu.Item
                key={index}
                className="flex items-center gap-2 px-3 py-2 text-sm text-foreground hover:bg-accent rounded cursor-pointer outline-none"
                onClick={item.onClick}
              >
                {item.icon}
                {item.label}
              </DropdownMenu.Item>
            )
          })}
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  )
}

// Exemplo de uso
export function UserMenu() {
  const items = [
    { label: 'Perfil', icon: <User className="w-4 h-4" />, href: '/perfil' },
    { label: 'Configurações', icon: <Settings className="w-4 h-4" />, href: '/configuracoes' },
    { separator: true },
    { label: 'Sair', icon: <LogOut className="w-4 h-4" />, onClick: handleLogout },
  ]

  return (
    <DropdownMenu items={items}>
      <Button variant="ghost" size="icon">
        <User className="w-5 h-5" />
      </Button>
    </DropdownMenu>
  )
}
```

---

### 5. Context Menu

**Quando usar:**
- Ações em itens específicos
- Right-click menus
- Long-press em mobile

**Estrutura:**

```tsx
// src/components/ui/ContextMenu.tsx
'use client'

import * as ContextMenu from '@radix-ui/react-context-menu'
import { Edit, Trash2, Copy } from 'lucide-react'

interface ContextMenuItem {
  label: string
  icon?: React.ReactNode
  onClick?: () => void
  shortcut?: string
}

interface ContextMenuProps {
  items: ContextMenuItem[]
  children: React.ReactNode
}

export function ContextMenu({ items, children }: ContextMenuProps) {
  return (
    <ContextMenu.Root>
      <ContextMenu.Trigger asChild>{children}</ContextMenu.Trigger>

      <ContextMenu.Portal>
        <ContextMenu.Content
          className="min-w-[180px] bg-background border rounded-md shadow-lg p-1 z-50"
        >
          {items.map((item, index) => (
            <ContextMenu.Item
              key={index}
              className="flex items-center justify-between gap-2 px-3 py-2 text-sm text-foreground hover:bg-accent rounded cursor-pointer outline-none"
              onClick={item.onClick}
            >
              <div className="flex items-center gap-2">
                {item.icon}
                {item.label}
              </div>
              {item.shortcut && (
                <span className="text-xs text-muted-foreground">{item.shortcut}</span>
              )}
            </ContextMenu.Item>
          ))}
        </ContextMenu.Content>
      </ContextMenu.Portal>
    </ContextMenu.Root>
  )
}

// Exemplo de uso
export function ComicCard({ comic }) {
  const items = [
    { label: 'Editar', icon: <Edit className="w-4 h-4" />, onClick: handleEdit },
    { label: 'Copiar link', icon: <Copy className="w-4 h-4" />, onClick: handleCopy },
    { label: 'Excluir', icon: <Trash2 className="w-4 h-4" />, onClick: handleDelete },
  ]

  return (
    <ContextMenu items={items}>
      <div className="comic-card">
        {/* Card content */}
      </div>
    </ContextMenu>
  )
}
```

---

## Padrões de Navegação

### Mobile-First

**Bottom Nav + Hamburger:**

```tsx
// src/components/layout/Layout.tsx
import { BottomNav } from './BottomNav'
import { Header } from './Header'
import { MobileMenu } from './MobileMenu'

export function Layout({ children }) {
  return (
    <div className="min-h-screen">
      {/* Desktop Header */}
      <Header className="hidden md:block" />

      {/* Mobile Header */}
      <header className="md:hidden sticky top-0 z-50 bg-background border-b">
        <div className="flex items-center justify-between h-16 px-4">
          <span className="text-lg font-bold">ComixFlix</span>
          <MobileMenu />
        </div>
      </header>

      {/* Main Content */}
      <main className="main-content">
        {children}
      </main>

      {/* Bottom Nav (Mobile) */}
      <BottomNav className="md:hidden" />
    </div>
  )
}
```

---

### Desktop-First

**Top Nav + Dropdown:**

```tsx
// src/components/layout/DesktopLayout.tsx
import { Header } from './Header'
import { UserMenu } from './UserMenu'

export function DesktopLayout({ children }) {
  return (
    <div className="min-h-screen">
      <Header>
        <div className="flex items-center gap-4">
          <UserMenu />
        </div>
      </Header>

      <main className="container mx-auto px-4 py-8">
        {children}
      </main>
    </div>
  )
}
```

---

## Acessibilidade

### Checklist

- [ ] Labels claros em todos os itens
- [ ] Estado ativo visível
- [ ] Navegação por teclado (Tab, Enter, Escape)
- [ ] Focus states visíveis
- [ ] ARIA roles apropriados
- [ ] Screen reader friendly

### Exemplo: Navegação por Teclado

```tsx
// BottomNav com navegação por teclado
export function BottomNav() {
  return (
    <nav role="navigation" aria-label="Navegação principal">
      {navItems.map((item, index) => (
        <Link
          key={item.href}
          href={item.href}
          role="menuitem"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') {
              // Navigate
            }
            if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
              // Focus next/prev item
            }
          }}
        >
          {item.label}
        </Link>
      ))}
    </nav>
  )
}
```

---

## Performance

### Otimizações

- **Lazy load** menus pesados
- **Prefetch** links de navegação
- **Memoize** componentes de menu
- **Debounce** search inputs

### Exemplo: Lazy Load

```tsx
import dynamic from 'next/dynamic'

const MobileMenu = dynamic(() => import('./MobileMenu').then(mod => mod.MobileMenu), {
  ssr: false,
  loading: () => <div className="w-6 h-6" />,
})
```

---

## Referências

- [real-sites-inspiration.md](../guides/real-sites-inspiration.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)
- [3d-web-guidelines.md](../guides/3d-web-guidelines.md)