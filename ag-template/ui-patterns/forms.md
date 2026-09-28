# Forms — Componentes de Formulário

## Visão Geral

Este guia define os padrões de componentes de formulário para projetos web mobile-first.

---

## Input

**Quando usar:** Campos de texto simples.

**Estrutura:**

```tsx
// src/components/ui/Input.tsx
import { forwardRef, InputHTMLAttributes } from 'react'
import { cn } from '@/lib/utils'

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  helperText?: string
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, helperText, id, ...props }, ref) => {
    return (
      <div className="space-y-2">
        {label && (
          <label htmlFor={id} className="text-sm font-medium">
            {label}
          </label>
        )}
        
        <input
          id={id}
          ref={ref}
          className={cn(
            'flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm',
            'ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium',
            'placeholder:text-muted-foreground',
            'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error && 'border-destructive focus-visible:ring-destructive',
            className
          )}
          {...props}
        />
        
        {error && (
          <p className="text-sm text-destructive">{error}</p>
        )}
        
        {helperText && !error && (
          <p className="text-sm text-muted-foreground">{helperText}</p>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'
```

**Uso:**

```tsx
<Input
  id="email"
  type="email"
  label="Email"
  placeholder="seu@email.com"
  error={errors.email?.message}
  helperText="Usado para login e recuperação"
/>
```

---

## Textarea

**Quando usar:** Campos de texto longo.

**Estrutura:**

```tsx
// src/components/ui/Textarea.tsx
import { forwardRef, TextareaHTMLAttributes } from 'react'
import { cn } from '@/lib/utils'

export interface TextareaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string
  error?: string
  helperText?: string
}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ className, label, error, helperText, id, ...props }, ref) => {
    return (
      <div className="space-y-2">
        {label && (
          <label htmlFor={id} className="text-sm font-medium">
            {label}
          </label>
        )}
        
        <textarea
          id={id}
          ref={ref}
          className={cn(
            'flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm',
            'placeholder:text-muted-foreground',
            'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error && 'border-destructive focus-visible:ring-destructive',
            className
          )}
          {...props}
        />
        
        {error && (
          <p className="text-sm text-destructive">{error}</p>
        )}
        
        {helperText && !error && (
          <p className="text-sm text-muted-foreground">{helperText}</p>
        )}
      </div>
    )
  }
)

Textarea.displayName = 'Textarea'
```

---

## Select

**Quando usar:** Seleção de uma opção de lista.

**Estrutura:**

```tsx
// src/components/ui/Select.tsx
'use client'

import * as SelectPrimitive from '@radix-ui/react-select'
import { Check, ChevronDown } from 'lucide-react'
import { cn } from '@/lib/utils'

interface SelectOption {
  value: string
  label: string
}

interface SelectProps {
  options: SelectOption[]
  placeholder?: string
  label?: string
  error?: string
  value?: string
  onChange?: (value: string) => void
}

export function Select({ options, placeholder, label, error, value, onChange }: SelectProps) {
  return (
    <div className="space-y-2">
      {label && (
        <label className="text-sm font-medium">{label}</label>
      )}
      
      <SelectPrimitive.Root value={value} onValueChange={onChange}>
        <SelectPrimitive.Trigger
          className={cn(
            'flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm',
            'focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2',
            error && 'border-destructive focus:ring-destructive'
          )}
        >
          <SelectPrimitive.Value placeholder={placeholder} />
          <SelectPrimitive.Icon>
            <ChevronDown className="w-4 h-4 opacity-50" />
          </SelectPrimitive.Icon>
        </SelectPrimitive.Trigger>
        
        <SelectPrimitive.Portal>
          <SelectPrimitive.Content className="bg-background border rounded-md shadow-lg">
            <SelectPrimitive.Viewport className="p-1">
              {options.map((option) => (
                <SelectPrimitive.Item
                  key={option.value}
                  value={option.value}
                  className="flex items-center gap-2 px-3 py-2 text-sm hover:bg-accent rounded cursor-pointer"
                >
                  <SelectPrimitive.ItemIndicator>
                    <Check className="w-4 h-4" />
                  </SelectPrimitive.ItemIndicator>
                  {option.label}
                </SelectPrimitive.Item>
              ))}
            </SelectPrimitive.Viewport>
          </SelectPrimitive.Content>
        </SelectPrimitive.Portal>
      </SelectPrimitive.Root>
      
      {error && (
        <p className="text-sm text-destructive">{error}</p>
      )}
    </div>
  )
}
```

