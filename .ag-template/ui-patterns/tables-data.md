# Tables & Data — Tabelas e Data Grids

## Visão Geral

Este guia define os padrões de tabelas e data grids para dashboards e listas de dados.

---

## Tabela Básica

**Quando usar:** Dados tabulares simples.

**Estrutura:**

```tsx
// src/components/ui/Table.tsx
import { cn } from '@/lib/utils'

export function Table({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className="w-full overflow-auto">
      <table className={cn('w-full text-sm', className)}>
        {children}
      </table>
    </div>
  )
}

export function TableHeader({ children }: { children: React.ReactNode }) {
  return <thead className="bg-muted">{children}</thead>
}

export function TableBody({ children }: { children: React.ReactNode }) {
  return <tbody>{children}</tbody>
}

export function TableRow({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <tr className={cn('border-b hover:bg-muted/50', className)}>
      {children}
    </tr>
  )
}

export function TableHead({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <th className={cn('h-12 px-4 text-left font-medium', className)}>
      {children}
    </th>
  )
}

export function TableCell({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <td className={cn('p-4', className)}>
      {children}
    </td>
  )
}
```

**Uso:**

```tsx
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableHead,
  TableCell,
} from '@/components/ui/Table'

<Table>
  <TableHeader>
    <TableRow>
      <TableHead>Título</TableHead>
      <TableHead>Editora</TableHead>
      <TableHead>Preço</TableHead>
      <TableHead>Status</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    {comics.map((comic) => (
      <TableRow key={comic.id}>
        <TableCell>{comic.titulo}</TableCell>
        <TableCell>{comic.editora}</TableCell>
        <TableCell>R$ {comic.preco.toFixed(2)}</TableCell>
        <TableCell>
          <Badge variant={comic.ativo ? 'success' : 'error'}>
            {comic.ativo ? 'Ativo' : 'Inativo'}
          </Badge>
        </TableCell>
      </TableRow>
    ))}
  </TableBody>
</Table>
```

---

## Tabela com Sorting

**Quando usar:** Dados que precisam ser ordenados.

**Estrutura:**

```tsx
// src/components/ui/SortableTable.tsx
'use client'

import { useState } from 'react'
import { ArrowUpDown, ArrowUp, ArrowDown } from 'lucide-react'
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableHead,
  TableCell,
} from '@/components/ui/Table'
import { cn } from '@/lib/utils'

type SortDirection = 'asc' | 'desc'

interface Column<T> {
  key: keyof T | string
  label: string
  sortable?: boolean
  render?: (item: T) => React.ReactNode
}

interface SortableTableProps<T> {
  columns: Column<T>[]
  data: T[]
  getKey: (item: T) => string
}

export function SortableTable<T>({ columns, data, getKey }: SortableTableProps<T>) {
  const [sortKey, setSortKey] = useState<string | null>(null)
  const [sortDirection, setSortDirection] = useState<SortDirection>('asc')
  
  const handleSort = (key: string) => {
    if (sortKey === key) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc')
    } else {
      setSortKey(key)
      setSortDirection('asc')
    }
  }
  
  const sortedData = [...data].sort((a, b) => {
    if (!sortKey) return 0
    
    const aValue = a[sortKey as keyof T]
    const bValue = b[sortKey as keyof T]
    
    if (aValue < bValue) return sortDirection === 'asc' ? -1 : 1
    if (aValue > bValue) return sortDirection === 'asc' ? 1 : -1
    return 0
  })
  
  return (
    <Table>
      <TableHeader>
        <TableRow>
          {columns.map((column) => (
            <TableHead
              key={column.key as string}
              className={cn(column.sortable && 'cursor-pointer')}
              onClick={() => column.sortable && handleSort(column.key as string)}
            >
              <div className="flex items-center gap-2">
                {column.label}
                {column.sortable && (
                  <span className="text-muted-foreground">
                    {sortKey === column.key ? (
                      sortDirection === 'asc' ? (
                        <ArrowUp className="w-4 h-4" />
                      ) : (
                        <ArrowDown className="w-4 h-4" />
                      )
                    ) : (
                      <ArrowUpDown className="w-4 h-4" />
                    )}
                  </span>
                )}
              </div>
            </TableHead>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {sortedData.map((item) => (
          <TableRow key={getKey(item)}>
            {columns.map((column) => (
              <TableCell key={column.key as string}>
                {column.render
                  ? column.render(item)
                  : String(item[column.key as keyof T])}
              </TableCell>
            ))}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
```

