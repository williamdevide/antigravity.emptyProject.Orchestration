# Commons Screens — Telas Comuns

## Visão Geral

Este guia define as telas comuns que aparecem em múltiplos projetos, com padrões de implementação e UX.

---

## Telas de Autenticação

### 1. Login

**Propósito:** Autenticar usuário no sistema.

**Componentes:**
- Logo da marca
- Email input
- Senha input
- Botão "Entrar"
- Link "Esqueci a senha"
- Link "Criar conta"
- OAuth buttons (Google, GitHub)

**Estrutura:**

```tsx
// src/app/login/page.tsx
import { AuthLayout } from '@/components/layout/AuthLayout'
import { LoginForm } from '@/components/features/auth/LoginForm'

export default function LoginPage() {
  return (
    <AuthLayout>
      <LoginForm />
    </AuthLayout>
  )
}
```

**UX Guidelines:**
- Auto-focus no email
- Mostrar/ocultar senha toggle
- Manter email após erro
- Rate limiting claro
- Mensagens de erro específicas

---

### 2. Registro

**Propósito:** Criar nova conta de usuário.

**Componentes:**
- Logo da marca
- Nome input
- Email input
- Senha input
- Confirmar senha input
- Checkbox termos de uso
- Botão "Criar Conta"
- Link "Já tem conta? Entrar"

**Estrutura:**

```tsx
// src/app/registro/page.tsx
import { AuthLayout } from '@/components/layout/AuthLayout'
import { RegisterForm } from '@/components/features/auth/RegisterForm'

export default function RegisterPage() {
  return (
    <AuthLayout>
      <RegisterForm />
    </AuthLayout>
  )
}
```

**UX Guidelines:**
- Validação em tempo real
- Senha strength indicator
- Email validation
- Termos com link
- Redirecionar para login após sucesso

---

### 3. Recuperar Senha

**Propósito:** Enviar link de recuperação de senha.

**Componentes:**
- Logo da marca
- Email input
- Botão "Enviar Link"
- Mensagem de sucesso
- Link "Voltar para login"

**Estrutura:**

```tsx
// src/app/recuperar-senha/page.tsx
import { AuthLayout } from '@/components/layout/AuthLayout'
import { ForgotPasswordForm } from '@/components/features/auth/ForgotPasswordForm'

export default function ForgotPasswordPage() {
  return (
    <AuthLayout>
      <ForgotPasswordForm />
    </AuthLayout>
  )
}
```

**UX Guidelines:**
- Não revelar se email existe (segurança)
- Mensagem genérica de sucesso
- Link expira em X horas
- Rate limiting

---

### 4. Resetar Senha

**Propósito:** Definir nova senha após clique no link.

**Componentes:**
- Logo da marca
- Nova senha input
- Confirmar nova senha input
- Botão "Redefinir Senha"
- Mensagem de sucesso

**Estrutura:**

```tsx
// src/app/resetar-senha/page.tsx
import { AuthLayout } from '@/components/layout/AuthLayout'
import { ResetPasswordForm } from '@/components/features/auth/ResetPasswordForm'

export default function ResetPasswordPage() {
  return (
    <AuthLayout>
      <ResetPasswordForm />
    </AuthLayout>
  )
}
```

**UX Guidelines:**
- Validar token de reset
- Exigir senha forte
- Auto-login após reset
- Invalidar token após uso

---

## Telas de Erro

### 5. 404 - Página Não Encontrada

**Propósito:** Informar que página não existe.

**Componentes:**
- "404" grande
- Título "Página não encontrada"
- Descrição
- Botão "Voltar para home"
- Busca (opcional)

**Estrutura:**

```tsx
// src/app/not-found.tsx
import Link from 'next/link'
import { Button } from '@/components/ui/Button'

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="text-center max-w-md">
        <h1 className="text-6xl font-bold text-muted-foreground mb-4">404</h1>
        <h2 className="text-2xl font-bold mb-4">Página não encontrada</h2>
        <p className="text-muted-foreground mb-8">
          A página que você está procurando não existe ou foi movida.
        </p>
        <Button asChild>
          <Link href="/">Voltar para a home</Link>
        </Button>
      </div>
    </div>
  )
}
```