**Uso:**

```tsx
<Select
  options={[
    { value: 'panini', label: 'Panini' },
    { value: 'mythos', label: 'Mythos' },
    { value: 'jbc', label: 'JBC' },
  ]}
  placeholder="Selecione uma editora"
  label="Editora"
  value={formData.editora}
  onChange={(value) => setFormData({ ...formData, editora: value })}
  error={errors.editora?.message}
/>
```

---

## Checkbox

**Quando usar:** Seleção binária (sim/não, verdadeiro/falso).

**Estrutura:**

```tsx
// src/components/ui/Checkbox.tsx
'use client'

import * as CheckboxPrimitive from '@radix-ui/react-checkbox'
import { Check } from 'lucide-react'
import { cn } from '@/lib/utils'

interface CheckboxProps {
  id: string
  label?: string
  checked?: boolean
  onCheckedChange?: (checked: boolean) => void
  error?: string
}

export function Checkbox({ id, label, checked, onCheckedChange, error }: CheckboxProps) {
  return (
    <div className="space-y-2">
      <div className="flex items-center gap-2">
        <CheckboxPrimitive.Root
          id={id}
          checked={checked}
          onCheckedChange={onCheckedChange}
          className={cn(
            'peer h-4 w-4 shrink-0 rounded border border-primary ring-offset-background',
            'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
            'disabled:cursor-not-allowed disabled:opacity-50',
            checked && 'bg-primary text-primary-foreground'
          )}
        >
          <CheckboxPrimitive.Indicator className="flex items-center justify-center">
            <Check className="w-3 h-3" />
          </CheckboxPrimitive.Indicator>
        </CheckboxPrimitive.Root>
        
        {label && (
          <label
            htmlFor={id}
            className="text-sm font-medium leading-none cursor-pointer"
          >
            {label}
          </label>
        )}
      </div>
      
      {error && (
        <p className="text-sm text-destructive">{error}</p>
      )}
    </div>
  )
}
```

**Uso:**

```tsx
<Checkbox
  id="terms"
  label="Concordo com os Termos de Uso"
  checked={formData.acceptTerms}
  onCheckedChange={(checked) => setFormData({ ...formData, acceptTerms: checked })}
  error={errors.acceptTerms?.message}
/>
```

---

## Radio Group

**Quando usar:** Seleção de uma opção entre múltiplas.

**Estrutura:**

```tsx
// src/components/ui/RadioGroup.tsx
'use client'

import * as RadioGroupPrimitive from '@radix-ui/react-radio-group'
import { cn } from '@/lib/utils'

interface RadioOption {
  value: string
  label: string
}

interface RadioGroupProps {
  options: RadioOption[]
  label?: string
  value?: string
  onChange?: (value: string) => void
  error?: string
}

export function RadioGroup({ options, label, value, onChange, error }: RadioGroupProps) {
  return (
    <div className="space-y-2">
      {label && (
        <label className="text-sm font-medium">{label}</label>
      )}
      
      <RadioGroupPrimitive.Root value={value} onValueChange={onChange}>
        <div className="flex flex-col gap-2">
          {options.map((option) => (
            <div key={option.value} className="flex items-center gap-2">
              <RadioGroupPrimitive.Item
                value={option.value}
                className={cn(
                  'peer h-4 w-4 rounded-full border border-primary ring-offset-background',
                  'focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2',
                  'disabled:cursor-not-allowed disabled:opacity-50'
                )}
              >
                <RadioGroupPrimitive.Indicator className="flex items-center justify-center">
                  <div className="h-2 w-2 rounded-full bg-primary" />
                </RadioGroupPrimitive.Indicator>
              </RadioGroupPrimitive.Item>
              
              <label className="text-sm cursor-pointer">
                {option.label}
              </label>
            </div>
          ))}
        </div>
      </RadioGroupPrimitive.Root>
      
      {error && (
        <p className="text-sm text-destructive">{error}</p>
      )}
    </div>
  )
}
```

