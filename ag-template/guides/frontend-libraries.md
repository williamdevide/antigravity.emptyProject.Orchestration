# Frontend Libraries — Bibliotecas Frontend Recomendadas

## Visão Geral

Este guia lista as bibliotecas frontend recomendadas para projetos, com justificativas e exemplos de uso.

---

## Stack Principal

### Framework

```json
{
  "next": "^14.0.0"
}
```

**Por que Next.js?**
- SSR e SSG out of the box
- App Router com React Server Components
- Otimização de imagens e fonts
- API routes integradas
- Deploy fácil (Vercel)

**Alternativas:**
- **Vite + React:** Para SPAs sem SSR
- **Astro:** Para sites de conteúdo estático
- **Remix:** Para apps com muito loader

---

### UI Framework

```json
{
  "tailwindcss": "^3.4.0",
  "@tailwindcss/typography": "^0.5.0",
  "@tailwindcss/forms": "^0.5.0",
  "clsx": "^2.1.0",
  "tailwind-merge": "^2.2.0"
}
```

**Por que Tailwind?**
- Desenvolvimento rápido
- Design system consistente
- Mobile-first por padrão
- Bundle size pequeno (purge)
- Comunidade grande

**Alternativas:**
- **Chakra UI:** Componentes prontos, mais opinativo
- **Mantine:** Componentes ricos, bom para dashboards
- **Radix UI + Tailwind:** Headless + styling custom

---

### Componentes UI

```json
{
  "@radix-ui/react-dialog": "^1.0.0",
  "@radix-ui/react-dropdown-menu": "^2.0.0",
  "@radix-ui/react-tabs": "^1.0.0",
  "@radix-ui/react-tooltip": "^1.0.0",
  "class-variance-authority": "^0.5.0",
  "lucide-react": "^0.300.0"
}
```

**Por que Radix?**
- Headless (você controla o styling)
- Acessibilidade built-in
- Composável
- Funciona com Tailwind

**Por que Lucide?**
- Ícones bonitos e consistentes
- Tree-shakeable
- Leve
- Ativo maintenance

**Alternativas:**
- **shadcn/ui:** Componentes prontos com Radix + Tailwind
- **Headless UI:** Alternativa ao Radix (da Tailwind Labs)
- **Heroicons:** Ícones da Tailwind Labs

---

### Animação

```json
{
  "framer-motion": "^10.18.0",
  "@motionone/dom": "^10.17.0"
}
```

**Por que Framer Motion?**
- API declarativa
- Layout animations
- Gestures (tap, drag, hover)
- Performance otimizada
- Funciona com SSR

**Alternativas:**
- **GSAP:** Animações complexas, timeline
- **AutoAnimate:** Animações automáticas simples
- **CSS transitions:** Para animações simples

---

### State Management

```json
{
  "zustand": "^4.5.0"
}
```

**Por que Zustand?**
- Simples e leve
- Sem boilerplate
- Funciona com SSR
- Devtools built-in

**Alternativas:**
- **Jotai:** State atômico, mais granular
- **Valtio:** Proxy-based, mutável
- **Redux Toolkit:** Para apps muito complexos
- **React Context + useReducer:** Para state simples

---

### Data Fetching

```json
{
  "@tanstack/react-query": "^5.17.0",
  "axios": "^1.6.0"
}
```

**Por que React Query?**
- Cache automático
- Background refetch
- Optimistic updates
- Devtools excelentes
- Funciona com qualquer API

**Por que Axios?**
- Interceptors
- Cancel requests
- TypeScript built-in
- Mais features que fetch

**Alternativas:**
- **SWR:** Mais simples, da Vercel
- **React Query + Axios:** Combinação recomendada
- **Fetch API:** Para casos simples

---

### Forms

```json
{
  "react-hook-form": "^7.49.0",
  "@hookform/resolvers": "^3.3.0",
  "zod": "^3.22.0"
}
```

**Por que React Hook Form?**
- Performance (menos re-renders)
- API simples
- Funciona com qualquer UI library
- Validação flexível

**Por que Zod?**
- Schema validation
- TypeScript inference
- Erros claros
- Ativo maintenance