---

### 6. 500 - Erro do Servidor

**Propósito:** Informar erro interno.

**Componentes:**
- "500" grande
- Título "Algo deu errado"
- Descrição
- Botão "Tentar novamente"
- Botão "Voltar para home"

**Estrutura:**

```tsx
// src/app/error.tsx
'use client'

import { useEffect } from 'react'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  useEffect(() => {
    console.error('Erro:', error)
  }, [error])
  
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="text-center max-w-md">
        <h1 className="text-6xl font-bold text-muted-foreground mb-4">500</h1>
        <h2 className="text-2xl font-bold mb-4">Algo deu errado</h2>
        <p className="text-muted-foreground mb-8">
          Ocorreu um erro inesperado. Tente novamente ou entre em contato com o suporte.
        </p>
        <div className="flex gap-4 justify-center">
          <Button onClick={reset}>Tentar novamente</Button>
          <Button variant="outline" asChild>
            <Link href="/">Voltar para a home</Link>
          </Button>
        </div>
      </div>
    </div>
  )
}
```

---

### 7. 403 - Acesso Negado

**Propósito:** Informar que usuário não tem permissão.

**Componentes:**
- "403" grande
- Título "Acesso negado"
- Descrição
- Botão "Voltar para home"
- Link para contato (opcional)

**Estrutura:**

```tsx
// src/app/forbidden/page.tsx
import Link from 'next/link'
import { Button } from '@/components/ui/Button'

export default function ForbiddenPage() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="text-center max-w-md">
        <h1 className="text-6xl font-bold text-muted-foreground mb-4">403</h1>
        <h2 className="text-2xl font-bold mb-4">Acesso negado</h2>
        <p className="text-muted-foreground mb-8">
          Você não tem permissão para acessar esta página.
        </p>
        <Button asChild>
          <Link href="/">Voltar para a home</Link>
        </Button>
      </div>
    </div>
  )
}
```

---

## Telas de Estado

### 8. Loading (Carregando)

**Propósito:** Mostrar que conteúdo está carregando.

**Componentes:**
- Loading spinner ou skeleton
- Mensagem de carregamento (opcional)
- Progress bar (se aplicável)

**Estrutura:**

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
```

---

### 9. Empty (Vazio)

**Propósito:** Mostrar que não há conteúdo.

**Componentes:**
- Ícone ou ilustração
- Título descritivo
- Descrição
- Call-to-action (opcional)

**Estrutura:**

```tsx
// src/components/ui/EmptyState.tsx
import { EmptyState } from '@/components/ui/EmptyState'

export function EmptyComics() {
  return (
    <EmptyState
      icon={<BookOpen className="w-16 h-16" />}
      title="Nenhum quadrinho encontrado"
      description="Comece explorando nossa coleção."
      action={
        <Button asChild>
          <Link href="/explorar">Explorar</Link>
        </Button>
      }
    />
  )
}
```

---

### 10. Error (Erro)

**Propósito:** Mostrar que ocorreu um erro.

**Componentes:**
- Ícone de erro
- Título
- Mensagem de erro
- Botão "Tentar novamente"

**Estrutura:**

```tsx
// src/components/ui/ErrorState.tsx
import { ErrorAlert } from '@/components/ui/ErrorAlert'
import { Button } from '@/components/ui/Button'

export function ErrorComics({ onRetry }) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <ErrorAlert
        title="Erro ao carregar"
        message="Não foi possível carregar os quadrinhos. Tente novamente."
      />
      <Button onClick={onRetry} className="mt-4">
        Tentar novamente
      </Button>
    </div>
  )
}
```

---

## Telas de Conteúdo

### 11. Lista / Grid

**Propósito:** Exibir coleção de itens.

**Componentes:**
- Header com título
- Filtros (opcional)
- Grid ou lista de cards
- Pagination ou infinite scroll
- Empty state (se vazio)

**Estrutura:**

```tsx
// src/app/explorar/page.tsx
import { ComicsGrid } from '@/components/features/comics/ComicsGrid'
import { Filters } from '@/components/features/comics/Filters'
import { Pagination } from '@/components/ui/Pagination'

