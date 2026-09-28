# 3D Web Guidelines — Diretrizes para 3D na Web

## Visão Geral

Este guia define as diretrizes para implementação de experiências 3D na web usando Three.js e React Three Fiber.

---

## Quando Usar 3D

### Use 3D Quando:

- **Produtos visuais:** Mostrar produtos de múltiplos ângulos
- **Experiências imersivas:** Landing pages impactantes
- **Visualização de dados:** Gráficos 3D, mapas
- **Jogos e gamificação:** Elementos interativos
- **Brand experiences:** Experiências de marca memoráveis

### Não Use 3D Quando:

- **Conteúdo principalmente textual:** Blogs, documentação
- **Forms e dashboards:** Interfaces de produtividade
- **Performance crítica:** Dispositivos antigos, conexões lentas
- **Acessibilidade prioritária:** 3D pode ser barreira

---

## Stack Recomendada

### Core

```json
{
  "three": "^0.160.0",
  "@react-three/fiber": "^8.15.0",
  "@react-three/drei": "^9.96.0"
}
```

### Opcional

```json
{
  "@react-three/postprocessing": "^2.16.0",
  "@react-three/rapier": "^1.2.0",
  "maath": "^0.10.0"
}
```

### Por Que Esta Stack?

| Biblioteca | Propósito |
|---|---|
| `three` | Engine 3D base |
| `@react-three/fiber` | React renderer para Three.js |
| `@react-three/drei` | Helpers e componentes prontos |
| `@react-three/postprocessing` | Efeitos de post-processing |
| `@react-three/rapier` | Física (opcional) |
| `maath` | Math helpers para animações |

---

## Estrutura de Pastas

```text
src/
├── components/
│   └── three/
│       ├── Canvas.tsx
│       ├── Scene.tsx
│       ├── Camera.tsx
│       ├── Lights.tsx
│       ├── models/
│       │   ├── ComicBook.tsx
│       │   └── Character.tsx
│       ├── effects/
│       │   ├── Bloom.tsx
│       │   └── DepthOfField.tsx
│       └── interactions/
│           ├── OrbitControls.tsx
│           └── ClickHandler.tsx
└── lib/
    └── three/
        ├── loader.ts
        ├── utils.ts
        └── constants.ts
```

---

## Componente Canvas Base

```tsx
// src/components/three/Canvas.tsx
import { Canvas } from '@react-three/fiber'
import { Suspense } from 'react'
import { Loader } from '@react-three/drei'

interface CanvasProps {
  children: React.ReactNode
  className?: string
}

export function Canvas3D({ children, className }: CanvasProps) {
  return (
    <div className={className}>
      <Canvas
        camera={{ position: [0, 0, 5], fov: 50 }}
        gl={{ antialias: true, alpha: true }}
        dpr={[1, 2]}
      >
        <Suspense fallback={null}>
          {children}
        </Suspense>
      </Canvas>
      <Loader />
    </div>
  )
}
```

---

## Scene Setup

```tsx
// src/components/three/Scene.tsx
import { Environment, OrbitControls } from '@react-three/drei'

export function Scene({ children }) {
  return (
    <>
      {/* Iluminação */}
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 10, 5]} intensity={1} />
      
      {/* Ambiente */}
      <Environment preset="city" />
      
      {/* Conteúdo */}
      {children}
      
      {/* Controles */}
      <OrbitControls 
        enableZoom={true}
        enablePan={false}
        minPolarAngle={Math.PI / 4}
        maxPolarAngle={Math.PI / 2}
      />
    </>
  )
}
```

---

## Carregamento de Modelos

### GLTF/GLB (Recomendado)

```tsx
// src/components/three/models/ComicBook.tsx
import { useGLTF } from '@react-three/drei'
import { useEffect, useRef } from 'react'
import { useFrame } from '@react-three/fiber'
import * as THREE from 'three'

export function ComicBook({ url, ...props }) {
  const { scene } = useGLTF(url)
  const ref = useRef<THREE.Group>(null)
  
  // Animação de rotação suave
  useFrame((state, delta) => {
    if (ref.current) {
      ref.current.rotation.y += delta * 0.5
    }
  })
  
  return (
    <group ref={ref} {...props}>
      <primitive object={scene} />
    </group>
  )
}

// Pre-carregar modelo
useGLTF.preload('/models/comic-book.glb')
```

