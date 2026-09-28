# Error States — Estados de Erro

## Visão Geral

Este guia define os padrões de error states para projetos web mobile-first.

---

## Tipos de Erro

### 1. Error Inline (Formulários)

**Quando usar:**
- Validação de campos
- Erros específicos de input
- Feedback imediato

**Estrutura:**

```tsx
// src/components/ui/FormError.tsx
import { cn } from '@/lib/utils'

interface FormErrorProps {
  message?: string | null
  className?: string
}

export function FormError({ message, className }: FormErrorProps) {
  if (!message) return null
  
  return (
    <p
      className={cn(
        'text-sm text-destructive mt-1',
        className
      )}
      role="alert"
    >
      {message}
    </p>
  )
}

// Uso em formulários
<Input
  type="email"
  label="Email"
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? 'email-error' : undefined}
/>
<FormError
  message={errors.email?.message}
  id="email-error"
/>
```

---

### 2. Error Alert (Banner)

**Quando usar:**
- Erros gerais da página
- Erros de sistema
- Notificações importantes

**Estrutura:**

```tsx
// src/components/ui/ErrorAlert.tsx
import { AlertCircle, X } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface ErrorAlertProps {
  title?: string
  message: string
  onDismiss?: () => void
  className?: string
}

export function ErrorAlert({ title = 'Erro', message, onDismiss, className }: ErrorAlertProps) {
  return (
    <div
      className={cn(
        'flex items-start gap-3 p-4 bg-destructive/10 border border-destructive rounded-md',
        className
      )}
      role="alert"
    >
      <AlertCircle className="w-5 h-5 text-destructive flex-shrink-0 mt-0.5" />
      
      <div className="flex-1">
        <h3 className="font-medium text-destructive">{title}</h3>
        <p className="text-sm text-destructive/80 mt-1">{message}</p>
      </div>
      
      {onDismiss && (
        <Button
          variant="ghost"
          size="icon"
          className="text-destructive hover:text-destructive"
          onClick={onDismiss}
          aria-label="Fechar"
        >
          <X className="w-4 h-4" />
        </Button>
      )}
    </div>
  )
}

// Uso
function Page() {
  const [error, setError] = useState<string | null>(null)
  
  return (
    <div>
      {error && (
        <ErrorAlert
          message={error}
          onDismiss={() => setError(null)}
          className="mb-4"
        />
      )}
      
      {/* Resto do conteúdo */}
    </div>
  )
}
```

---

### 3. Error Page (Página de Erro)

**Quando usar:**
- Erros 404 (página não encontrada)
- Erros 500 (erro do servidor)
- Erros de acesso (403)

**Estrutura:**

```tsx
// src/app/not-found.tsx (Next.js 404)
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

```tsx
// src/app/error.tsx (Next.js error boundary)
'use client'

import { useEffect } from 'react'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'

interface ErrorProps {
  error: Error & { digest?: string }
  reset: () => void
}