---

## File Upload

**Quando usar:** Upload de arquivos.

**Estrutura:**

```tsx
// src/components/ui/FileUpload.tsx
'use client'

import { useState, useRef } from 'react'
import { Upload, X, File } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface FileUploadProps {
  label?: string
  accept?: string
  maxSize?: number // MB
  multiple?: boolean
  value?: File[]
  onChange?: (files: File[]) => void
  error?: string
}

export function FileUpload({ label, accept, maxSize = 5, multiple, value, onChange, error }: FileUploadProps) {
  const [isDragging, setIsDragging] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)
  
  const handleFiles = (files: FileList | null) => {
    if (!files) return
    
    const validFiles = Array.from(files).filter(file => {
      if (maxSize && file.size > maxSize * 1024 * 1024) {
        alert(`Arquivo ${file.name} excede o tamanho máximo de ${maxSize}MB`)
        return false
      }
      return true
    })
    
    onChange?.(multiple ? validFiles : [validFiles[0]])
  }
  
  const handleRemove = (index: number) => {
    const newFiles = value?.filter((_, i) => i !== index)
    onChange?.(newFiles || [])
  }
  
  return (
    <div className="space-y-2">
      {label && (
        <label className="text-sm font-medium">{label}</label>
      )}
      
      <div
        className={cn(
          'border-2 border-dashed rounded-md p-6 text-center',
          'hover:bg-accent/50 transition-colors',
          isDragging && 'border-primary bg-accent/50',
          error && 'border-destructive'
        )}
        onDragOver={(e) => {
          e.preventDefault()
          setIsDragging(true)
        }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={(e) => {
          e.preventDefault()
          setIsDragging(false)
          handleFiles(e.dataTransfer.files)
        }}
      >
        <Upload className="w-8 h-8 mx-auto mb-2 text-muted-foreground" />
        <p className="text-sm text-muted-foreground mb-2">
          Arraste e solte arquivos aqui ou
        </p>
        <Button
          type="button"
          variant="outline"
          size="sm"
          onClick={() => inputRef.current?.click()}
        >
          Selecionar arquivos
        </Button>
        <input
          ref={inputRef}
          type="file"
          accept={accept}
          multiple={multiple}
          className="hidden"
          onChange={(e) => handleFiles(e.target.files)}
        />
      </div>
      
      {value && value.length > 0 && (
        <div className="space-y-2">
          {value.map((file, index) => (
            <div
              key={index}
              className="flex items-center justify-between p-2 bg-muted rounded"
            >
              <div className="flex items-center gap-2">
                <File className="w-4 h-4" />
                <span className="text-sm">{file.name}</span>
                <span className="text-xs text-muted-foreground">
                  ({(file.size / 1024 / 1024).toFixed(2)} MB)
                </span>
              </div>
              <Button
                type="button"
                variant="ghost"
                size="icon"
                onClick={() => handleRemove(index)}
              >
                <X className="w-4 h-4" />
              </Button>
            </div>
          ))}
        </div>
      )}
      
      {error && (
        <p className="text-sm text-destructive">{error}</p>
      )}
    </div>
  )
}
```

---

## Date Picker

**Quando usar:** Seleção de data.

**Estrutura:**