### Otimização de Modelos

- **Formato:** GLB (binário, menor que glTF)
- **Compressão:** Draco compression
- **Texturas:** Max 1024x1024 para mobile
- **Polígonos:** < 50k para mobile, < 100k para desktop
- **Materiais:** Reuse materiais quando possível

### Ferramentas de Otimização

```bash
# Instalar glTF Transform
npm install -g @gltf-transform/cli

# Otimizar modelo
gltf-transform optimize input.glb output.glb \
  --compress draco \
  --texture-compress webp \
  --texture-size 1024
```

---

## Interações

### Click/Touch

```tsx
// src/components/three/interactions/ClickHandler.tsx
import { useFrame } from '@react-three/fiber'
import { useState, useRef } from 'react'
import * as THREE from 'three'

export function ClickableModel({ onClick, children }) {
  const [hovered, setHovered] = useState(false)
  const ref = useRef<THREE.Mesh>(null)
  
  useFrame((state) => {
    if (ref.current) {
      // Cursor pointer quando hover
      document.body.style.cursor = hovered ? 'pointer' : 'auto'
    }
  })
  
  return (
    <mesh
      ref={ref}
      onClick={onClick}
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
    >
      {children}
    </mesh>
  )
}
```

### Scroll-based Animation

```tsx
import { useScroll } from '@react-three/drei'
import { useFrame } from '@react-three/fiber'
import { useRef } from 'react'
import * as THREE from 'three'

export function ScrollModel() {
  const ref = useRef<THREE.Group>(null)
  const scroll = useScroll()
  
  useFrame(() => {
    if (ref.current) {
      // Rotação baseada no scroll (0 a 1)
      ref.current.rotation.y = scroll.offset * Math.PI * 2
      ref.current.position.y = scroll.offset * 2
    }
  })
  
  return (
    <group ref={ref}>
      {/* Modelo */}
    </group>
  )
}
```

---

## Performance

### Regras de Performance

1. **Instancing:** Use `InstancedMesh` para muitos objetos iguais
2. **LOD:** Use `LOD` para modelos distantes
3. **Frustum Culling:** Habilitado por padrão no Three.js
4. **Texture Loading:** Use `useTexture` do drei
5. **Geometry Reuse:** Reuse geometrias quando possível

### Exemplo: Instancing

```tsx
import { InstancedMesh } from '@react-three/fiber'
import { useMemo } from 'react'
import * as THREE from 'three'

export function ComicCollection({ count = 100 }) {
  const dummy = useMemo(() => new THREE.Object3D(), [])
  
  const positions = useMemo(() => {
    const positions = []
    for (let i = 0; i < count; i++) {
      positions.push({
        x: (Math.random() - 0.5) * 20,
        y: (Math.random() - 0.5) * 20,
        z: (Math.random() - 0.5) * 20,
      })
    }
    return positions
  }, [count])
  
  return (
    <InstancedMesh
      args={[undefined, undefined, count]}
      position={[0, 0, 0]}
    >
      <boxGeometry args={[1, 1.5, 0.1]} />
      <meshStandardMaterial color="hotpink" />
      {positions.map((pos, i) => {
        dummy.position.set(pos.x, pos.y, pos.z)
        dummy.updateMatrix()
        return <primitive key={i} object={dummy} />
      })}
    </InstancedMesh>
  )
}
```

### Budget de Performance

| Métrica | Mobile | Desktop |
|---|---|---|
| Draw Calls | < 100 | < 500 |
| Triangles | < 50k | < 200k |
| Textures | < 10 | < 50 |
| Texture Size | < 1024 | < 2048 |
| FPS Target | 30 | 60 |

---

## Responsividade

### Canvas Responsivo

```tsx
import { Canvas } from '@react-three/fiber'
import { useMediaQuery } from 'react-responsive'

export function ResponsiveCanvas({ children }) {
  const isMobile = useMediaQuery({ maxWidth: 768 })
  
  return (
    <Canvas
      camera={{ 
        position: [0, 0, isMobile ? 3 : 5], 
        fov: isMobile ? 60 : 50 
      }}
      gl={{ 
        antialias: !isMobile, // Desligar em mobile para performance
        alpha: true 
      }}
      dpr={isMobile ? [1, 1.5] : [1, 2]} // Menor DPR em mobile
    >
      {children}
    </Canvas>
  )
}
```

