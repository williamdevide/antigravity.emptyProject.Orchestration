# Search & Filter — Busca e Filtros

## Visão Geral

Este guia define os padrões de busca e filtros para projetos web mobile-first.

---

## Search Bar

**Quando usar:**
- Busca de conteúdo
- Filtro por texto
- Autocomplete

**Estrutura:**

```tsx
// src/components/ui/SearchBar.tsx
'use client'

import { useState, useEffect } from 'react'
import { Search, X } from 'lucide-react'
import { Input } from '@/components/ui/Input'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface SearchBarProps {
  placeholder?: string
  value?: string
  onChange?: (value: string) => void
  onClear?: () => void
  onSubmit?: (value: string) => void
  className?: string
  autoFocus?: boolean
}

export function SearchBar({
  placeholder = 'Buscar...',
  value,
  onChange,
  onClear,
  onSubmit,
  className,
  autoFocus,
}: SearchBarProps) {
  const [localValue, setLocalValue] = useState(value || '')
  
  useEffect(() => {
    setLocalValue(value || '')
  }, [value])
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onSubmit?.(localValue)
  }
  
  const handleClear = () => {
    setLocalValue('')
    onClear?.()
  }
  
  return (
    <form onSubmit={handleSubmit} className={cn('relative', className)}>
      <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
      
      <Input
        type="search"
        placeholder={placeholder}
        value={localValue}
        onChange={(e) => setLocalValue(e.target.value)}
        className="pl-10 pr-10"
        autoFocus={autoFocus}
      />
      
      {localValue && (
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="absolute right-1 top-1/2 -translate-y-1/2 h-8 w-8"
          onClick={handleClear}
        >
          <X className="w-4 h-4" />
        </Button>
      )}
    </form>
  )
}
```

**Uso:**

```tsx
import { SearchBar } from '@/components/ui/SearchBar'

<SearchBar
  placeholder="Buscar quadrinhos..."
  value={searchQuery}
  onChange={setSearchQuery}
  onSubmit={handleSearch}
  onClear={() => setSearchQuery('')}
/>
```

---

## Search com Autocomplete

**Quando usar:**
- Sugestões de busca
- Busca rápida
- Histórico

**Estrutura:**

```tsx
// src/components/ui/SearchWithSuggestions.tsx
'use client'

import { useState, useEffect, useRef } from 'react'
import { Search, X, Clock } from 'lucide-react'
import { Input } from '@/components/ui/Input'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface Suggestion {
  id: string
  label: string
  type?: 'recent' | 'suggestion'
}

interface SearchWithSuggestionsProps {
  suggestions: Suggestion[]
  value?: string
  onChange?: (value: string) => void
  onSelect?: (suggestion: Suggestion) => void
  onSubmit?: (value: string) => void
  placeholder?: string
}

export function SearchWithSuggestions({
  suggestions,
  value,
  onChange,
  onSelect,
  onSubmit,
  placeholder = 'Buscar...',
}: SearchWithSuggestionsProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [localValue, setLocalValue] = useState(value || '')
  const inputRef = useRef<HTMLInputElement>(null)
  
  useEffect(() => {
    setLocalValue(value || '')
  }, [value])
  
  const filteredSuggestions = suggestions.filter(
    (s) => s.label.toLowerCase().includes(localValue.toLowerCase())
  )
  
  const handleSelect = (suggestion: Suggestion) => {
    setLocalValue(suggestion.label)
    onSelect?.(suggestion)
    setIsOpen(false)
    onSubmit?.(suggestion.label)
  }
  
  return (
    <div className="relative">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
        
        <Input
          ref={inputRef}
          type="search"
          placeholder={placeholder}
          value={localValue}
          onChange={(e) => {
            setLocalValue(e.target.value)
            onChange?.(e.target.value)
            setIsOpen(true)
          }}
          onFocus={() => setIsOpen(true)}
          onBlur={() => setTimeout(() => setIsOpen(false), 200)}
          className="pl-10 pr-10"
        />
        
        {localValue && (
          <Button
            type="button"
            variant="ghost"
            size="icon"
            className="absolute right-1 top-1/2 -translate-y-1/2 h-8 w-8"
            onClick={() => {
              setLocalValue('')
              onChange?.('')
              inputRef.current?.focus()
            }}
          >
            <X className="w-4 h-4" />
          </Button>
        )}
      </div>
      
      {/* Suggestions dropdown */}
      {isOpen && filteredSuggestions.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-background border rounded-md shadow-lg z-50 max-h-64 overflow-y-auto">
          {filteredSuggestions.map((suggestion) => (
            <button
              key={suggestion.id}
              type="button"
              className="w-full flex items-center gap-3 px-4 py-2 text-left hover:bg-accent transition-colors"
              onClick={() => handleSelect(suggestion)}
            >
              {suggestion.type === 'recent' && (
                <Clock className="w-4 h-4 text-muted-foreground" />
              )}
              <span className="text-sm">{suggestion.label}</span>
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
```