```tsx
// src/components/ui/DatePicker.tsx
'use client'

import { format } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import { CalendarIcon } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface DatePickerProps {
  label?: string
  value?: Date
  onChange?: (date: Date) => void
  error?: string
}

export function DatePicker({ label, value, onChange, error }: DatePickerProps) {
  return (
    <div className="space-y-2">
      {label && (
        <label className="text-sm font-medium">{label}</label>
      )}
      
      <div className="relative">
        <Button
          type="button"
          variant="outline"
          className={cn(
            'w-full justify-start text-left font-normal',
            !value && 'text-muted-foreground',
            error && 'border-destructive'
          )}
          onClick={() => {/* Open calendar modal */}}
        >
          <CalendarIcon className="w-4 h-4 mr-2" />
          {value ? format(value, 'PPP', { locale: ptBR }) : 'Selecionar data'}
        </Button>
      </div>
      
      {error && (
        <p className="text-sm text-destructive">{error}</p>
      )}
    </div>
  )
}
```

---

## Form com Validação

**Exemplo Completo:**

```tsx
// src/components/features/comics/ComicForm.tsx
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Input } from '@/components/ui/Input'
import { Textarea } from '@/components/ui/Textarea'
import { Select } from '@/components/ui/Select'
import { Checkbox } from '@/components/ui/Checkbox'
import { FileUpload } from '@/components/ui/FileUpload'
import { Button } from '@/components/ui/Button'

const comicSchema = z.object({
  titulo: z.string().min(1, 'Título é obrigatório'),
  editora: z.string().min(1, 'Editora é obrigatória'),
  descricao: z.string().optional(),
  preco: z.string().min(1, 'Preço é obrigatório'),
  urlCapa: z.string().url('URL inválida').optional(),
  capaFile: z.instanceof(File).optional(),
  acceptTerms: z.boolean().refine(val => val, 'Você deve aceitar os termos'),
})

type ComicFormData = z.infer<typeof comicSchema>

export function ComicForm() {
  const { register, handleSubmit, formState: { errors }, watch } = useForm<ComicFormData>({
    resolver: zodResolver(comicSchema),
  })
  
  const capaFile = watch('capaFile')
  
  const onSubmit = async (data: ComicFormData) => {
    // Submit logic
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      <Input
        id="titulo"
        label="Título"
        placeholder="Nome do quadrinho"
        error={errors.titulo?.message}
        {...register('titulo')}
      />
      
      <Select
        options={[
          { value: 'panini', label: 'Panini' },
          { value: 'mythos', label: 'Mythos' },
          { value: 'jbc', label: 'JBC' },
        ]}
        label="Editora"
        placeholder="Selecione uma editora"
        error={errors.editora?.message}
        value={watch('editora')}
        onChange={(value) => {/* Set value */}}
      />
      
      <Textarea
        id="descricao"
        label="Descrição"
        placeholder="Descrição do quadrinho"
        error={errors.descricao?.message}
        {...register('descricao')}
      />
      
      <Input
        id="preco"
        type="number"
        step="0.01"
        label="Preço"
        placeholder="0,00"
        error={errors.preco?.message}
        {...register('preco')}
      />
      
      <FileUpload
        label="Capa"
        accept="image/*"
        maxSize={5}
        value={capaFile ? [capaFile] : []}
        onChange={(files) => {/* Set file */}}
        error={errors.capaFile?.message}
      />
      
      <Checkbox
        id="terms"
        label="Concordo com os termos de uso"
        checked={watch('acceptTerms')}
        onCheckedChange={(checked) => {/* Set value */}}
        error={errors.acceptTerms?.message}
      />
      
      <div className="flex gap-4">
        <Button type="submit">Salvar</Button>
        <Button type="button" variant="outline">Cancelar</Button>
      </div>
    </form>
  )
}
```

---

## Referências

- [auth-flows.md](./auth-flows.md)
- [error.md](./error.md)
- [modals.md](./modals.md)