**Alternativas:**
- **Formik:** Mais antigo, mais boilerplate
- **Yup:** Validação alternativa ao Zod
- **Valibot:** Validação mais leve que Zod

---

### Types

```json
{
  "typescript": "^5.3.0"
}
```

**Por que TypeScript?**
- Type safety
- Autocomplete
- Refactoring seguro
- Documentação viva

**Configuração Mínima:**

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

---

### Utils

```json
{
  "date-fns": "^3.2.0",
  "nuqs": "^1.15.0",
  "sonner": "^1.3.0"
}
```

**Por que date-fns?**
- Tree-shakeable
- Funcional
- Leve
- Boa tipagem

**Por que nuqs?**
- Query strings type-safe
- Sync com URL
- Serialização automática

**Por que Sonner?**
- Toasts bonitos
- Simples de usar
- Performance
- Acessível

**Alternativas:**
- **date-fns:** Day.js (mais leve), Luxon (mais features)
- **nuqs:** Query params manual, useQueryParams
- **Sonner:** React Hot Toast, react-toastify

---

## Stack por Tipo de Projeto

### Landing Page / Site Institucional

```json
{
  "next": "^14.0.0",
  "tailwindcss": "^3.4.0",
  "framer-motion": "^10.18.0",
  "@mdx-js/react": "^3.0.0",
  "next-mdx-remote": "^4.0.0"
}
```

**Foco:**
- Performance (Core Web Vitals)
- SEO
- Conteúdo estático
- Animações sutis

---

### Produto Web com Backend

```json
{
  "next": "^14.0.0",
  "tailwindcss": "^3.4.0",
  "@radix-ui/*": "^1.0.0",
  "framer-motion": "^10.18.0",
  "zustand": "^4.5.0",
  "@tanstack/react-query": "^5.17.0",
  "axios": "^1.6.0",
  "react-hook-form": "^7.49.0",
  "zod": "^3.22.0",
  "typescript": "^5.3.0"
}
```

**Foco:**
- CRUD operations
- Autenticação
- State management
- Validação
- Types

---

### Dashboard / Admin

```json
{
  "next": "^14.0.0",
  "tailwindcss": "^3.4.0",
  "@tanstack/react-table": "^8.11.0",
  "@tanstack/react-query": "^5.17.0",
  "recharts": "^2.10.0",
  "date-fns": "^3.2.0",
  "react-hook-form": "^7.49.0",
  "zod": "^3.22.0"
}
```

**Foco:**
- Tabelas complexas
- Gráficos
- Filtros
- Forms
- Data handling

---

### E-commerce

```json
{
  "next": "^14.0.0",
  "tailwindcss": "^3.4.0",
  "@radix-ui/*": "^1.0.0",
  "framer-motion": "^10.18.0",
  "zustand": "^4.5.0",
  "@tanstack/react-query": "^5.17.0",
  "react-hook-form": "^7.49.0",
  "zod": "^3.22.0",
  "@stripe/stripe-js": "^3.0.0"
}
```

**Foco:**
- Product listings
- Cart
- Checkout
- Pagamentos
- Performance

---

## Estrutura de Imports

```text
src/
├── app/                    # Next.js App Router
├── components/
│   ├── ui/                # Componentes de UI genéricos
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   └── index.ts
│   ├── features/          # Componentes específicos de features
│   │   ├── comics/
│   │   └── series/
│   └── layout/            # Layout components
│       ├── Header.tsx
│       ├── BottomNav.tsx
│       └── Footer.tsx
├── lib/
│   ├── api/               # API client
│   │   ├── client.ts
│   │   └── endpoints.ts
│   ├── hooks/             # Custom hooks
│   │   ├── useAuth.ts
│   │   └── useComics.ts
│   ├── utils/             # Utility functions
│   │   ├── format.ts
│   │   └── validate.ts
│   └── types/             # TypeScript types
│       ├── index.ts
│       └── comic.ts
├── styles/
│   ├── globals.css
│   └── tokens.css
└── types/                 # Global types
    └── index.ts
```

---

## Exemplos de Uso

### Button Component

