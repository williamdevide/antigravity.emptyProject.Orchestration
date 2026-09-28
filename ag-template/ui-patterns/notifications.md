# Notifications — Toasts, Banners e Badges

## Visão Geral

Este guia define os padrões de notificações para projetos web mobile-first.

---

## Toast/Snackbar

**Quando usar:**
- Feedback de ações
- Mensagens temporárias
- Notificações não intrusivas

**Estrutura (com Sonner):**

```tsx
// src/components/ui/Toast.tsx
'use client'

import { Toaster } from 'sonner'

export function ToastProvider() {
  return <Toaster position="bottom-right" />
}

// Hooks para usar em qualquer lugar
import { toast } from 'sonner'

export function useToast() {
  return {
    success: (message: string) => {
      toast.success(message, {
        duration: 3000,
        position: 'bottom-right',
      })
    },
    error: (message: string) => {
      toast.error(message, {
        duration: 5000,
        position: 'bottom-right',
      })
    },
    info: (message: string) => {
      toast.info(message, {
        duration: 3000,
        position: 'bottom-right',
      })
    },
    loading: (message: string) => {
      return toast.loading(message, {
        position: 'bottom-right',
      })
    },
  }
}
```

**Uso:**

```tsx
// src/components/features/comics/ComicForm.tsx
import { useToast } from '@/components/ui/Toast'

function ComicForm() {
  const toast = useToast()
  
  const handleSubmit = async (data) => {
    const loadingToast = toast.loading('Salvando...')
    
    try {
      await saveComic(data)
      toast.dismiss(loadingToast)
      toast.success('Quadrinho salvo com sucesso!')
    } catch (error) {
      toast.dismiss(loadingToast)
      toast.error('Erro ao salvar quadrinho')
    }
  }
  
  return <form onSubmit={handleSubmit}>...</form>
}

// No layout root
// src/app/layout.tsx
import { ToastProvider } from '@/components/ui/Toast'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <ToastProvider />
        {children}
      </body>
    </html>
  )
}
```

---

## Banner de Aviso

**Quando usar:**
- Avisos importantes
- Manutenção agendada
- Novas features
- Alertas de sistema

**Estrutura:**

```tsx
// src/components/ui/Banner.tsx
'use client'

import { useState } from 'react'
import { X, Info, AlertTriangle, AlertCircle, CheckCircle } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import Link from 'next/link'
import { cn } from '@/lib/utils'

type BannerVariant = 'info' | 'warning' | 'error' | 'success'

interface BannerProps {
  variant?: BannerVariant
  title?: string
  message: string
  actionLabel?: string
  actionHref?: string
  onDismiss?: () => void
  persistent?: boolean
}

const variants = {
  info: {
    bg: 'bg-blue-50',
    border: 'border-blue-200',
    icon: Info,
    iconColor: 'text-blue-600',
  },
  warning: {
    bg: 'bg-yellow-50',
    border: 'border-yellow-200',
    icon: AlertTriangle,
    iconColor: 'text-yellow-600',
  },
  error: {
    bg: 'bg-red-50',
    border: 'border-red-200',
    icon: AlertCircle,
    iconColor: 'text-red-600',
  },
  success: {
    bg: 'bg-green-50',
    border: 'border-green-200',
    icon: CheckCircle,
    iconColor: 'text-green-600',
  },
}

export function Banner({ variant = 'info', title, message, actionLabel, actionHref, onDismiss, persistent }: BannerProps) {
  const [isDismissed, setIsDismissed] = useState(false)
  const Icon = variants[variant].icon
  
  if (isDismissed) return null
  
  return (
    <div className={cn('border-b p-4', variants[variant].bg, variants[variant].border)}>
      <div className="container mx-auto flex items-start gap-3">
        <Icon className={cn('w-5 h-5 flex-shrink-0 mt-0.5', variants[variant].iconColor)} />
        
        <div className="flex-1">
          {title && (
            <h3 className="font-medium mb-1">{title}</h3>
          )}
          <p className="text-sm">{message}</p>
          
          {actionLabel && actionHref && (
            <Link href={actionHref} className="text-sm font-medium underline mt-2 inline-block">
              {actionLabel}
            </Link>
          )}
        </div>
        
        {!persistent && onDismiss && (
          <Button
            variant="ghost"
            size="icon"
            className="flex-shrink-0 -mr-2 -mt-2"
            onClick={() => setIsDismissed(true)}
          >
            <X className="w-4 h-4" />
          </Button>
        )}
      </div>
    </div>
  )
}
```

**Uso:**

```tsx
// Manutenção agendada
<Banner
  variant="warning"
  title="Manutenção Agendada"
  message="O sistema estará indisponível em 25/12 das 00:00 às 06:00."
  persistent
/>

// Nova feature
<Banner
  variant="info"
  message="Nova funcionalidade: Agora você pode filtrar por editora!"
  actionLabel="Experimentar"
  actionHref="/explorar"
  onDismiss={() => localStorage.setItem('banner-feature-dismissed', 'true')}
/>

// Erro de sistema
<Banner
  variant="error"
  title="Erro no Sistema"
  message="Estamos enfrentando problemas técnicos. Nossa equipe está trabalhando para resolver."
  persistent
/>
```

---

## Badge de Notificação

**Quando usar:**
- Contador de notificações
- Status de item
- Labels

**Estrutura:**