**Uso:**

```tsx
import { SortableTable } from '@/components/ui/SortableTable'
import { Badge } from '@/components/ui/Badge'

const columns = [
  { key: 'titulo', label: 'Título', sortable: true },
  { key: 'editora', label: 'Editora', sortable: true },
  {
    key: 'preco',
    label: 'Preço',
    sortable: true,
    render: (comic) => `R$ ${comic.preco.toFixed(2)}`,
  },
  {
    key: 'ativo',
    label: 'Status',
    render: (comic) => (
      <Badge variant={comic.ativo ? 'success' : 'error'}>
        {comic.ativo ? 'Ativo' : 'Inativo'}
      </Badge>
    ),
  },
]

<SortableTable
  columns={columns}
  data={comics}
  getKey={(comic) => comic.id}
/>
```

---

## Tabela com Pagination

**Quando usar:** Dados paginados.

**Estrutura:**

```tsx
// src/components/ui/PaginatedTable.tsx
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableHead,
  TableCell,
} from '@/components/ui/Table'
import { Pagination } from '@/components/ui/Pagination'

interface PaginatedTableProps<T> {
  columns: Column<T>[]
  data: T[]
  getKey: (item: T) => string
  currentPage: number
  totalPages: number
  onPageChange: (page: number) => void
}

export function PaginatedTable<T>({ columns, data, getKey, currentPage, totalPages, onPageChange }: PaginatedTableProps<T>) {
  return (
    <div>
      <Table>
        <TableHeader>
          <TableRow>
            {columns.map((column) => (
              <TableHead key={column.key as string}>
                {column.label}
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((item) => (
            <TableRow key={getKey(item)}>
              {columns.map((column) => (
                <TableCell key={column.key as string}>
                  {column.render
                    ? column.render(item)
                    : String(item[column.key as keyof T])}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      <div className="flex items-center justify-end mt-4">
        <Pagination
          currentPage={currentPage}
          totalPages={totalPages}
          onPageChange={onPageChange}
        />
      </div>
    </div>
  )
}
```

---

## Data Grid Avançado (TanStack Table)

**Quando usar:** Tabelas complexas com features avançadas.

**Estrutura:**

```tsx
// src/components/ui/DataTable.tsx
'use client'

import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  getFilteredRowModel,
  flexRender,
  ColumnDef,
  SortingState,
} from '@tanstack/react-table'
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableHead,
  TableCell,
} from '@/components/ui/Table'
import { useState } from 'react'

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({ columns, data }: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = useState<SortingState>([])
  const [globalFilter, setGlobalFilter] = useState('')
  
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      globalFilter,
    },
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
  })
  
  return (
    <div>
      {/* Search */}
      <input
        type="text"
        placeholder="Buscar..."
        value={globalFilter}
        onChange={(e) => setGlobalFilter(e.target.value)}
        className="mb-4 px-3 py-2 border rounded-md w-full max-w-sm"
      />
      
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <TableHead key={header.id}>
                  {flexRender(
                    header.column.columnDef.header,
                    header.getContext()
                  )}
                </TableHead>
              ))}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows.map((row) => (
            <TableRow key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <TableCell key={cell.id}>
                  {flexRender(
                    cell.column.columnDef.cell,
                    cell.getContext()
                  )}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      {/* Pagination */}
      <div className="flex items-center justify-end gap-2 mt-4">
        <button
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
          className="px-3 py-1 border rounded disabled:opacity-50"
        >
          Anterior
        </button>
        <span className="text-sm">
          Página {table.getState().pagination.pageIndex + 1} de {table.getPageCount()}
        </span>
        <button
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
          className="px-3 py-1 border rounded disabled:opacity-50"
        >
          Próxima
        </button>
      </div>
    </div>
  )
}
```