export default function ExplorePage() {
  const { data, isLoading } = useComics()
  
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-6">Explorar Quadrinhos</h1>
      
      <Filters />
      
      {isLoading ? (
        <ComicsGridSkeleton />
      ) : data.comics.length === 0 ? (
        <EmptyComics />
      ) : (
        <>
          <ComicsGrid comics={data.comics} />
          <Pagination currentPage={data.page} totalPages={data.totalPages} />
        </>
      )}
    </div>
  )
}
```

---

### 12. Detalhes

**Propósito:** Exibir detalhes de um item.

**Componentes:**
- Breadcrumb
- Imagem principal
- Título
- Informações principais
- Ações (editar, excluir, etc.)
- Conteúdo relacionado

**Estrutura:**

```tsx
// src/app/quadrinhos/[id]/page.tsx
import { ComicDetail } from '@/components/features/comics/ComicDetail'
import { RelatedComics } from '@/components/features/comics/RelatedComics'

export default function ComicDetailPage({ params }) {
  const { data, isLoading } = useComic(params.id)
  
  if (isLoading) {
    return <ComicDetailSkeleton />
  }
  
  if (!data) {
    return <NotFound />
  }
  
  return (
    <div className="container mx-auto px-4 py-8">
      <Breadcrumb items={[{ label: 'Explorar', href: '/explorar' }, { label: data.titulo }]} />
      
      <ComicDetail comic={data} />
      
      <RelatedComics comicId={data.id} />
    </div>
  )
}
```

---

### 13. Perfil

**Propósito:** Exibir informações do usuário.

**Componentes:**
- Avatar
- Nome
- Email
- Informações adicionais
- Ações (editar, configurações)

**Estrutura:**

```tsx
// src/app/perfil/page.tsx
import { ProtectedRoute } from '@/components/features/auth/ProtectedRoute'
import { ProfileHeader } from '@/components/features/profile/ProfileHeader'
import { ProfileStats } from '@/components/features/profile/ProfileStats'

export default function ProfilePage() {
  return (
    <ProtectedRoute>
      <div className="container mx-auto px-4 py-8">
        <ProfileHeader />
        <ProfileStats />
      </div>
    </ProtectedRoute>
  )
}
```

---

### 14. Configurações

**Propósito:** Permitir usuário configurar conta.

**Componentes:**
- Tabs ou sidebar de navegação
- Forms de configuração
- Botão "Salvar"
- Mensagem de sucesso

**Estrutura:**

```tsx
// src/app/configuracoes/page.tsx
import { ProtectedRoute } from '@/components/features/auth/ProtectedRoute'
import { SettingsTabs } from '@/components/features/settings/SettingsTabs'
import { AccountSettings } from '@/components/features/settings/AccountSettings'
import { NotificationSettings } from '@/components/features/settings/NotificationSettings'

export default function SettingsPage() {
  return (
    <ProtectedRoute>
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-2xl font-bold mb-6">Configurações</h1>
        
        <SettingsTabs>
          <SettingsTabs.Tab value="conta">
            <AccountSettings />
          </SettingsTabs.Tab>
          <SettingsTabs.Tab value="notificacoes">
            <NotificationSettings />
          </SettingsTabs.Tab>
        </SettingsTabs>
      </div>
    </ProtectedRoute>
  )
}
```

---

## Telas de Ação

### 15. Criar / Editar

**Propósito:** Criar ou editar um item.

**Componentes:**
- Título (Criar/Editar)
- Form com campos
- Validação
- Botões (Salvar, Cancelar)
- Preview (opcional)

**Estrutura:**

```tsx
// src/app/quadrinhos/novo/page.tsx
import { ComicForm } from '@/components/features/comics/ComicForm'