---

## Filter Drawer

**Quando usar:**
- Mobile: filtros laterais
- Múltiplos filtros
- Filtros complexos

**Estrutura:**

```tsx
// src/components/ui/FilterDrawer.tsx
'use client'

import { useState } from 'react'
import { SlidersHorizontal, X } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { Drawer, DrawerHeader, DrawerTitle, DrawerContent, DrawerFooter } from '@/components/ui/Drawer'
import { Badge } from '@/components/ui/Badge'

interface FilterOption {
  id: string
  label: string
  count?: number
}

interface FilterSection {
  id: string
  title: string
  type: 'checkbox' | 'radio' | 'range'
  options: FilterOption[]
  min?: number
  max?: number
}

interface FilterDrawerProps {
  sections: FilterSection[]
  filters: Record<string, any>
  onApply: (filters: Record<string, any>) => void
  onClear: () => void
  activeFiltersCount?: number
}

export function FilterDrawer({ sections, filters, onApply, onClear, activeFiltersCount }: FilterDrawerProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [localFilters, setLocalFilters] = useState(filters)
  
  const handleToggle = (sectionId: string, optionId: string) => {
    setLocalFilters((prev) => ({
      ...prev,
      [sectionId]: prev[sectionId]?.includes(optionId)
        ? prev[sectionId].filter((id: string) => id !== optionId)
        : [...(prev[sectionId] || []), optionId],
    }))
  }
  
  const handleApply = () => {
    onApply(localFilters)
    setIsOpen(false)
  }
  
  const handleClear = () => {
    setLocalFilters({})
    onClear()
  }
  
  return (
    <>
      {/* Toggle button */}
      <Button
        variant="outline"
        onClick={() => setIsOpen(true)}
        className="relative"
      >
        <SlidersHorizontal className="w-4 h-4 mr-2" />
        Filtros
        {activeFiltersCount && activeFiltersCount > 0 && (
          <Badge className="absolute -top-2 -right-2" size="sm" variant="primary">
            {activeFiltersCount}
          </Badge>
        )}
      </Button>
      
      {/* Drawer */}
      <Drawer open={isOpen} onOpenChange={setIsOpen} side="right">
        <DrawerHeader>
          <DrawerTitle>Filtros</DrawerTitle>
        </DrawerHeader>
        <DrawerContent>
          <div className="space-y-6">
            {sections.map((section) => (
              <div key={section.id}>
                <h3 className="font-medium mb-3">{section.title}</h3>
                
                {section.type === 'checkbox' && (
                  <div className="space-y-2">
                    {section.options.map((option) => (
                      <label key={option.id} className="flex items-center gap-2 cursor-pointer">
                        <input
                          type="checkbox"
                          checked={localFilters[section.id]?.includes(option.id)}
                          onChange={() => handleToggle(section.id, option.id)}
                          className="rounded"
                        />
                        <span className="text-sm">{option.label}</span>
                        {option.count !== undefined && (
                          <span className="text-xs text-muted-foreground">({option.count})</span>
                        )}
                      </label>
                    ))}
                  </div>
                )}
                
                {section.type === 'radio' && (
                  <div className="space-y-2">
                    {section.options.map((option) => (
                      <label key={option.id} className="flex items-center gap-2 cursor-pointer">
                        <input
                          type="radio"
                          name={section.id}
                          checked={localFilters[section.id] === option.id}
                          onChange={() => setLocalFilters({ ...localFilters, [section.id]: option.id })}
                          className="rounded"
                        />
                        <span className="text-sm">{option.label}</span>
                      </label>
                    ))}
                  </div>
                )}
                
                {section.type === 'range' && (
                  <div className="space-y-4">
                    <input
                      type="range"
                      min={section.min}
                      max={section.max}
                      value={localFilters[section.id] || section.min}
                      onChange={(e) => setLocalFilters({ ...localFilters, [section.id]: Number(e.target.value) })}
                      className="w-full"
                    />
                    <div className="flex justify-between text-xs text-muted-foreground">
                      <span>R$ {section.min}</span>
                      <span>R$ {localFilters[section.id] || section.min}</span>
                      <span>R$ {section.max}</span>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </DrawerContent>
        <DrawerFooter>
          <div className="flex gap-2">
            <Button variant="outline" onClick={handleClear} className="flex-1">
              Limpar
            </Button>
            <Button onClick={handleApply} className="flex-1">
              Aplicar
            </Button>
          </div>
        </DrawerFooter>
      </Drawer>
    </>
  )
}
```

