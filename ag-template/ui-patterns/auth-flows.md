# Auth Flows — Fluxos de Autenticação

## Visão Geral

Este guia define os padrões de autenticação para projetos web mobile-first.

---

## Tipos de Autenticação

### 1. Email + Senha

**Quando usar:**
- Método tradicional
- Maior controle sobre UX
- Sem dependência de terceiros

**Fluxo:**
1. Usuário entra email e senha
2. Validação de formato
3. Submit para backend
4. Recebe token
5. Armazena token
6. Redireciona para dashboard

---

### 2. OAuth (Google, GitHub, etc.)

**Quando usar:**
- Reduzir atrito no registro
- Confiança em provedores
- Menos responsabilidade com senhas

**Fluxo:**
1. Usuário clica "Entrar com Google"
2. Redirect para OAuth provider
3. Usuário autoriza
4. Redirect de volta com code
5. Exchange code por token
6. Armazena token
7. Redireciona para dashboard

---

### 3. Magic Link

**Quando usar:**
- Zero senha para gerenciar
- Experiência simplificada
- Email já verificado

**Fluxo:**
1. Usuário entra email
2. Recebe email com link mágico
3. Clica no link
4. Token é gerado automaticamente
5. Redireciona para dashboard

---

## Componentes de Autenticação

### Login Form

```tsx
// src/components/features/auth/LoginForm.tsx
'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { useAuth } from '@/lib/hooks/useAuth'

const loginSchema = z.object({
  email: z.string().email('Email inválido'),
  senha: z.string().min(6, 'Senha deve ter pelo menos 6 caracteres'),
})

type LoginFormData = z.infer<typeof loginSchema>

export function LoginForm() {
  const [error, setError] = useState<string | null>(null)
  const { login, isPending } = useAuth()
  
  const { register, handleSubmit, formState: { errors } } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  })
  
  const onSubmit = async (data: LoginFormData) => {
    try {
      setError(null)
      await login(data.email, data.senha)
      // Redirect handled by hook
    } catch (err) {
      setError('Email ou senha inválidos')
    }
  }
  
  return (
    <div className="auth-form w-full max-w-md mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Entrar</h1>
      
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {/* Email */}
        <div>
          <Input
            {...register('email')}
            type="email"
            placeholder="seu@email.com"
            label="Email"
            autoComplete="email"
          />
          {errors.email && (
            <p className="text-sm text-destructive mt-1">{errors.email.message}</p>
          )}
        </div>
        
        {/* Senha */}
        <div>
          <Input
            {...register('senha')}
            type="password"
            placeholder="••••••••"
            label="Senha"
            autoComplete="current-password"
          />
          {errors.senha && (
            <p className="text-sm text-destructive mt-1">{errors.senha.message}</p>
          )}
        </div>
        
        {/* Error */}
        {error && (
          <div className="p-3 bg-destructive/10 text-destructive rounded-md text-sm">
            {error}
          </div>
        )}
        
        {/* Submit */}
        <Button type="submit" className="w-full" disabled={isPending}>
          {isPending ? 'Entrando...' : 'Entrar'}
        </Button>
      </form>
      
      {/* Forgot Password */}
      <div className="mt-4 text-center">
        <Link href="/recuperar-senha" className="text-sm text-muted-foreground hover:text-foreground">
          Esqueceu a senha?
        </Link>
      </div>
      
      {/* Register */}
      <div className="mt-6 text-center">
        <p className="text-sm text-muted-foreground">
          Não tem uma conta?{' '}
          <Link href="/registro" className="text-primary hover:underline">
            Criar conta
          </Link>
        </p>
      </div>
      
      {/* OAuth */}
      <div className="mt-8">
        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t" />
          </div>
          <div className="relative flex justify-center text-xs uppercase">
            <span className="bg-background px-2 text-muted-foreground">
              Ou entre com
            </span>
          </div>
        </div>
        
        <div className="mt-4 space-y-2">
          <Button variant="outline" className="w-full" onClick={() => loginWithGoogle()}>
            <GoogleIcon className="w-5 h-5 mr-2" />
            Google
          </Button>
          <Button variant="outline" className="w-full" onClick={() => loginWithGitHub()}>
            <GitHubIcon className="w-5 h-5 mr-2" />
            GitHub
          </Button>
        </div>
      </div>
    </div>
  )
}
```

---

### Register Form

