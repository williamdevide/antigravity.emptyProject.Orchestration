# Splash Screen — Tela de Abertura

## Visão Geral

Este guia define os padrões de splash screen para projetos web mobile-first e PWA.

---

## Quando Usar

**Use splash screen quando:**
- App é PWA (Progressive Web App)
- Carregamento inicial é perceptível
- Branding é importante
- Quer reduzir percepção de tempo de carga

**Não use quando:**
- Carregamento é instantâneo (< 500ms)
- Landing page já serve como splash
- Conteúdo é prioritário sobre branding

---

## Tipos de Splash Screen

### 1. Splash Estática

**Quando usar:**
- Branding simples
- Carregamento rápido
- PWA básico

**Estrutura:**

```tsx
// src/components/ui/SplashScreen.tsx
import Image from 'next/image'

export function SplashScreen() {
  return (
    <div className="splash-screen fixed inset-0 z-50 bg-background">
      <div className="flex flex-col items-center justify-center min-h-screen">
        {/* Logo */}
        <div className="relative w-32 h-32 mb-8">
          <Image
            src="/images/logo.svg"
            alt="ComixFlix"
            fill
            className="object-contain"
            priority
          />
        </div>

        {/* Tagline (opcional) */}
        <p className="text-muted-foreground text-lg">
          Descubra quadrinhos incríveis
        </p>

        {/* Loading indicator (opcional) */}
        <div className="mt-8">
          <LoadingSpinner />
        </div>
      </div>
    </div>
  )
}
```

**Estilos Tailwind:**

```css
.splash-screen {
  @apply bg-background;
  @apply flex items-center justify-center;
}
```

---

### 2. Splash Animada

**Quando usar:**
- Branding mais elaborado
- Quer criar impacto
- Carregamento médio (1-3s)

**Estrutura (com Framer Motion):**

```tsx
// src/components/ui/AnimatedSplash.tsx
'use client'

import { useEffect, useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import Image from 'next/image'

interface AnimatedSplashProps {
  isLoading: boolean
  onReady?: () => void
}

export function AnimatedSplash({ isLoading, onReady }: AnimatedSplashProps) {
  const [isExiting, setIsExiting] = useState(false)

  useEffect(() => {
    if (!isLoading && !isExiting) {
      // Delay para animação de saída
      setTimeout(() => {
        setIsExiting(true)
        setTimeout(() => {
          onReady?.()
        }, 500) // Duração da animação de saída
      }, 1000) // Tempo mínimo de exibição
    }
  }, [isLoading, isExiting, onReady])

  return (
    <AnimatePresence>
      {!isExiting && (
        <motion.div
          className="splash-screen fixed inset-0 z-50 bg-background"
          initial={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.5 }}
        >
          <div className="flex flex-col items-center justify-center min-h-screen">
            {/* Logo com scale animation */}
            <motion.div
              className="relative w-32 h-32 mb-8"
              initial={{ scale: 0.5, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.5, delay: 0.2 }}
            >
              <Image
                src="/images/logo.svg"
                alt="ComixFlix"
                fill
                className="object-contain"
                priority
              />
            </motion.div>

            {/* Tagline com fade in */}
            <motion.p
              className="text-muted-foreground text-lg"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.4 }}
            >
              Descubra quadrinhos incríveis
            </motion.p>

            {/* Loading spinner */}
            <motion.div
              className="mt-8"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.5, delay: 0.6 }}
            >
              <LoadingSpinner />
            </motion.div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

---

### 3. Splash com Progresso

**Quando usar:**
- Carregamento longo (> 3s)
- Quer mostrar progresso real
- Múltiplos recursos para carregar

**Estrutura:**

```tsx
// src/components/ui/ProgressSplash.tsx
'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import Image from 'next/image'

interface ProgressSplashProps {
  total: number
  current: number
  onReady?: () => void
}