---

## Filter Chips

**Quando usar:**
- Mostrar filtros ativos
- Remover filtros rapidamente
- Filtros visíveis

**Estrutura:**

```tsx
// src/components/ui/FilterChips.tsx
import { X } from 'lucide-react'
import { Badge } from '@/components/ui/Badge'
import { Button } from '@/components/ui/Button'

interface FilterChip {
  id: string
  label: string
  onRemove: () => void
}

interface FilterChipsProps {
  chips: FilterChip[]
  onClearAll?: () => void
}

export function FilterChips({ chips, onClearAll }: FilterChipsProps) {
  if (chips.length === 0) return null
  
  return (
    <div className="flex items-center gap-2 flex-wrap">
      {chips.map((chip) => (
        <Badge key={chip.id} variant="primary" className="gap-1 pr-1">
          {chip.label}
          <Button
            variant="ghost"
            size="icon"
            className="h-4 w-4 hover:bg-primary/20"
            onClick={chip.onRemove}
          >
            <X className="w-3 h-3" />
          </Button>
        </Badge>
      ))}
      
      {onClearAll && (
        <Button variant="ghost" size="sm" onClick={onClearAll}>
          Limpar tudo
        </Button>
      )}
    </div>
  )
}
```

**Uso:**

```tsx
import { FilterChips } from '@/components/ui/FilterChips'

const activeFilters = [
  { id: 'editora-panini', label: 'Panini', onRemove: () => removeFilter('editora', 'panini') },
  { id: 'preco-0-50', label: 'R$ 0 - R$ 50', onRemove: () => removeFilter('preco') },
]

<FilterChips
  chips={activeFilters}
  onClearAll={() => clearAllFilters()}
/>
```

---

## Search + Filters Combined

**Quando usar:**
- E-commerce
- Listas com busca e filtros
- Dashboards

**Estrutura:**

```tsx
// src/components/ui/SearchAndFilters.tsx
import { SearchBar } from './SearchBar'
import { FilterDrawer } from './FilterDrawer'
import { FilterChips } from './FilterChips'

interface SearchAndFiltersProps {
  searchValue: string
  onSearchChange: (value: string) => void
  onSearchSubmit: (value: string) => void
  filters: Record<string, any>
  onFiltersApply: (filters: Record<string, any>) => void
  onFiltersClear: () => void
  filterSections: any[]
  activeFiltersCount: number
}

export function SearchAndFilters({
  searchValue,
  onSearchChange,
  onSearchSubmit,
  filters,
  onFiltersApply,
  onFiltersClear,
  filterSections,
  activeFiltersCount,
}: SearchAndFiltersProps) {
  return (
    <div className="space-y-4">
      {/* Search bar */}
      <SearchBar
        value={searchValue}
        onChange={onSearchChange}
        onSubmit={onSearchSubmit}
        placeholder="Buscar quadrinhos..."
      />
      
      {/* Filters bar */}
      <div className="flex items-center justify-between">
        <FilterDrawer
          sections={filterSections}
          filters={filters}
          onApply={onFiltersApply}
          onClear={onFiltersClear}
          activeFiltersCount={activeFiltersCount}
        />
      </div>
      
      {/* Active filters */}
      <FilterChips
        chips={getActiveFilterChips(filters)}
        onClearAll={onFiltersClear}
      />
    </div>
  )
}
```

---

## Referências

- [lists-feeds.md](./lists-feeds.md)
- [tables-data.md](./tables-data.md)
- [modals.md](./modals.md)