**Uso:**

```tsx
import { DataTable } from '@/components/ui/DataTable'
import { ColumnDef } from '@tanstack/react-table'
import { Badge } from '@/components/ui/Badge'

const columns: ColumnDef<Comic>[] = [
  {
    accessorKey: 'titulo',
    header: 'Título',
    cell: ({ getValue }) => <span className="font-medium">{getValue<string>()}</span>,
  },
  {
    accessorKey: 'editora',
    header: 'Editora',
  },
  {
    accessorKey: 'preco',
    header: 'Preço',
    cell: ({ getValue }) => `R$ ${getValue<number>().toFixed(2)}`,
  },
  {
    accessorKey: 'ativo',
    header: 'Status',
    cell: ({ getValue }) => (
      <Badge variant={getValue<boolean>() ? 'success' : 'error'}>
        {getValue<boolean>() ? 'Ativo' : 'Inativo'}
      </Badge>
    ),
  },
]

<DataTable columns={columns} data={comics} />
```

---

## Tabela com Row Selection

**Quando usar:** Selecionar múltiplos itens.

**Estrutura:**

```tsx
// src/components/ui/SelectableTable.tsx
'use client'

import { useState } from 'react'
import { Checkbox } from '@/components/ui/Checkbox'
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableHead,
  TableCell,
} from '@/components/ui/Table'

interface SelectableTableProps<T> {
  columns: Column<T>[]
  data: T[]
  getKey: (item: T) => string
  onSelectionChange?: (selectedIds: string[]) => void
}

export function SelectableTable<T>({ columns, data, getKey, onSelectionChange }: SelectableTableProps<T>) {
  const [selectedIds, setSelectedIds] = useState<string[]>([])
  
  const handleSelectAll = (checked: boolean) => {
    if (checked) {
      const allIds = data.map(getKey)
      setSelectedIds(allIds)
      onSelectionChange?.(allIds)
    } else {
      setSelectedIds([])
      onSelectionChange?.([])
    }
  }
  
  const handleSelectRow = (id: string, checked: boolean) => {
    const newSelectedIds = checked
      ? [...selectedIds, id]
      : selectedIds.filter((selectedId) => selectedId !== id)
    
    setSelectedIds(newSelectedIds)
    onSelectionChange?.(newSelectedIds)
  }
  
  const allSelected = data.length > 0 && selectedIds.length === data.length
  
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[50px]">
            <Checkbox
              id="select-all"
              checked={allSelected}
              onCheckedChange={handleSelectAll}
            />
          </TableHead>
          {columns.map((column) => (
            <TableHead key={column.key as string}>
              {column.label}
            </TableHead>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((item) => {
          const id = getKey(item)
          const isSelected = selectedIds.includes(id)
          
          return (
            <TableRow key={id} className={isSelected && 'bg-muted'}>
              <TableCell>
                <Checkbox
                  id={id}
                  checked={isSelected}
                  onCheckedChange={(checked) => handleSelectRow(id, checked as boolean)}
                />
              </TableCell>
              {columns.map((column) => (
                <TableCell key={column.key as string}>
                  {column.render
                    ? column.render(item)
                    : String(item[column.key as keyof T])}
                </TableCell>
              ))}
            </TableRow>
          )
        })}
      </TableBody>
    </Table>
  )
}
```

---

## Referências

- [cards.md](./cards.md)
- [lists-feeds.md](./lists-feeds.md)
- [navigation-secondary.md](./navigation-secondary.md)