```tsx
// src/components/features/auth/RegisterForm.tsx
'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { useAuth } from '@/lib/hooks/useAuth'

const registerSchema = z.object({
  nome: z.string().min(2, 'Nome deve ter pelo menos 2 caracteres'),
  email: z.string().email('Email inválido'),
  senha: z.string().min(6, 'Senha deve ter pelo menos 6 caracteres'),
  confirmarSenha: z.string(),
}).refine((data) => data.senha === data.confirmarSenha, {
  message: 'Senhas não coincidem',
  path: ['confirmarSenha'],
})

type RegisterFormData = z.infer<typeof registerSchema>

export function RegisterForm() {
  const [error, setError] = useState<string | null>(null)
  const { register: registerUser, isPending } = useAuth()
  
  const { register, handleSubmit, formState: { errors } } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
  })
  
  const onSubmit = async (data: RegisterFormData) => {
    try {
      setError(null)
      await registerUser({
        nome: data.nome,
        email: data.email,
        senha: data.senha,
      })
      // Redirect handled by hook
    } catch (err) {
      setError('Erro ao criar conta. Tente novamente.')
    }
  }
  
  return (
    <div className="auth-form w-full max-w-md mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Criar Conta</h1>
      
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {/* Nome */}
        <div>
          <Input
            {...register('nome')}
            type="text"
            placeholder="Seu nome"
            label="Nome"
            autoComplete="name"
          />
          {errors.nome && (
            <p className="text-sm text-destructive mt-1">{errors.nome.message}</p>
          )}
        </div>
        
        {/* Email */}
        <div>
          <Input
            {...register('email')}
            type="email"
            placeholder="seu@email.com"
            label="Email"
            autoComplete="email"
          />
          {errors.email && (
            <p className="text-sm text-destructive mt-1">{errors.email.message}</p>
          )}
        </div>
        
        {/* Senha */}
        <div>
          <Input
            {...register('senha')}
            type="password"
            placeholder="••••••••"
            label="Senha"
            autoComplete="new-password"
          />
          {errors.senha && (
            <p className="text-sm text-destructive mt-1">{errors.senha.message}</p>
          )}
        </div>
        
        {/* Confirmar Senha */}
        <div>
          <Input
            {...register('confirmarSenha')}
            type="password"
            placeholder="••••••••"
            label="Confirmar Senha"
            autoComplete="new-password"
          />
          {errors.confirmarSenha && (
            <p className="text-sm text-destructive mt-1">{errors.confirmarSenha.message}</p>
          )}
        </div>
        
        {/* Error */}
        {error && (
          <div className="p-3 bg-destructive/10 text-destructive rounded-md text-sm">
            {error}
          </div>
        )}
        
        {/* Submit */}
        <Button type="submit" className="w-full" disabled={isPending}>
          {isPending ? 'Criando conta...' : 'Criar Conta'}
        </Button>
      </form>
      
      {/* Login */}
      <div className="mt-6 text-center">
        <p className="text-sm text-muted-foreground">
          Já tem uma conta?{' '}
          <Link href="/login" className="text-primary hover:underline">
            Entrar
          </Link>
        </p>
      </div>
    </div>
  )
}
```

---

### Auth Hook

```ts
// src/lib/hooks/useAuth.ts
'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { api } from '@/lib/api/client'

interface User {
  id: string
  email: string
  nome: string
}

interface AuthResponse {
  user: User
  token: string
}

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [isPending, setIsPending] = useState(false)
  const router = useRouter()
  
  // Check auth on mount
  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      loadUser()
    }
  }, [])
  
  async function loadUser() {
    try {
      const { data } = await api.get<AuthResponse>('/auth/me')
      setUser(data.user)
    } catch {
      localStorage.removeItem('token')
      setUser(null)
    }
  }
  
  async function login(email: string, senha: string) {
    setIsPending(true)
    try {
      const { data } = await api.post<AuthResponse>('/auth/login', { email, senha })
      localStorage.setItem('token', data.token)
      setUser(data.user)
      router.push('/dashboard')
    } finally {
      setIsPending(false)
    }
  }
  
  async function register(data: { nome: string; email: string; senha: string }) {
    setIsPending(true)
    try {
      const { data: response } = await api.post<AuthResponse>('/auth/register', data)
      localStorage.setItem('token', response.token)
      setUser(response.user)
      router.push('/dashboard')
    } finally {
      setIsPending(false)
    }
  }
  
  async function logout() {
    setIsPending(true)
    try {
      await api.post('/auth/logout')
    } finally {
      localStorage.removeItem('token')
      setUser(null)
      router.push('/login')
      setIsPending(false)
    }
  }
  
  async function loginWithGoogle() {
    // Redirect to OAuth
    window.location.href = `${api.defaults.baseURL}/auth/google`
  }
  
  async function loginWithGitHub() {
    // Redirect to OAuth
    window.location.href = `${api.defaults.baseURL}/auth/github`
  }
  
  return {
    user,
    isPending,
    isAuthenticated: !!user,
    login,
    register,
    logout,
    loginWithGoogle,
    loginWithGitHub,
  }
}
```

---

### Protected Route

```tsx
// src/components/features/auth/ProtectedRoute.tsx
'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/hooks/useAuth'
import { LoadingSpinner } from '@/components/ui/LoadingSpinner'

interface ProtectedRouteProps {
  children: React.ReactNode
}

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { isAuthenticated, isPending } = useAuth()
  const router = useRouter()
  
  useEffect(() => {
    if (!isPending && !isAuthenticated) {
      router.push('/login')
    }
  }, [isAuthenticated, isPending, router])
  
  if (isPending) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <LoadingSpinner />
      </div>
    )
  }
  
  if (!isAuthenticated) {
    return null
  }
  
  return <>{children}</>
}

// Exemplo de uso
// src/app/dashboard/page.tsx
import { ProtectedRoute } from '@/components/features/auth/ProtectedRoute'

export default function DashboardPage() {
  return (
    <ProtectedRoute>
      <DashboardContent />
    </ProtectedRoute>
  )
}
```