export default function NewComicPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-6">Novo Quadrinho</h1>
      <ComicForm mode="create" />
    </div>
  )
}

// src/app/quadrinhos/[id]/editar/page.tsx
import { ComicForm } from '@/components/features/comics/ComicForm'

export default function EditComicPage({ params }) {
  const { data } = useComic(params.id)
  
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-6">Editar Quadrinho</h1>
      <ComicForm mode="edit" initialData={data} />
    </div>
  )
}
```

---

### 16. Confirmar Exclusão

**Propósito:** Confirmar ação destrutiva.

**Componentes:**
- Título de confirmação
- Descrição do que será excluído
- Botões (Excluir, Cancelar)
- Warning visual

**Estrutura:**

```tsx
// src/components/features/comics/DeleteConfirmDialog.tsx
import {
  AlertDialog,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogCancel,
  AlertDialogAction,
} from '@/components/ui/AlertDialog'

interface DeleteConfirmDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  onConfirm: () => void
  itemName: string
}

export function DeleteConfirmDialog({ open, onOpenChange, onConfirm, itemName }: DeleteConfirmDialogProps) {
  return (
    <AlertDialog open={open} onOpenChange={onOpenChange}>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Excluir quadrinho?</AlertDialogTitle>
          <AlertDialogDescription>
            Esta ação não pode ser desfeita. O quadrinho "{itemName}" será permanentemente excluído.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancelar</AlertDialogCancel>
          <AlertDialogAction
            variant="destructive"
            onClick={onConfirm}
          >
            Excluir
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```

---

## Telas Utilitárias

### 17. Busca

**Propósito:** Buscar conteúdo.

**Componentes:**
- Search input
- Filtros (opcional)
- Resultados
- Empty state (se sem resultados)

**Estrutura:**

```tsx
// src/app/busca/page.tsx
import { SearchInput } from '@/components/features/search/SearchInput'
import { SearchResults } from '@/components/features/search/SearchResults'
import { EmptySearch } from '@/components/ui/EmptySearch'

export default function SearchPage() {
  const [query, setQuery] = useState('')
  const { data } = useSearch(query)
  
  return (
    <div className="container mx-auto px-4 py-8">
      <SearchInput value={query} onChange={setQuery} />
      
      {query && data.results.length === 0 ? (
        <EmptySearch query={query} onClear={() => setQuery('')} />
      ) : (
        <SearchResults results={data.results} />
      )}
    </div>
  )
}
```

---

### 18. Notificações

**Propósito:** Exibir notificações do usuário.

**Componentes:**
- Lista de notificações
- Marcar como lida
- Limpar todas
- Empty state

**Estrutura:**

```tsx
// src/app/notificacoes/page.tsx
import { ProtectedRoute } from '@/components/features/auth/ProtectedRoute'
import { NotificationsList } from '@/components/features/notifications/NotificationsList'
import { EmptyNotifications } from '@/components/features/notifications/EmptyNotifications'

export default function NotificationsPage() {
  const { data } = useNotifications()
  
  return (
    <ProtectedRoute>
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-2xl font-bold mb-6">Notificações</h1>
        
        {data.notifications.length === 0 ? (
          <EmptyNotifications />
        ) : (
          <NotificationsList notifications={data.notifications} />
        )}
      </div>
    </ProtectedRoute>
  )
}
```

---

## Checklist de Implementação

### Para Cada Tela

- [ ] Layout responsivo (mobile-first)
- [ ] Loading state
- [ ] Empty state (se aplicável)
- [ ] Error state
- [ ] Acessibilidade (ARIA, keyboard nav)
- [ ] SEO (meta tags, se aplicável)
- [ ] Analytics (page view, se aplicável)

---

## Referências

- [menus.md](./menus.md)
- [splash.md](./splash.md)
- [auth-flows.md](./auth-flows.md)
- [loading.md](./loading.md)
- [error.md](./error.md)
- [empty.md](./empty.md)