export function ProgressSplash({ total, current, onReady }: ProgressSplashProps) {
  const progress = (current / total) * 100
  const isComplete = current >= total

  useEffect(() => {
    if (isComplete) {
      setTimeout(() => {
        onReady?.()
      }, 500)
    }
  }, [isComplete, onReady])

  return (
    <div className="splash-screen fixed inset-0 z-50 bg-background">
      <div className="flex flex-col items-center justify-center min-h-screen px-4">
        {/* Logo */}
        <div className="relative w-32 h-32 mb-8">
          <Image
            src="/images/logo.svg"
            alt="ComixFlix"
            fill
            className="object-contain"
            priority
          />
        </div>

        {/* Progress bar */}
        <div className="w-full max-w-xs bg-muted rounded-full h-2 mb-4">
          <motion.div
            className="bg-primary h-2 rounded-full"
            initial={{ width: 0 }}
            animate={{ width: `${progress}%` }}
            transition={{ duration: 0.3 }}
          />
        </div>

        {/* Progress text */}
        <p className="text-muted-foreground text-sm">
          Carregando... {Math.round(progress)}%
        </p>

        {/* Loading status */}
        <p className="text-muted-foreground text-xs mt-2">
          {current} de {total} recursos
        </p>
      </div>
    </div>
  )
}

// Exemplo de uso
export function AppLoader() {
  const [loaded, setLoaded] = useState(0)
  const total = 5 // Imagens, dados, etc.

  useEffect(() => {
    // Simular carregamento
    const interval = setInterval(() => {
      setLoaded(prev => {
        if (prev >= total) {
          clearInterval(interval)
          return total
        }
        return prev + 1
      })
    }, 500)

    return () => clearInterval(interval)
  }, [])

  return <ProgressSplash total={total} current={loaded} onReady={() => console.log('Ready!')} />
}
```

---

### 4. Splash com Skeleton

**Quando usar:**
- Quer mostrar estrutura da app
- Carregamento de dados
- Reduz percepção de espera

**Estrutura:**

```tsx
// src/components/ui/SkeletonSplash.tsx
import { Skeleton } from '@/components/ui/Skeleton'

