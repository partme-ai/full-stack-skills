# Data API

## API Reference

uCharts data format API.

### Line/Column/Area Chart Data

```typescript
{
  categories: string[],      // X-axis categories
  series: Array<{
    name: string,           // Series name
    data: number[]          // Series data
  }>
}
```

### Pie/Ring Chart Data

```typescript
{
  series: Array<{
    name: string,           // Item name
    value: number           // Item value
  }>
}
```

### Radar Chart Data

```typescript
{
  categories: string[],     // Radar categories
  series: Array<{
    name: string,           // Series name
    data: number[]          // Series data
  }>
}
```

### Candle Chart Data

```typescript
{
  categories: string[],     // X-axis categories
  series: Array<{
    name: string,           // Series name
    data: Array<[number, number, number, number]>  // [open, close, low, high]
  }>
}
```

### Data Transformation

Transform API data to chart format:

```javascript
// Example: Transform API response
function transformData(apiData) {
  return {
    categories: apiData.map(item => item.date),
    series: [
      {
        name: 'Sales',
        data: apiData.map(item => item.sales)
      }
    ]
  }
}
```

**See also:** `examples/features/data-format.md` for detailed examples