### Modelos Diferentes por Device

```tsx
export function AdaptiveModel() {
  const isMobile = useMediaQuery({ maxWidth: 768 })
  
  return (
    <>
      {isMobile ? (
        <ComicBookMobile url="/models/comic-mobile.glb" />
      ) : (
        <ComicBookDesktop url="/models/comic-desktop.glb" />
      )}
    </>
  )
}
```

---

## Acessibilidade

### Fallback para 2D

```tsx
import { Suspense } from 'react'
import { Canvas } from '@react-three/fiber'
import { ErrorBoundary } from 'react-error-boundary'

export function AccessibleScene() {
  return (
    <ErrorBoundary fallback={<Fallback2D />}>
      <Suspense fallback={<Loading />}>
        <Canvas>
          <Scene3D />
        </Canvas>
      </Suspense>
    </ErrorBoundary>
  )
}

function Fallback2D() {
  return (
    <div className="fallback-2d">
      <img src="/images/comic-fallback.jpg" alt="Comic book" />
      <p>Comic Book - Visualize em 3D com um dispositivo compatível</p>
    </div>
  )
}
```

### ARIA Labels

```tsx
export function InteractiveModel({ label, onClick }) {
  return (
    <mesh
      onClick={onClick}
      aria-label={label}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          onClick(e)
        }
      }}
    >
      {/* Modelo */}
    </mesh>
  )
}
```

---

## Exemplos de Uso

### Hero Section com 3D

```tsx
// src/app/page.tsx
import { Canvas3D } from '@/components/three/Canvas'
import { Scene } from '@/components/three/Scene'
import { ComicBook } from '@/components/three/models/ComicBook'

export default function HomePage() {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>ComixFlix</h1>
        <p>Descubra quadrinhos incríveis</p>
      </div>
      <Canvas3D className="hero-canvas">
        <Scene>
          <ComicBook url="/models/comic-book.glb" />
        </Scene>
      </Canvas3D>
    </section>
  )
}
```

### Product Viewer

```tsx
// src/components/ProductViewer.tsx
import { Canvas3D } from '@/components/three/Canvas'
import { Scene } from '@/components/three/Scene'
import { ComicBook } from '@/components/three/models/ComicBook'
import { OrbitControls } from '@react-three/drei'

export function ProductViewer({ modelUrl }) {
  return (
    <div className="product-viewer">
      <Canvas3D className="viewer-canvas">
        <Scene>
          <ComicBook url={modelUrl} />
          <OrbitControls 
            enableZoom={true}
            enablePan={false}
            minDistance={2}
            maxDistance={10}
          />
        </Scene>
      </Canvas3D>
      <div className="viewer-controls">
        <button onClick={() => {/* Zoom in */}}>+</button>
        <button onClick={() => {/* Zoom out */}>-</button>
        <button onClick={() => {/* Reset */}}>Reset</button>
      </div>
    </div>
  )
}
```

---

## Checklist de Implementação

### Setup

- [ ] Three.js e R3F instalados
- [ ] Estrutura de pastas criada
- [ ] Canvas base configurado
- [ ] Scene setup (luzes, ambiente)

### Modelos

- [ ] Modelos otimizados (GLB, Draco)
- [ ] Texturas comprimidas (WebP)
- [ ] Carregamento com Suspense
- [ ] Fallback para erro

### Performance

- [ ] Budget de performance respeitado
- [ ] Instancing para muitos objetos
- [ ] LOD para modelos distantes
- [ ] DPR ajustado por device

### Interação

- [ ] OrbitControls configurado
- [ ] Click handlers implementados
- [ ] Hover states
- [ ] Scroll animations (se aplicável)

### Responsividade

- [ ] Canvas responsivo
- [ ] Modelos adaptados por device
- [ ] Performance mobile otimizada

### Acessibilidade

- [ ] Fallback 2D
- [ ] ARIA labels
- [ ] Keyboard navigation
- [ ] Error boundary

---

## Referências

- [Three.js Docs](https://threejs.org/docs/)
- [React Three Fiber Docs](https://docs.pmnd.rs/react-three-fiber/)
- [Drei Helpers](https://github.com/pmndrs/drei)
- [glTF Transform](https://gltf-transform.dev/)
- [frontend-libraries.md](./frontend-libraries.md)