export default function Error({ error, reset }: ErrorProps) {
  useEffect(() => {
    console.error('Erro na aplicação:', error)
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

### 4. Error Boundary (Componente)

**Quando usar:**
- Isolar erros de componentes
- Prevenir crash da app inteira
- Fallback UI

**Estrutura:**

```tsx
// src/components/ui/ErrorBoundary.tsx
'use client'

import { Component, ErrorInfo, ReactNode } from 'react'
import { Button } from '@/components/ui/Button'
import { AlertTriangle } from 'lucide-react'

interface ErrorBoundaryProps {
  children: ReactNode
  fallback?: ReactNode
  onError?: (error: Error, errorInfo: ErrorInfo) => void
}

interface ErrorBoundaryState {
  hasError: boolean
  error: Error | null
}

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props)
    this.state = { hasError: false, error: null }
  }
  
  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error }
  }
  
  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('ErrorBoundary caught error:', error, errorInfo)
    this.props.onError?.(error, errorInfo)
  }
  
  handleReset = () => {
    this.setState({ hasError: false, error: null })
  }
  
  render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback
      }
      
      return (
        <div className="p-4 bg-destructive/10 border border-destructive rounded-md">
          <div className="flex items-start gap-3">
            <AlertTriangle className="w-5 h-5 text-destructive flex-shrink-0 mt-0.5" />
            
            <div className="flex-1">
              <h3 className="font-medium text-destructive">Algo deu errado</h3>
              <p className="text-sm text-destructive/80 mt-1">
                {this.state.error?.message || 'Ocorreu um erro inesperado.'}
              </p>
              
              <div className="mt-4">
                <Button size="sm" onClick={this.handleReset}>
                  Tentar novamente
                </Button>
              </div>
            </div>
          </div>
        </div>
      )
    }
    
    return this.props.children
  }
}

// Uso
function ComicCard({ comic }) {
  return (
    <ErrorBoundary>
      <ComicCardContent comic={comic} />
    </ErrorBoundary>
  )
}
```

---

### 5. API Error Handler

**Quando usar:**
- Erros de API
- Tratamento centralizado
- Retry logic

**Estrutura:**

```ts
// src/lib/api/errorHandler.ts
export class ApiError extends Error {
  status: number
  code: string
  
  constructor(message: string, status: number, code: string) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.code = code
  }
}

export function handleApiError(error: unknown): never {
  if (error instanceof ApiError) {
    switch (error.status) {
      case 400:
        throw new ApiError('Requisição inválida', 400, error.code)
      case 401:
        throw new ApiError('Não autorizado. Faça login novamente.', 401, error.code)
      case 403:
        throw new ApiError('Acesso negado', 403, error.code)
      case 404:
        throw new ApiError('Recurso não encontrado', 404, error.code)
      case 409:
        throw new ApiError('Recurso já existe', 409, error.code)
      case 429:
        throw new ApiError('Muitas requisições. Tente novamente em alguns instantes.', 429, error.code)
      case 500:
        throw new ApiError('Erro do servidor. Tente novamente mais tarde.', 500, error.code)
      default:
        throw new ApiError('Ocorreu um erro inesperado.', error.status, error.code)
    }
  }
  
  throw error
}

// Uso no client
// src/lib/api/client.ts
import { handleApiError } from './errorHandler'

export const api = axios.create({ baseURL: process.env.NEXT_PUBLIC_API_URL })

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      const { status, data } = error.response
      throw handleApiError(new ApiError(data.message, status, data.code))
    }
    throw error
  }
)
```

---

### 6. Retry Logic

**Quando usar:**
- Erros temporários
- Network flaky
- Melhorar UX

**Estrutura:**

```tsx
// src/components/ui/RetryError.tsx
import { useState } from 'react'
import { RefreshCw } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { ErrorAlert } from './ErrorAlert'

interface RetryErrorProps {
  error: string
  onRetry: () => Promise<void>
  maxRetries?: number
}

export function RetryError({ error, onRetry, maxRetries = 3 }: RetryErrorProps) {
  const [retryCount, setRetryCount] = useState(0)
  const [isRetrying, setIsRetrying] = useState(false)
  
  const handleRetry = async () => {
    if (retryCount >= maxRetries) return
    
    setIsRetrying(true)
    try {
      await onRetry()
      setRetryCount(0)
    } catch {
      setRetryCount(prev => prev + 1)
    } finally {
      setIsRetrying(false)
    }
  }
  
  const isMaxRetries = retryCount >= maxRetries
  
  return (
    <div className="space-y-4">
      <ErrorAlert
        title={isMaxRetries ? 'Erro permanente' : 'Erro temporário'}
        message={
          isMaxRetries
            ? `${error} Após ${maxRetries} tentativas, não foi possível completar a ação.`
            : error
        }
      />
      
      {!isMaxRetries && (
        <Button
          variant="outline"
          onClick={handleRetry}
          disabled={isRetrying}
        >
          <RefreshCw className={cn('w-4 h-4 mr-2', isRetrying && 'animate-spin')} />
          {isRetrying ? 'Tentando...' : `Tentar novamente (${maxRetries - retryCount} restantes)`}
        </Button>
      )}
    </div>
  )
}

// Uso
function ComicsList() {
  const [error, setError] = useState<string | null>(null)
  
  const loadComics = async () => {
    try {
      const data = await fetchComics()
      setError(null)
      // Set data...
    } catch (err) {
      setError(err.message)
    }
  }
  
  if (error) {
    return <RetryError error={error} onRetry={loadComics} />
  }
  
  return <ComicsContent />
}
```

---

## Mensagens de Erro

### Guia de Redação

**Bom:**
- ✅ "Email ou senha inválidos"
- ✅ "Erro ao carregar dados. Tente novamente."
- ✅ "Conexão perdida. Verifique sua internet."

**Ruim:**
- ❌ "Erro 401"
- ❌ "Falha na requisição POST /api/comics"
- ❌ "TypeError: Cannot read property 'map' of undefined"

---

### Exemplos por Contexto

**Autenticação:**
- "Email ou senha inválidos"
- "Esta conta não existe"
- "Senha incorreta. Tente novamente."
- "Muitas tentativas. Tente novamente em 5 minutos."

**Dados:**
- "Erro ao carregar dados. Tente novamente."
- "Nenhum dado encontrado"
- "Erro ao salvar. Verifique sua conexão."

**Upload:**
- "Arquivo muito grande. Tamanho máximo: 5MB"
- "Formato não suportado. Use JPG, PNG ou WebP"
- "Erro ao enviar arquivo. Tente novamente."

**Network:**
- "Sem conexão com a internet"
- "Conexão lenta. Alguns recursos podem não carregar."
- "Servidor indisponível. Tente novamente mais tarde."

---

## Acessibilidade

### Checklist

- [ ] `role="alert"` em mensagens de erro
- [ ] `aria-invalid="true"` em inputs com erro
- [ ] `aria-describedby` linkando input ao erro
- [ ] Focus no primeiro erro após submit
- [ ] Mensagens claras e descritivas
- [ ] Contraste adequado

### Exemplo: Form com Erro

```tsx
<form onSubmit={handleSubmit}>
  <div>
    <Input
      type="email"
      label="Email"
      aria-invalid={!!errors.email}
      aria-describedby={errors.email ? 'email-error' : undefined}
    />
    {errors.email && (
      <p id="email-error" className="text-destructive text-sm mt-1" role="alert">
        {errors.email.message}
      </p>
    )}
  </div>
  
  <Button type="submit">Enviar</Button>
</form>
```

---

## Referências

- [loading.md](./loading.md)
- [empty.md](./empty.md)
- [auth-flows.md](./auth-flows.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)