```tsx
// src/components/ui/Badge.tsx
import { cn } from '@/lib/utils'

interface BadgeProps {
  children: React.ReactNode
  variant?: 'default' | 'primary' | 'success' | 'warning' | 'error'
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

const variants = {
  default: 'bg-muted text-muted-foreground',
  primary: 'bg-primary text-primary-foreground',
  success: 'bg-green-500 text-white',
  warning: 'bg-yellow-500 text-white',
  error: 'bg-red-500 text-white',
}

const sizes = {
  sm: 'px-2 py-0.5 text-xs',
  md: 'px-2.5 py-0.5 text-sm',
  lg: 'px-3 py-1 text-base',
}

export function Badge({ children, variant = 'default', size = 'md', className }: BadgeProps) {
  return (
    <span
      className={cn(
        'inline-flex items-center rounded-full font-medium',
        variants[variant],
        sizes[size],
        className
      )}
    >
      {children}
    </span>
  )
}

// Badge com contador
interface NotificationBadgeProps {
  count: number
  max?: number
}

export function NotificationBadge({ count, max = 99 }: NotificationBadgeProps) {
  if (count === 0) return null
  
  return (
    <Badge variant="error" size="sm" className="absolute -top-1 -right-1 min-w-[20px] h-5 px-1">
      {count > max ? `${max}+` : count}
    </Badge>
  )
}
```

**Uso:**

```tsx
// Status
<Badge variant="success">Ativo</Badge>
<Badge variant="warning">Pendente</Badge>
<Badge variant="error">Inativo</Badge>

// Notificações
import { Bell } from 'lucide-react'
import { NotificationBadge } from '@/components/ui/Badge'

function NotificationButton({ count }) {
  return (
    <Button variant="ghost" size="icon" className="relative">
      <Bell className="w-5 h-5" />
      <NotificationBadge count={count} />
    </Button>
  )
}

// Labels
<Badge variant="primary">Novo</Badge>
<Badge variant="default">Rascunho</Badge>
```

---

## Toast Customizado

**Quando usar:**
- Notificações complexas
- Ações no toast
- Ícones customizados

**Estrutura:**

```tsx
// src/components/ui/CustomToast.tsx
import { Info, CheckCircle, AlertTriangle, AlertCircle } from 'lucide-react'
import { cn } from '@/lib/utils'

type ToastType = 'success' | 'error' | 'warning' | 'info'

interface CustomToastProps {
  type: ToastType
  title: string
  message?: string
  action?: React.ReactNode
}

const icons = {
  success: CheckCircle,
  error: AlertCircle,
  warning: AlertTriangle,
  info: Info,
}

const colors = {
  success: 'text-green-600',
  error: 'text-red-600',
  warning: 'text-yellow-600',
  info: 'text-blue-600',
}

export function CustomToast({ type, title, message, action }: CustomToastProps) {
  const Icon = icons[type]
  
  return (
    <div className="flex items-start gap-3">
      <Icon className={cn('w-5 h-5 flex-shrink-0 mt-0.5', colors[type])} />
      
      <div className="flex-1">
        <p className="font-medium">{title}</p>
        {message && (
          <p className="text-sm text-muted-foreground mt-1">{message}</p>
        )}
        {action && (
          <div className="mt-2">{action}</div>
        )}
      </div>
    </div>
  )
}

// Uso com Sonner
import { toast } from 'sonner'
import { CustomToast } from '@/components/ui/CustomToast'
import { Button } from '@/components/ui/Button'

function showCustomToast() {
  toast.custom(
    (t) => (
      <CustomToast
        type="success"
        title="Quadrinho salvo!"
        message="O quadrinho foi adicionado à sua coleção."
        action={
          <Button
            size="sm"
            variant="outline"
            onClick={() => toast.dismiss(t.id)}
          >
            Ver
          </Button>
        }
      />
    )
  )
}
```

---

## Toast Queue

**Quando usar:**
- Múltiplos toasts
- Evitar spam
- Fila de notificações

**Estrutura:**

```tsx
// src/lib/toastQueue.ts
import { toast } from 'sonner'

interface ToastQueueItem {
  id: string
  type: 'success' | 'error' | 'info' | 'warning'
  message: string
  duration?: number
}

const queue: ToastQueueItem[] = []
let isProcessing = false

export function addToQueue(item: Omit<ToastQueueItem, 'id'>) {
  const id = Math.random().toString(36).substr(2, 9)
  queue.push({ ...item, id })
  processQueue()
}

async function processQueue() {
  if (isProcessing || queue.length === 0) return
  
  isProcessing = true
  
  while (queue.length > 0) {
    const item = queue.shift()!
    
    toast[item.type](item.message, {
      duration: item.duration || 3000,
    })
    
    await new Promise(resolve => setTimeout(resolve, item.duration || 3000))
  }
  
  isProcessing = false
}

// Uso
addToQueue({ type: 'success', message: 'Item 1 salvo' })
addToQueue({ type: 'success', message: 'Item 2 salvo' })
addToQueue({ type: 'error', message: 'Item 3 falhou' })
```

---

## Acessibilidade

### Checklist

- [ ] `role="status"` para toasts
- [ ] `aria-live="polite"` para announcements
- [ ] Auto-dismiss com tempo suficiente
- [ ] Pausar hover/keyboard
- [ ] Focus management
- [ ] Screen reader friendly

### Exemplo: ARIA

```tsx
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
  className="toast"
>
  {message}
</div>
```

---

## Referências

- [error.md](./error.md)
- [loading.md](./loading.md)
- [modals.md](./modals.md)