# Modals — Modals, Dialogs e Drawers

## Visão Geral

Este guia define os padrões de modals, dialogs e drawers para projetos web mobile-first.

---

## Modal/Dialog

**Quando usar:**
- Confirmar ações
- Exibir informações importantes
- Forms rápidos
- Alertas

**Estrutura:**

```tsx
// src/components/ui/Dialog.tsx
'use client'

import * as DialogPrimitive from '@radix-ui/react-dialog'
import { X } from 'lucide-react'
import { cn } from '@/lib/utils'

interface DialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  children: React.ReactNode
}

export function Dialog({ open, onOpenChange, children }: DialogProps) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="fixed inset-0 z-50 bg-black/50" />
        <DialogPrimitive.Content
          className={cn(
            'fixed left-[50%] top-[50%] z-50 translate-x-[-50%] translate-y-[-50%]',
            'w-full max-w-lg bg-background p-6 rounded-lg shadow-lg',
            'duration-200'
          )}
        >
          {children}
          <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 hover:opacity-100">
            <X className="w-4 h-4" />
          </DialogPrimitive.Close>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  )
}

// Header, Title, Description, Footer
export function DialogHeader({ children }: { children: React.ReactNode }) {
  return <div className="mb-4">{children}</div>
}

export function DialogTitle({ children }: { children: React.ReactNode }) {
  return (
    <DialogPrimitive.Title className="text-lg font-semibold">
      {children}
    </DialogPrimitive.Title>
  )
}

export function DialogDescription({ children }: { children: React.ReactNode }) {
  return (
    <DialogPrimitive.Description className="text-sm text-muted-foreground mt-1">
      {children}
    </DialogPrimitive.Description>
  )
}

export function DialogFooter({ children }: { children: React.ReactNode }) {
  return <div className="flex justify-end gap-2 mt-6">{children}</div>
}
```

**Uso:**

```tsx
// Confirm dialog
import {
  Dialog,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from '@/components/ui/Dialog'
import { Button } from '@/components/ui/Button'

function DeleteConfirm({ open, onOpenChange, onConfirm }) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogHeader>
        <DialogTitle>Excluir quadrinho?</DialogTitle>
        <DialogDescription>
          Esta ação não pode ser desfeita. O quadrinho será permanentemente excluído.
        </DialogDescription>
      </DialogHeader>
      <DialogFooter>
        <Button variant="outline" onClick={() => onOpenChange(false)}>
          Cancelar
        </Button>
        <Button variant="destructive" onClick={onConfirm}>
          Excluir
        </Button>
      </DialogFooter>
    </Dialog>
  )
}
```

---

## Alert Dialog

**Quando usar:** Alertas importantes que requerem confirmação.

**Estrutura:**

```tsx
// src/components/ui/AlertDialog.tsx
'use client'

import * as AlertDialogPrimitive from '@radix-ui/react-alert-dialog'
import { cn } from '@/lib/utils'

interface AlertDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  children: React.ReactNode
}

export function AlertDialog({ open, onOpenChange, children }: AlertDialogProps) {
  return (
    <AlertDialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      {children}
    </AlertDialogPrimitive.Root>
  )
}

export function AlertDialogTrigger({ children }: { children: React.ReactNode }) {
  return <AlertDialogPrimitive.Trigger asChild>{children}</AlertDialogPrimitive.Trigger>
}

export function AlertDialogContent({ children }: { children: React.ReactNode }) {
  return (
    <AlertDialogPrimitive.Portal>
      <AlertDialogPrimitive.Overlay className="fixed inset-0 z-50 bg-black/50" />
      <AlertDialogPrimitive.Content
        className={cn(
          'fixed left-[50%] top-[50%] z-50 translate-x-[-50%] translate-y-[-50%]',
          'w-full max-w-lg bg-background p-6 rounded-lg shadow-lg'
        )}
      >
        {children}
      </AlertDialogPrimitive.Content>
    </AlertDialogPrimitive.Portal>
  )
}

export function AlertDialogHeader({ children }: { children: React.ReactNode }) {
  return <div className="mb-4">{children}</div>
}

export function AlertDialogTitle({ children }: { children: React.ReactNode }) {
  return (
    <AlertDialogPrimitive.Title className="text-lg font-semibold">
      {children}
    </AlertDialogPrimitive.Title>
  )
}

export function AlertDialogDescription({ children }: { children: React.ReactNode }) {
  return (
    <AlertDialogPrimitive.Description className="text-sm text-muted-foreground mt-1">
      {children}
    </AlertDialogPrimitive.Description>
  )
}

export function AlertDialogFooter({ children }: { children: React.ReactNode }) {
  return <div className="flex justify-end gap-2 mt-6">{children}</div>
}

export function AlertDialogCancel({ children, ...props }: any) {
  return (
    <AlertDialogPrimitive.Cancel asChild>
      <button {...props} className="px-4 py-2 rounded-md border bg-background hover:bg-accent">
        {children}
      </button>
    </AlertDialogPrimitive.Cancel>
  )
}

export function AlertDialogAction({ children, ...props }: any) {
  return (
    <AlertDialogPrimitive.Action asChild>
      <button {...props} className="px-4 py-2 rounded-md bg-primary text-primary-foreground">
        {children}
      </button>
    </AlertDialogPrimitive.Action>
  )
}
```