export function SkeletonSplash() {
  return (
    <div className="splash-screen fixed inset-0 z-50 bg-background">
      <div className="container mx-auto px-4 py-8">
        {/* Header skeleton */}
        <div className="flex items-center justify-between mb-8">
          <Skeleton className="w-32 h-8" />
          <Skeleton className="w-8 h-8 rounded-full" />
        </div>

        {/* Hero skeleton */}
        <Skeleton className="w-full h-64 rounded-lg mb-8" />

        {/* Content grid skeleton */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="space-y-2">
              <Skeleton className="w-full h-40 rounded" />
              <Skeleton className="w-3/4 h-4" />
              <Skeleton className="w-1/2 h-4" />
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
```

---

## PWA Splash Screen

### Configuração manifest.json

```json
// public/manifest.json
{
  "name": "ComixFlix",
  "short_name": "ComixFlix",
  "description": "Descubra quadrinhos incríveis",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "splash_pages": null
}
```

### Apple Touch Icon

```html
<!-- src/app/layout.tsx -->
<head>
  <link rel="apple-touch-icon" href="/icons/apple-touch-icon.png" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="ComixFlix" />
</head>
```

### Native Splash Screen (iOS)

Para iOS, criar imagens de splash screen:

```text
public/
└── splash/
    ├── splash-iphone-se.png (640x1136)
    ├── splash-iphone-8.png (750x1334)
    ├── splash-iphone-x.png (1125x2436)
    ├── splash-ipad.png (1536x2048)
    └── splash-ipad-pro.png (2048x2732)
```

---

## Gerenciamento de Estado

### Hook de Loading

```tsx
// src/hooks/useAppLoading.ts
'use client'

import { useState, useEffect } from 'react'

interface UseAppLoadingOptions {
  minDuration?: number
  onReady?: () => void
}

export function useAppLoading(options: UseAppLoadingOptions = {}) {
  const { minDuration = 1000, onReady } = options
  const [isLoading, setIsLoading] = useState(true)
  const [isReady, setIsReady] = useState(false)

  useEffect(() => {
    // Simular carregamento inicial
    const loadApp = async () => {
      try {
        // Carregar recursos essenciais
        await Promise.all([
          loadImages(),
          loadData(),
          // ... outros recursos
        ])

        // Garantir tempo mínimo de splash
        await new Promise(resolve => setTimeout(resolve, minDuration))

        setIsLoading(false)
        
        // Delay antes de considerar pronto
        setTimeout(() => {
          setIsReady(true)
          onReady?.()
        }, 500)
      } catch (error) {
        console.error('Erro no carregamento:', error)
        setIsLoading(false)
        setIsReady(true)
      }
    }

    loadApp()
  }, [minDuration, onReady])

  return { isLoading, isReady }
}

// Helpers
async function loadImages() {
  // Carregar imagens críticas
}

async function loadData() {
  // Carregar dados iniciais
}
```

### Uso no Layout

```tsx
// src/app/page.tsx
'use client'

import { useAppLoading } from '@/hooks/useAppLoading'
import { AnimatedSplash } from '@/components/ui/AnimatedSplash'
import { MainContent } from '@/components/MainContent'

export default function HomePage() {
  const { isLoading, isReady } = useAppLoading({
    minDuration: 1000,
    onReady: () => console.log('App ready!'),
  })

  return (
    <>
      {isLoading && <AnimatedSplash isLoading={isLoading} />}
      {isReady && <MainContent />}
    </>
  )
}
```

---

## Acessibilidade

### Checklist

- [ ] Alt text em logos
- [ ] Loading indicator para screen readers
- [ ] Não bloquear navegação após carregamento
- [ ] Respeitar preferências de redução de movimento
- [ ] Contraste adequado

### Exemplo: Respeitar Preferências

```tsx
import { useReducedMotion } from 'framer-motion'

export function AnimatedSplash({ isLoading }) {
  const shouldReduceMotion = useReducedMotion()

  return (
    <motion.div
      initial={{ opacity: 1 }}
      animate={{ opacity: isLoading ? 1 : 0 }}
      transition={{ 
        duration: shouldReduceMotion ? 0 : 0.5,
        ease: shouldReduceMotion ? 'linear' : 'easeInOut'
      }}
    >
      {/* Splash content */}
    </motion.div>
  )
}
```

---

## Performance

### Otimizações

- **Imagens otimizadas:** WebP, SVG
- **Lazy load:** Imagens não críticas
- **Preload:** Recursos essenciais
- **Cache:** Service worker para PWA

### Exemplo: Preload

```html
<head>
  <link rel="preload" href="/images/logo.svg" as="image" />
  <link rel="preload" href="/fonts/inter.woff2" as="font" crossorigin />
</head>
```

### Exemplo: Service Worker

```ts
// src/service-worker.ts
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('splash-v1').then((cache) => {
      return cache.addAll([
        '/',
        '/images/logo.svg',
        '/fonts/inter.woff2',
      ])
    })
  )
})
```

---

## Exemplos de Uso

### App com Carregamento de Dados

```tsx
// src/app/page.tsx
'use client'

import { useEffect, useState } from 'react'
import { AnimatedSplash } from '@/components/ui/AnimatedSplash'
import { useAppLoading } from '@/hooks/useAppLoading'

export default function HomePage() {
  const [data, setData] = useState(null)
  const { isLoading, isReady } = useAppLoading({
    minDuration: 1500,
  })

  useEffect(() => {
    // Carregar dados
    fetch('/api/comics')
      .then(res => res.json())
      .then(data => setData(data))
  }, [])

  return (
    <>
      {isLoading && <AnimatedSplash isLoading={isLoading} />}
      {isReady && data && (
        <MainContent comics={data.comics} />
      )}
    </>
  )
}
```

### PWA com Splash Nativo

```tsx
// src/app/layout.tsx
import { PwaSplash } from '@/components/ui/PwaSplash'

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <head>
        <link rel="manifest" href="/manifest.json" />
        <meta name="theme-color" content="#000000" />
      </head>
      <body>
        <PwaSplash />
        {children}
      </body>
    </html>
  )
}
```

---

## Referências

- [menus.md](./menus.md)
- [loading.md](./loading.md)
- [frontend-libraries.md](../guides/frontend-libraries.md)
- [3d-web-guidelines.md](../guides/3d-web-guidelines.md)