```tsx
// src/components/ui/Button.tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border border-input bg-background hover:bg-accent',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {}

export function Button({ className, variant, size, ...props }: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}
```

### API Client

```ts
// src/lib/api/client.ts
import axios from 'axios'

export const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para auth
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Interceptor para erros
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect para login
    }
    return Promise.reject(error)
  }
)
```

### Custom Hook

```ts
// src/lib/hooks/useComics.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '@/lib/api/client'
import type { Comic } from '@/lib/types'

export function useComics() {
  return useQuery({
    queryKey: ['comics'],
    queryFn: async () => {
      const { data } = await api.get<Comic[]>('/comics')
      return data
    },
  })
}

export function useComic(id: string) {
  return useQuery({
    queryKey: ['comics', id],
    queryFn: async () => {
      const { data } = await api.get<Comic>(`/comics/${id}`)
      return data
    },
    enabled: !!id,
  })
}

export function useCreateComic() {
  const queryClient = useQueryClient()
  
  return useMutation({
    mutationFn: async (data: Partial<Comic>) => {
      const { data: response } = await api.post<Comic>('/comics', data)
      return response
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['comics'] })
    },
  })
}
```

### Form com Validação

```tsx
// src/components/features/comics/ComicForm.tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { useCreateComic } from '@/lib/hooks/useComics'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'

const comicSchema = z.object({
  titulo: z.string().min(1, 'Título é obrigatório'),
  editora: z.string().min(1, 'Editora é obrigatória'),
  preco: z.number().min(0, 'Preço deve ser positivo'),
  urlCapa: z.string().url('URL inválida'),
})

type ComicFormData = z.infer<typeof comicSchema>

export function ComicForm() {
  const createComic = useCreateComic()
  
  const { register, handleSubmit, formState: { errors } } = useForm<ComicFormData>({
    resolver: zodResolver(comicSchema),
  })
  
  const onSubmit = async (data: ComicFormData) => {
    await createComic.mutateAsync(data)
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <Input {...register('titulo')} placeholder="Título" />
        {errors.titulo && <span>{errors.titulo.message}</span>}
      </div>
      
      <div>
        <Input {...register('editora')} placeholder="Editora" />
        {errors.editora && <span>{errors.editora.message}</span>}
      </div>
      
      <div>
        <Input type="number" step="0.01" {...register('preco', { valueAsNumber: true })} placeholder="Preço" />
        {errors.preco && <span>{errors.preco.message}</span>}
      </div>
      
      <div>
        <Input {...register('urlCapa')} placeholder="URL da Capa" />
        {errors.urlCapa && <span>{errors.urlCapa.message}</span>}
      </div>
      
      <Button type="submit" disabled={createComic.isPending}>
        {createComic.isPending ? 'Salvando...' : 'Salvar'}
      </Button>
    </form>
  )
}
```

---

## Checklist de Setup

### Core

- [ ] Next.js instalado e configurado
- [ ] TypeScript configurado
- [ ] Tailwind configurado
- [ ] ESLint e Prettier configurados

### UI

- [ ] Radix UI instalado
- [ ] Lucide icons instalado
- [ ] Componentes de UI base criados (Button, Input, Card)

### State & Data

- [ ] Zustand instalado (se necessário)
- [ ] React Query instalado
- [ ] Axios instalado
- [ ] API client configurado

### Forms & Validation

- [ ] React Hook Form instalado
- [ ] Zod instalado
- [ ] Hookform resolvers instalado

### Utils

- [ ] date-fns instalado
- [ ] nuqs instalado (se necessário)
- [ ] Sonner instalado
- [ ] clsx e tailwind-merge instalados

### Types

- [ ] Types globais criados
- [ ] Types de API criados
- [ ] Path aliases configurados

---

## Referências

- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind Docs](https://tailwindcss.com/docs)
- [Radix UI](https://www.radix-ui.com/)
- [React Query Docs](https://tanstack.com/query/latest)
- [Zod Docs](https://zod.dev/)
- [3d-web-guidelines.md](./3d-web-guidelines.md)
- [mcp-servers.md](./mcp-servers.md)