**Uso:**

```tsx
import {
  AlertDialog,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogCancel,
  AlertDialogAction,
} from '@/components/ui/AlertDialog'

function DeleteButton({ onDelete }) {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button variant="destructive">Excluir</Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Tem certeza?</AlertDialogTitle>
          <AlertDialogDescription>
            Esta ação não pode ser desfeita.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancelar</AlertDialogCancel>
          <AlertDialogAction onClick={onDelete}>Excluir</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```

---

## Drawer (Mobile)

**Quando usar:**
- Mobile-first
- Forms longos
- Navegação secundária
- Substitui modal em mobile

**Estrutura:**

```tsx
// src/components/ui/Drawer.tsx
'use client'

import * as DialogPrimitive from '@radix-ui/react-dialog'
import { X } from 'lucide-react'
import { cn } from '@/lib/utils'

interface DrawerProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  children: React.ReactNode
  side?: 'top' | 'bottom' | 'left' | 'right'
}

export function Drawer({ open, onOpenChange, children, side = 'bottom' }: DrawerProps) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="fixed inset-0 z-50 bg-black/50" />
        <DialogPrimitive.Content
          className={cn(
            'fixed z-50 bg-background shadow-lg',
            'duration-200',
            side === 'bottom' && 'bottom-0 left-0 right-0 rounded-t-lg max-h-[90vh] overflow-y-auto',
            side === 'top' && 'top-0 left-0 right-0 rounded-b-lg max-h-[90vh] overflow-y-auto',
            side === 'left' && 'left-0 top-0 bottom-0 rounded-r-lg w-full max-w-sm',
            side === 'right' && 'right-0 top-0 bottom-0 rounded-l-lg w-full max-w-sm'
          )}
        >
          {children}
          <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 hover:opacity-100">
            <X className="w-4 h-4" />
          </DialogPrimitive.Close>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  )
}

export function DrawerHeader({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-b">{children}</div>
}

export function DrawerTitle({ children }: { children: React.ReactNode }) {
  return <h2 className="text-lg font-semibold">{children}</h2>
}

export function DrawerContent({ children }: { children: React.ReactNode }) {
  return <div className="p-4">{children}</div>
}

export function DrawerFooter({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-t bg-muted">{children}</div>
}
```

**Uso:**

```tsx
import {
  Drawer,
  DrawerHeader,
  DrawerTitle,
  DrawerContent,
  DrawerFooter,
} from '@/components/ui/Drawer'
import { Button } from '@/components/ui/Button'

function FilterDrawer({ open, onOpenChange, filters, onApply }) {
  return (
    <Drawer open={open} onOpenChange={onOpenChange} side="bottom">
      <DrawerHeader>
        <DrawerTitle>Filtros</DrawerTitle>
      </DrawerHeader>
      <DrawerContent>
        {/* Filter controls */}
        <div className="space-y-4">
          {/* ... */}
        </div>
      </DrawerContent>
      <DrawerFooter>
        <Button onClick={() => onApply(filters)}>Aplicar filtros</Button>
      </DrawerFooter>
    </Drawer>
  )
}
```

---

## Sheet (Lateral)

**Quando usar:**
- Sidebar de configurações
- Carrinho de compras
- Navegação detalhada

**Estrutura:**

```tsx
// src/components/ui/Sheet.tsx
'use client'

import * as DialogPrimitive from '@radix-ui/react-dialog'
import { X } from 'lucide-react'
import { cn } from '@/lib/utils'

interface SheetProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  children: React.ReactNode
  side?: 'left' | 'right'
}

export function Sheet({ open, onOpenChange, children, side = 'right' }: SheetProps) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="fixed inset-0 z-50 bg-black/50" />
        <DialogPrimitive.Content
          className={cn(
            'fixed top-0 h-full w-full max-w-md bg-background shadow-lg',
            'duration-200',
            side === 'right' && 'right-0 border-l',
            side === 'left' && 'left-0 border-r'
          )}
        >
          {children}
          <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 hover:opacity-100">
            <X className="w-4 h-4" />
          </DialogPrimitive.Close>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  )
}

export function SheetHeader({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-b">{children}</div>
}

export function SheetTitle({ children }: { children: React.ReactNode }) {
  return <h2 className="text-lg font-semibold">{children}</h2>
}

export function SheetContent({ children }: { children: React.ReactNode }) {
  return <div className="p-4 overflow-y-auto h-[calc(100vh-80px)]">{children}</div>
}

export function SheetFooter({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-t">{children}</div>
}
```