---

### Forgot Password Flow

```tsx
// src/components/features/auth/ForgotPasswordForm.tsx
'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { api } from '@/lib/api/client'

const forgotPasswordSchema = z.object({
  email: z.string().email('Email inválido'),
})

type ForgotPasswordFormData = z.infer<typeof forgotPasswordSchema>

export function ForgotPasswordForm() {
  const [isSent, setIsSent] = useState(false)
  const [isPending, setIsPending] = useState(false)
  
  const { register, handleSubmit, formState: { errors } } = useForm<ForgotPasswordFormData>({
    resolver: zodResolver(forgotPasswordSchema),
  })
  
  const onSubmit = async (data: ForgotPasswordFormData) => {
    setIsPending(true)
    try {
      await api.post('/auth/forgot-password', { email: data.email })
      setIsSent(true)
    } catch (err) {
      console.error('Erro ao enviar email:', err)
    } finally {
      setIsPending(false)
    }
  }
  
  if (isSent) {
    return (
      <div className="auth-form w-full max-w-md mx-auto p-6 text-center">
        <h1 className="text-2xl font-bold mb-4">Email Enviado!</h1>
        <p className="text-muted-foreground mb-6">
          Enviamos um link de recuperação para seu email.
        </p>
        <Link href="/login">
          <Button>Voltar para o login</Button>
        </Link>
      </div>
    )
  }
  
  return (
    <div className="auth-form w-full max-w-md mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Recuperar Senha</h1>
      
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div>
          <Input
            {...register('email')}
            type="email"
            placeholder="seu@email.com"
            label="Email"
          />
          {errors.email && (
            <p className="text-sm text-destructive mt-1">{errors.email.message}</p>
          )}
        </div>
        
        <Button type="submit" className="w-full" disabled={isPending}>
          {isPending ? 'Enviando...' : 'Enviar Link'}
        </Button>
      </form>
      
      <div className="mt-6 text-center">
        <Link href="/login" className="text-sm text-muted-foreground hover:text-foreground">
          Voltar para o login
        </Link>
      </div>
    </div>
  )
}
```

---

## Layouts de Autenticação

### Auth Layout

```tsx
// src/components/layout/AuthLayout.tsx
import Link from 'next/link'

interface AuthLayoutProps {
  children: React.ReactNode
}

export function AuthLayout({ children }: AuthLayoutProps) {
  return (
    <div className="min-h-screen grid md:grid-cols-2">
      {/* Left: Branding */}
      <div className="hidden md:flex flex-col items-center justify-center bg-muted p-8">
        <div className="max-w-md text-center">
          <h1 className="text-4xl font-bold mb-4">Bem-vindo ao ComixFlix</h1>
          <p className="text-muted-foreground text-lg">
            Descubra e acompanhe seus quadrinhos favoritos em um só lugar.
          </p>
        </div>
      </div>
      
      {/* Right: Form */}
      <div className="flex items-center justify-center p-6">
        <div className="w-full max-w-md">
          {/* Mobile Logo */}
          <Link href="/" className="md:hidden block mb-8">
            <span className="text-2xl font-bold">ComixFlix</span>
          </Link>
          
          {children}
        </div>
      </div>
    </div>
  )
}

// Uso: src/app/login/page.tsx
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

---

## Acessibilidade

### Checklist

- [ ] Labels em todos os inputs
- [ ] Error messages claras
- [ ] Focus states visíveis
- [ ] Navegação por teclado
- [ ] Screen reader friendly
- [ ] Contraste adequado

### Exemplo: Error Messages

```tsx
<Input
  type="email"
  label="Email"
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? 'email-error' : undefined}
/>
{errors.email && (
  <p id="email-error" className="text-sm text-destructive mt-1" role="alert">
    {errors.email.message}
  </p>
)}
```

---

## Segurança

### Melhores Práticas

1. **HTTPS sempre**
2. **Senhas hash (bcrypt, argon2)**
3. **Rate limiting em login**
4. **JWT com expiração curta**
5. **Refresh tokens**
6. **CSRF protection**
7. **XSS protection**

### Exemplo: Rate Limiting

```ts
// functions/api/auth/login.ts
import { rateLimit } from '@/lib/rate-limit'

export async function POST(req: Request) {
  const ip = req.headers.get('x-forwarded-for')
  
  // Check rate limit
  const { success } = await rateLimit({
    key: `login:${ip}`,
    limit: 5,
    window: 60 * 1000, // 5 tentativas por minuto
  })
  
  if (!success) {
    return new Response('Muitas tentativas. Tente novamente em 1 minuto.', { status: 429 })
  }
  
  // Proceed with login...
}
```

---

## Referências

- [menus.md](./menus.md)
- [loading.md](./loading.md)
- [error.md](./error.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)