**Uso:**

```tsx
// Shopping cart sheet
import {
  Sheet,
  SheetHeader,
  SheetTitle,
  SheetContent,
  SheetFooter,
} from '@/components/ui/Sheet'
import { Button } from '@/components/ui/Button'

function CartSheet({ open, onOpenChange, cartItems }) {
  const total = cartItems.reduce((sum, item) => sum + item.preco, 0)
  
  return (
    <Sheet open={open} onOpenChange={onOpenChange} side="right">
      <SheetHeader>
        <SheetTitle>Carrinho ({cartItems.length})</SheetTitle>
      </SheetHeader>
      <SheetContent>
        {/* Cart items */}
        <div className="space-y-4">
          {cartItems.map(item => (
            <CartItem key={item.id} item={item} />
          ))}
        </div>
      </SheetContent>
      <SheetFooter>
        <div className="w-full">
          <p className="text-lg font-semibold mb-2">Total: R$ {total.toFixed(2)}</p>
          <Button className="w-full">Finalizar Compra</Button>
        </div>
      </SheetFooter>
    </Sheet>
  )
}
```

---

## Full Screen Modal

**Quando usar:**
- Mobile: forms longos
- Edição de conteúdo rico
- Experiências imersivas

**Estrutura:**

```tsx
// src/components/ui/FullScreenModal.tsx
'use client'

import * as DialogPrimitive from '@radix-ui/react-dialog'
import { X, ArrowLeft } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface FullScreenModalProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  children: React.ReactNode
  title?: string
  showBackButton?: boolean
}

export function FullScreenModal({ open, onOpenChange, children, title, showBackButton }: FullScreenModalProps) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="fixed inset-0 z-50 bg-background" />
        <DialogPrimitive.Content className="fixed inset-0 z-50">
          <div className="flex flex-col h-full">
            {/* Header */}
            <div className="flex items-center gap-4 p-4 border-b">
              {showBackButton && (
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={() => onOpenChange(false)}
                >
                  <ArrowLeft className="w-5 h-5" />
                </Button>
              )}
              {title && (
                <DialogPrimitive.Title className="text-lg font-semibold flex-1">
                  {title}
                </DialogPrimitive.Title>
              )}
              <DialogPrimitive.Close asChild>
                <Button variant="ghost" size="icon">
                  <X className="w-5 h-5" />
                </Button>
              </DialogPrimitive.Close>
            </div>
            
            {/* Content */}
            <div className="flex-1 overflow-y-auto">
              {children}
            </div>
          </div>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  )
}
```

**Uso:**

```tsx
// Edit comic full screen
import { FullScreenModal } from '@/components/ui/FullScreenModal'
import { ComicForm } from '@/components/features/comics/ComicForm'

function EditComicModal({ comic, open, onOpenChange }) {
  return (
    <FullScreenModal
      open={open}
      onOpenChange={onOpenChange}
      title="Editar Quadrinho"
      showBackButton
    >
      <div className="p-4 max-w-2xl mx-auto">
        <ComicForm mode="edit" initialData={comic} />
      </div>
    </FullScreenModal>
  )
}
```

---

## Acessibilidade

### Checklist

- [ ] Focus trap (focus permanece no modal)
- [ ] Escape fecha modal
- [ ] Click no overlay fecha modal
- [ ] ARIA labels apropriados
- [ ] Focus retorna ao trigger após fechar
- [ ] Screen reader announcements

### Exemplo: ARIA

```tsx
<DialogPrimitive.Root>
  <DialogPrimitive.Title id="modal-title">
    Título do Modal
  </DialogPrimitive.Title>
  <DialogPrimitive.Description id="modal-description">
    Descrição do modal
  </DialogPrimitive.Description>
</DialogPrimitive.Root>
```

---

## Performance

### Otimizações

- **Lazy load** modals pesados
- **Portal** para evitar z-index issues
- **Unmount** quando fechado
- **Animation** com CSS transforms

### Exemplo: Lazy Load

```tsx
import dynamic from 'next/dynamic'

const DeleteConfirmDialog = dynamic(
  () => import('@/components/features/comics/DeleteConfirmDialog'),
  { ssr: false }
)
```

---

## Referências

- [forms.md](./forms.md)
- [error.md](./error.md)
- [menus.md](./menus.md)